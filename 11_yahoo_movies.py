"""
yahoo movie top100, save to csv
https://movies.yahoo.com.tw/movie_intheaters.html
Movie Name、Release Time
 ↓↓↓↓
page 1 = https://movies.yahoo.com.tw/movie_intheaters.html?
page 2 = https://movies.yahoo.com.tw/movie_intheaters.html?page=2
page n = https://movies.yahoo.com.tw/movie_intheaters.html?page=n
"""
import urllib.request
import csv,re

class YahooMovie(object):
    def __init__(self):
        self.base_url = 'https://movies.yahoo.com.tw/movie_intheaters.html?'
        self.headers = {'User-Agent':'Morzilla/5.0'}
        self.page = 1
        
        
    def loadPage(self,url):
        request = urllib.request.Request(url,headers = self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        self.ParseContext(html)
        
        
    def ParseContext(self,html):
        pattern = re.compile(r'<div class="release_movie_name">.*?]">(.*?)</a>.*?movie_time">(.*?)</div>',re.S)
        movie = pattern.findall(html)
        # [(，),(,),(,)...]
        self.SaveCsv(movie)
    
    
    def SaveCsv(self,movie):
        if self.page == 1:
            with open('Yahoo_OnMovies.csv','a',newline='',encoding='utf-8')as f:
                #初始化寫入對象 writer = csv.writer()
                writer = csv.writer(f)
                writer.writerow(['2020 Oct Release Movie : '])
            
        for m_tuple in movie :
            with open('Yahoo_OnMovies.csv','a',newline='',encoding='utf-8')as f:
                writer = csv.writer(f)
                #將列表寫入csv內(列表形式)
                #須將m_tuple改成列表[ , , ]再存入，記得去空白
                movie_list = [m_tuple[0].strip(),m_tuple[1]]                
                writer.writerow(movie_list)
                writer.writerow('')
                
    
    def Work(self):
        self.loadPage(self.base_url)
        while True:
            print('Done!')
            c = input('Going on next page? (y/n) : ')
            if c.strip().lower() == 'y':
                self.page += 1
                url = self.base_url + 'page=' + str(self.page)
                self.loadPage(url)
            else:
                print('Thanks, bye.')
                break
        
        
if __name__ == "__main__":
    DH = YahooMovie()
    DH.Work()

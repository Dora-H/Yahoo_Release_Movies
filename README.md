Yahoo Movie Website scraping, data(name,release date) extraction.

 
## Requirements
● Python 3    
● urllib.request   
● csv   
● re


## Class
YahooMovie


## Functions
● LoadPage    
● ParseContext   
● SaveCsv   
● Work


## Run Codes
### Simply Crawling and Scraping Web Pages with below descriptions to start:

#### 1. Call the main finction to work, Work.
    if __name__ == "__main__":
        DH = YahooMovie()
        DH.Work()
				
#### 2. Go to the first function, LoadPage:
    # requests the url 'https://movies.yahoo.com.tw/movie_intheaters.html'	    
    request = urllib.request.Request(url,headers = self.headers)  
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    # get the url's html and go to ParseContext function.
    self.ParseContext(html)   
				
#### 3. Go to the ParsePage function:
    # use regex patterns to parse html 
    pattern = re.compile(r'<div class="release_movie_name">.*?]">(.*?)</a>.*?movie_time">(.*?)</div>',re.S)
    movie = pattern.findall(html)
    # the type of movies is tuple : [(，),(,),(,)...]
    self.SaveCsv(movie)				
    
#### 4. Go to the SaveCsv function:
     # write the title " 2020 Oct Release Movie" first.
     if self.page == 1:
         with open('Yahoo_OnMovies.csv','a',newline='',encoding='utf-8')as f:
         writer = csv.writer(f)
         writer.writerow(['2020 Oct Release Movie : '])
     
     # then write the contexts.       
     for m_tuple in movie :
         with open('Yahoo_OnMovies.csv','a',newline='',encoding='utf-8')as f:
         writer = csv.writer(f)
         movie_list = [m_tuple[0].strip(),m_tuple[1]]                
         writer.writerow(movie_list)
         writer.writerow('')
        
#### 5. Rerun again:
	c = input('Going on next page? (y/n) : ')
	# if going to crawl next page >>> y
        if c.strip().lower() == 'y':
           self.page += 1
           url = self.base_url + 'page=' + str(self.page)
	   # Go to the first function, LoadPage
           self.LoadPage(url)
	# if not going to crawl next page >>> n
        else:
	    # Exit from the code, and shows 'Thanks, bye.'
            print('Thanks, bye.')
            break

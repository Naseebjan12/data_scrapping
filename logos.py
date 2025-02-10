from bs4 import BeautifulSoup
# import requests

# # url = 'https://www.empireonline.com/movies/features/best-movies-2/'
# # data = requests.get(url=url)
# # with open('movie.html','w') as f:
# #     f.write(data.text)
    
    
     
     
with open('movie.html','r') as f:
    content = f.read()
    
    
soup = BeautifulSoup(content,'html.parser')
# print(soup.title.text)

title = soup.title.text
all_movies = soup.find_all('h2')
for movie in all_movies:
    with open('100movies.html','+a') as f:
        f.write(movie.get_text()+'\n')


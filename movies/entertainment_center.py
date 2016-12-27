import media
import fresh_tomatoes

films = [
    ['Toy Story', 'Toys come to life',
    'http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc'],
    ['Avatar', 'Marine visits alien planet',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY'],
    ['Midnight in Paris', 'Writer visits Paris',
    'https://natashastander.files.wordpress.com/2014/07/mip.jpg',
    'https://www.youtube.com/watch?v=FAfR8omt-CY'],
    ['La La Land', 'Two aspiring artists meet in LA',
    'http://www.filmpro.sk/files/plagat/llland_teaser_sk.jpg',
    'https://www.youtube.com/watch?v=0pdqf4P9MB8'],
    ['Alien: Covenant', 'Aliens returns',
    'http://cdn3-www.comingsoon.net/assets/uploads/gallery/alien-covenant/alien-covenant-1280.jpg',
    'https://www.youtube.com/watch?v=H0VW6sg50Pk'],
    ['The Edge of Seventeen', 'A teenager comes of age',
    'http://d2118lkw40i39g.cloudfront.net/wp-content/uploads/2016/11/the-edge-of-seventeen.jpg',
    'https://www.youtube.com/watch?v=EB6Gecy6IP8']
]

movies = []
for film in films:
    movies.append(media.Movie(*film))
fresh_tomatoes.open_movies_page(movies)

from server import movies
import requests
import json

# genre = {
#         '28':'action',
#         '12':'adventure',
#         '16':'animation',
#         '35':'comedy',
#         '80':'crime',
#         '99':'documentary',
#         '18':'drama',
#         '10751':'family',
#         '14':'fantasy',
#         '36':'history',
#         '27':'horror',
#         '9648':'mystery',
#         '10749':'romance',
#         '878':'SF',
#         '53':'thriller',
#         '10752':'war',
# }
API_KEY = '0624ed7928bb6576d3a3e4a85ffd49cf'
genres = ['28', '12', '16', '35', '80', '99', 
          '18', '10751', '14', '36', '27', '9648',
          '10749', '878', '53', '10752'
        ]
results = []

for genre in genres:
    URL = 'https://api.themoviedb.org/3/discover/movie?api_key=' \
            + API_KEY + '&language=ko-KR&sort_by=popularity.desc&include_adult=false&include_video=false'\
            + '&page=1&release_date.gte=20200101&with_genres=' \
            + genre + '&with_watch_monetization_types=flatrate'

    response = requests.get(URL)
    # response.status_code
    data = response.json()
    for j in range(len(data['results'])):
        results.append(data['results'][j])
    
file_path = './myMovies.json'
file_path2 = './movie_genre_info.json'
# print(result[0])
data = []
data2 = []
titles = []
genre_pk = 0
for index, movieInfo in enumerate(results):
    # 중복되는 영화는 배제해야 한다.
    if movieInfo['title'] not in titles:
        titles.append(movieInfo['title'])
        tmp = {}
        tmp["model"] = "movies.movie"
        tmp["pk"] = str(index)
        tmp["fields"] = {}
        tmp["fields"]["title"] = movieInfo['title']
        tmp["fields"]["image"] = "https://www.themoviedb.org/t/p/w1280/" + movieInfo['poster_path']
        tmp["fields"]["overview"] = movieInfo['overview']
        tmp["fields"]["subtitle"] = movieInfo['original_title']
        tmp["fields"]["pubDate"] = movieInfo['release_date']
        tmp["fields"]["userRating"] = movieInfo['vote_average']
    
        # # Genre 처리해줘야 한다...
        genres = movieInfo["genre_ids"]
        for genre in genres:
            tmp2 = {}
            tmp2["model"] = "movies.movie_genres"
            tmp2["pk"] = str(genre_pk);genre_pk += 1
            tmp2["fields"] = {}
            tmp2["fields"]["movie_id"] = str(index)
            tmp2["fields"]["genre_id"] = str(genre)
            data2.append(tmp2)
    
    data.append(tmp)

with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

with open(file_path2, 'w', encoding='UTF-8') as outfile2:
    json.dump(data2, outfile2, indent=4, ensure_ascii=False)

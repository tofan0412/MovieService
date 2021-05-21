import requests
import json



API_KEY = '0624ed7928bb6576d3a3e4a85ffd49cf'
result = []
for i in range(1,6):
    URL = 'https://api.themoviedb.org/3/discover/movie?api_key=0624ed7928bb6576d3a3e4a85ffd49cf&language=ko-KR&sort_by=popularity.desc&include_adult=false&include_video=false&page=' \
            + str(i) +'&with_watch_monetization_types=flatrate'

    response = requests.get(URL)
    # response.status_code
    data = response.json()
    for j in range(len(data['results'])):
        result.append(data['results'][j])
    
file_path = './movies.json'
json.dump(result, file_path)



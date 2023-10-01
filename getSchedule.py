import requests

baseurl = "https://koleo.pl/pl/connections"
date = "01-10-2023+19:00:00"
start_station = "mokronos-gorny"
end_station = "wroclaw-glowny"
query_url = f"{baseurl}?query[date]={date}&query[start_station]={start_station}&query[end_station]={end_station}"
query_headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                 'X-Requested-With': 'XMLHttpRequest'}

res = requests.get(query_url, headers=query_headers)
print(res.json())

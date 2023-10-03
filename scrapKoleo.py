import requests as req

start_range = 0
end_range = 2000
entries = []

for iter in range(start_range,end_range):
    request = req.get(f"https://koleo.pl/ls?q={iter}")
    if request.status_code == 200:
        res = request.json()
        try:
            station_name = res['stations'][0]['name']
            ibnr = res['stations'][0]['ibnr']
            entries.append(f"- {ibnr}: {station_name}")
            print(f"Found {ibnr}: {station_name}")
        except IndexError:
            print(f"Index error raised on index {iter}")
            print(f"Details: {res}")

with open("stations.to.1k.txt", "w", encoding="utf-8") as file:
    file.write('\n'.join(entries))

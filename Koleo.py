import requests
import datetime


def get_stations_by_id(start_id: int, end_id: int) -> dict or requests.status_codes:
    entries = []
    for station_id in range(start_id, end_id+1):
        request = requests.get(f"https://koleo.pl/ls?q={station_id}")
        if request.status_code == 200:
            res = request.json()
            try:
                station_name = res['stations'][0]['name']
                entries.append(f"- {station_id}: {station_name}")
            except IndexError:
                entries.append(f"= {station_id}: station not found")
    return entries


def get_schedule_for_stations(start_station: str, end_station: str, date: datetime) -> dict or requests.status_codes:
    entries = []
    query_url = (
        f"https://koleo.pl/pl/connections?"
        f"query[date]={date}&"
        f"query[start_station]={start_station}&"
        f"query[end_station]={end_station}"
    )
    query_headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                     'X-Requested-With': 'XMLHttpRequest'}
    request = requests.get(query_url, headers=query_headers)
    if request.status_code == 200:
        res = request.json()["connections"]
        for i in res:
            entries.append(i)
        return entries
    else:
        return request.status_code


if __name__ == "__main__":
    print(get_stations_by_id(50, 60))
    print(get_schedule_for_stations("mokronos-gorny", "wroclaw-glowny", "03-10-2023+10:30:00"))

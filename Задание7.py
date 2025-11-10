all_stations, his_station, finish_station = map(int, input().split())

distance = (finish_station - his_station - 1 + all_stations) % all_stations

distance2 = (his_station - finish_station - 1 + all_stations) % all_stations
print(min(distance, distance2))
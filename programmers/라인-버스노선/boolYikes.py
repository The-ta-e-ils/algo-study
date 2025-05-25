from collections import deque
def solution(a, b, routes, record):
    # Routes graph init using dictionaries, marking each station's association with routes
    stations = {}
    for i, rt in enumerate(routes):
        for j, station in enumerate(rt):
            station_info = stations.get(station, {})

            rt_ids = station_info.get('rt_assoc', [])
            rt_ids.append(i)
            station_info['rt_assoc'] = rt_ids

            neighbors = station_info.get('neighbors', [])
            # add child if not self
            for child_cand in rt:
                if child_cand != station:
                    neighbors.append(child_cand)

            station_info['neighbors'] = neighbors
            stations[station] = station_info
    
    for start_route in stations[record[0]]['rt_assoc']:
        tracks_start = []
        # copy the empty track
        dq = deque([(record[0], stations[record[0]], start_route, a, tracks_start[:], start_route)])
        while dq:
            stn, curr, route, fee, tracks, prev_route = dq.popleft()
            print(f"Current: {(stn, curr, route, fee, tracks, prev_route)}")

            # Can you visit the same station again ? probably no. 
            # But can you visit the same station if it is for a transfer? -> let's assume no
            # So let's stick to never visiting the same node again because the problem constaint seems to be super loose
            if stn in tracks:
                print(f"Station {stn} in route {route}'s been already visited.")
                print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-")
                continue

            # Should not mutate the original tracks!!!! -> do not append!
            new_tracks = tracks + [stn]
            if new_tracks == record:
                print(f"Found the answer--tracks: {new_tracks}, fee:{fee + a}")
                return fee + a

            route_ids, neighbors = curr['rt_assoc'], curr['neighbors']

            for neighbor in neighbors:
                for next_route in stations[neighbor]['rt_assoc']:
                    if next_route == route and prev_route == route:
                        print(f"Same route. Fee: {fee} + {a}", end=" ")
                        dq.append((neighbor, stations[neighbor], next_route, fee + a, new_tracks, route))
                        print(f"Adding {(neighbor, stations[neighbor], next_route, fee + a, new_tracks, route)}")
                    else:
                        print(f"Transfer. Fee: {fee} + {b}", end=" ")
                        dq.append((neighbor, stations[neighbor], next_route, fee + b, new_tracks, route))
                        print(f"Adding {(neighbor, stations[neighbor], next_route, fee + b, new_tracks, route)}")
            print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-")
cases = [
    [10, 1, ["ABCD", "XYBZ"], ["A", "B", "Z"], 21],
    [10, 1, ["ABCD", "XYBZ"], ["X", "Z", "B","Y"], 40]
]

for c in cases:
    answer = solution(*c[:4])
    assert answer == c[4], f"Wrong. The answer should be {c[4]}, not {answer}"
    print(f"Case {c[:4]} passed: answer - {c[4]}")
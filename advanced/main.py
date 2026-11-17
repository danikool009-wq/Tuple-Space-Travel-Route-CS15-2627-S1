mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print("first destination on the journey:", mission_route[0])
print("last destination on the journey:", mission_route[-1])
print("all destinations:", len(mission_route))
print("Mission route:")
for destination in mission_route:
    print(destination)
if "Europa" in mission_route:
    print("europa is included in the route currently.")
else:
    print("europa is not included in the route, sucks for you.")
destination = input("Enter a destination: ").strip()

if destination in mission_route:
    print(f"{destination} is part of the mission route.")

    position = mission_route.index(destination)
    stops_from_start = position
    stops_from_end = len(mission_route) - 1 - position

    print(f"Stops away from the start: {stops_from_start}")
    print(f"Stops away from the end: {stops_from_end}")

    if stops_from_end > 0:
        print(f"Next stop: {mission_route[position + 1]}")
else:
    print(f"{destination} is not part of the mission route.")
destination = input("Enter a destination: ").strip()

if destination in mission_route:
    print(f"{destination} is part of the mission route.")

    position = mission_route.index(destination)
    stops_from_start = position
    stops_from_end = len(mission_route) - 1 - position

    print(f"Stops away from the start: {stops_from_start}")
    print(f"Stops away from the end: {stops_from_end}")

    if stops_from_end > 0:
        print(f"Next stop: {mission_route[position + 1]}")
else:
    print(f"{destination} is not part of the trip.")
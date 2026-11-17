mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)
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
print("\nMission route:")
for destination in mission_route:
    print(destination)
if "Europa" in mission_route:
    print("\neuropa is included in the route currently.")
else:
    print("\neuropa is not included in the route, sucks for you.")

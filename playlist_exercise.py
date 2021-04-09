playlist = {"name": "Monthly Mix April 2021",
            "creator": "Ravi",
            "songs": [
                {"title": "New Reality", "artists": [
                    "Patrick Topping", "Hayley Topping"], "album": "New Reality", "duration": 4.03},
                {"title": "LFO", "artists": "LFO",
                    "album": "LFO", "duration": 5.19},
                {"title": "Take A Look Around", "artists": "Limp Bizkit",
                    "album": "Chocolate Starfish", "duration": 5.21},
                {"title": "Nakhra Nawabi", "artists": [
                    "Dr Zeus", "Zora Randhawa", "Fateh"], "album": "Global Injection", "duration": 3.28},
            ]}

total_duration = 0

for song in playlist["songs"]:
    total_duration += song["duration"]
print(total_duration)

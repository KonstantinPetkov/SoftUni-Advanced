def add_songs(*data):
    songs_info = {}
    list_lyrics = []

    for current_data in data:
        title, lyrics = current_data
        if title not in songs_info:
            songs_info[title] = []
        songs_info[title] += lyrics

    for name, text in songs_info.items():
        list_lyrics.append(f'- {name}')
        for value in text:
            list_lyrics.append(value)

    return '\n'.join(list_lyrics)



print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
#
# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))

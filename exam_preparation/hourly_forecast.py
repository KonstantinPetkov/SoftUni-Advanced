def forecast(*data):
    weather = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    result = []

    for current_data in data:
        location_name, weather_name = current_data
        weather[weather_name].append(location_name)

    for key, value in weather.items():
        for town_name in sorted(value):
            result.append(f'{town_name} - {key}')

    return '\n'.join(result)



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
#
# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
#
# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))

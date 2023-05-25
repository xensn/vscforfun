def find_closest_object():
    timings = input("Enter the round trip times (seconds) separated by commas: ").split(",")
    timings = [float(time.strip()) for time in timings]

    if len(timings) < 5:
        print("Error: Please enter at least 5 round trip times.")
        return [-1, -1]

    closest_distance = float('inf')
    closest_index = -1

    for i, time in enumerate(timings):
        distance = time * 344 / 2
        if distance < closest_distance:
            closest_distance = distance
            closest_index = i

    print("Closest object index:", closest_index)
    print("Distance to closest object:", closest_distance, "m")

    return [closest_index, closest_distance]


# Call the function
find_closest_object()

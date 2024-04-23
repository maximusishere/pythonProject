robots = '30 50 70 80'
weight_limit = '100'

def platform(robots, weight_limit):
    robots_list = sorted(list(map(int, robots.split())))
    weight_limit = int(weight_limit)
    platform_count = 0
    left = 0
    right = len(robots_list) - 1

    while left <= right:

        if robots_list[right] > weight_limit:
            right -= 1

        elif robots_list[left] + robots_list[right] <= weight_limit:
            left += 1
            right -= 1
            platform_count += 1

        elif robots_list[right] == weight_limit:
            right -= 1
            platform_count += 1

        elif robots_list[right] < weight_limit:
            right -= 1
            platform_count += 1

        elif robots_list[right] == robots_list[left]:
            platform_count += 1
            break

    return platform_count

print(platform(robots, weight_limit))

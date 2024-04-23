a = int(input())
b = int(input())
def choose_one_to_exit(people_count, target_count):
    people = list(range(1, people_count+1))
    current_index = 0

    while len(people) > 1:
        current_index = (current_index + target_count - 1) % len(people)
        people.pop(current_index)

    return people[0]

print(choose_one_to_exit(a, b))
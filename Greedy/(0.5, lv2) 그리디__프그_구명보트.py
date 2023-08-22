# people: 몸무게 배열
# limit: 무게 제한


def solution(people: list, limit: int):
    total_boat = 0          # min of boat
    
    # Sort by DESCENDING order
    people.sort(key=lambda x: -x)
    num_of_people = len(people)
    
    # Set two pointer
    left_idx, right_idx = 0, num_of_people - 1
    
    while left_idx <= right_idx:
        # Take a maximum weight person.
        one_boat = people[left_idx]
        
        # Take some minimum weight people.
        if left_idx < right_idx and one_boat + people[right_idx] <= limit:
            one_boat = one_boat + people[right_idx]
            right_idx = right_idx - 1
        
        left_idx = left_idx + 1
        total_boat += 1

    return total_boat

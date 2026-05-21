"""
Title : List and Dictionary Operations.

Task: 
    ->to create a list
    ->to remove duplicates from the list
    ->create a dict containing max,min,avg values and frequency of each element
    ->print the result in a clear format.
"""

def prepare_dict(l: list[int], d=None) -> dict:
    """
    adds min,max,avg values 
    and frequencies of each element to the dictionary
    """
    if d is None:
        d = {}

    #adding values and their frequencies to dictionary
    for i in l:
        d[i] = d.get(i, 0) + 1

    #adding max,min , avg
    d["maximum"] = max(l)
    d["minimum"] = min(l)
    d["average"] = sum(l) / len(l)

    #returning the dict
    return d


def remove_duplicates(l: list[int]) -> list[int]:
    """removes duplicates from the list."""
    unique = set()
    res = []

    for i in l:
        #appending unique elements
        if i not in unique:
            unique.add(i)
            res.append(i)

    #returning updated list
    return res


def format_output(l: list[int], l_updated: list[int], d: dict) -> None:
    print(f"\nOriginal list : {l}")
    print(f"List without duplicates : {l_updated}")

    print("\nList Info:")
    print(f"Maximum valued element: {d['maximum']}")
    print(f"Minimum valued element: {d['minimum']}")
    print(f"Average value of the list: {d['average']}")

    print("\nFrequency Dictionary:")
    for key, value in d.items():
        if isinstance(key, int):
            print(f"value {key} repeated {value} time(s)")


if __name__ == "__main__":
    #taking list input
    try:
        print("Task-1\n")
        l = list(map(int, input("Enter list (space separated): ").split()))

        #checking empty input
        if not l:
            raise ValueError

        d = prepare_dict(l) #dict

        l_updated = remove_duplicates(l) #list without duplicates

        format_output(l, l_updated, d)

    except ValueError:
        print("Only integers are allowed as input")
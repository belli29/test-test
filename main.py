import json


def read_and_write(my_dict):
    j = json.dumps(my_dict)
    with open('a.json', 'w') as f:
        f.write(j)


my_dicto = {
    'name': "shila",
    'animal': "dog",
    'age': 13
}


if __name__ == '__main__':
    read_and_write(my_dicto)
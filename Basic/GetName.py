"""


The following code is not giving the expected results. Can you debug what the issue is?

The following is an example of data that would be passed in to the function.

data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]
get_names(data) # should return ['Joe', 'Bill', 'Kate']


"""


def get_names(data):
    result = []
    for i in range(len(data)):
        result.append(data[i]['name'])
    return result

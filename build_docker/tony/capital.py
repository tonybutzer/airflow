def capital_cities(**kwargs):
    # initialize an empty list to store the result
    result = []
    for key, value in kwargs.items():
        result.append("The capital city of {} is {}".format (key,value))

    return result

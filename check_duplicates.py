def check_duplicates(input_list):
    seen = set()
    duplicates = set(z for z in input_list if z in seen or seen.add(z))
    if duplicates:
        return list(duplicates)
    else:
        return "No duplicates"

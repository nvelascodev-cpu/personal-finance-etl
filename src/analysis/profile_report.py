
def print_dict_list_value(value, indent=0): #Recursividad
    space = " " * indent

    if isinstance(value, dict):
        for key, item in value.items():
            print(f"{space}{key}:")
            print_dict_list_value(item, indent + 4)

    elif isinstance(value, list):
        for element in value:
            print_dict_list_value(element, indent + 4)

    else:
        print(f"{space}{value}")

def print_profile(profile):
    print("---- General ----\n-----")
    print(f"Rows: {profile['rows']}")
    print(f"Columns: {profile['columns']}")

    print("\nData Types")
    print_dict_list_value(profile['data_types'])

    print("\nDuplicates")
    print_dict_list_value(profile['duplicates'])

    print("\nInvalid_values")
    print_dict_list_value(profile['invalid_values'])

    return



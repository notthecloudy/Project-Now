import random
import string

def generate_key():
    key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return key

def create_entry(value):
    key = generate_key()
    while check_validity(key) == "valid":
        key = generate_key()
    entry = f"key: {key} value: {value} view: 0\n"
    with open("database.txt", "a") as file:
        file.write(entry)
    return key, value

def read_database(line_number=None):
    if line_number is None:
        with open("database.txt", "r") as file:
            data = file.readlines()
    else:
        with open("database.txt", "r") as file:
            data = file.readlines()
        try:
            line = data[line_number].strip()
        except IndexError:
            line = None
        return line
    return data

def update_value(key, new_value):
    data = read_database()
    with open("database.txt", "w") as file:
        for line in data:
            if line.startswith(f"key: {key}"):
                file.write(f"key: {key} value: {new_value}\n")
            else:
                file.write(line)

def add_view(key):
    data = read_database()
    with open("database.txt", "w") as file:
        for line in data:
            if line.startswith(f"key: {key}"):
                parts = line.strip().split(" ")
                for i, part in enumerate(parts):
                    if part == "view:":
                        view_count = int(parts[i+1])
                        view_count += 1
                        parts[i+1] = str(view_count)
                updated_line = " ".join(parts) + "\n"
                file.write(updated_line)
            else:
                file.write(line)

def check_validity(key):
    data = read_database()
    for line in data:
        parts = line.strip().split(" ")
        if len(parts) >= 2 and parts[0] == "key:" and parts[1] == key:
            return "valid"
    return "invalid"

def delete_entry(key):
    data = read_database()
    with open("database.txt", "w") as file:
        for line in data:
            if not line.startswith(f"key: {key}"):
                file.write(line)

def refresh_keys():
    data = read_database()
    keys = []
    picked_keys = set()
    for line in data:
        parts = line.strip().split(" ")
        if len(parts) >= 2 and parts[0] == "key:":
            keys.append(parts[1])
    random.shuffle(keys)
    for key in keys:
        if key not in picked_keys:
            picked_keys.add(key)
            if len(picked_keys) == 10:
                break
    return list(picked_keys)

def refresh_values():
    data = read_database()
    values = []
    for line in data:
        parts = line.strip().split(" ")
        if len(parts) >= 4 and parts[0] == "key:" and parts[2] == "value:":
            values.append(parts[3])
    random.shuffle(values)
    return values[:10]



if __name__ == "__main__":
    pass

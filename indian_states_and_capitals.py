import json

def write_states_and_capitals_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    states_and_capitals_file_path = "states_and_capitals.json"
    write_states_and_capitals_to_json(states_and_capitals_file_path, indian_states_and_capitals)

import json
import argparse
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def remove_fields(data, fields):
    field_map = {
        'cpiu': 'collection_page_img_url',
        'hriu': 'high_res_img_url',
        'attr': 'attributes',
    }
    for item in data:
        if 'meta' in item:
            for field in fields:
                if field in field_map:
                    field = field_map[field]
                if field in item['meta']:
                    del item['meta'][field]

def change_to_ids_only(data):
    return [{"id": item["id"]} for item in data]

def change_to_name_only(data):
    for item in data:
        item['meta'] = {'name': item['meta']['name']}

def change_to_img_only(data, field, retain_attributes):
    new_data = []
    for item in data:
        new_item = {
            'id': item['id'],
            'meta': {
                'name': item['meta']['name'],
                field: item['meta'][field]
            }
        }
        if retain_attributes:
            new_item['meta']['attributes'] = item['meta'].get('attributes', [])
        new_data.append(new_item)
    return new_data

def replace_fields(data, find, replace):
    json_str = json.dumps(data)
    new_json_str = json_str.replace(find, replace)
    return json.loads(new_json_str)

def ids_from_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            ids = [line.strip() for line in file.readlines()]
        return [{"id": item} for item in ids]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

def identify_duplicates(data):
    id_count = {}
    duplicates = []
    for item in data:
        item_id = item['id']
        if item_id in id_count:
            duplicates.append(item_id)
        else:
            id_count[item_id] = True
    return duplicates

def remove_duplicates(data, duplicates):
    seen = set()
    new_data = []
    for item in data:
        item_id = item['id']
        if item_id not in seen:
            seen.add(item_id)
            new_data.append(item)
        else:
            duplicates.remove(item_id)
    return new_data

def main():
    parser = argparse.ArgumentParser(description="Edit JSON files")
    parser.add_argument("file_path", help="Path to the JSON file or TXT file containing IDs")
    parser.add_argument("-r", "--remove", nargs='+', help="Remove specified fields. Use shorthand aliases: 'cpiu' for 'collection_page_img_url', 'hriu' for 'high_res_img_url', 'attr' for 'attributes'")
    parser.add_argument("--ids-only", action="store_true", help="Convert to Inscription IDs Only")
    parser.add_argument("--name-only", action="store_true", help="Convert to Metadata with Name Only")
    parser.add_argument("--collection-img-only", action="store_true", help="Convert to Metadata with Collection Page Image Only")
    parser.add_argument("--high-res-only", action="store_true", help="Convert to Metadata with High-Resolution Image URL Only")
    parser.add_argument("--retain-attributes", action="store_true", help="Retain attributes when converting to image URL only")
    parser.add_argument("--find", help="String to find in the JSON")
    parser.add_argument("--replace", help="String to replace in the JSON")
    args = parser.parse_args()

    file_path = args.file_path

    if file_path.endswith('.txt'):
        ids = ids_from_txt(file_path)
        data = change_to_ids_only(ids)
    elif file_path.endswith('.json'):
        data = load_json(file_path)
    else:
        print("Error: Unsupported file format. Only JSON and TXT files are supported.")
        sys.exit(1)

    if args.remove:
        remove_fields(data, args.remove)

    if args.ids_only:
        data = change_to_ids_only(data)

    if args.name_only:
        change_to_name_only(data)

    if args.collection_img_only:
        data = change_to_img_only(data, 'collection_page_img_url', args.retain_attributes)

    if args.high_res_only:
        data = change_to_img_only(data, 'high_res_img_url', args.retain_attributes)

    if args.find and args.replace:
        data = replace_fields(data, args.find, args.replace)

    duplicates = identify_duplicates(data)
    if duplicates:
        print("Duplicate IDs found:", duplicates)
        confirmation = input("Do you want to remove duplicates? (yes/no): ")
        if confirmation.lower() == 'yes':
            data = remove_duplicates(data, duplicates)
            print("Duplicates removed.")
        else:
            print("Duplicates not removed.")

    print(json.dumps(data, indent=4))

    save_file_path = input("Enter the path to save the edited JSON file: ")
    save_json(data, save_file_path)
    print("Edited JSON saved successfully.")

if __name__ == "__main__":
    main()

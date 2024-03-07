# Bitcoin Ordinals JSON Editor - Magic Eden Listing

## Introduction

The Bitcoin Ordinals JSON Editor is a Python script designed to facilitate the manipulation and editing of JSON files containing Bitcoin Ordinal inscription data. It offers various functionalities for modifying the JSON structure according to the requirements of listing on the Magic Eden platform.

## Features

### 1. Loading and saving JSON files

The script provides functions to load and save JSON files, ensuring seamless editing of data.

### 2. Handling duplicates

The script includes functionality to identify and handle duplicate inscription IDs within the JSON data. If duplicates are found, the script prompts the user to confirm whether they should be removed. This ensures compliance with Magic Eden's listing guidelines, which require unique IDs for each inscription.

### 3. Removing fields

Fields such as 'collection_page_img_url', 'high_res_img_url', and 'attributes' can be removed from the JSON data using shorthand aliases or full field names.

### 4. Conversion functions

The script offers several conversion functions to transform the JSON data into different formats:

- `--ids-only`: Convert to Inscription IDs Only format.
- `--name-only`: Convert to Metadata with Name Only format.
- `--collection-img-only`: Convert to Metadata with Collection Page Image Only format.
- `--high-res-only`: Convert to Metadata with High-Resolution Image URL Only format.

### 5. Field replacement

Users can replace specific strings within the JSON data using the `--find` and `--replace` arguments. This feature is particularly useful for scenarios where adjustments are needed to specific field names, such as when switching between 'high_res_img_url' and 'collection_page_img_url' fields, as required by certain Magic Eden listing guidelines.

### 6. Integration with plain text files

The script supports reading IDs from plain text files and converting them into the `--ids-only` JSON format. This feature extends the usability of the script by allowing users to process raw hash data provided by creators.

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/cryptocav/ordinals-metatransform.git
```

2. **Navigate to the directory:**
```bash
cd ordinals-metatransform
```

*The script requires Python to be installed on your system.*

## Command line arguments

The script accepts the following command line arguments:

- `file_path`: Path to the input JSON file or TXT file containing IDs.
- `-r`, `--remove`: Specify fields to remove from the JSON data.
- `--ids-only`: Convert to Inscription IDs Only format.
- `--name-only`: Convert to Metadata with Name Only format.
- `--collection-img-only`: Convert to Metadata with Collection Page Image URL Only format.
- `--high-res-only`: Convert to Metadata with High-Resolution Image URL Only format.
- `--retain-attributes`: Retain attributes when converting to Image URL Only format.
- `--find`: String to find in the JSON.
- `--replace`: String to replace in the JSON.

### Shortened field aliases

The script utilizes shortened aliases for commonly used field names to simplify command-line usage. Here's a brief explanation of each alias:

- `cpiu`: Short for `collection_page_img_url`. Specifies the collection page image URL field.
- `hriu`: Short for `high_res_img_url`. Specifies the high-resolution image URL field.
- `attr`: Short for `attributes`. Specifies the attributes field.

These shortened aliases can be used interchangeably with their full field names when specifying fields for removal or replacement, enhancing the flexibility and ease of use of the script.

## Example usage

### 1. Handling duplicates

```bash
python metatransform.py my_data.json
```

This command will automatically identify and remove any duplicate inscription IDs within the dataset. Removal will require confirmation. You can also use this command to view the current state of the JSON.

### 2. Converting to Inscription IDs Only 

```bash
python metatransform.py my_data.json --ids-only
```

This command will convert the JSON data in my_data.json to Inscription IDs Only format, retaining only the inscription IDs.

### 3. Removing specific fields

```bash
python metatransform.py my_data.json --remove cpiu hriu
```

This command will remove the 'collection_page_img_url' and 'high_res_img_url' fields from the JSON data in my_data.json.

### 4. Converting to Metadata with Name Only

```bash
python metatransform.py my_data.json --name-only
```

This command will convert the JSON data in my_data.json to Metadata with Name Only format, retaining only the ID's and names of the inscriptions.

### 5. Converting to Metadata with Collection Page Image Only

```bash
python metatransform.py my_data.json --collection-img-only
```

This command will convert the JSON data in my_data.json to Metadata with Collection Page Image Only format, retaining only the Collection Page Image URLs, names and IDs.

### 6. Removing High-Resolution Image URL while retaining Attributes

```bash
python metatransform.py my_data.json --remove hriu --retain-attributes
```

This command will remove the "high_res_img_url" field from the JSON data while retaining the attributes.


### 7. Field replacement

```bash
python metatransform.py my_data.json --find "high_res_img_url" --replace "collection_page_img_url"
```

This command will replace all occurrences of 'high_res_img_url' with 'collection_page_img_url' in the JSON data of my_data.json.

### 8. Converting plain text file to Inscription IDs Only format

```bash
python metatransform.py my_data.txt --ids-only
```

This command will read the IDs from txtexample.txt and convert them into the Inscription IDs Only format.


## Integration with Magic Eden Bitcoin

- This script is designed to be used in conjunction with the [Magic Eden](https://magiceden.io) platform for listing Bitcoin Ordinal inscriptions. It offers functionalities to prepare JSON data in the required formats specified by Magic Eden's listing guidelines.
- Ensure that the JSON data provided follows the structure outlined in the Magic Eden [documentation](https://help.magiceden.io/en/articles/7957891-guide-to-listing-bitcoin-ordinal-inscriptions-on-magic-eden) for seamless integration.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

thonimport json

def export_to_json(data, filename):
    """Exports the scraped data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data successfully exported to {filename}")
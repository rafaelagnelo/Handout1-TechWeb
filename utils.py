from pathlib import Path
import json


def extract_route(request):
    lines = request.split('\n')
    first_line = lines[0]
    parts = first_line.split()
    route = parts[1][1:]
    return route

def read_file(file_path: Path) -> bytes:
    with open(file_path, 'rb') as file:
        content = file.read()
    return content
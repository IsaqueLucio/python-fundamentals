PAGES = {
    1: [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ],
    2: [
        {"id": 4, "name": "Diana"},
        {"id": 5, "name": "Eve"},
        {"id": 6, "name": "Frank"},
    ],
    3: [
        {"id": 7, "name": "Grace"},
        {"id": 8, "name": "Heidi"},
        {"id": 9, "name": "Ivan"},
    ],
}

def get_pages(page_number):
    return PAGES[page_number]


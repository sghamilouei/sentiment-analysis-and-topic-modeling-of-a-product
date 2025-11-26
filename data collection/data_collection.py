import csv
import requests

def retrieve_comments(product_id: str) -> list:
    # First request to get max_page
    url = f"https://api.digikala.com/v1/product/{product_id}/comments/?page=1"
    response = requests.get(url)
    response.raise_for_status()
    max_page = response.json()["data"]["pager"]["total_pages"]

    all_comments = []

    for page in range(1, max_page + 1):
        url = f"https://api.digikala.com/v1/product/{product_id}/comments/?page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error {response.status_code} on page {page}")
            break

        data = response.json()
        comments = data["data"]["comments"]
        all_comments.extend(comments)

    return all_comments


def write_to_csv(comments: list, file_name: str):
    rows = [["comment", "rate"]]
    data = [[c.get("body"), c.get("rate")] for c in comments]
    rows.extend(data)

    with open(f"{file_name}.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


data = retrieve_comments("16801385")
write_to_csv(data, "comments")

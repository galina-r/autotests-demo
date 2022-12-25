import pytest
import requests

domain_name = 'http://private-api.com'


# checking the title of the second book
def test_books_list():
    req_get = requests.get(f'{domain_name}/v1/books')
    req_get_json = req_get.json()
    books_list = req_get_json['data']
    assert books_list[1]['title'] == 'PHP & MySQL Novice to Ninja'


# checking the id of a new book
def test_new_book():
    req_post = requests.post(f'{domain_name}/v1/books', json={
        "data": {
            "title": "New Book about PHP",
            "pages": 123
        }
    })
    req_post_json = req_post.json()
    assert req_post_json['data']['id'] != None, "user was no added"


# checking the changing in third book
def test_changes_book():
    req_put = requests.put(f'{domain_name}/v1/books/3', json={
        "data": {
            "title": "PHP",
            "pages": 453
        }
    })
    req_put_json = req_put.json()
    req_get = requests.get(f'{domain_name}/v1/books')
    req_get_json = req_get.json()
    assert req_put_json['data'] in req_get_json['data'],  "was no changes"

# cheking of the deleted book
def test_deleted_book():
    req_delete = requests.delete(f'{domain_name}/v1/books/1')
    assert req_delete.status_code == 204,  "item wasn't deleted"
    req_get = requests.get(f'{domain_name}/v1/books/1')
    assert req_get.status_code == 404,  "item is still in directory"



import requests

from constants import *
from reqres_schemas import *

BASE_URL = "https://reqres.in/api"
headers = {"x-api-key": "reqres-free-v1"}


def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
    assert response.status_code == HTTP_200_OK
    data = UsersListResponse.model_validate(response.json())
    assert len(data.data) > 0


def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/{VALID_USER_ID}", headers=HEADERS)
    assert response.status_code == HTTP_200_OK
    data = SingleUserResponse.model_validate(response.json())
    assert data.data.id == VALID_USER_ID
    assert data.data.email == EXPECTED_EMAIL


def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/{INVALID_USER_ID}", headers=HEADERS)
    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.text == EMPTY_JSON_STRING


def test_create_user():
    payload = CreateUserRequest(name=CREATE_USER_NAME, job=CREATE_USER_JOB)
    response = requests.post(
        f"{BASE_URL}/users", json=payload.model_dump(), headers=HEADERS
    )
    assert response.status_code == HTTP_201_CREATED
    data = CreateUserResponse.model_validate(response.json())
    assert data.name == CREATE_USER_NAME
    assert data.job == CREATE_USER_JOB


def test_register_successful():
    payload = RegisterRequest(email=REGISTER_EMAIL_SUCCESS, password=REGISTER_PASSWORD)
    response = requests.post(
        f"{BASE_URL}/register", json=payload.model_dump(), headers=HEADERS
    )
    assert response.status_code == HTTP_200_OK
    data = RegisterSuccessfulResponse.model_validate(response.json())
    assert data.id > 0
    assert data.token


def test_register_unsuccessful():
    payload = RegisterRequest(email=REGISTER_EMAIL_FAIL)
    response = requests.post(
        f"{BASE_URL}/register",
        json=payload.model_dump(exclude_none=True),
        headers=HEADERS,
    )
    assert response.status_code == HTTP_400_BAD_REQUEST
    data = RegisterUnsuccessfulResponse.model_validate(response.json())
    assert data.error == ERROR_MISSING_PASSWORD

import random

from sNeeds.utils import skyroom
from sNeeds.settings.passwords import ALL_SKYROOM_USERS_PASSWORD

NUMBER_OF_TRIES = 5
s = skyroom.SkyroomAPI()


def _get_all_users():
    for i in range(0, NUMBER_OF_TRIES):
        response = s.getUsers()
        if response.get('ok'):
            break
        if i == NUMBER_OF_TRIES - 1:
            raise Exception("1")

    all_users = response.get("result")
    return all_users


def _check_user_in_all_users(username, all_users):
    for user_dict in all_users:
        if username == user_dict.get("username"):
            return True
    return False


def _get_user_id_in_all_users(username, all_users):
    for user_dict in all_users:
        if username == user_dict.get("username"):
            return user_dict.get("id")
    return None


def create_user_or_get_current_id(username, password, nickname, email, expiry_date=None):
    params = {
        "username": username,
        "password": password,
        "nickname": nickname,
        "email": email,
        "expiry_date": expiry_date,
        "status": 1,
        "is_public": False
    }
    all_users = _get_all_users()

    if not _check_user_in_all_users(username, all_users):

        for i in range(0, NUMBER_OF_TRIES):
            response = s.createUser(params=params)

            if response.get('ok'):
                break

            if i == NUMBER_OF_TRIES - 1:
                raise Exception("1")

        user_id = response.get("result")

    else:
        user_id = _get_user_id_in_all_users(username, all_users)

    return user_id


def _get_all_rooms():
    for i in range(0, NUMBER_OF_TRIES):
        response = s.getRooms()
        if response.get('ok'):
            break
        if i == NUMBER_OF_TRIES - 1:
            raise Exception("1")

    all_rooms = response.get("result")
    return all_rooms


def _check_room_in_all_rooms(room_title, all_rooms):
    for room_dict in all_rooms:
        if room_title == room_dict.get("title"):
            return True
    return False


def _get_room_id_in_all_rooms(room_title, all_rooms):
    for room_dict in all_rooms:
        if room_title == room_dict.get("title"):
            return room_dict.get("id")
    return None


def create_room_or_get(room_id):
    name = "مشاوره اسنیدز {}".format(room_id)
    title = "مشاوره اسنیدز {}".format(room_id)

    params = {
        "name": name,
        "title": title,
        "guest_login": False,
        "op_login_first": False,
        "max_users": 3
    }

    all_rooms = _get_all_rooms()

    if not _check_room_in_all_rooms(title, all_rooms):
        for i in range(0, NUMBER_OF_TRIES):

            response = s.createRoom(params=params)
            if response.get('ok'):
                break
            if i == NUMBER_OF_TRIES - 1:
                raise Exception("1")
        room_id = response.get("result")
    else:
        room_id = _get_room_id_in_all_rooms(title, all_rooms)

    return room_id


def _get_user_all_rooms(user_id):
    params = {
        "user_id": user_id
    }
    for i in range(0, NUMBER_OF_TRIES):
        response = s.getUserRooms(params=params)
        if response.get('ok'):
            break
        if i == NUMBER_OF_TRIES - 1:
            raise Exception("1")

    return response.get("result")


def _is_user_in_rooms(room_id, user_rooms):
    for room_dict in user_rooms:
        if room_id == room_dict.get("room_id"):
            return True
    return False


def _remove_user_from_room(user_id, room_id):
    params = {
        "user_id": user_id,
        "rooms": [room_id, ]
    }

    for i in range(0, NUMBER_OF_TRIES):
        response = s.removeUserRooms(params=params)
        if response.get('ok'):
            break
        if i == NUMBER_OF_TRIES - 1:
            raise Exception("1")


def make_user_room_presentor(user_id, room_id):
    params = {
        "room_id": room_id,
        "users": [
            {"user_id": user_id, "access": 2}
        ]
    }

    user_all_rooms = _get_user_all_rooms(user_id)

    if _is_user_in_rooms(room_id, user_all_rooms):
        _remove_user_from_room(user_id, room_id)

    for i in range(0, NUMBER_OF_TRIES):
        response = s.addRoomUsers(params=params)
        if response.get('ok'):
            break
        if i == NUMBER_OF_TRIES - 1:
            raise Exception("1")


def get_login_url_without_password(user_id, room_id):
    params = {
        "user_id": user_id,
        "room_id": room_id,
        "language": "fa",
        "ttl": 7200
    }

    for i in range(0, NUMBER_OF_TRIES):
        response = s.getLoginUrl(params=params)
        if response.get('ok'):
            break

        if i == NUMBER_OF_TRIES - 1:
            raise Exception("1")

    return response.get('result')


def create_2members_chat_room(user1id, nickname1, user1email, user2id, nickname2, user2email, roomid):
    username1 = "sneeds_user_{}_for_roomid_{}".format(str(user1id), str(roomid))
    username2 = "sneeds_user_{}_for_roomid_{}".format(str(user1id), str(roomid))

    if nickname1 == "" or nickname1 is None:
        nickname1 = "کاربر"

    if nickname2 == "" or nickname2 is None:
        nickname2 = "مشاور"

    user1_id = create_user_or_get_current_id(username1, ALL_SKYROOM_USERS_PASSWORD, nickname1, user1email, expiry_date=1565948998)
    user2_id = create_user_or_get_current_id(username2, ALL_SKYROOM_USERS_PASSWORD, nickname2, user2email, expiry_date=1565948998)

    room_id = create_room_or_get(roomid)

    make_user_room_presentor(user1_id, room_id)
    make_user_room_presentor(user2_id, room_id)

    user1_url = get_login_url_without_password(user1_id, room_id)
    user2_url = get_login_url_without_password(user2_id, room_id)

    return user1_url, user2_url

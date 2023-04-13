import requests

URL = f"https://my.dtm.uz/api-push/ilmiy-markaz?"
LIST_SERVICES_URL = f"https://my.dtm.uz/api-push/list-service"
HEADERS = {'Authorization': 'HASH_4e13e96538e5cc63f386259fd3e0400cfcfe8f32c'}


def get_all_data(url, headers):
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    return data['data']


def get_page(url, headers):
    response = requests.get(url=url, headers=headers, verify=False)
    data = response.json()['pages']
    count_element = data['totalCount']
    defaultPageSize = data['defaultPageSize']
    count_page = None
    k = round(count_element / defaultPageSize)
    q = count_element % defaultPageSize
    if q != 0 and count_element > (defaultPageSize * k):
        count_page = k + 1
    if q != 0 and count_element < (defaultPageSize * k):
        count_page = k
    if q == 0:
        count_page = k
    return count_page


def get_data(test_day, Users, course_name, service_id):
    reg_count = 0
    pay_count = 0
    for user in Users:
        if user['pay'] == 1 and user['test_day'] == test_day:
            pay_count += 1
        if user['test_day'] == test_day:
            reg_count += 1

    data = {
        "service_id": service_id,
        "reg_count": reg_count,
        "pay_count": pay_count,
        "course_name": course_name,
        "test_day": test_day,
    }

    return data

import requests

jshshr = 41605975930036
course_id = 4

token = {"Authorization": "Token 66e3b4335550532ed469eeda7feaa07027253eae"}
endpoint = f"http://192.168.0.87:443/api/?jshshr={jshshr}&course={course_id}"

response = requests.post(endpoint, headers=token)
if response.status_code == 200:
    print("token invalid")
else:
    get_response = requests.get(endpoint, headers=token)
    data = get_response.json()
    try:
        print(data[0]['pdf_certificate'])
    except IndexError:
        print("Bu kursda o'qimagansiz")

import unittest, requests, json, jsonpath, datetime

class TestAPI(unittest.TestCase):

    def test_GET_user(self):
        url = 'https://restful-booker.herokuapp.com/booking/3'
        must_content = ['firstname','lastname','totalprice','depositpaid','bookingdates','additionalneeds']
        header_content = 'application/json; charset=utf-8'
        #GET data info
        response = requests.get(url)
        key_headers = response.headers
        # GET booking{id} keys
        json_response = json.loads(response.text)
        key_list = list(json_response)
        # Check header content
        actual_header = key_headers['Content-Type']
        #Check bookingdates format
        data = jsonpath.jsonpath(json_response, 'bookingdates')
        checkin = data[0]['checkin']
        checkout = data[0]['checkout']
        exp_pat = "YYYY-MM-DD"

        def date_patern(date_text):
            try:
                datetime.datetime.strptime(date_text, '%Y-%m-%d')
                return "YYYY-MM-DD"
            except Valuerror:
                raise Valuerror("Incorrect date format, not YYYY-MM-DD")

        assert response.status_code == 200
        # Header content
        assert header_content == actual_header
        #Must content
        assert must_content == key_list
        #Date format
        assert exp_pat == date_patern(checkin)
        assert exp_pat == date_patern(checkout)
        print("Content header:PASS")
        print("Body content: PASS")
        print("Booking date format: PASS")

    def test_DELETE_user(self):
        url = 'https://restful-booker.herokuapp.com/auth'
        token = {"username": "admin",
                 "password": "password123"}
        response = requests.post(url, data=token)
        get_token = json.loads(response.text)
        url = 'https://restful-booker.herokuapp.com/booking/5'
        response_del = requests.delete(url, cookies=get_token)
        assert response_del.status_code == 201
        assert response_del.text == 'Created'
        print(response_del.text)

if __name__ == '__main__':
    unittest.main()

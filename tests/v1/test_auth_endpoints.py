"""This module contains tests to user authentication endpoints"""

import json

from . import base_test
from . import general_helper_functions

class TestUserAuthEndpoints(base_test.BaseTestClass):

    def test_add_new_user_with_all_data(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "newuser@gmail.com",
        "role": "Admin",
        "password": "Password1@"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['email'], "newuser@gmail.com")
        self.assertEqual(res.status_code, 202)
    
    def test_add_new_user_already_existing(self):
        
        """Test POST /auth/signup"""
        self.register_admin_test_account()
        response = self.register_admin_test_account()
        data = json.loads(response.data.decode())

        self.assertEqual(data['message'], "User already exists in the system")
        self.assertEqual(response.status_code, 406)

    def test_add_new_user_with_no_data(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={}, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(res)

        self.assertEqual(data['message'], "Missing critical credentials")
        self.assertEqual(res.status_code, 400)

    def test_add_new_user_with_some_missing_parameter(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "",
        "role": "Admin",
        "password": "Password2#"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "You are missing critical information")
        self.assertEqual(res.status_code, 400)
    
    def test_add_new_user_short_password(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "testnewuser@gmail.com",
        "role": "Admin",
        "password": "Less#"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "Password must range between 6 to 12 characters")
        self.assertEqual(res.status_code, 400)

    def test_add_new_user_with_invalid_email(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "newuser",
        "role": "Admin",
        "password": "Password12#"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "Invalid email")
        self.assertEqual(res.status_code, 400)

    def test_add_new_user_with_no_digit_in_password(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "testnewuser@gmail.com",
        "role": "Admin",
        "password": "@Nodigit"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "Password must include at least one digit")
        self.assertEqual(res.status_code, 400)
    
    def test_add_new_user_with_no_upper_case_in_password(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "testingnewuser@gmail.com",
        "role": "Admin",
        "password": "noupper2@"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "Password must include at least one upper case character")
        self.assertEqual(res.status_code, 400)
    
    def test_add_new_user_with_no_lower_case_in_password(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "testingnewuser@gmail.com",
        "role": "Admin",
        "password": "NOLOWER2@"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "Password must include at least one lower case character")
        self.assertEqual(res.status_code, 400)

    def test_add_new_user_with_no_special_char_in_password(self):

        res = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "testingnewuser@gmail.com",
        "role": "Admin",
        "password": "Nospecial2"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        data = json.loads(res.data.decode())
        print(data)

        self.assertEqual(data['message'], "Password must include at least one special charater")
        self.assertEqual(res.status_code, 400)
    
    def test_login_with_no_credentials(self):

        self.register_admin_test_account()
        resp = self.app_test_client.post("api/v1/auth/login",
        json={

        },
        headers={
        "Content-Type": "application/json"
        })

        self.assertTrue(general_helper_functions.convert_json(
        resp)['message'], "Kindly provide your credentials")
        self.assertEqual(resp.status_code, 400)
 
    def test_login_already_existing_user(self):

        self.register_admin_test_account()
        resp = self.app_test_client.post("api/v1/auth/login",
        json={
            "email": "admin@gmail.com",
            "password": "Password2@"
        },
        headers={
        "Content-Type": "application/json"
        })

        self.assertTrue(general_helper_functions.convert_json(
        resp)['token'])
        self.assertTrue(general_helper_functions.convert_json(
        resp)['message'], "You are successfully logged in!")
        self.assertEqual(resp.status_code, 200)

    def test_login_user_with_no_matching_credentials(self):

        self.register_admin_test_account()
        resp = self.app_test_client.post("api/v1/auth/login",
        json={
            "email": "nomatchingusercredentials@gmail.com",
            "password": "notevensure"
        },
        headers={
        "Content-Type": "application/json"
        })

        self.assertTrue(general_helper_functions.convert_json(
        resp)['message'], "Wrong credentials provided")
        self.assertEqual(resp.status_code, 403)
    
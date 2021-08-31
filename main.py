from netcat import Netcat
import os

# email information
email_info = {"sender": "", "receiver": "", "subject": "", "content_file": ""}

keys = email_info.keys()

for key in keys:
    email_info[key] = input(f'please enter {key}: ')

print(email_info)

if os.path.exists(email_info.get('content_file')):
    with open(email_info.get('content_file'), 'r') as f :
        data = f.read()

    # connect to server
    netcat = Netcat()
    netcat.connect()
    netcat.write(data)
    print(str(netcat.read()))
else:
    print('file not found')
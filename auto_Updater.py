import os
import time as timer

# Path: auto_Updater.py
time = 3600 # 1 hour
def Node_update():
    os.system('sudo npm install -g pm2');
    os.system('sudo pm2 update');
    os.system('sudo npm install -g npm@latest');
    os.system('sudo npm install -g express');
    os.system('sudo npm install -g body-parser@latest');
    os.system('sudo npm install -g mongoose@latest');
    os.system('sudo npm install -g express-session@latest');
    os.system('sudo npm install -g cookie-parser@latest');
    os.system('sudo npm install -g express-validator@latest');
    os.system('sudo npm install -g express-flash@latest');
    os.system('sudo npm install -g jsonwebtoken@latest');
    os.system('sudo npm install -g bcryptjs@latest');
    os.system('sudo npm install -g nodemailer@latest');
    os.system('sudo npm install -g cors@latest');
    os.system('sudo npm install -g multer@latest');
    os.system('sudo npm install -g multer-s3@latest');
    os.system('sudo npm install -g unique-random@latest');
    os.system('sudo npm install -g uuid@latest');
    os.system('sudo npm install -g axios@latest');
#loop to run the function every 10 seconds
while True:
    timer.sleep(1)
    time = time - 1
    if time == 0:
        Node_update()
        time = 3600 # 1 hour
    else:
        print('Waiting for Update in ' + str(time) + ' Seconds')

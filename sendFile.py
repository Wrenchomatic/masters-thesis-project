import os
import paramiko
import time


while (True):
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect("192.168.43.209", username="pi", password="rasp123berry!/")

    sftp = ssh.open_sftp()
    sftp.put("/home/pi/Desktop/picture.jpg", "/home/pi/Desktop/project/masters-thesis-project/djangoWebApp/static/images/picture.jpg")
    sftp.close()
    ssh.close()
    time.sleep(30)

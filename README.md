# Proxer
<h1 align="center">
    Proxer
    <br>
    <div align="center">
    <img src="https://img.shields.io/badge/Python-3.10.6-blue" align="center"/>
    <img src="https://img.shields.io/badge/proxmoxer-2.0.1-orange" align="center"/>
    <img src="https://img.shields.io/badge/Developing-Active-brightgreen" align="center"/>
    <img src="https://img.shields.io/badge/Version-1.0-green" align="center"/>
    </div>
</h1>

A little private tool i use as a proxmox user. Its a simple terminal based proxmox status panel

# Example
<img src="https://raw.githubusercontent.com/AIO-Develope/Proxer/main/images/proxer.PNG" width="40%" height="40%"/>

# Installation
```
Pillow==9.4.0
Pillow==9.5.0
proxmoxer==2.0.1
pystray==0.19.4
termcolor==2.3.0
urllib3==1.26.14
```
To install the requirements run:
```
pip install -r requirements.txt
```

Now rename ```example.config.json``` to config.json and change the informations to youre desire.

```
{
    "proxmox-address": "ip:port or domain", //  the domain or ip with port to youre proxmox dashboard
    "user": "for example: root@pam",        //  the username with auth type
    "password": "banana1234",               //  youre users password
    "ssl": false                            //  if using ssl (https) enable this
}
```
now you can start it with
```
1. python main.py  // it will just start the programm in the terminal
```
```
2. python icon.py  // this will start it in the System Tray
```
# Info

This project is just a randome upload i will not focus on it! but if someone ask for an improvement i will hear it.

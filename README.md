# what is pyPassword?
secure password manager written in python !


# Screenshots
![pyPassword](https://github.com/RedMads/pyPassword/blob/main/screenshots/sign_up.png)
![pyPassword](https://github.com/RedMads/pyPassword/blob/main/screenshots/login.png)
![pyPassword](https://github.com/RedMads/pyPassword/blob/main/screenshots/menu.png)
![pyPassword](https://github.com/RedMads/pyPassword/blob/main/screenshots/list_data.png)


# install for linux
***
~~~
sudo apt install git python python3

git clone https://github.com/RedMads/pyPassword.git && cd pyPassword

chmod +x installers/install_linux.sh && chmod +x update.sh

bash installers/install_linux.sh

python3 main.py
~~~

# install for termux
***
~~~
pkg install git

git clone https://github.com/RedMads/pyPassword.git && cd pyPassword

chmod +x installers/install_termux.sh && chmod +x update.sh

bash installers/install_termux.sh

python3 main.py
~~~

# install for windows
***
make sure youre install python language from [Here](https://python.org/)

Download the repo zip extract it

and double click on `installers/install_win.bat`
it will install some librarys the program will need
when the install is done just double click on `main.py`
it will execute the program follow the sign up !


# update
***
to update this program just execute `update.sh` file !

# attention !
***
to add more security convert the progrom from py source code to executable using PyInstaller module!

make sure you in the pyPassword directory!
```
pip3 install PyInstaller

python3 -m PyInstaller --onefile main.py

mv dist/main .

rm dist build -rf

rm main.spec

chmod +x main && ./main
```

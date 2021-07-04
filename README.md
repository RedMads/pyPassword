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
sudo apt install git

git clone https://github.com/RedMads/pyPassword.git

cd pyPassword

chmod +x install.sh && chmod +x update.sh

bash install.sh

python3 main.py
~~~

# install for termux
***
~~~
pkg install git

git clone https://github.com/RedMads/pyPassword.git

cd pyPassword

chmod +x install_termux && chmod +x update.sh

bash install_termux.sh

python3 main.py
~~~

# update
***
to update this program just execute ~update.sh~ file !

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

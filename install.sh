
#check if this script run as root or not
if [ "$EUID" -ne 0 ]; then

    echo "[!] Run this script as root!"
    exit

fi

# install some good things !
apt update -y && apt upgrade -y
apt install git python python3 python3-pip -y

pip3 install cryptography prettytable bcrypt


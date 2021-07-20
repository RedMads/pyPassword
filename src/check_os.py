# This File to check if user use linux or termux !
import os


class Check_os:


    def __init__(self):

        self.cwd = os.getcwd()

    # check the os by trying to change directory to "/usr"
    # if no Errors is linux OS
    # if There's Error is Termux
    def check_os(self):

        try:

            os.chdir("/usr")
            os.chdir(self.cwd)
            return "linux"

        except FileNotFoundError:

            return "termux"

    # check if it is linux !
    def is_linux(self):

        if self.check_os() == "linux": return True
        else: return False

    # check if it is termux !
    def is_termux(self):

        if self.check_os() == "termux": return True
        else: return False
    
    # check if it is windows !
    def is_windows(self):

        if os.name == "nt": return True
        else: return False

    # this function clear in different opreating systems (Linux, Windows)
    def clear(self):

        if os.name == "nt": os.system("cls")
        else: os.system("clear")


# Test !
if __name__ == "__main__":

    os_obj = Check_os()

    print("is it linux? : {}".format(os_obj.is_linux()))
    print("is it termux? : {}".format(os_obj.is_termux()))

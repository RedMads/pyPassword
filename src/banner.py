# this file for banner!


# print banner 
def Banner():


    with open("resources/banner.txt") as file:

        print(file.read()); file.close()







# Test the banner !
if __name__ == "__main__":

    Banner()
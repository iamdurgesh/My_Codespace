def welcome():
    print("This is a test file to learn how to import files in python")
    
# print(__name__)


# to prevent the function to run only when it is called from inside, otherwise it won't run while importing to other file
if __name__ == "__main__":
    welcome()

        
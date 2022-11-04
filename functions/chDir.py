import os
req_path = input("Enter path to change Dir: ")
# print("Now your New working Directory is: ", os.getcwd())
def main():
    try: 
        os.chdir(req_path)
        print("Now your New working Directory is: ", os.getcwd())
    except FileNotFoundError:
        print("Given path is not a valid Path. So cant Change Working Directory.")
    except NotADirectoryError: 
        print("Given path is file. So cant Change Working Directory.")
    except PermissionError: 
        print("Sorry you dont have access to given path. So cant Change Working Directory.")
    except Exception as e:
        print(e)
    return None
if __name__=="__main__":
    main()
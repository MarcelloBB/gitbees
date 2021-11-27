from utils import repolist
from utils import userdata
from gitcolors import Gitcolors as gc

def main():
    # Username
    print(gc.white)
    print(f"[🛠️] Enter Username: {gc.res}",end="")

    username = input("")

    # Request
    if username is not None:
        repo = repolist.RepoList(username)
        udata = userdata.UserData(username)

    else:
        main()

    print()

    print("Please select a option below:")
    print(f"{gc.white}[1]{gc.res} - {gc.cyan}See repositories 📚{gc.res}")
    print(f"{gc.white}[2]{gc.res} - {gc.cyan}See user data 💡{gc.res}")
    print()
    
    # Option
    option = input("Enter option: ")
    print()

    if option == "1":
        repo.listRepos()

    elif option == "2":
        udata.ShowData()

if __name__ == "__main__":
    main()
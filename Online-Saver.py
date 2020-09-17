import os


print('''


                ░█████╗░███╗░░██╗██╗░░░░░██╗███╗░░██╗███████╗        ░██████╗░█████╗░██╗░░░██╗███████╗██████╗░
                ██╔══██╗████╗░██║██║░░░░░██║████╗░██║██╔════╝        ██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
                ██║░░██║██╔██╗██║██║░░░░░██║██╔██╗██║█████╗░░        ╚█████╗░███████║╚██╗░██╔╝█████╗░░██████╔╝
                ██║░░██║██║╚████║██║░░░░░██║██║╚████║██╔══╝░░        ░╚═══██╗██╔══██║░╚████╔╝░██╔══╝░░██╔══██╗
                ╚█████╔╝██║░╚███║███████╗██║██║░╚███║███████╗        ██████╔╝██║░░██║░░╚██╔╝░░███████╗██║░░██║
                ░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝╚═╝░░╚══╝╚══════╝        ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝ by 1Syntaxxx1

    ''')


url = input("Enter file url: ")

print("\nExamples:  \n>> pdf.\n>> jpeg or jpg.\n>> png.\n>> doc.\n>>mp4/3.\n=> etc...")
ext = input("what is the file extension? ")

print("\nThe file will be present in the current directory.")
nameoffile = input("What do you want the file to be named? ")

downloadcommand = ("curl -o " + nameoffile + "." + ext + " " + url)

try:
    os.system(downloadcommand)
    print("Done!")
except:
    Exception("An Unexpected Error(s) Occurred!")

import argparse
from colorama import Fore, Style
from ReadConfig import *

# parser
parser = argparse.ArgumentParser()
parser.add_argument('pda_file', help='PDA file name (.txt)')
parser.add_argument('html_file', help='HTML file name (".html")', type=argparse.FileType('r'))
args = parser.parse_args()

# akses file
pda_file = args.pda_file
html_file = args.html_file.name

# splash screen
print(f'''{Fore.CYAN}
    htmlgtv++
    __  __________  _____         ________  ________________ __ __________ 
   / / / /_  __/  |/  / /        / ____/ / / / ____/ ____/ //_// ____/ __ \\
  / /_/ / / / / /|_/ / /        / /   / /_/ / __/ / /   / ,<  / __/ / /_/ /
 / __  / / / / /  / / /___     / /___/ __  / /___/ /___/ /| |/ /___/ _, _/ 
/_/ /_/ /_/ /_/  /_/_____/     \____/_/ /_/_____/\____/_/ |_/_____/_/ |_| 
{Style.RESET_ALL}''')

# display
print(Fore.YELLOW + f"Checking {html_file}, please wait..." + Style.RESET_ALL)

# proses cek file html
with open(html_file, 'r') as file:
    file_contents = file.read()
# print(file_contents) #delete
pda.start(file_contents)

isAccepted = True
if isAccepted:
    print(Fore.GREEN + "\nAccepted\n"+ Style.RESET_ALL)
else:
    print(Fore.RED + "\nRejected\nSyntax Error\n"+ Style.RESET_ALL)
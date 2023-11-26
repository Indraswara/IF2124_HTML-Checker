import argparse
from colorama import Fore, Style
from ReadConfigNopal import *

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

# wait screen
print("PDA file     : ",pda_file)
print("HTML file    : ",html_file)
print(Fore.YELLOW + f"Checking {html_file}, please wait..." + Style.RESET_ALL)

# proses cek file html
with open(html_file, 'r') as file:
    html_file_contents = file.read()
checkPDA(pda_file,html_file_contents)
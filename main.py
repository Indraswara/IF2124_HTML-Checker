import argparse
from colorama import Fore, Style
from ConfigParser import parsePDAConfig
from PDA import PDA

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
   ▄█    █▄        ███       ▄▄▄▄███▄▄▄▄    ▄█                                         
  ███    ███   ▀█████████▄ ▄██▀▀▀███▀▀▀██▄ ███                                         
  ███    ███      ▀███▀▀██ ███   ███   ███ ███                                         
 ▄███▄▄▄▄███▄▄     ███   ▀ ███   ███   ███ ███                                         
▀▀███▀▀▀▀███▀      ███     ███   ███   ███ ███                                         
  ███    ███       ███     ███   ███   ███ ███                                         
  ███    ███       ███     ███   ███   ███ ███▌    ▄                                   
  ███    █▀       ▄████▀    ▀█   ███   █▀  █████▄▄██                                   
                                           ▀                                           
 ▄████████    ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████
███    ███   ███    ███     ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███
███    █▀    ███    ███     ███    █▀  ███    █▀    ███▐██▀     ███    █▀    ███    ███
███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀
███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀  
███    █▄    ███    ███     ███    █▄  ███    █▄    ███▐██▄     ███    █▄  ▀███████████
███    ███   ███    ███     ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███
████████▀    ███    █▀      ██████████ ████████▀    ███   ▀█▀   ██████████   ███    ███
                                                    ▀                        ███    ███
{Fore.WHITE}by {Fore.RED}h{Fore.LIGHTRED_EX}t{Fore.YELLOW}m{Fore.YELLOW}l{Fore.GREEN}g{Fore.LIGHTGREEN_EX}t{Fore.CYAN}v{Fore.BLUE}+{Fore.LIGHTBLUE_EX}+
{Style.RESET_ALL}''')

# wait screen
print("PDA file     : ", pda_file)
print("HTML file    : ", html_file)
print(Fore.YELLOW + f"Checking {html_file}, please wait..." + Style.RESET_ALL)

# proses cek file html
with open(html_file, 'r') as file:
    html_content = file.read()

with open(pda_file, 'r') as file:
    pda_content = file.read()

[startState, startStack, transition] = parsePDAConfig(pda_content)

pda = PDA(startState, startStack, transition)
pda.start(html_content)
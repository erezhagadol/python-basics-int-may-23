import datetime
import hello
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
print(Back.GREEN + Fore.BLACK + f"{datetime.date.today()}")



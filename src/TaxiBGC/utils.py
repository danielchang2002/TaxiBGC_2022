import os

# get the directory that contains this script
taxibgc_script_install_folder = os.path.dirname(os.path.abspath(__file__))
# get the default database folder
DEFAULT_DB_FOLDER = os.path.join(taxibgc_script_install_folder, "TaxiBGC_databases")
string = """
████████╗░█████╗░██╗░░██╗██╗██████╗░░██████╗░░█████╗░
╚══██╔══╝██╔══██╗╚██╗██╔╝██║██╔══██╗██╔════╝░██╔══██╗
░░░██║░░░███████║░╚███╔╝░██║██████╦╝██║░░██╗░██║░░╚═╝
░░░██║░░░██╔══██║░██╔██╗░██║██╔══██╗██║░░╚██╗██║░░██╗
░░░██║░░░██║░░██║██╔╝╚██╗██║██████╦╝╚██████╔╝╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░░╚═════╝░░╚════╝░
"""

def logo():
  splits = [(0, 9), (9, 17), (17, 25), (25, 28), (28, 36), (36, 45), (45, 53)]

  class bcolors:
      HEADER = "\033[95m"
      OKBLUE = "\033[94m"
      OKCYAN = "\033[96m"
      OKGREEN = "\033[92m"
      WARNING = "\033[93m"
      FAIL = "\033[91m"
      ENDC = "\033[0m"
      BOLD = "\033[1m"
      UNDERLINE = "\033[4m"

  colors = [
    bcolors.HEADER,
    bcolors.OKBLUE,
    bcolors.OKCYAN,
    bcolors.OKGREEN,
    bcolors.WARNING,
    bcolors.FAIL,
    bcolors.HEADER,
    ]

  taxi_logo = "\n".join([
  "".join([color + st[split[0]:split[1]] + bcolors.ENDC for color, split in zip(colors, splits)])
  for st in string.split("\n")[1:-1]])

  return taxi_logo
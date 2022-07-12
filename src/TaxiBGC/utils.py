import os

# get the directory that contains this script
taxibgc_script_install_folder = os.path.dirname(os.path.abspath(__file__))
# get the default database folder
DEFAULT_DB_FOLDER = os.path.join(taxibgc_script_install_folder, "TaxiBGC_databases")
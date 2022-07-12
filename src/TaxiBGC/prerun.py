import subprocess

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


def print_check_message(boolean):
    print(
        bcolors.OKGREEN + "passed" + bcolors.ENDC
        if boolean
        else bcolors.FAIL + "failed" + bcolors.ENDC
    )

version_dict = {
    "repair.sh": "38.90",
    "bowtie2": "2.4.4",
    "metaphlan": "3.0.13",
}

def check_tool(tool):
    gt = version_dict[tool]
    print(tool, "version:", gt)
    flag = "--version"
    cmd = [tool, flag]
    try:
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if not tool == "repair.sh":
            output = proc.stdout.read().decode("ASCII")
        else:
            output = proc.stderr.read().decode("ASCII")
        correct = gt in output
    except:
        correct = False
    print_check_message(correct)
    if not correct:
        if tool == "repair.sh":
            tool = "bbmap"
        print(bcolors.WARNING + tool, "not found on path or wrong version")
        print(
            'please run: "conda install -c bioconda',
            tool + "=" + gt + '"',
            bcolors.ENDC,
        )
    print()
    return correct

def check_versions():
    print(
        "-" * 5,
        "Version checks",
        "-" * 5,
    )
    any_failed = False
    for tool in version_dict:
        if not check_tool(tool):
            any_failed = True
    if any_failed:
        print(
            bcolors.FAIL,
            "Please (re)install dependencies with above instructions and rerun",
            bcolors.ENDC,
        )
    else:
        print(
            bcolors.OKGREEN,
            "All dependencies up to date",
            bcolors.ENDC,
        )
    print("-" * 5, "Version checks done", "-" * 5, "\n")
    return not any_failed
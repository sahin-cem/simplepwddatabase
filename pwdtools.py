class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def linestripsplit(file, splitter):
    with open(file, "rb") as fobj:
        userpass = {}
        i = 0 
        content = fobj.read().decode("utf-8")
        lines = content.splitlines()
        while i < len(lines):
            zuordnung = lines[i].split(splitter)
            userpass[zuordnung[0]] = zuordnung[1][2:-1]
            i = i + 1
    return userpass

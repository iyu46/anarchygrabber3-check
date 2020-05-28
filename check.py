import glob
from os import path
checkPath = path.expandvars(r'%AppData%\Discord\0.0.*\modules\discord_desktop_core\index.js')
checkString = "module.exports = require('./core.asar');"

print("running check...\n")

for filename in glob.glob(checkPath):
    with open(filename, 'r') as f:
        for ctx in f:
            if ctx != checkString:
                print("> you're infected! <\n")
                print("replace everything in the file at the following path:\n")
                print(filename + "\n")
                print("with:\n")
                print(checkString + "\n")

            else:
                print("you're safe! nothing needs to be done\n")

input("press enter to exit")
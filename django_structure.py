import json
import os
import re
import shutil
import subprocess
import pathlib

getVersion = subprocess.Popen("node -v", shell=True, stdout=subprocess.PIPE).stdout
check_v = getVersion.read().decode('utf-8')
version = re.sub('[^0-9]+', '', check_v)

if int(version) > 1000:
    install_path = input("Enter the installation path: ")

    if install_path:
        if os.path.exists(install_path):
            os.chdir(install_path)
            proj_name = input("Name this project: ")
            if not os.path.exists(proj_name):
                os.mkdir(proj_name)
                os.chdir(proj_name)

                #   Creating necessary DIRs & files
                os.system(f'''npm init -y && mkdir static templates {proj_name} users users/templates''')
                os.system(f"touch manage.js users/views.js")

                #   Installing Express & other necessary packages
                os.system("npm i express --save && npm i dotenv && npm install nodemon -D && touch .env")

                with open(".env", "w") as env_f:
                    env_f.write("API_PORT=3000")

                env_f.close()

                manage_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/manage.txt")

                with open(f"manage.js", "w") as manage_f:  # Editing manage.js files
                    lines = open(manage_file, "r").readlines()
                    lines.insert(5, f"const settings = require('./{proj_name}/settings')")
                    manage_f.writelines(lines)

                manage_f.close()

                settings_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/settings.js")  # Copying settings.js file
                shutil.copyfile(settings_file, f"{os.getcwd()}/{proj_name}/settings.js")

                urls_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/users/urls.js")   # Copying urls.js file
                shutil.copyfile(urls_file, f"{os.getcwd()}/users/urls.js")

                urls_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/users/sign-in.ejs")  # Copying sign-in file
                shutil.copyfile(settings_file, f"{os.getcwd()}/users/templates/sign-in.ejs")

                with open("package.json", "r") as pkg_file:  # Editing path in package.json
                    data = json.load(pkg_file)

                data["main"] = f"./{proj_name}/manage.js"

                with open("package.json", "w") as pkg_file:
                    json.dump(data, pkg_file, indent=2)

                os.system("nodemon manage.js")  # Starting server with nodemon

            else:
                raise Exception("Another project with the same name already exists.")

        else:
            raise Exception("Incorrect installation path. Folder does not exist.")

    else:
        raise Exception("Please enter a valid installation path to continue.")

else:
    raise Exception("You have an old version of Node.js installed. Please upgrade to continue.")

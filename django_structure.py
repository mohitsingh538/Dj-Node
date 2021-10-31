import json
import os
import re
import shutil
import subprocess
import pathlib
import webbrowser

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
                os.system(f'''npm init -y && touch manage.js && mkdir {proj_name}''')

                #   Installing Express & other necessary packages
                os.system("npm i express ejs dotenv && npm i nodemon -D && touch .env")

                with open(".env", "w") as env_f:
                    env_f.write("API_PORT=3000")

                env_f.close()

                manage_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/manage.js")
                shutil.copyfile(manage_file, f"{os.getcwd()}/manage.js")

                settings_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/settings.js")  # Copying settings.js file
                shutil.copyfile(settings_file, f"{os.getcwd()}/{proj_name}/settings.js")

                users_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/users")    # Copying users directory
                shutil.copytree(users_dir, f"{os.getcwd()}/users/")

                home_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/home")  # Copying home directory
                shutil.copytree(home_dir, f"{os.getcwd()}/home/")

                static_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/static")  # Copying static directory
                shutil.copytree(static_dir, f"{os.getcwd()}/static/")

                templates_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), "files/templates")    # Copying templates directory
                shutil.copytree(templates_dir, f"{os.getcwd()}/templates/")

                with open(f"manage.js", "w") as manage_f:  # Editing manage.js files
                    lines = open(manage_file, "r").readlines()
                    lines.insert(5, f"const settings = require('./{proj_name}/settings')\n")
                    manage_f.writelines(lines)
                    
                manage_f.close()

                with open("package.json", "r") as pkg_file:  # Editing path in package.json
                    data = json.load(pkg_file)

                data["main"] = "manage.js"

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

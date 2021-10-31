
## Django-ExpressJS: Creates Django-like ExpressJS project


### Introduction

Creates Express project similar to Django project structure. Useful for if you are a Python/Django developer and learning Express.js

This script creates an example folder named - **users**. This is similar to apps in Django project. You can copy it to create more 'apps'.

**Note:** It uses ```ejs``` for template view

#### Download
```bash
git clone https://github.com/mohitsingh538/Dj-Node.git
```

#### Create an ExpressJS project
```bash
python3 django_structure.py
```

Enter the path where you want to install the project, example:
```bash
Enter the installation path: /var/www/html/
```

Give a name to the project, example:
```bash
Name this project: Express_site
```


#### Once the installation is complete, your structure project should look like this:

```
|-- Express_site
    |-- manage.js
    |-- Express_site
	    |-- settings.js

    |-- templates
    |-- static
    |-- package.json
    |-- package-lock.json
    |-- node_modules
    |-- users
```

And, your console will show this:
```bash
Development server started at http://127.0.0.1:3000
```
Here's how your default homepage will look like:

<img src="https://i.ibb.co/GpzpWZ2/django-express.png" width="100%" />

Don't forget to add your 'apps' in project_name/settings.js file. If you add an app named '***home***', add it here:
```bash
const CONFIG = { INSTALLED_APPS:
        [
            'users',
            'home'
        ]
}

module.exports.config = CONFIG;
```

I will soon be adding a homepage and a login page. 

*Contributions would be appreciated.*

**Issues should be raised directly in the repository.**

DJANGO project web application, user atted plateform via browser (pc ...)
Browser shows the data from sensor, devices status, and other information besides, user can set the system and send commands to devices via browser. Components : 
    - Django Framework
    - Mysql Database
    - jQuery, Ajax(support notification)
    - JSON parser
    - Visualization framework
# Preparation your Env
when you'are ready to start your new Django web application, create a new folder and navigate into it. In this folder, you'will set up a new virtual environment using your command line:

```console
foo@bar:~$ python -m venv env
foo
```

This command sets up a new virtual environment named env in your current working directory, once the proocess is complete, you also need to activate the virtual environment: 
```console
foo@bar:~$ env/bin/activate
foo
```
## Warning : 
Before you activate you env or  ven in your IDE in my case it was Vscode.
You need to autorise l'execution of the Scripts POWERSHELL :
1. Execute your powershell(Admin) and after that write the commande line :
```console
foo@bar:~$ set-executionpolicy unrestricted
foo
```
2. Valide by answering  <O>
3. you can know activate you env in your vscode (autorisation of utilisation powershell is active know)

## Install Django and pin your dependency :
Once you'have created and activated your python virtual environement,
```console
foo@bar:~$ python -m pip install django
foo
```
This command fetches the django from the package index(Pypi) using pip, after the installation has completed, you can pin your dependencies to make sur that you'are keeping track of which djanfo version you installed :
```console
foo@bar:~$ python -m pip freeze > requirements.txt
foo
```
this command writes the names and version of all external python packages that are currently in your virtual environment to file called requirements.txt, this file will include the django package and all of it dependencies.
```console
(ven)foo@bar:~$ python -m pip install django == 2.2.11
foo
```

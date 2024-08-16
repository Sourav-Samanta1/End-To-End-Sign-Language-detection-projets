# End-To-End-Sign-Language-detection-projets
## Project Step 1:

```bash
#Create a github repository then clone it into a foulder
git clone https://github.com/
```

```bash
#open VS code 
ls             -Foulder in the Foulder(End-To-End-Sign-Language-detection-projets)
cd  End-To-End-Sign-Language-detection-projets            -(go to project Foulder)
code .                          - (Open the Foulder is VS CODE)
```

```bash
#Create a template.py file code and write code to it. After write code always save all the files
python template.py  -for run and create all the files
```

```bash
#Push into the github from local machine
git add .
git commit -m "Foulder structure added"
git push origin main/master 
```
or 
```bash
# Push in Github another way using commit(VSCODE-3 Source control)
requirments added (commit)
```


```bash
#Create a virtual environment for the project
conda create -n signlang python=3.7 -y
```
```bash
#Active the virtual environment
conda activate signlang
```
```bash
#Then write requirements.txt and setup.py files code and Active the virtual environment and install all the packages 
pip install -r requirements.txt
pip list       -check all requirements install or not
```
## Project DAY 2:

```bash
#AGENDA
data collections- kaggle, Roboflow universe(create a file named data_collector.py)
annotations of data-Roboflow/labellmg
utility of models
```

```bash
#AGENDA
data collections- create a file named data_collector.py
write the code    -then save and run it
python data_collector.py   
```
```bash
#Don't push the collected image in github write in .gitignore
ColleectedImages/*  
```
```bash
#write the logger code for create timetemp
```
```bash
#write the exception code for rise the error message
```
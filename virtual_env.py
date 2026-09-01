## VIRTUAL ENVIRONMENT ====>>> isolated python workspace for each project . It keeps each project's libraries separate from each other and from your main Python installation. It keeps each project's libraries separate from each other and from your main Python installationc
Without venv:                    With venv:
                                 
Your Computer                    Your Computer
└── Python                       └── Python
    └── pandas 1.0                   ├── Project 1 (venv)
    └── numpy 1.0                    │   ├── pandas 1.0
        ↑                            │   └── numpy 1.0
    ALL projects                     └── Project 2 (venv)
    share same                           ├── pandas 2.0
    libraries ❌                         └── numpy 2.0 ✅


## without venv ->> only one version installed -->one project works other breaks
## with venv ->> both projects works


## commands 

#  1 ... create virtual env 
pyhton -m venv venv

#  2....activate wondows
venv\Scripts\activate

#  3....when it is active then you may  see
(venv) C:\your_projct>

#  4.. installed library inside venv
pip install pandas

# 5 ...see all lirary installed 
pip list

# 6... save all library to file
pip freeze > requirments.txt

#  7... installed from reqiremnet.txt -->>> ..A text file that lists all libraries your project uses with their exact versions
                #                             and somebody uses my project clone then it runs only this command and it automatically installed all library
pip install -r requirment.txt

#  8.. deactivate venv
deactivate

##  How Virtual Environment Works Internally

my-project/
├── venv/
│   ├── Scripts/        ← activate file lives here (Windows)
│   ├── Lib/            ← all installed libraries stored here
│   └── pyvenv.cfg      ← configuration file
├── app.py
└── requirements.txt
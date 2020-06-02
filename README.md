# Gradler 1.1
Android Marking Project

### Note:
> Create a directory in your home folder called gradler_tests

> Documentation In Progress



# How It Works
The system uses a crawler to fetch and organize html files and save them inside a json file.
The bash script runs on a Linux Distribution to run the python file. It also outputs a status code inside a text file to indicate whether the system failed or passed. "1" indicates that the system passed and a json file is available on the machine, "0" indicates something went wrong in the process.

The php file will use the status code to check that a json file has indeed been created, then once it is successful the php file will first clean the files. NB: The json file needs to be removed each time it is ran to avoid corruption.
After cleaning, the php file will run the gradler and return a JSON object that can be used for being displayed

# Requirements
+ php7x
+ Ubuntu
+ python3

This is where we will store the classes, until we move them to a database
## Installation
`sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`

`git clone https://github.com/OpenSauce-Wits/gradler`

`cd gradler`

`git checkout gradler1.0`

`git pull --set-upstream origin gradler1.0`

`sudo apt-get install python3-virtualenv`

`virtualenv -p python3.6 venv`

`source venv/bin/activate`

## New Features

> Generalised Crawler

> Bash Script To Run Crawler

> phpFunction To Return JSON Objects



## Preparing to run the "marker"
`pip3 install -r requirements.txt`

### Running the gradle fetcher
`scrapy crawl gradle -a abs="/home/molefe/Software/Developer/AttributeChangeProject"`
> Abs is path/to/android/root/folder


## TODO
1. Archictectural Description
2. Class Diagram
 + UML Diagram
3. Crawler Testing 
4. phpFile Testing
5. Migration To Online Server




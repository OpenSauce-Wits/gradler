# Gradler
Android Marking Project

Note:
> Create a directory in your home folder called gradler_tests

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



## Preparing to run the "marker"
`pip3 install -r requirements.txt`


> Move to gradler/gradle/spiders/gradle.py

> modiy the script
>`start_urls = []`

Change the contents to point your gradler_tests


Move back to the gradle directory (the top project folder)
### Running the gradle fetcher
`scrapy crawl gradle -a abs="/home/molefe/Software/Developer/AttributeChangeProject"`
> Where abs is your project folder







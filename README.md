# Gutenberg-Graph-Network

## Useful links 
| Links  |Beschreibung   |
|---|---|
| [Python Dokumentation](https://docs.python.org/3.11/library/index.html)  | Doku zu Python.  |
| [Project Gutenberg](https://www.gutenberg.org/)  | Ein Projekt auf dem unserer Projekt aufbaut.  |
| [Natural Language Toolkit](https://www.nltk.org/) | Website zum ziehen von Daten  |
| [spaCy](https://spacy.io/)  | Modelle für Entity Name Recognition (ENR) |
| [BERTopic](https://github.com/MaartenGr/BERTopic)  | Modell für Topic Modelling  |
| [GitHub Projectboard](https://github.com/users/schanikk/projects/3/views/1?layout=board)  | Unser Projektboard mit Tickets  |
| [Beispielprojekt zu Gutenberg](https://dharc-org.github.io/mythlod/index.html)  | Beispielimplementation unserers Projekts  |
|   |   |

## About the Project

Our project makes use of already built models from "spaCy" and the Topic Modelling Algorithm BERTopic to create and visualize associations between characters and topics in a book from the [Project Gutenberg](https://www.gutenberg.org/) or from the complete corpus.

## Technologies

## Documentation


## Quickstart(WIP)

First Clone the Github Repository into the desired directory

```bash
git clone https://github.com/schanikk/Gutenberg-Graph-Network.git

```
Next you need to have Docker Installed, if you dont have Docker already installed check the following Link https://www.docker.com/products/docker-desktop/

If Docker is installed Change into the web Application Directory and Start Docker-Compose

```bash

cd gutemberg-Graph-Network/gutenbergApp
docker-compose up

```

Next Step is to open the Docker bash of the Django Web app Container. We do this by first checking the Container id and then execute the bash inside the desired container by following the steps below. The Container ID we need is the one from the Image gutenbergapp-web. In this example it is 5f794608962e.


```
bash(base) ➜  ~ docker ps

CONTAINER ID   IMAGE              COMMAND                  CREATED      STATUS          PORTS                    NAMES
5f794608962e   gutenbergapp-web   "python manage.py ru…"   4 days ago   Up 20 seconds   0.0.0.0:8000->8000/tcp   gutenbergapp-web-1
14c8f8a5fa52   postgres           "docker-entrypoint.s…"   4 days ago   Up 21 seconds   5432/tcp                 gutenbergapp-db-1

docker exec -t -i 5f794608962e bash
```

First we Check if there are any migrations to make by running the following Command. Normaly there shouldnt be any to make, but just to be sure we check it anyway.
```bash
python manage.py makemigrations

System check identified some issues:

WARNINGS:
?: (staticfiles.W004) The directory '/var/www/static/' in the STATICFILES_DIRS setting does not exist.
No changes detected
```
The Warning can be ignored but the last line is the important one where it says "No changes detected. However even tho there are no changes detected, there aare still migrations we need to do after running the web application the first time. Because Django manages the changes of the Database and their Models with Migration files which are also stored in the Repository. We Migrate all the changes with the migrate command.

```bash
python manage.py migrate

WARNINGS:
?: (staticfiles.W004) The directory '/var/www/static/' in the STATICFILES_DIRS setting does not exist.
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, webDB
Running migrations:
  No migrations to apply.

```

Again the Warning can be ignored, as its indicates that the STATICFILE_DIRS doesnt exist, however the Static Files are caught by Django. If u run this command u will see several Changes Applied. 

Next we need to initalize the Database with some Data so the Application can visualize the Relationship between Characters and Topics. We do this with the build in loaddata command which uses Fixtures to Upload Data into the Database. More about Fixtures can be found here(https://docs.djangoproject.com/en/4.1/howto/initial-data/). The Order of loading the Data is important, because there are severeal Relations between the Tables. The Correct order is books, character, topics, sentences, sent2char.

NOTE: The Final Fixtures for 81 Books is too big for the GitHub Repository, therefore we had to upload them to a extern service (Mafiasi) where u need to download them extract them from the ZIP and place them into a directory in fixtures/ with the name BigFixtures.

Fixtures Link: https://cloud.mafiasi.de/s/Sgb72AGeaBB3gWM

```bash

python manage.py loaddata webDB/fixtures/BigFixtures/bookFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/characterFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/topicsFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/sentencesFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/sent2charFixturesSmall.json
```

Now the Application is ready to use! Have Fun to pick a book and start Filtering!!

## About Us

- Till
- Sanaz
- Martin

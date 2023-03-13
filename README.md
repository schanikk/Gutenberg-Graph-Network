# Gutenberg-Graph-Network

## About the Project

Our project makes use of already built models from "spaCy" and the Topic Modelling Algorithm BERTopic to create and visualize associations between characters and topics in a book from the [Project Gutenberg](https://www.gutenberg.org/) or from the complete corpus.
Inside our App you are able to pick a book and make it display every character of that book, which has been found by the ENT-model. Once displayed, you can pick a character and every topic which is associated with that character is shown to you. The topics were found beforehand by BERTTopic. 

Once done with the filtering, you can reset your selection to start anew by clicking on the red resetbutton or just pick a different book.
In addtion to the book's characters and the character's topics, a counter next to the columns shows you the total number of books which are loaded into the app, the number of characters found in a book and the number of topics in a book (derived from the character-topic association).

![image](https://user-images.githubusercontent.com/56537013/224679979-259fd15b-faba-46c3-bcbb-0cb14b054fe8.png)
*Starting screen*

![image](https://user-images.githubusercontent.com/56537013/224683429-fb10121e-3a94-4481-bd2a-01661176e29d.png)
*Picked a book only*

![image](https://user-images.githubusercontent.com/56537013/224683297-7ba86bea-f1c9-42e7-9ced-5aa3a07a6353.png)
*Picked a book and a character*



## How To Run The App

First Clone the Github Repository into the desired directory

```bash
git clone https://github.com/schanikk/Gutenberg-Graph-Network.git

```
Next you need to have Docker Installed, if you don't have Docker already installed check the following Link https://www.docker.com/products/docker-desktop/

Once Docker is installed, change into the Web Application Directory and Start docker-Compose

```bash

cd gutemberg-Graph-Network/gutenbergApp
docker-compose up

```

Next Step is to open the Docker bash of the Django Web App container. We do this by first checking the Container id and then execute the bash inside the desired container by following the steps below. The Container ID we need is the one from the image gutenbergapp-web. In this example it is 5f794608962e.


```
bash(base) ➜  ~ docker ps

CONTAINER ID   IMAGE              COMMAND                  CREATED      STATUS          PORTS                    NAMES
5f794608962e   gutenbergapp-web   "python manage.py ru…"   4 days ago   Up 20 seconds   0.0.0.0:8000->8000/tcp   gutenbergapp-web-1
14c8f8a5fa52   postgres           "docker-entrypoint.s…"   4 days ago   Up 21 seconds   5432/tcp                 gutenbergapp-db-1

docker exec -t -i 5f794608962e bash
```

First we check if there are any migrations to make by running the following Command. Normally there shouldn't be any to make, but just to be sure we check it anyway.
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

Again the warning can be ignored, as it indicates that the STATICFILE_DIRS doesnt exist, however the static files are caught by Django. When you run this command you will see several changes applied. 

Next we need to initalize the database with some data so the Application can visualize the relationship between Characters and Topics. We do this with the built-in loaddata command which uses Fixtures to upload data into the database. More about Fixtures can be found here(https://docs.djangoproject.com/en/4.1/howto/initial-data/). The order of loading the data is important, because there are severeal relations between the tables. 
The correct order is: 
1. books 
2. character
3. topics 
4. sentences
5. sent2char

NOTE: The final Fixtures for 81 Books is too big for the GitHub Repository, therefore we had to upload them to an external service (Mafiasi) where you need to download them, extract them from the ZIP and place them into a directory in fixtures/ with the name BigFixtures.

Fixtures Link: https://cloud.mafiasi.de/s/Sgb72AGeaBB3gWM

```bash

python manage.py loaddata webDB/fixtures/BigFixtures/bookFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/characterFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/topicsFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/sentencesFixturesSmall.json
python manage.py loaddata webDB/fixtures/BigFixtures/sent2charFixturesSmall.json
```

Now the Application is ready to use! You can access it via localhost:8000/gutenberg.
Have Fun to pick a book and start filtering!!

## Technologies/Data

- **FrontEnd**:
HTML, CSS, Vanilla JS, Bootstrap

- **BackEnd**:
  - Logic: Django
  - Database: PostgreSQL
  
- **Containerization**: 
Docker

- **Preprocessing**:
spaCy
BERTTopic

- **Data**:
Gutenberg Corpus Books

## Architecture Overview
![image](https://user-images.githubusercontent.com/56537013/224675408-20296718-35de-4b6b-bd70-3d2373ffb468.png)

## Useful links 
| Links  |Beschreibung   |
|---|---|
| [Python Dokumentation](https://docs.python.org/3.11/library/index.html) | Python Docs |
| [Project Gutenberg](https://www.gutenberg.org/)  | Actual Gutenberg Project  |
| [Natural Language Toolkit](https://www.nltk.org/) | Useful data  |
| [The Standardized Project Gutenberg Corpus](https://github.com/pgcorpus/gutenberg) | Used for Data Extraction  |
| [spaCy](https://spacy.io/)  | Models for Entity Name Recognition (ENR) |
| [BERTopic](https://github.com/MaartenGr/BERTopic)  | Model for Topic Modelling  |
| [GitHub Projectboard](https://github.com/users/schanikk/projects/3/views/1?layout=board)  | Our Projectboard in HitHub  |
| [Beispielprojekt zu Gutenberg](https://dharc-org.github.io/mythlod/index.html)  | Different implementation of the project (not ours)  |
|   |   |

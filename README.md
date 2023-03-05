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

Our project makes use of already built models from "spaCy" to create and visualize associations between characters and topics in a book from the [Project Gutenberg](https://www.gutenberg.org/) or from the complete corpus.

## Technologies

## Documentation


## Quickstart(WIP)

git clone (link)

Install Docker

- cd gutemberg-Graph-Network/gutenbergApp
- docker-compose up

Open second terminal:

- docker ps
- extract container id
- docker exec -t -i <CONTAINERID> bash
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata webDB/fixtures/utf9fixtures/bookFixturesSmall.json
- python manage.py loaddata webDB/fixtures/utf9fixtures/characterFixturesSmall.json
- python manage.py loaddata webDB/fixtures/utf9fixtures/topicsFixturesSmall.json
- python manage.py loaddata webDB/fixtures/utf9fixtures/sentencesFixturesSmall.json
- python manage.py loaddata webDB/fixtures/utf9fixtures/sent2charFixturesSmall.json


## About Us

- Till
- Sanaz
- Martin

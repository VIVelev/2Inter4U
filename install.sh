pipenv --rm
pipenv install
pipenv run python -m nltk.downloader all
pipenv run python -m spacy download en_core_web_sm
pipenv update
pipenv check

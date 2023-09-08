@echo off

REM Create main project directory
mkdir spotify_lyric_analyzer

cd spotify_lyric_analyzer

REM Create API directories
mkdir api
mkdir api\models api\routes api\utils
echo. > api\main.py

REM Create NLP module directories
mkdir nlp
echo. > nlp\__init__.py
echo. > nlp\sentiment_analysis.py
echo. > nlp\topic_modeling.py
echo. > nlp\word_cloud.py

REM Create database directory
mkdir database
echo. > database\__init__.py
echo. > database\db_manager.py

REM Create tests directory
mkdir tests

echo. > requirements.txt
echo. > README.md
FROM python:3
COPY . /Scores.txt
COPY . /Utils.py 
COPY . /MainScores.py
RUN pip install Flask
RUN chmod 644 MainScores.py
CMD [ "python3", "./MainScores.py" ]

FROM python:3.6.9

# MAINTANER Felipe Alfaro "felialois@gmail.com"

RUN apt-get update -y

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm
RUN python -m spacy download es_core_news_sm
RUN python -m spacy download fr_core_news_sm
RUN python -m spacy download pt_core_news_sm
RUN python -m spacy download xx_ent_wiki_sm

ENTRYPOINT [ "python" ]
CMD ["-m", "api.__init__"]
FROM python:3.10-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN pip install --upgrade -r requirements.txt

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \
                                        libsndfile1 
										
ENV PORT 8080

EXPOSE 8080

CMD ["gunicorn", "app:app", "-b", ":8080", "--timeout", "300"]






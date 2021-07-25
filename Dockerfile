FROM python:3.9.6-alpine3.14
ARG URL_BACK_ENV="http://192.168.1.102:8000"
ENV URL_BACK_ENV="${URL_BACK_ENV}"
WORKDIR /app
RUN pip install requests
RUN pip install flask
RUN mkdir /app/templates
COPY templates/ /app/templates/
ADD app.py /app/app.py
VOLUME /volume
EXPOSE 5000
CMD ["python","app.py"]


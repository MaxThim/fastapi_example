FROM python:3.11.0

# Set the working directory
WORKDIR /src

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
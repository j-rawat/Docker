FROM python:3.9.0b5-buster


#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy our source code
COPY . ./

#make a directory
WORKDIR test

#run the app
CMD ["pytest"]
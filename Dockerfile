# pull python3 docker image form docker hun
FROM python:3.10-slim  

# in Container creating an folder
RUN mkdir /app

# set the working directory , by default open folder
WORKDIR /app

# copy the dependinces file to working directory
COPY requirements.txt .

# Copy .. , file dot tell copy all requiremtn and print it into woring directory
COPY . .
# when image creating it automatically install all things which is in requirement.txt
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python" , "calc.py" ]

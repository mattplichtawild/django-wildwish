# Use Python3.8 image
FROM python:3.8

# Sets dumping log messages directly to stream instead of buffering
# I don't even know what this means or if I need to do it
ENV PYTHONUNBUFFERED 1

# Set permissions so file can be executed
# Doesn't solve permissions problem...
# RUN chmod +x ./wait-for-postgres.sh


# Create environment variables
# These lines copied from tutorial before I knew what I was doing
# ENV PROJECT_DIR /usr/local/src/django-wildwish
# WORKDIR ${PROJECT_DIR}

# Create directory for image build and set as working directory
RUN mkdir /django-wildwish
WORKDIR /django-wildwish

# Get list of required packages
COPY requirements.txt /django-wildwish/

# Install packages listed in requirements.txt
RUN pip install -r requirements.txt
COPY . /django-wildwish/

CMD python manage.py runserver 0.0.0.0:8000

# Skip using pipenv, just use pip
# RUN pip install pipenv
# COPY Pipfile Pipfile.lock

# What do these flags mean?
# --system flag will install packages into system python instead of into a virtual env (use is not recommended by pipenv)
# --deploy flag will make the build fail if Pipfile.lock is out of date
# RUN pipenv install --deploy --ignore-pipfile
FROM python:3.7

# Database requirements
RUN pip install psycopg2

# Test requirements
RUN pip install flake8==3.7.7
RUN pip install pylint==2.3.1
RUN pip install pylint-django==2.0.9
RUN pip install pydocstyle==3.0.0
RUN pip install flake8-print==3.1.0
RUN pip install pytest==4.5.0

# Main requirements
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app/
WORKDIR /app/

EXPOSE 8000

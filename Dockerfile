FROM python:3.8.6

RUN mkdir /app

WORKDIR /app

COPY . .

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 
ENV PORT 8080

# Run the application:
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:8080", "app:app"]

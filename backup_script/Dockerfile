FROM python:3.10

# Install dependencies
RUN apt-get update && apt-get install -y cron
RUN pip install python-dotenv

# Set working directory
WORKDIR /backup

COPY backup_script.py /backup/backup_script.py

# Set cron job to run the backup script everyday at 1 AM
RUN echo "* * * * * python3 /backup/backup_script.py >> /var/log/cron.log >2&1" | crontab -

# Run cron in the foreground
CMD ["cron", "-f"]
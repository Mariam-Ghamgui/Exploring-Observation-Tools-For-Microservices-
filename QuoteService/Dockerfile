# Select official python 3 runtime
FROM python:3

# Install Netdata dependencies and agent
RUN apt-get update && \
    apt-get install -y wget && \
    wget -O /tmp/netdata-kickstart.sh https://my-netdata.io/kickstart.sh && \
    sh /tmp/netdata-kickstart.sh --non-interactive && \
    rm /tmp/netdata-kickstart.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Creates a directory in /usr/src/app
RUN mkdir -p /usr/src/app

# Change work directory to it
WORKDIR /usr/src/app

# Copy current directory into the created directory
COPY . /usr/src/app

COPY requirements.txt /usr/src/app/

# Install all dependencies and OpenTelemetry packages
RUN python -m pip install -r requirements.txt && \
    python -m pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-flask opentelemetry-exporter-otlp

# Expose the ports (5000 for your app, 19999 for Netdata)
EXPOSE 5000 19999

# Create a startup script
RUN echo '#!/bin/bash\n\
/usr/sbin/netdata -D &\n\
python main.py' > /usr/src/app/start.sh && \
chmod +x /usr/src/app/start.sh

# Start the application and Netdata
CMD ["/usr/src/app/start.sh"]

# Use the official Node.js image
FROM node:14

# Install Netdata dependencies and agent
RUN apt-get update && \
    apt-get install -y wget && \
    wget -O /tmp/netdata-kickstart.sh https://my-netdata.io/kickstart.sh && \
    sh /tmp/netdata-kickstart.sh --non-interactive && \
    rm /tmp/netdata-kickstart.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create application directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install application dependencies and OpenTelemetry packages
RUN npm install && \
    npm install @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node @opentelemetry/exporter-trace-otlp-http

# Copy the rest of the application code
COPY . .

# Expose ports (3000 for your app, 19999 for Netdata)
EXPOSE 3000 19999

# Create a startup script
RUN echo '#!/bin/bash\n\
/usr/sbin/netdata -D &\n\
node -r ./tracing.js app.js' > /usr/src/app/start.sh && \
chmod +x /usr/src/app/start.sh

# Start the application and Netdata
CMD ["/usr/src/app/start.sh"]

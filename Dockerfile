# Use Node.js LTS version
FROM node:20-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y systemd dbus && \
    rm -rf /var/lib/apt/lists/*

# Create pete user and required directories
RUN useradd -m pete && \
    mkdir -p /run/user/1000 && \
    chown pete:pete /run/user/1000 && \
    chmod 700 /run/user/1000

# Set pete as the user
USER pete

# Create app directory
WORKDIR /app

# Install app dependencies
# Copy package files first to leverage Docker cache
COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

# Expose port
EXPOSE 3000

# Start the application
CMD [ "npm", "start" ]

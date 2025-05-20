# Use Node.js LTS version
FROM node:20-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y systemd dbus && \
    rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy package files first to leverage Docker cache
COPY package*.json ./

# Install dependencies
RUN npm install

# Create pete user and required directories
RUN useradd -m pete && \
    mkdir -p /run/user/1000 && \
    chown pete:pete /run/user/1000 && \
    chmod 700 /run/user/1000 && \
    chown -R pete:pete /app

# Set pete as the user
USER pete

# Bundle app source
COPY . .

# Expose port
EXPOSE 3000

# Start the application
CMD [ "npm", "start" ]

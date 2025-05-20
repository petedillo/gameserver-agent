# Use Node.js LTS version
FROM node:20-slim

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

FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

# React copy
COPY . .
RUN npm run build

# Run
CMD ["npm", "start"]

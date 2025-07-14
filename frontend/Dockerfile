# Stage 1: Install dependencies
FROM node:20-alpine AS base

WORKDIR /app

COPY package*.json ./
RUN npm install && npm install -D sass-embedded

# Stage 2: Run dev server
FROM base AS dev

COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev"]

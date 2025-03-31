version: '3.8'

services:
  backend:
    build: ./backend
    container_name: backend
    restart: always
    env_file: .env
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    container_name: frontend
    restart: always
    depends_on:
      - backend
    ports:
      - "3000:3000"

  nginx:
    image: nginx:latest
    container_name: nginx
    restart: always
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - frontend
      - backend

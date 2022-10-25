all: website backend scraper es

website:
	docker compose up -d --build website

backend:
	docker compose up -d --build backend

scraper:
	docker compose up -d --build scraper

es:
	docker compose up -d --build elasticsearch


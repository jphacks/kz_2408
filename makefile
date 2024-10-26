.PHONY: network_clean dbinit init login dbattach up down

up:
	docker compose up -d

down:
	docker compose down


# ネットワーク関連
network_clean:
	docker network prune


# PostgreSQLデータベースコンテナ関連
dbinit:
	sudo chown 999 -R data
	sudo chgrp 999 -R data
	# sudo chmod 775 -R data

init:
	psql -u postgres -f setup.sql -d postgres -h localhost -p 5432
	# sudo -u postgres psql -d postgres -f setup.sql

login:
	psql -U postgres -d postgres -h localhost -p 5432
	# sudo -U postgres psql

dbattach:
	docker compose logs -f db

backendattach:
	docker compose logs -f backend

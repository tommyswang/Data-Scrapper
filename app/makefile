DB_USER=root
DB_NAME=data_scrapper

setup:
	@mysql -u $(DB_USER) -e "create database if not exists $(DB_NAME)"
	@mysql -u $(DB_USER) -e "create database if not exists $(DB_NAME)_test"
	@mysql -u $(DB_USER) $(DB_NAME) < schema.sql
	@mysql -u $(DB_USER) $(DB_NAME)_test < schema.sql
	@mkdir -p files

update:
	@pip3 install -r requirements.txt
	@echo "Python packages updated"

	@mysqldump --no-create-info --complete-insert -u $(DB_USER) $(DB_NAME) > data.sql
	@mysql -u $(DB_USER) $(DB_NAME) < schema.sql
	@mysql -u $(DB_USER) $(DB_NAME) < data.sql
	@rm -f data.sql

	@mysql -u $(DB_USER) -e "drop database $(DB_NAME)_test"
	@mysql -u $(DB_USER) -e "create database if not exists $(DB_NAME)_test"
	@mysql -u $(DB_USER) $(DB_NAME)_test < schema.sql

	@echo "Database migrated"

server: # run server
	python3 main.py

test:
	python3 -m pytest -v

clear:
	@rm -rf ./files/*
	@mysql -u $(DB_USER) -e "drop database $(DB_NAME)"
	@mysql -u $(DB_USER) -e "drop database $(DB_NAME)_test"
	@make setup
	@echo "Data cleared"
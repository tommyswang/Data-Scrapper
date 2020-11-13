DB_USER=root
DB_NAME=data_scrapper

setup:
	@mysql -u $(DB_USER) -e "create database $(DB_NAME)"
	mkdir -p files

update:
	@pip3 install -r requirements.txt
	@pip install -r requirements.txt
	@echo "Python packages updated"

	@mysqldump --no-create-info --complete-insert -u $(DB_USER) $(DB_NAME) > data.sql
	@mysql -u $(DB_USER) $(DB_NAME) < schema.sql
	@mysql -u $(DB_USER) $(DB_NAME) < data.sql
	@rm -f data.sql
	@echo "Database migrated"

server: # run server
	python3 main.py

test:
	pytest -v
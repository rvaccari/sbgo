help:
	@echo -e "lint             Lint the project for coding standards. Recommended to run before pushing to remote (adding a git pre-commit hook must be nice ;)"
	@echo -e "format           Format the project for coding standards black"
	@echo -e "docker-build     Start build docker-compose"
	@echo -e "docker-up        Start all the environment on docker-compose"
	@echo -e "docker-down      Stop docker-compose environment"
	@echo -e "docker-test      Run the full teste suite in Docker. IMPORTANT: You must have a database named "web_test" created to successfully run them"

pre-install:
	sudo -u postgres psql -c "DROP DATABASE IF EXISTS sbgo"
	sudo -u postgres psql -c "DROP DATABASE IF EXISTS sbgo_test"
	sudo -u postgres psql -c "CREATE DATABASE sbgo"
	sudo -u postgres psql -c "CREATE DATABASE sbgo_test"

docker-build:
	docker-compose up -d --build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down -v

docker-test:
	docker-compose exec web python -m pytest

test:
	pytest -ra --disable-warnings --color=yes $(ARGS)

lint:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f .coverage
	make test ARGS="--cov=app/ --cov-fail-under=70 --pydocstyle --mypy --black $(ARGS)"

format:
	black app tests external_services
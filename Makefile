DOCKER := docker run -it --rm battleship-franco

install: ## Build the docker container
	docker build -t battleship-franco .

run: ## Run the game.
	$(DOCKER) python3 ./src/main.py 

test: ## Run the tests
	$(DOCKER) python3 -m unittest discover -v -s . -p "*_test.py"
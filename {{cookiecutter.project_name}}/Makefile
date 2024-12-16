.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "Creating virtual environment using pyenv and poetry"
	@uv sync
	@uv run pre-commit install

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "Creating wheel file"
	@uv build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: publish
publish: ## publish a release to pypi.
	@echo "Publishing: Dry run."
	@uv publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := install

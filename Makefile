APP_NAME=infoelectoral_madrid
build:
	@docker build -t ${APP_NAME} .
run: build
	@docker run -i -t --rm --name="$(APP_NAME)" $(APP_NAME) | tr -d '\r'
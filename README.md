# make me sad bot
#### Instantly makes you sad by sending you the current USD to TRY ratio
---

## Usage
```
/dollar         to make yourself sad
/dollar 10      to make yourself even sadder
```

## Running with Docker
[DockerHub](https://hub.docker.com/repository/docker/cccaaannn/make_me_sad_bot)
## Build
```shell
sudo docker build -t cccaaannn/make_me_sad_bot .
```

## Run
```shell
sudo docker run -d --name make_me_sad_bot -e TELEGRAM_BOT_KEY=<YOUR_BOT_KEY> -e CURRENCY_API_KEY=<YOUR_CURRENCY_KEY> cccaaannn/make_me_sad_bot
```

### Currency api from
[exchangerate-api](https://app.exchangerate-api.com)

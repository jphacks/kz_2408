.PHONY: up ac dac
# include ../.env

# サーバー立ち上げ
run:
	# uvicorn main:app --reload
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 仮想環境有効化
ac:
	. ./venv/bin/activate

# 仮想環境無効化
dac:
	deactivate

# api test
apitest:
	curl https://api.openai.com/v1/chat/completions \
		-H "Content-Type: application/json" \
		-H "Authorization: Bearer $(OPENAI_API_KEY)" \
		-d '{
		"model": "gpt-4o-mini",
		"messages": [{"role": "user", "content": "Say this is a test!"}],
		"temperature": 0.7
		}'

# docker コンテナ ビルド
dockerbuild:
	docker build -t backend-jphacks2024 .

# dockerコンテナ立ち上げテスト(単体)
up:
	docker run --publish 8000:8000 --name backend-jphacks2024 --rm backend-jphacks2024

	
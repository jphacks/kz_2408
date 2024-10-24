.PHONY: up ac dac
include .env

# サーバー立ち上げ
up:
	uvicorn main:app --reload

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
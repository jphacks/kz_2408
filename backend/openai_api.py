from openai import OpenAI
from dotenv import load_dotenv
import os, sys
from os.path import join, dirname
import json

load_dotenv()


def isJsonFormat(string: str):
    try:
        json.loads(string)
    except json.JSONDecodeError as e:
        print(sys.exc_info())
        print(e)
        return False
    # 以下の例外でも捕まえるので注意
    except ValueError as e:
        print(sys.exc_info())
        print(e)
        return False
    except Exception as e:
        print(sys.exc_info())
        print(e)
        return False
    return True


def convert2params_json(self_introduction: str, client: OpenAI):
    with open("./script.txt") as f:
        script = f.read()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"""{script}```{self_introduction}```""",
                },
            ],
        )
    result: str = completion.choices[0].message.content
    result = result.replace("\n", "")  # 改行削除
    print(result)
    if isJsonFormat(result):
        result_json = json.loads(result)
        return result_json
    else:
        return {"Error ChatGPT response is not json format": result}

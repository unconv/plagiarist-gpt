#!/bin/env python3

import config
import openai
import os

if not os.path.exists(config.PROMPTS_DIR):
    os.mkdir(config.PROMPTS_DIR)

with open(config.PREPROMPT_FILE) as f:
    preprompt = f.read()

for file in os.scandir(config.LYRICS_DIR):
    basename = os.path.basename(file)

    with open(file) as f:
        prompt = preprompt + "\n\n" + f.read()

    print(f"Handling {file}")

    response = openai.ChatCompletion.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo-0613"
    )

    answer = response["choices"][0]["message"]["content"]
    answer = answer.removeprefix("Prompt:").strip()

    desc_file = os.path.join(config.PROMPTS_DIR, basename)
    with open(desc_file, "w") as f:
        f.write(answer)

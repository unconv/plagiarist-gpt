#!/bin/env python3

import config
import json
import os

fine_tuning_data = open(config.FINE_TUNING_FILE, "w")

for file in os.scandir(config.PROMPTS_DIR):
    basename = os.path.basename(file)
    lyrics_file = os.path.join(config.LYRICS_DIR, basename)

    with open(file) as f:
        prompt = f.read()

    with open(lyrics_file) as f:
        lyrics = f.read()

    if hasattr(config, "SYSTEM_MESSAGE_FILE") and config.SYSTEM_MESSAGE_FILE:
        with open(config.SYSTEM_MESSAGE_FILE) as f:
            sysmessage = f.read()

        if sysmessage:
            system_message = [
                {
                    "role": "system",
                    "content": sysmessage
                }
            ]
    else:
        system_message = []

    data = {
        "messages": system_message + [
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": lyrics
            }
        ]
    }

    fine_tuning_data.write(json.dumps(data)+"\n")

fine_tuning_data.close()

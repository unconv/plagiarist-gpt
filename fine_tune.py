#!/bin/env python3

import config
import openai
import time
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) > 1:
    file_id = sys.argv[1]
else:
    file = openai.File.create(
        file=open(config.FINE_TUNING_FILE, "rb"),
        purpose='fine-tune'
    )

    time.sleep(15) # wait for processing

    file_id = file.id

job = openai.FineTuningJob.create(
    training_file=file_id,
    model="gpt-3.5-turbo"
)

print(job)
print()

print("Fine tuning started!")
print("Check status by running:")
print(f"  ./check_fine_tune.py {job.id}")

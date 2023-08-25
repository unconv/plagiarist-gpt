#!/bin/env python3

import openai
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

job_id = sys.argv[1]

retrieved_job = openai.FineTuningJob.retrieve(job_id)

print("JOB DATA:")
print(retrieved_job)

events = openai.FineTuningJob.list_events(
    id=job_id,
    limit=1
)

print("LATEST EVENT:")
print(events.data[0])
print()

if retrieved_job.finished_at:
    print("Fine tuning has finished!")
    print(f"Your model is: {retrieved_job.fine_tuned_model}")
else:
    print("Fine tuning is still in progress (see details above)")
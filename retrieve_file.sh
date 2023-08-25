#!/bin/bash
curl https://api.openai.com/v1/files/$1/content \
  -H "Authorization: Bearer $OPENAI_API_KEY"

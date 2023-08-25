# Plagiarist-GPT

This project allows you to fine tune ChatGPT to generate lyrics based on the existing lyrics of an artist. It can also be modified to work with other text than lyrics.

# How to use

1. Put all the lyrics in separate text files in the `lyrics` directory
2. Run `./create_prompts.py` to create prompts from each of the lyrics
3. Run `./create_data.py` to create the fine-tuning data
4. Run `./fine_tune.py` to start fine tuning job
5. Run `./check_fine_tune.py [JOB_ID]` to check the status of the fine tuning

Once fine tuning has finished, you can use a ChatGPT API client, like [ChatWTF](https://github.com/unconv/chat-wtf) to use it. Just change the model name from `gpt-3.5-turbo` to your newly created fine-tuned model `ft:gpt-3.5-turbo-0613:XXXXX:XXXXXX`

You can modify the prompt in `preprompt.txt` to make it work with other things than lyrics, or modify the type of input you want to give to ChatGPT as a prompt. The purpose of the preprompt is to convert the desired output data into a prompt that should generate the output data when sent to ChatGPT.

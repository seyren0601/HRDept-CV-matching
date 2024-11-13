import os
import requests
import json
from openai import OpenAI
from LLMData import prompts

MODEL_NAME = "qwen2.5-14b-instruct"
MODEL_URL = "http://127.0.0.1:1234/v1" # Replace with your actual API URL if different
CLIENT = OpenAI(
    base_url=MODEL_URL,
    api_key="lm-studio"
)

def cv_summary(raw_text:str):
    completion = CLIENT.chat.completions.create(
        model=MODEL_NAME,
        messages = [
            {"role":"system", "content":prompts.system_prompt},
            {"role":"user","content":raw_text}
        ]
    )
    return completion.choices[0].message.content

def summary_to_json(summary:str, ocp:str):
    completion = CLIENT.chat.completions.create(
        model=MODEL_NAME,
        messages = [
            {"role":"system", "content":prompts.system_prompt_json},
            {
                "role": "user",
                "content" : summary
            },
            {
                "role": "user",
                "content": prompts.get_summary_to_json_prompt(ocp)
            }
        ]
    )
    return completion.choices[0].message.content

def json_double_check(summary:str, json_string:str, ocp:str):
    double_check_prompt = prompts.get_json_doublecheck_prompt(ocp) + json_string

    completion = CLIENT.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role":"system", "content":prompts.system_prompt_doublecheck},
            {
                "role": "user",
                "content" : summary
            },
            {
                "role": "user",
                "content": double_check_prompt
            }
        ]
    )

    return completion.choices[0].message.content
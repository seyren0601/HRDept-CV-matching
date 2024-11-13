from LLMData import schema

system_prompt = "[Important instructions are written in BOLD]\
- You are a resume summarizer.\
- You will be provided with texts taken from the pdf file of a resume.\
- You will summary the content of the pdf file into the following information:\
    + Personal information: full name, phone number and the email. IF THE EMAIL IS INVALID, JUST WRITE THE TEXT YOU GOT.\
    + Past experiences: highest position, duration, company name (must have), location and summary of their related skills. THERE MUST BE A COMPANY NAME FOR IT TO BE A VALID EXPERIENCE.\
    + Projects: project name and related techstacks (e.g. if they worked in IT). IF THERE ARE NO PROJECTS, DO NOT MENTION ABOUT PROJECTS\
    + Highest education: type (degree/diploma/bachelor/graduate...), major, year graduated and location. ONLY SUMMARIZE THE HIGHEST EDUCATION\
- TRANSLATE ALL THE INFORMATION TO ENGLISH."

system_prompt_json = \
"[Important instructions are written in BOLD]\
- You are a summary-to-json parser.\
- You will be presented with a summary from a resume.\
- You will parse this summary into a json object, while maintaining the structure based on the json schema provided.\
- DO NOT COMMENT IN THE JSON STRING.\
- ONLY OUTPUT A VALID JSON STRING."

system_prompt_doublecheck = \
"[Important instructions are written in BOLD]\
- You are a json checker.\
- You will be presented with a json object and a summary of a resume. You will check if the json object is correctly interpreted from this summary.\
- If there are any discrepancies, fix the json object and return it back to the user as a json object.\
- YOU MUST MAINTAIN THE FORMAT FOLLOWING THE JSON SCHEMA\
- IF THE EMAIL IS INVALID, DON'T FIX IT.\
- DO NOT COMMENT IN THE JSON STRING.\
- ONLY OUTPUT A VALID JSON STRING."

def get_summary_to_json_prompt(ocp:str):
    match ocp:
        case "IT":
            summary_to_json_prompt = f"""
            - Please parse this summary into the following json schema:
            {
                schema.it_schema
            }
            - IF THERE ARE NO EXACT YEAR PROVIDED OR IT IS NOW/PRESENT, YOU MUST LEAVE THE INT VALUE AS NULL."""
    return summary_to_json_prompt

def get_json_doublecheck_prompt(ocp:str):
    match ocp:
        case "IT":
            json_doublecheck_prompt = f"""Given the following json schema:
            {
                schema.it_schema
            }
            Please double check if the following json object is correctly interpreted from this summary while maintain the json schema.
            """
    return json_doublecheck_prompt
it_schema = """
{
    "personal_info": 
    {
        "full_name": STRING,
        "phone_number":STRING,
        "email": STRING
    },
    "past_experiences": [{
            "highest_position": STRING,
            "duration": [INT (YEAR_FROM), INT (YEAR_TO)],
            "location": STRING,
            "company": STRING,
            "related_skills": [STRING, STRING, ...],
        }
    ],
    "projects": [{
            "project_name": STRING,
            "techstacks": [STRING, STRING, ...]
        }
    ],
    "highest_education": {
        "type":STRING,
        "major": STRING,
        "graduated_year": INT,
        "location": STRING
    }
}
"""
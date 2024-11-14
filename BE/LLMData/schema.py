import json

it_json_sample = """{
    "personal_info":
    {
        "full_name": "Thinh Nguyen",
        "phone_number": "0903179970",
        "email": "sorrenw@gmail.com"
    },
    "past_experiences": 
    [
        {
            "highest_position": "Java Lead Developer",
            "duration": [2022, null],
            "location": "Vietnam",
            "company": "ABC Company",
            "related_skills": ["Java", "Spring Boot"]
        },
        {
            "highest_position": "Java Senior Developer",
            "duration": [2020, 2022],
            "location": "Vietnam",
            "company": "XYZ Company",
            "related_skills": ["Java", "Spring Boot", "Frontend Developer"]
        }
    ],
    "projects": 
    [
        {
            "project_name": "ECommerce Web Application",
            "techstacks": ["MySQL", "ASP.Net Core"]
        }
    ],
    "highest_education": {
        "type":"Bachelor",
        "major": "Software Engineering",
        "graduated_year": 2019,
        "location": "RMIT University"
    }
}"""

it_schema = """
{
    "type":"json_schema",
    "json_schema":{
        "name" : "CV Summary",
        "schema" : {
            "type": "object",
            "properties": {
                "personal_info": {
                    "type": "object",
                    "properties": {
                        "full_name": { "type": "string" },
                        "phone_number": { "type": "string" },
                        "email": { "type": "string", "format": "email" }
                    },
                    "required": ["full_name", "phone_number", "email"]
                },
                "past_experiences": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "highest_position": { "type": "string" },
                        "duration": {
                            "type": "array",
                            "description":"This is a 2 elements array that describes the starting and ending year of a position. If the end year is not specified, it should be left as null",
                            "items": [
                                { "type": "integer" },
                                { "type": ["integer", "null"] }
                            ],
                            "minItems": 2,
                            "maxItems": 2
                        },
                        "location": { "type": "string" },
                        "company": { "type": "string" },
                        "related_skills": {
                                "type": "array",
                                "items": { "type": "string" }
                            },
                        
                    },
                    "required":["duration", "location", "highest_position"]
                }
                },
                "projects": {
                "type": "array",
                "description":"A list of IT projects that the candidate has worked on. It can be either a company project or personal project.",
                "items": {
                    "type": "object",
                    "properties": {
                        "project_name": { "type": "string" },
                        "techstacks": {
                            "type": "array",
                            "items": { "type": "string" }
                        }
                    },
                }
                },
                "highest_education": {
                    "type": "object",
                    "properties": {
                        "type": { "type": "string" },
                        "major": { "type": "string" },
                        "graduated_year": { "type": "integer" },
                        "location": { "type": "string" }
                    },
                }
            },
            "required": ["personal_info", "projects", "highest_education"]
        }
    }
}
"""

it_schema_obj = {
    "type":"json_schema",
    "json_schema":{
        "name" : "CV Summary",
        "schema" : {
            "type": "object",
            "properties": {
                "personal_info": {
                    "type": "object",
                    "properties": {
                        "full_name": { "type": "string" },
                        "phone_number": { "type": "string" },
                        "email": { "type": "string", "format": "email" }
                    },
                    "required": ["full_name", "phone_number", "email"]
                },
                "past_experiences": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "highest_position": { "type": "string" },
                        "duration": {
                            "type": "array",
                            "description":"This is a 2-elements array that describes the starting and ending year of a position. If the end year is not specified, it should be left as null",
                            "items": [
                                { "type": "integer" },
                                { "type": ["integer", "null"] }
                            ],
                            "minItems": 2,
                            "maxItems": 2
                        },
                        "location": { "type": "string" },
                        "company": { "type": "string" },
                        "related_skills": {
                                "type": "array",
                                "items": { "type": "string" }
                            },
                        
                    },
                    "required":["duration", "location", "highest_position"]
                }
                },
                "projects": {
                "type": "array",
                "description":"A list of project that the candidate has worked on, it can be either a company project or personal project.",
                "items": {
                    "type": "object",
                    "properties": {
                        "project_name": { "type": "string" },
                        "techstacks": {
                            "type": "array",
                            "items": { "type": "string" }
                        }
                    },
                }
                },
                "highest_education": {
                    "type": "object",
                    "properties": {
                        "type": { "type": "string" },
                        "major": { "type": "string" },
                        "graduated_year": { "type": "integer" },
                        "location": { "type": "string" }
                    },
                }
            },
            "required": ["personal_info", "projects", "highest_education"]
        }
    }
}
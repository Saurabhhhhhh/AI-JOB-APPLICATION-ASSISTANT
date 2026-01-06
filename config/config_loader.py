import json
import os


class ConfigLoader():
    def __init__(self, path):
        self.path = path
    
    def load(self):
        try:
            with open(self.path, "r") as file:
                self.config_data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in config file")


    def validate(self):
        if not hasattr(self, 'config_data'):
            raise RuntimeError("Config not loaded. Call load() first.")

        if not isinstance(self.config_data, dict):
            raise TypeError("Config root must be a dictionary")

        required_top_keys = ["job_preferences", "platforms", "resumes"]
        for key in required_top_keys:
            if key not in self.config_data:
                raise KeyError(f"Missing required config key: {key}")

        job_prefs = self.config_data["job_preferences"]
        if not isinstance(job_prefs, dict):
            raise TypeError("job_preferences must be a dictionary")
        
        resumes = self.config_data["resumes"]
        if not isinstance(resumes, dict) or not resumes:
            raise TypeError("resumes must be a non-empty dictionary")
        

        required_job_prefs_keys = [
            "job_roles",
            "locations",
            "experience_level",
            "max_applications"
        ]

        for key in required_job_prefs_keys:
            if key not in job_prefs:
                raise KeyError(f"Missing required job_preferences key: {key}")

        list_keys = ["job_roles", "locations", "experience_level"]
        for key in list_keys:
            if not isinstance(job_prefs[key], list):
                raise TypeError(f"{key} must be a list")
            if len(job_prefs[key]) == 0:
                raise ValueError(f"{key} cannot be empty")

        if not isinstance(job_prefs["max_applications"], int):
            raise TypeError("max_applications must be an integer")

        if job_prefs["max_applications"] <= 0:
            raise ValueError("max_applications must be greater than 0")


current_dir = os.path.dirname(__file__)
abs_path = os.path.abspath(current_dir)
path = os.path.join(abs_path, 'user_config.json')





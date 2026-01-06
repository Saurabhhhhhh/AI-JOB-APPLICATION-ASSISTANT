class AppConfig:
    def __init__(self, config_data: dict):
        self.job_preferences = JobPreferences(
            config_data["job_preferences"]
        )

        self.platform_config = PlatformConfig(
            config_data["platforms"]
        )

        self.resume_config = ResumeConfig(
            config_data["resumes"]
        )

class JobPreferences:
    def __init__(self, job_pref_dict: dict):
        self.roles = job_pref_dict["job_roles"]
        self.locations = job_pref_dict["locations"]
        self.experience_level = job_pref_dict["experience_level"]
        self.max_applications = job_pref_dict["max_applications"]

        self._validate()

    def _validate(self):
        if len(self.roles) == 0:
            raise ValueError("At least one job role must be provided")
        if len(self.locations) == 0:
            raise ValueError("At least one location must be provided")
        if self.max_applications <= 0:
            raise ValueError("max_applications must be greater than 0")

class PlatformConfig:
    def __init__(self, platform_list: list):
        self.platforms = platform_list

        self._validate()
    def _validate(self):
        if len(self.platforms) == 0:
            raise ValueError("At least one platform must be provided")

class ResumeConfig:
    def __init__(self, resumes_dict: dict):
        self.resumes = resumes_dict

        self._validate()

    def _validate(self):
        for role, path in self.resumes.items():
            if not isinstance(path, str) or path.strip() == "":
                raise ValueError(
                    f"Resume path for role '{role}' must be a non-empty string"
                )
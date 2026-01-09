class ResumeSelector:

    def __init__(self, app_config):
        self.resumes = app_config.resume_config.resumes

    def select(self, role:str) -> str:
        if role not in self.resumes:
            raise ValueError(f"No resume configured for role: {role}")

        return self.resumes[role]
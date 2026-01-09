class PlannedApplication:
    def __init__(self, platform: str, role: str, location: str, resume: str):
        self.platform = platform
        self.role = role
        self.location = location
        self.resume = resume

    def __repr__(self):
        return (
            f"PlannedApplication("
            f"platform={self.platform}, "
            f"role={self.role}, "
            f"location={self.location}, "
            f"resume={self.resume}"
            f")"
        )
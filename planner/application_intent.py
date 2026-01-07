class ApplicationIntent:
    def __init__(self, platform: str, role: str, location: str):
        self.platform = platform
        self.role = role
        self.location = location

    def __repr__(self):
        return (
            f"ApplicationIntent("
            f"platform={self.platform}, "
            f"role={self.role}, "
            f"location={self.location}"
            f")"
        )
        
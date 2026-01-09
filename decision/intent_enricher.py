from decision.planned_application import PlannedApplication


class IntentEnricher:
    def __init__(self, resume_selector):
        self.resume_selector = resume_selector

    def enrich(self, intent):
        resume = self.resume_selector.select(intent.role)

        return PlannedApplication(
            platform=intent.platform,
            role=intent.role,
            location=intent.location,
            resume=resume
        )

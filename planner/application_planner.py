from planner.application_intent import ApplicationIntent


class ApplicationPlanner:
    def __init__(self, app_config):
        self.app_config = app_config

    def generate_plan(self):
        plan = []

        platforms = self.app_config.platform_config.platforms
        roles = self.app_config.job_preferences.roles
        locations = self.app_config.job_preferences.locations
        max_apps = self.app_config.job_preferences.max_applications

        for platform in platforms:
            for role in roles:
                for location in locations:
                    intent = ApplicationIntent(
                        platform=platform,
                        role=role,
                        location=location
                    )
                    plan.append(intent)

                    if len(plan) >= max_apps:
                        return plan

        return plan

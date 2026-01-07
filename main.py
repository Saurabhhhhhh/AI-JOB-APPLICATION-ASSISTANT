from config.config_parser import AppConfig
from config.config_loader import ConfigLoader, path
from planner.application_planner import ApplicationPlanner


# 1. Load and validate config
loader = ConfigLoader(path)
config_data = loader.load_and_validate()

# 2. Create AppConfig instance
app_config = AppConfig(config_data)

# 3. Create planner with REAL config
planner = ApplicationPlanner(app_config)

# 4. Generate plan
plan = planner.generate_plan()

# 5. Inspect output
for intent in plan:
    print(intent)

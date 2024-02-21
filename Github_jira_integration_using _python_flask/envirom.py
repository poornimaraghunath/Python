import os

# Replace 'YOUR_ENV_VARIABLE' with the actual name of the environment variable
env_variable_name = 'JIRA_API_TOKEN'

# Check if the environment variable is set
env_variable_value = os.environ.get(env_variable_name)

if env_variable_value is not None:
    print(f"The value of {env_variable_name} is: {env_variable_value}")
else:
    print(f"{env_variable_name} is not set.")

# config_manager.py

"""
A simple app configuration manager to simulate real-world usage
of Python variables, scopes, global values, and good practices.

PEP8 styling is followed (PEP 8 is the official style guide for Python).
"""

# ✅ GLOBAL VARIABLE (Accessible throughout the app)
APP_NAME = "ConfigPro"
VERSION = "1.0.0"

# ✅ GLOBAL CONFIGURATION DICTIONARY (used across modules)
CONFIG = {
    "debug": False,
    "database_url": "localhost:5432",
    "retry_limit": 3
}


# ✅ Example of VARIABLE SCOPE: local, enclosing, global
def update_config(key, value):
    """Update the CONFIG dictionary with a new key-value pair."""
    global CONFIG  # Referring to the global CONFIG variable

    if key in CONFIG:
        print(f"Updating config '{key}' from {CONFIG[key]} to {value}")
    else:
        print(f"Adding new config '{key}' with value: {value}")

    CONFIG[key] = value


def print_config():
    """Local + Enclosing scope demo with nested functions"""

    prefix = "[CONFIG INFO]"  # Enclosing variable

    def print_key_value(key, value):
        message = f"{prefix} {key}: {value}"  # Uses enclosing + local
        print(message)

    for key, value in CONFIG.items():
        print_key_value(key, value)


# ✅ MAIN SCRIPT MODE: this code runs only when executed directly, not when imported
if __name__ == "__main__":
    print(f"Welcome to {APP_NAME} v{VERSION}")
    
    print("\n📦 Initial Configuration:")
    print_config()

    print("\n⚙️ Updating configuration...")
    update_config("debug", True)
    update_config("max_users", 100)

    print("\n📦 Updated Configuration:")
    print_config()

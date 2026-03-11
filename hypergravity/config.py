import os
from pathlib import Path


def get_config_dir():
    """Get the configuration directory path"""
    return Path.home() / ".hypergravity"


def get_token_path():
    """Get the token file path"""
    return get_config_dir() / "ads_token"


def save_token(token):
    """Save token to ~/.hypergravity/ads_token"""
    config_dir = get_config_dir()
    try:
        config_dir.mkdir(exist_ok=True)
    except PermissionError:
        raise PermissionError(
            f"Cannot create directory {config_dir}. Please check permissions or create it manually."
        )
    
    token_path = get_token_path()
    try:
        with open(token_path, "w") as f:
            f.write(token.strip())
    except PermissionError:
        raise PermissionError(
            f"Cannot write to {token_path}. Please check permissions."
        )
    
    return token_path


def load_token():
    """Load token from ~/.hypergravity/ads_token"""
    token_path = get_token_path()
    if token_path.exists():
        try:
            with open(token_path, "r") as f:
                return f.read().strip()
        except PermissionError:
            raise PermissionError(
                f"Cannot read from {token_path}. Please check permissions."
            )
    return None


def token_exists():
    """Check if token file exists"""
    return get_token_path().exists()

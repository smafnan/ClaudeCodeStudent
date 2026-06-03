"""Shared filesystem paths for ClaudeCodeStudent configuration."""

from pathlib import Path

CCS_CONFIG_DIRNAME = ".ccs"
CCS_ENV_FILENAME = ".env"
LEGACY_REPO_DIRNAME = "claude-code-student"
LEGACY_XDG_CONFIG_DIRNAME = ".config"
CLAUDE_WORKSPACE_DIRNAME = "agent_workspace"
CCS_LOGS_DIRNAME = "logs"
SERVER_LOG_FILENAME = "server.log"


def config_dir_path() -> Path:
    """Return the default user config directory."""

    return Path.home() / CCS_CONFIG_DIRNAME


def managed_env_path() -> Path:
    """Return the default user-managed env file path."""

    return config_dir_path() / CCS_ENV_FILENAME


def legacy_env_paths() -> tuple[Path, ...]:
    """Return legacy user env paths that can be migrated to ~/.ccs/.env."""

    home = Path.home()
    return (
        home / LEGACY_REPO_DIRNAME / CCS_ENV_FILENAME,
        home / LEGACY_XDG_CONFIG_DIRNAME / LEGACY_REPO_DIRNAME / CCS_ENV_FILENAME,
    )


def default_claude_workspace_path() -> Path:
    """Return the default Claude workspace path."""

    return config_dir_path() / CLAUDE_WORKSPACE_DIRNAME


def server_log_path() -> Path:
    """Return the canonical server log path."""

    return config_dir_path() / CCS_LOGS_DIRNAME / SERVER_LOG_FILENAME

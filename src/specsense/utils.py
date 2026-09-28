"""
Utility functions for SpecSenseAI.

This module provides common utilities for file handling and application
logging configuration.
"""

import logging
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def get_logger(name: str) -> logging.Logger:
    """
    Create and return a logger configured using the LOG_LEVEL environment variable.

    The LOG_LEVEL environment variable controls the minimum logging level.
    If LOG_LEVEL is not set or contains an invalid value, INFO is used.

    Args:
        name: Name of the logger to create or retrieve.
    Returns:
        A configured logging.Logger instance.
    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
         handlers=[
            logging.FileHandler("logs/specsense.log"), # Python interprets the relative path based on the current working directory (CWD), not based on the location of utils.py. CWD for this project is C:\.........\SpecSenseAI
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(name)

logger = get_logger(__name__)

def load_file(file_path: str) -> str:
    """
    Load and return the contents of a text file.

    Args:
        file_path: Path to the file to be loaded.
    Returns:
        The file contents as a string with leading and trailing whitespace
        removed.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        OSError: If the file cannot be read.
    """
    try:
        return Path(file_path).read_text().strip()
    except FileNotFoundError as e:
        logger.error("File not found: %s", file_path)
        raise

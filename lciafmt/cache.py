# cache.py (lciafmt)
# !/usr/bin/env python3
# coding=utf-8
"""
Functions to support storing and retrieving files from local cache
"""

import logging
import os
import shutil
import tempfile

import requests

logger = logging.getLogger(__name__)

def clear():
    """Delete the cached files."""
    d = get_folder()
    if not os.path.isdir(d):
        return
    logger.info("delete cache folder %s", d)
    shutil.rmtree(d)


def get_folder(create=False) -> str:
    """Returns the path to the folder where cached files are stored. """
    tdir = tempfile.gettempdir()
    cdir = os.path.join(tdir, "lciafmt")
    if create:
        os.makedirs(cdir, exist_ok=True)
    return cdir


def get_path(file_name: str) -> str:
    """Returns the full file path to a file with the given name in the cache
       folder. """
    f = get_folder()
    return os.path.join(f, file_name)


def exists(file_name: str) -> bool:
    """Returns true when a file with the given name exists in this folder. """
    path = get_path(file_name)
    return os.path.isfile(path)


def download(url: str, file: str) -> str:
    """Downloads the resource with the given URL to a file with the given name
       and returns the full file path to the downloaded resource. """
    get_folder(create=True)
    path = get_path(file)
    logger.info("downloading from %s to %s", url, path)
    resp = requests.get(url, allow_redirects=True)
    with open(path, "wb") as f:
        f.write(resp.content)
    return path


def get_or_download(file: str, url: str) -> str:
    """Checks for local version of path or file or downloads if not present."""
    path = get_path(file)
    if os.path.isfile(path):
        logger.info("take %s from cache", file)
        return path
    download(url, file)
    return path

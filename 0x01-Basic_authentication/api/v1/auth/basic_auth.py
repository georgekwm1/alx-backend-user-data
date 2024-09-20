#!/usr/bin/env python3
"""6. Basic auth"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth Class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts base64 authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # return authorization_header.split(" ")[1]
        return authorization_header.lstrip("Basic ")

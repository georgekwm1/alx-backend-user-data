#!/usr/bin/env python3
"""6. Basic auth"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts user credentials"""
        if decoded_base64_authorization_header is None:
            return None
        if not isinstance(decoded_base64_authorization_header, str):
            return None
        if ':' not in decoded_base64_authorization_header:
            return None
        return decoded_base64_authorization_header.split(':')

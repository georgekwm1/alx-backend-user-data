#!/usr/bin/env python3
"""3. Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None or len(excluded_paths) == 0:
            return True
        if not path.endswith("/"):
            path = path + "/"
        for paths in excluded_paths:
            if not paths.endswith("/"):
                paths = paths + "/"
        if path not in excluded_paths:
            return True
        elif path == "/api/v1/status/" and "/api/v1/status/" in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None

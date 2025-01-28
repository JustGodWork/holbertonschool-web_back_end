#!/usr/bin/env python3

"""Filtering data from logs"""

import re


def filter_datum(fields, redaction, message, separator):
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

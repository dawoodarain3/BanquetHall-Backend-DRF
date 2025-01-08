from django.core.exceptions import ValidationError
import re

def validate_cnic(value):
    pattern = r'^\d{5}-\d{7}-\d{1}$'
    if not re.match(pattern, value):
        raise ValidationError("CNIC must be in the format XXXXX-XXXXXXX-X.")

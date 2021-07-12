def errors_dict_to_string(errors):
    """Flatten Django Rest Framework errors into simple dict with key:value"""
    for key, value in errors.items():
        if isinstance(value, list) or isinstance(value, tuple):
            if isinstance(value[0], dict):
                for i, item in enumerate(value):
                    value[i] = errors_dict_to_string(item)
            else:
                if isinstance(value, str) or isinstance(value, list):
                    errors[key] = "\n".join(value)
                else:
                    errors[key] = value
        elif isinstance(value, dict):
            errors[key] = errors_dict_to_string(value)
    return errors

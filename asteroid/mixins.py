from rest_framework.utils.serializer_helpers import ReturnList

from asteroid.utils import errors_dict_to_string


class StringErrorsMixin:
    """
    Mixin for DRF serializers. Changes errors from lists to string
    """

    @property
    def errors(self):
        errors = super().errors

        if isinstance(errors, ReturnList):
            for i, item in enumerate(errors):
                errors[i] = errors_dict_to_string(errors[i])

            return errors
        return errors_dict_to_string(errors)

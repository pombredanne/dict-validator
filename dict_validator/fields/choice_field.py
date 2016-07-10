""" dict_validator.fields.choice_field """

from ..field import Field


class ChoiceField(Field):
    """
    Accept any type of input as long as it matches on of the choices
    mentioned in the provided list.

    :param choices: list of choices to match against
    """

    def __init__(self, choices, *args, **kwargs):
        super(ChoiceField, self).__init__(*args, **kwargs)
        self._choices = choices

    def _validate(self, value):
        if value not in self._choices:
            return "Value \"{}\" is not among the choices".format(value)

    def _describe(self):
        return {
            "choices": self._choices
        }

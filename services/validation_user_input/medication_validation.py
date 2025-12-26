from pathlib import Path

path_to_medication_list_txt = (
    Path(__file__).parent.parent / 'medication' / 'medication_list.txt'
)


def validate_medication_name(name: str) -> bool:
    """This function validates the medication name. If variable pass all controls about type and invalid char,
    the last control will be check if this name exist in list of medication names that exists in medication_list.txt file
    """
    if not isinstance(name, str):
        raise TypeError('Medication name must be a string')
    with path_to_medication_list_txt.open(
        mode='r', encoding='utf-8'
    ) as medication_list_file:
        for line in medication_list_file:
            if name == line.strip('\n'):
                return True
    raise ValueError("Medication with this name does not exist")

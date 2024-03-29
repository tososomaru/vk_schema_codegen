import logging
from io import StringIO

import isort
from utils.os_utils import create_results_dir
from utils.strings_util import (
    get_json_dict,
    shift_json_dict_names,
    snake_case_to_camel_case,
)
from utils.titles import ExportAll, Imports
from utils.tools import create_objects_from_enum_types, sort_by_reference

from .models.schema_objects import schema_object_fabric_method

logging.basicConfig(level=logging.INFO)


def write_translated_json(
    filepath_to: str, prepared_dict: dict, imports: dict, tabulation="    "
) -> None:
    create_results_dir(filepath_to)
    text = str(Imports(**imports))

    for classname in prepared_dict:
        class_form = schema_object_fabric_method(classname, prepared_dict)
        text += str(class_form)
    text += str(ExportAll(*prepared_dict))
    text = text.replace("\t", tabulation)
    output = StringIO()
    isort.stream(StringIO(text), output, profile="black")
    text = output.getvalue()

    with open(f"{filepath_to}/objects.py", "w") as file:
        file.write(text)


def parse_file(path: str, filepath_to: str, imports_dict: dict) -> None:
    types_dict: dict = create_objects_from_enum_types(
        sort_by_reference(get_json_dict(path)["definitions"])
    )
    classnames: dict = {key: snake_case_to_camel_case(key) for key in types_dict}
    prepared_dict: dict = shift_json_dict_names(types_dict, classnames)
    write_translated_json(filepath_to, prepared_dict, imports_dict)

    logging.info("READY")

import json
import logging
from io import StringIO

import autoflake
import black
import isort
from utils.os_utils import create_results_dir
from utils.strings_util import camel_case_to_snake_case, snake_case_to_camel_case
from utils.titles import ExportAll, Imports
from utils.tools import get_methods_imports

from .models import ClassForm

logging.basicConfig(level=logging.INFO)


def parse_file(
    filepath: str,
    filepath_to: str,
    imports: dict,
    return_type_annotations: dict,
    tabulation="    ",
) -> None:
    base_dir = create_results_dir(f"{filepath_to}/methods")
    categories = sort_jsonmethods_schema(filepath)

    for category, methods in categories.items():
        text = construct_schema(
            category, methods, imports, return_type_annotations[category]
        ).replace("\t", tabulation)
        text += str(ExportAll(f"{snake_case_to_camel_case(category)}Category"))
        text = autoflake.fix_code(text, remove_all_unused_imports=True)
        output = StringIO()
        isort.stream(StringIO(text), output, profile="black")
        text = output.getvalue()
        text = black.format_str(text, mode=black.FileMode())
        with open(f"{base_dir}/{category}.py", "w") as file:
            file.write(text)


def construct_schema(category, methods, imports, return_type_annotations: dict):
    text = str(
        Imports(**imports, **get_methods_imports(methods, return_type_annotations))
    )
    form = ClassForm(category)
    for method in methods:
        form.add_method(method["name"], method, return_type_annotations)
    text += str(form)
    return text


def sort_jsonmethods_schema(path: str) -> dict:
    with open(path, "r") as f:
        json_dict = json.load(f)
    return collecter(json_dict["methods"])


def collecter(methods: dict) -> dict:
    result = {}
    for method in methods:
        method_name = camel_case_to_snake_case(method["name"].split(".")[0])

        if result.get(method_name):
            result[method_name].append(method)
        else:
            result[method_name] = [method]
    return result

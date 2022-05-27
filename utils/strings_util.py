import json
import re
from keyword import kwlist
from typing import Any


def get_type_from_reference(str_ref, convert_to_calmel_case=True) -> str:
    pattern = r".*/(.*)"
    match = re.search(pattern, str_ref)
    ref_type = match[1] if match else str_ref
    if convert_to_calmel_case:
        return snake_case_to_camel_case(ref_type)
    return ref_type


def get_annotation_type(item: dict) -> Any:
    if item.get("type") == "array":
        if item["items"].get("type"):
            type_anno = [item["items"]["type"]]
        else:
            type_anno = item["items"].get("$ref")
            type_anno = [get_type_from_reference(type_anno)]
    elif item.get("type") and not item.get("$ref"):
        type_anno = item.get("type")
    elif item.get("oneOf"):
        type_anno = [get_annotation_type(item) for item in item["oneOf"]]
    else:
        type_anno = item.get("$ref")
        type_anno = get_type_from_reference(type_anno)
    return type_anno


def get_json_dict(path: str) -> dict:
    with open(path, "r") as f:
        return json.loads(f.read())


def snake_case_to_camel_case(string: str) -> str:
    return "".join(word[0].upper() + word[1:] for word in string.split("_"))


CAMEL_CASE_PATTERN = re.compile(r"((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))")


def camel_case_to_snake_case(string: str) -> str:
    return CAMEL_CASE_PATTERN.sub(r"_\1", string).lower()


def convert_to_python_type(field):
    if field.lower() == "array":
        return "list"
    elif field.lower() == "boolean":
        return "bool"
    elif field.lower() == "integer":
        return "int"
    elif field.lower() == "number":
        return "float"
    elif field.lower() == "object":
        return "typing.Any"
    elif field.lower() == "string":
        return "str"
    else:
        return str(field)


def shift_json_dict_names(plain_data: dict, classnames: dict) -> dict:
    return {v: plain_data[k] for k, v in classnames.items()}


def categorize_methods_as_files(json_dict: dict) -> dict:
    filenames = set()
    for method_dict in json_dict["methods"]:
        method_name = method_dict["name"].split(".")[0]
        filenames.add(method_name)

    return {name: {} for name in filenames}


def resolve_property_name(name: str):
    if name[0].isdigit() or name in kwlist:
        name = f"_{name}"
    return name

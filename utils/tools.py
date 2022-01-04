import re

from utils.strings_util import get_type_from_reference, snake_case_to_camel_case


def get_references(item: dict):
    references = []
    all_of = item.get("allOf", [])
    one_of = item.get("oneOf", [])
    for i in [*all_of, *one_of, item]:
        reference = i.get("$ref")
        if reference:
            references.append(get_type_from_reference(reference, False))
    return references


def sort_by_reference(definitions: dict):
    sorted_dict = {}
    for key, value in definitions.items():
        references = get_references(value)
        while references:
            reference = references[0]
            new_references = get_references(definitions[reference])
            if not new_references:
                if reference not in sorted_dict:
                    sorted_dict[reference] = definitions[reference]
                references.remove(reference)
                continue
            for ref in new_references:
                if ref in sorted_dict:
                    sorted_dict[reference] = definitions[reference]
                    if reference in references:
                        references.remove(reference)
                    continue
                references.insert(0, ref)
        if key not in sorted_dict:
            sorted_dict[key] = value
    return sorted_dict


def create_objects_from_enum_types(definitions: dict):
    sorted_dict = {}
    for key, value in definitions.items():
        properties = value.get("properties")
        if not properties:
            sorted_dict[key] = value
            continue
        for item_name, item_value in properties.items():
            item_type = item_value.get("type")
            item_enum = item_value.get("enum")
            item_description = item_value.get("description")
            enum_name = key + "_" + item_name
            if not (item_type and item_enum):
                continue
            if item_description:
                name_from_description = item_description
                match = re.match(r"(.*) of (.*)", item_description)
                if match:
                    name_from_description = f"{match.group(2)} {match.group(1)}"
                if len(name_from_description.split()) <= 4:
                    enum_name = "_".join(name_from_description.split())
            sorted_dict[enum_name] = item_value
            properties[item_name] = {"$ref": f"objects.json#/definitions/{enum_name}"}
            if item_description:
                properties[item_name]["description"] = item_description
        sorted_dict[key] = value
    return sorted_dict


def get_response_imports(definitions: dict):
    imports = []
    for value in definitions.values():
        properties = value.get("properties", {})
        response = properties.get("response", {})
        ref = response.get("$ref")
        if ref:
            imports.append(get_type_from_reference(ref))
            continue
        if response.get("PatternProperties"):
            continue
        for item in [*response.get("properties", {}).values(), response]:
            if item.get("type") == "array":
                ref = item["items"].get("$ref")
                if not ref and item["items"].get("type") == "object":
                    for property_item in item["items"]["properties"].values():
                        property_ref = property_item.get("$ref")
                        if property_ref:
                            imports.append(get_type_from_reference(property_ref))
            else:
                ref = item.get("$ref")
            if ref:
                imports.append(get_type_from_reference(ref))
    return {"vkbottle_types.objects": sorted(set(imports))}


def get_methods_imports(definitions: list, return_type_annotations: dict):
    imports = {}
    for item in definitions:
        for response in item["responses"].values():
            if not isinstance(response, dict) and not response.get("$ref"):
                continue
            response_base, response_object = (
                response["$ref"].split("/")[-1].split("_", 1)
            )
            response_object = snake_case_to_camel_case(response_object)
            _import = imports.get("vkbottle_types.responses." + response_base)
            if not _import:
                _import = imports["vkbottle_types.responses." + response_base] = [
                    response_object
                ]
            elif response_object not in _import:
                _import.append(response_object)
            if response_object in ("GetUploadServerResponse", "BoolResponse"):
                additional_response = (
                    "BaseBoolInt"
                    if response_object == "BoolResponse"
                    else "BaseUploadServer"
                )
            elif response_object not in return_type_annotations:
                continue
            else:
                additional_response = return_type_annotations[response_object]
            if "typing.List" in additional_response:
                additional_response = (
                    re.match(r".*\[(.*),?.*\]", additional_response)
                    .group(1)
                    .replace('"', "")
                )
            if additional_response in ("BaseBoolInt", "BaseUploadServer"):
                if imports.get("vkbottle_types.responses.base"):
                    imports["vkbottle_types.responses.base"].append(additional_response)
                else:
                    imports["vkbottle_types.responses.base"] = [additional_response]
            elif (
                additional_response not in ("int", "bool", "str", "list")
                and "typing.Dict" not in additional_response
            ):
                _import.append(additional_response.replace('"', ""))
    return {k: sorted(set(v)) for k, v in imports.items()}

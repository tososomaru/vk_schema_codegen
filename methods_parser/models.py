from typing import Any, Dict

from utils.strings_util import (
    camel_case_to_snake_case,
    convert_to_python_type,
    resolve_property_name,
    snake_case_to_camel_case,
)
import copy

CLASSMETHOD_PATTERN = (
    "\tasync def {snake_name}(\n"
    "\t\t{args}\n"
    "\t) -> {return_type}:\n"
    "\t\t{desc}\n"
    "\t\tparams = self.get_set_params(locals())\n"
    '\t\tresponse = await self.api.request("{name}", params)\n'
    "{model}\n"
    "\t\treturn model(**response).response"
)
OVERLOAD_PATTERN = (
    "\t@typing.overload\n"
    "\tasync def {snake_name}(\n"
    "\t\t{args}\n"
    "\t) -> {return_type}:\n"
    "\t\t...\n"
)


class ObjectModel:
    def __init__(self, method_name: str = "", method: dict = {}, **params):
        self.method = method
        self.method_name = method_name
        self.params = params


class Description(ObjectModel):
    def __str__(self):
        title = self.method.get("description") or self.method_name + " method"
        descriptions = []
        for param in self.params["sorted_params"]:
            param_description = param.get("description", "").strip()
            descriptions.append(
                f'\t\t:param {param["name"]}:'
                + ((" " + param_description) if param_description else "")
            )

        description = (
            ("\n\n" + "\n".join(descriptions) + "\n\t\t") if descriptions else ""
        )
        return f'"""{title}{description}"""\n'


class Annotation(ObjectModel):
    def __str__(self):
        items = self.params["items"]
        required = self.params["type"]
        param_annotate = convert_to_python_type(self.params["annotate"])
        overload = self.params["overload"]
        oveload_value = self.params["overload_value"]
        is_typed = self.params["is_typed"]

        if not is_typed:
            return "=None"

        if oveload_value:
            return f"{oveload_value}" + (" = ..." if not required else "")
        elif param_annotate == "list" and items.get("$ref", items.get("type")):
            if items.get("$ref"):
                post_annotate = "str"  # it's enum
            else:
                post_annotate = convert_to_python_type(items["type"])
            param_annotate = "typing.List[%s]" % convert_to_python_type(post_annotate)
        elif self.params.get("enum"):
            if isinstance(self.params["enum"][0], str):
                self.params["enum"] = [item.lower() for item in self.params["enum"]]
            return f"Literal{str(self.params['enum'])}" + (
                " = None"
                if not required and not overload
                else " = ..."
                if overload and not required
                else ""
            )
        if overload:
            return f"{param_annotate}" + (" = ..." if not required else "")
        if required is False:
            return f"typing.Optional[{param_annotate}] = None"
        return param_annotate


class ConvertToArgs(ObjectModel):
    def __str__(self):
        params = ["self"]
        for param in self.params["sorted_params"]:
            params.append(
                f"{param['name']}"
                + (": " if param.get("is_typed", True) else "")
                + str(
                    Annotation(
                        annotate=param["type"],
                        type=param.get("required", False),
                        items=param.get("items", {}),
                        overload=param.get("overload", False),
                        overload_value=param.get("overload_value"),
                        enum=param.get("enum", []),
                        is_typed=param.get("is_typed", True),
                    )
                )
            )

        params.append("**kwargs")
        return ", ".join(params)


class MethodForm:
    @staticmethod
    def parse_return_type(referense: str):
        response_base, response_object = referense.split("/")[-1].split("_", 1)
        if response_base == "base" and response_object == "getUploadServer_response":
            response_object = "BaseGetUploadServerResponse"
        return snake_case_to_camel_case(response_object)

    @staticmethod
    def costruct(**kwargs):
        params: Dict[str, Any] = copy.deepcopy(kwargs)
        if not params["additional_responses"]:
            params["model"] = f"\t\tmodel = {params['response']}"
            return CLASSMETHOD_PATTERN.format(**params)

        overloads = ""
        responses = []
        no_type_flag = False
        default_type_flag = False
        first_arg = params["args"].params["sorted_params"][0]
        overload_args = copy.deepcopy(params["args"])
        overload_keys = [
            key for keys in params["additional_responses"].keys() for key in keys
        ]
        for item in [
            item
            for item in overload_args.params["sorted_params"]
            if item["name"] in overload_keys
            and item["name"] not in first_arg.get("enum", [])
        ]:
            item["overload"] = True
            if item["type"] == "boolean":
                item["overload_value"] = "typing.Optional[Literal[False]]"
            else:
                item["overload_value"] = "typing.Optional[Literal[None]]"
        for (keys, response), return_type in zip(
            params["additional_responses"].items(), params["return_types"]
        ):
            args = copy.deepcopy(overload_args)
            enums = first_arg.get("enum", [])

            if first_arg.get("required") and all(key in enums for key in keys):
                responses.append(
                    f"""((["{first_arg['name']}", "{'", "'.join(keys)}"],), {response})"""
                )
                for k in keys:
                    first_arg["enum"].remove(k)
                args.params["sorted_params"][0]["overload"] = True
                args.params["sorted_params"][0][
                    "overload_value"
                ] = f"""Literal["{'", "'.join(keys)}"]"""
                overloads += (
                    OVERLOAD_PATTERN.format(
                        snake_name=params["snake_name"],
                        args=args,
                        return_type=return_type,
                    )
                    + "\n"
                )
                if not no_type_flag:
                    no_type_flag = True
                continue

            responses.append(
                f"""(("{'", "'.join(keys)}"{"," if len(keys) == 1 else ""}), {response})"""
            )
            args_ = [
                item for item in args.params["sorted_params"] if item["name"] in keys
            ]
            for item in args_:
                item["overload"] = True
                if not default_type_flag:
                    no_type_flag = True
                    default_type_flag = True
                    if item["type"] == "boolean":
                        item["overload_value"] = "typing.Optional[Literal[False]]"
                    else:
                        item["overload_value"] = "typing.Optional[Literal[None]]"
                    overloads += (
                        OVERLOAD_PATTERN.format(
                            snake_name=params["snake_name"],
                            args=args,
                            return_type=params["return_type"],
                        )
                        + "\n"
                    )
                item["overload_value"] = (
                    "Literal[True]" if item["type"] == "boolean" else ""
                )
                overloads += (
                    OVERLOAD_PATTERN.format(
                        snake_name=params["snake_name"],
                        args=args,
                        return_type=return_type,
                    )
                    + "\n"
                )

        params["model"] = (
            "\t\tmodel = self.get_model(\n"
            "\t\t\t(" + ", ".join(responses) + ",),\n"
            f"\t\t\tdefault={params['response']},\n"
            "\t\t\tparams=params,\n"
            "\t\t)"
        )
        if overloads and no_type_flag:
            if not default_type_flag:
                overloads += OVERLOAD_PATTERN.format(**params)
            for item in params["args"].params["sorted_params"]:
                item["is_typed"] = False
            if params["return_types"]:
                params["return_type"] = (
                    "typing.Union[\n"
                    + ", ".join([params["return_type"], *params["return_types"]])
                    + "]"
                )

        return overloads + CLASSMETHOD_PATTERN.format(**params)


class ClassForm:
    def __init__(self, classname, predproc="BaseCategory"):
        self.name = classname
        self.predproc = predproc
        self.constructed_methods = []

    def add_method(self, method_name, method, return_type_annotations):
        sorted_params = sorted(
            method.get("parameters", {}), key=lambda x: not x.get("required", False)
        )
        for item in sorted_params:
            item["name"] = resolve_property_name(item["name"])
        desc = Description(method_name, method, sorted_params=sorted_params)
        args = ConvertToArgs(sorted_params=sorted_params)
        response = None
        additional_responses = {}
        return_types = []
        for key, value in method["responses"].items():
            if key == "response":
                response_ = response = MethodForm.parse_return_type(value["$ref"])
            else:
                response_ = MethodForm.parse_return_type(value["$ref"])
                additional_responses[
                    tuple(
                        camel_case_to_snake_case(k)
                        for k in key.replace("Response", "").split("_")
                        if k
                    )
                ] = MethodForm.parse_return_type(value["$ref"])
            if response_ == "BoolResponse":
                return_types.append("BaseBoolInt")
            elif response_ == "BaseGetUploadServerResponse":
                return_types.append("BaseUploadServer")
            elif response_ == "OkResponse":
                return_types.append("int")
            else:
                return_types.append(
                    return_type_annotations.get(response_, response_).replace('"', "")
                )
        return_type = return_types.pop(0)
        self.constructed_methods.append(
            MethodForm.costruct(
                name=method_name,
                snake_name=camel_case_to_snake_case(method_name.split(".")[1]),
                args=args,
                desc=desc,
                response=response,
                return_type=return_type,
                return_types=return_types,
                additional_responses=additional_responses,
            )
        )

    def __str__(self):
        return (
            f"\n\nclass {snake_case_to_camel_case(self.name)}Category({self.predproc}):\n"
            + "\n\n".join(self.constructed_methods)
            + "\n"
        )

from io import StringIO

import autoflake
import black
import isort
from utils.titles import Imports, UpdateForwardRefs, ExportAll
from utils.tools import get_response_imports

from .models import jsonschema_object_factory, write_response_alias
from .response_utils import generate_response_dir, put_responses_by_filename


def parse_file(
    schema_path: str, filepath_to: str, imports: dict, tabulation="    "
) -> dict:
    files_dir = f"{filepath_to}/responses"
    filenames, json_dict = generate_response_dir(schema_path, files_dir)
    categorized_responses = {name: {} for name in sorted(filenames)}
    definitions = json_dict["definitions"]

    responses_by_files = put_responses_by_filename(definitions, categorized_responses)
    return_type_annotations = {}
    for filename, schema_body in responses_by_files.items():
        additional_imports = get_response_imports(schema_body)
        text = str(Imports(**imports, **additional_imports))
        if filename == "base":
            # just some hardcoded stuff
            schema_body["BaseGetUploadServerResponse"] = schema_body.pop(
                "GetUploadServerResponse"
            )
        text_, annotations = write_response_alias(schema_body)
        text += text_
        return_type_annotations[filename] = annotations
        export_objects = []
        for classname, body in schema_body.items():
            schema_object = jsonschema_object_factory(
                f"{classname}Model", body["properties"]
            )
            export_objects.append(classname)
            if not schema_object:
                continue
            if not isinstance(schema_object, list):
                text += str(schema_object)
                export_objects.append(schema_object.classname)  # type: ignore
                continue
            for item in schema_object:
                export_objects.append(item.classname)  # type: ignore
                text += str(item)
        text += str(UpdateForwardRefs(**schema_body, subclass="BaseResponse"))
        text += str(
            ExportAll(
                *sorted(
                    [*additional_imports["vkbottle_types.objects"], *export_objects]
                )
            )
        )
        text = autoflake.fix_code(text, remove_all_unused_imports=True)
        text = text.replace("\t", tabulation)
        output = StringIO()
        isort.stream(StringIO(text), output, profile="black")
        text = output.getvalue()
        text = black.format_str(text, mode=black.FileMode())
        with open(f"{filepath_to}/responses/{filename}.py", "w") as file:
            file.write(text)
    return return_type_annotations

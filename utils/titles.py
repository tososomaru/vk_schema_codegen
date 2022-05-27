import abc


class AbstractTitle(abc.ABC):
    def __init__(self, **params):
        self.params = params

    @abc.abstractmethod
    def __repr__(self):
        pass


class Imports(AbstractTitle):
    def __repr__(self):
        imports = ""
        for key, value in self.params.items():
            if not value:
                imports += f"import {key}\n"
                continue
            formatted = ", ".join(value)
            if len(formatted) >= 80:
                formatted = "(\n\t" + formatted.replace(", ", ",\n\t") + "\n)"
            imports += f"from {key} import {formatted}\n"
        return imports


class UpdateForwardRefs(AbstractTitle):
    def __repr__(self):
        return (
            "\n\n"
            + (
                "for item in locals().copy().values():"
                "\n\tif inspect.isclass(item) and issubclass("
                f"item, {self.params.get('subclass', 'BaseModel')}):"
                "\n\t\titem.update_forward_refs()"
            )
            + "\n"
        )


class ExportAll(AbstractTitle):
    def __init__(self, *objects):
        self.objects = objects

    def __repr__(self):
        return (
            "\n\n"
            + ("__all__ = (\n\t")
            + ",\n\t".join(f'"{_}"' for _ in self.objects)
            + ",\n)\n"
        )

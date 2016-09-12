import os, yaml
from . import resolver


def render_from_path(path, context={}):
    abs_source = os.path.abspath(os.path.expanduser(path))
    yaml_resolver = resolver.TYamlResolver.new_from_path(abs_source)

    return yaml_resolver.resolve(context)


def render_from_string(content, context={}):
    yaml_resolver = resolver.TYamlResolver.new_from_string(content)

    return yaml_resolver.resolve(context)
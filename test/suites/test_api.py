import templated_yaml.api as tapi, yaml
import os


def get_test_paths(folder):
    return (config_path(folder, 'input.yml'), config_path(folder, 'expected-output.yml'))


def get_contents(file):
    with open(file, 'r') as stream:
        return stream.read()


def config_path(folder, file):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs/{}/{}'.format(folder, file))


def run_test(test_name):
    input, output = get_test_paths(test_name)
    processed_input = tapi.render_from_path(input)
    expected_output = yaml.load(get_contents(output))

    assert processed_input == expected_output


def test_simple_render():
    run_test('tyaml.variable-substitution')


def test_nested_render():
    run_test('tyaml.nested-variable-substitution')


def test_extends_render():
    run_test('tyaml.extends')


def test_extends_multiple_parents_render():
    run_test('tyaml.extends-multiple-parents')


def test_extends_multiple_mixins_render():
    run_test('tyaml.extends-multiple-mixins')


def test_extends_preserve_child_render():
    run_test('tyaml.extends-preserve-child')


def test_newline_render():
    run_test('tyaml.newline-test')


def test_list_variable_substitution():
    run_test('tyaml.list-variable-substitution')

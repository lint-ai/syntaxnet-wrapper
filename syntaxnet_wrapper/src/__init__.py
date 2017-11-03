import yaml
import os.path as path
import os

# Load config file and paths
if os.environ.get('SYNTAXNET_WRAPPER_CONFIG') is not None:
    file_path = os.environ['SYNTAXNET_WRAPPER_CONFIG']
elif path.exists('/usr/share/syntaxnet_wrapper_config.yml'):
    file_path = '/usr/share/syntaxnet_wrapper_config.yml'
elif path.exists(path.join(path.dirname(__file__), '../config.yml')):
    file_path = path.join(path.dirname(__file__), '../config.yml')
else:
    raise ValueError("SyntaxNet Wrapper config file can not be found")

config_file = yaml.load(open(file_path))
config_syntaxnet = config_file['syntaxnet']
root_dir = config_syntaxnet['ROOT_DIR']
parser_eval_path = config_syntaxnet['PARSER_EVAL']
context_path = config_syntaxnet['CONTEXT']
model_path = config_syntaxnet['MODEL']

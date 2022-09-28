from GUI import start_gui
from initialization.load_defaults import load_defaults

json_defaults_file = 'initialization/defaults/defaults.json'

if __name__ == '__main__':
    defaults = load_defaults(json_defaults_file)
    print(defaults.__str__())

    start_gui(defaults.__str__())

# ParamSet

ParamSet is a Python program that generates a graphical user interface (GUI) based on parameters defined in a JSON file. It uses the tkinter library to create the GUI and provides various input widgets based on the type of parameter.

## Features

- Reads parameters from a JSON file
- Dynamically creates input widgets such as entry fields, spinboxes, checkboxes, and radio buttons
- Supports different states for parameters (normal, disabled, readonly)

## Requirements

- Python 3.x
- tkinter library (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/amonmk2/ParamSet.git
    ```

2. Navigate to the directory:

    ```bash
    cd ParamSet
    ```

3. Run the program:

    ```bash
    python3 param_set.py
    ```

## Usage

1. Upon running the program, the GUI will display parameters loaded from the specified JSON file.
2. Input values for each parameter as required.
3. Click the OK button to save changes or the CANCEL button to exit without saving.

## Parameter Definition

The JSON file should follow this format:

```json
{
    "00": {
        "param1": {
            "method": "create_entry",
            "label": "Parameter 1",
            "defvalue": "default_value",
            "state": "normal"
        }
    },
    "01": {
        "param2": {
            "method": "create_label",
            "label": "Parameter 2",
            "defvalue": "",
            "state": "normal"
        }
    },
    ...
}
```

- The numeric keys indicate the order in which widgets are displayed.
- To disable the generation of a widget, change the numeric key to "//".
- `method`: The method used to create the parameter's input widget
- `label`: The label displayed for the parameter
- `defvalue`: The default value for the parameter
- `state`: The state of the parameter (normal, disabled, readonly, etc.)

## Example Parameters

### 1. create_label

```json
"00": {
    "param1": {
        "method": "create_label",
        "label": "Parameter Label",
        "defvalue": "",
        "state": "normal"
    }
}
```

### 2. create_entry

```json
"01": {
    "param2": {
        "method": "create_entry",
        "label": "Parameter Entry",
        "defvalue": "default_value",
        "state": "normal"
    }
}
```

### 3. create_entry_filedialog

```json
"02": {
    "param3": {
        "method": "create_entry_filedialog",
        "label": "Parameter Entry (File Dialog)",
        "defvalue": "default_file",
        "state": "normal"
    }
}
```

### 4. create_spinbox

```json
"03": {
    "param4": {
        "method": "create_spinbox",
        "label": "Parameter Spinbox",
        "list": ["1", "2", "3", "4", "5"],
        "defvalue": "3",
        "state": "normal"
    }
}
```

### 5. create_listbox

```json
"04": {
    "param5": {
        "method": "create_listbox",
        "label": "Parameter Listbox",
        "list": ["Option 1", "Option 2", "Option 3"],
        "defvalue": 0,
        "state": "normal"
    }
}
```

### 6. create_checkbutton

```json
"05": {
    "param6": {
        "method": "create_checkbutton",
        "label": "Parameter Checkbutton",
        "button_label": "Check Option",
        "defvalue": "true",
        "state": "normal"
    }
}
```

### 7. create_radiobutton

```json
"06": {
    "param7": {
        "method": "create_radiobutton",
        "label": "Parameter Radiobutton",
        "list": ["Option A", "Option B", "Option C"],
        "defvalue": 1,
        "state": "normal"
    }
}
```

## Contributing

Contributions, bug reports, and feature requests are welcome! Please feel free to open an issue or submit a pull request.



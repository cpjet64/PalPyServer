# ini_parser.py


def read_and_parse(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        section_started = False
        section_content = []
        for line in lines:
            if "OptionSettings=(" in line:
                section_started = True
            if section_started:
                section_content.append(line.strip())
                if line.strip().endswith(")"):
                    break

        return section_content, lines
    except FileNotFoundError:
        return [], []


def extract_pairs(section_content):
    extracted_pairs = []
    content = " ".join(section_content)
    content = (
        content.split("OptionSettings=(", 1)[1].rstrip(")") if section_content else ""
    )
    key_values = [kv.strip() for kv in content.split(",") if "=" in kv]

    for kv in key_values:
        key, value = kv.split("=", 1)
        # Try to remove trailing zeros from the value and convert it back to a float,
        # if it contains a decimal point and value is a valid number
        try:
            value = str(float(value)).rstrip("0").rstrip(".") if "." in value else value
        except ValueError:
            pass  # the value must be a string and not a number
        extracted_pairs.append((key.strip(), value.strip()))

    return extracted_pairs


def reconstruct_section(modified_pairs, original_section):
    new_section = (
        original_section[0].split("OptionSettings=(")[0] + "OptionSettings=("
        if original_section
        else "OptionSettings=("
    )
    new_content = ", ".join([f"{k}={v}" for k, v in modified_pairs.items()])
    new_section += new_content + ")"
    return new_section


def rewrite_file(new_file_path, new_section, original_lines):
    with open(new_file_path, "w") as file:
        section_started = False
        for line in original_lines:
            if "OptionSettings=(" in line and not section_started:
                file.write(new_section + "\n")
                section_started = True
            elif section_started and line.endswith(")\n"):
                section_started = False
            elif not section_started:
                file.write(line)


def load_settings(default_file_path, modified_file_path):
    try:
        if not open(modified_file_path, "r").read().strip():
            file_path_to_use = default_file_path
        else:
            file_path_to_use = modified_file_path
    except FileNotFoundError:
        file_path_to_use = default_file_path

    section_content, _ = read_and_parse(file_path_to_use)
    return extract_pairs(section_content)


def save_modified_pairs(default_file_path, modified_file_path, modified_pairs):
    original_lines = []
    with open(default_file_path, "r") as file:
        original_lines = file.readlines()

    new_section = reconstruct_section(modified_pairs, original_lines)
    rewrite_file(modified_file_path, new_section, original_lines)

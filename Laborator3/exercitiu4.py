# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "

def build_xml_element(tag, content, **kwargs):
    string = f"<{tag} "
    for key, value in kwargs.items():
        string += f'"{key} = "{value} \ '
    string += '"> '
    string += f' {content} "'
    return string


if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

    # <a href=" http: // python.org \ "_class = " my - link \ "id = " someid \ "> Hello there "

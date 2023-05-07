def polyfill_css(variables_file, stylesheet_file):
    """
    This function takes in a variables file and a stylesheet file and
    returns a new stylesheet string with the variables replaced with
    their values.
    """
    with open(variables_file, 'r') as f:
        variables = f.read()
    
    custom_properties = {}
    for line in variables.split('\n'):
        if ': ' in line:
            property_name, property_value = line.split(': ')
            # trim property_name
            property_name = property_name.strip()
            property_value = property_value.strip()

            # remove any ';' from property_value
            property_value = property_value.replace(';', '')
            custom_properties[property_name] = property_value

    
    
    # Read in the stylesheet CSS file and substitute the custom properties
    with open(stylesheet_file, 'r') as f:
        stylesheet = f.read()
    
    for property_name, property_value in custom_properties.items():
        
        property_to_replace = f'var({property_name})'
        # print(property_name, property_value, property_to_replace)
        stylesheet = stylesheet.replace(property_to_replace, property_value)
    
    print(stylesheet)
    # Print out the resulting new stylesheet
    return stylesheet


if __name__ == '__main__':

    """ save the polyfilled stylesheets to dist/"""

    dolphin_light = polyfill_css('css/light.css', 'css/dolphin.css')

    # save to dist/dark.css
    with open('dist/light.css', 'w') as f:
        f.write(dolphin_light)
    
    dolphin_dark = polyfill_css('css/dark.css', 'css/dolphin.css')

    # save to dist/dark.css
    with open('dist/dark.css', 'w') as f:
        f.write(dolphin_dark)

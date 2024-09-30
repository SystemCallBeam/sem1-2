import re

def decode_string(s):
    return re.sub(r'M([eE])(\d{2})([wW])', lambda m: chr(int(m.group(2)) + (65 if m.group(1) == 'E' else 97)), s)

decoded_message = decode_string('Me05wMe02wMe08wMe00wME02WME19WME05WMe{00ME12WMe04wM3000Me22wMe_00Me12wMe04wMe14wMe22wMe_00ME18WME20WME15WME04WME17WME15WM3000ME15WME02WM3004ME19WMe}00')
print(decoded_message)

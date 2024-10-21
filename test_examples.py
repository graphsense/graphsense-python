import pypandoc
import json
import os
import glob
from io import StringIO
from contextlib import redirect_stdout

pattern = "*Api"
key = os.environ.get('API_KEY')
url = os.environ.get('API_URL')

for fil in glob.glob("./docs/"+pattern+".md"):
    print(fil)
    data = pypandoc.convert_file(fil, 'json')

    for block in json.loads(data)['blocks']:
        if block['t'] != 'CodeBlock':
            continue
        code = block['c'][1].replace('YOUR_API_KEY', key)
        code = code.replace('https://api.ikna.io', url)
        f = StringIO()
        try:
            with redirect_stdout(f):
                exec(code)
            output = f.getvalue()
            if 'Exception' in output:
                raise Exception(output)

        except Exception as e:
            print(code)
            raise e

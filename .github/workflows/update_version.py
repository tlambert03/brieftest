import tomlkit
import os
from brieftest import __version__

tomlfile = os.path.join(os.path.dirname(__file__), '..', '..', 'pyproject.toml')

with open(tomlfile, 'r') as f:
    content = f.read()

doc = tomlkit.parse(content)
doc['tool']['briefcase']['version'] = __version__

with open(tomlfile, 'w') as f:
    f.write(tomlkit.dumps(doc))

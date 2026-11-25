from pathlib import Path
import json
from analysis import analyse
p=Path(__file__).parent
s=(p/'dashboard.template.html').read_text(); (p/'index.html').write_text(s.replace('__METRICS__',json.dumps(analyse())))

import re
import sys
t = "\n".join([i.strip() for i in sys.stdin])
print("\n".join(re.findall(r"//.*|/\*[\S\s]*?\*/", t)))

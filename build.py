# Inlines data.json into template.html -> index.html
import json, datetime
d = json.load(open("data.json")); d["generated"] = datetime.date.today().isoformat()
open("index.html", "w").write(open("template.html").read().replace("__DATA__", json.dumps(d, ensure_ascii=False)))

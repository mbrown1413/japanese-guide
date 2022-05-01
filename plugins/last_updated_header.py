import hashlib
import json
import os
from typing import Dict
from datetime import datetime

from mkdocs.plugins import BasePlugin

LAST_UPDATED_FILE = "last_updated.json"

today = datetime.today().isoformat(" ").split(" ")[0]


def get_last_updated_date(file: str, contents: str):

    # Load update data from file
    data: Dict[str, dict]  # {<file_path>: <page_info>}
    page_info: Dict[str, str]  # Keys: last_updated, contents_hash
    if os.path.exists(LAST_UPDATED_FILE):
        with open(LAST_UPDATED_FILE) as f:
            data = json.load(f)
    else:
        data = {}

    page_info = data.get(file, {})
    last_updated = page_info.get("last_updated", today)
    old_hash = page_info.get("contents_hash", None)

    # Compare contents with old contents
    new_hash = hashlib.sha256(contents.encode()).hexdigest()
    if new_hash != old_hash:
        # Contents have changed! Update our data
        last_updated = today
        data[file] = {
            "last_updated": last_updated,
            "contents_hash": new_hash,
        }
        with open(LAST_UPDATED_FILE, "w") as f:
            json.dump(data, f)

    return last_updated

class LastUpdatedHeaderPlugin(BasePlugin):

    def on_page_markdown(self, markdown, page, config,
                         site_navigation=None, **kwargs):
        last_updated = get_last_updated_date(page.file.src_path, markdown)
        header = f"""
<div style="float: right; color: #aaa">
    Page last updated {last_updated}
</div>
        """.strip()
        return header + markdown

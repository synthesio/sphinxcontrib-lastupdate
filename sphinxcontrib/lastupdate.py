# Lastupdate transform for Sphinx.
import os
from datetime import datetime

from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util.i18n import format_date
from sphinx.locale import _


class LastUpdate(SphinxTransform):
    # run before the default Substitutions
    default_priority = 210

    def apply(self):
        for ref in self.document.traverse(nodes.substitution_reference):
            if ref['refname'] == 'lastupdate':
                statbuf = os.stat('%s.rst' % self.env.docname)
                mtime = datetime.fromtimestamp(statbuf.st_mtime)
                # special handling: can also specify a strftime format
                text = format_date(_('%b %d, %Y'), date=mtime,
                                   language=self.config.language)
                ref.replace_self(nodes.Text(text, text))


def setup(app):
    app.add_transform(LastUpdate)

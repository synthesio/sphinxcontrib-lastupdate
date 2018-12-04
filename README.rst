=========================
 sphinxcontrib-lastupdate
=========================

This package contains sphinxcontrb.lastupdate, to add a last update substitution for
Sphinx-based documentation.


Installation
============

1. ``pip install sphinxcontrib-lastupdate``

Configuration
=============

1. Add ``'sphinxcontrib.lastupdate'`` to the ``extensions`` list in ``conf.py``.

  ::

    extensions = [ 'sphinxcontrib.lastupdate' ]


Usage
=====

To insert last update modification of current file, use something like::

    :Lastupdate: |lastupdate|

History
=======

0.1
  First public release.

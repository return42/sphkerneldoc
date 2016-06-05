.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _vintage-kernel-doc-mode:

=======================
Vintage kernel-doc mode
=======================

All kernel-doc markup is processed as described in :ref:`kernel-doc-syntax`, all
descriptive text is further processed, scanning for the following special
patterns, which are highlighted appropriately.

* ``funcname()``   - function
* ``$ENVVAR``      - environmental variable
* ``&struct name`` - name of a structure (up to two words including ``struct``)
* ``@parameter``   - name of a parameter
* ``%CONST``       - name of a constant.

These highlighted patterns are not used when you are using the reST addition
(:ref:`reST-kernel-doc-mode`).  This is, because reST brings it's own markup to
refer and highlight function, structs or whatever definition.

Within the *vintage* kernel-doc mode the kernel-doc parser highlights the pattern
above, but he also dogged ignores any whitespace formatting/markup.

.. hint::

   Formatting with whitespaces is substantial for ASCII markups. By this, it's
   recommended to use the :ref:`reST-kernel-doc-mode` on any new or changed
   comment.


.. _vintage-mode-quirks:

vintage mode quirks
===================

In the following, you will find some quirks of the *vintage* kernel-doc mode.

* Since a colon introduce a new section, you can't use colons. E.g. a comment
  line like::

      prints out: hello world

  will result in a section with the title "prints out" and a paragraph with only
  "hello world" in, this is mostly not what you expect. To avoid sectioning,
  place a space in front of the column::

      prints out : hello world

* The multi-line descriptive text you provide does *not* recognize
  line breaks, so if you try to format some text nicely, as in::

      Return:
         0 - cool
         1 - invalid arg
         2 - out of memory

  this will all run together and produce::

      Return: 0 - cool 1 - invalid arg 2 - out of memory

* If the descriptive text you provide has lines that begin with some phrase
  followed by a colon, each of those phrases will be taken as a new section
  heading, which means you should similarly try to avoid text like::

      Return:
        0: cool
        1: invalid arg
        2: out of memory

  every line of which would start a new section.  Again, probably not what you
  were after.

Determined by the historical development of the kernel-doc comments, the
*vintage* kernel-doc comments contain characters like "*" or strings with
e.g. leading/trailing underscore ("_"), which are inline markups in reST. Here a
short example from a *vintage* comment::

    <SNIP> -----
    * In contrast to the other drm_get_*_name functions this one here returns a
    * const pointer and hence is threadsafe.
    <SNAP> -----

Within reST markup (the new bas format), the wildcard in the string
``drm_get_*_name`` has to be masked: ``drm_get_\\*_name``. Some more examples
from reST markup:

* Emphasis "*":  like ``*emphasis*`` or ``**emphasis strong**``
* Leading "_" :  is a *anchor* in reST markup (``_foo``).
* Trailing "_:  is a reference in reST markup (``foo_``).
* interpreted text: "`"
* inline literals: "``"
* substitution references: "|"

As long as you in the *vintage* kernel-doc mode, these special strings will be
masked in the reST output and can't be used as *plain-text markup*.



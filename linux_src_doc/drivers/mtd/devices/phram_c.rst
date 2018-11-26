.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/devices/phram.c

.. _`pr_fmt`:

pr_fmt
======

.. c:function::  pr_fmt( fmt)

    Copyright (c) 2003-2004      Joern Engel <joern@wh.fh-wedel.de>

    :param fmt:
        *undescribed*
    :type fmt: 

.. _`pr_fmt.usage`:

Usage
-----


one commend line parameter per device, each in the form:
phram=<name>,<start>,<len>
<name> may be up to 63 characters.
<start> and <len> can be octal, decimal or hexadecimal.  If followed
by "ki", "Mi" or "Gi", the numbers will be interpreted as kilo, mega or
gigabytes.

.. _`pr_fmt.example`:

Example
-------

.. code-block:: c

    phram=swap,64Mi,128Mi phram=test,900Mi,1Mi


.. This file was automatic generated / don't edit.


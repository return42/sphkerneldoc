.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/earlycon.c

.. _`setup_earlycon`:

setup_earlycon
==============

.. c:function:: int setup_earlycon(char *buf)

    match and register earlycon console

    :param char \*buf:
        earlycon param string

.. _`setup_earlycon.description`:

Description
-----------

Registers the earlycon console matching the earlycon specified
in the param string \ ``buf``\ . Acceptable param strings are of the form
<name>,io\|mmio\|mmio32\|mmio32be,<addr>,<options>
<name>,0x<addr>,<options>
<name>,<options>
<name>

Only for the third form does the earlycon \ :c:func:`setup`\  method receive the
<options> string in the 'options' parameter; all other forms set
the parameter to NULL.

Returns 0 if an attempt to register the earlycon was made,
otherwise negative error code

.. This file was automatic generated / don't edit.


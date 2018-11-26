.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/amba-pl011.c

.. _`pl011_console_match`:

pl011_console_match
===================

.. c:function:: int pl011_console_match(struct console *co, char *name, int idx, char *options)

    non-standard console matching

    :param co:
        registering console
    :type co: struct console \*

    :param name:
        name from console command line
    :type name: char \*

    :param idx:
        index from console command line
    :type idx: int

    :param options:
        ptr to option string from console command line
    :type options: char \*

.. _`pl011_console_match.only-attempts-to-match-console-command-lines-of-the-form`:

Only attempts to match console command lines of the form
--------------------------------------------------------

console=pl011,mmio\|mmio32,<addr>[,<options>]
console=pl011,0x<addr>[,<options>]
This form is used to register an initial earlycon boot console and
replace it with the amba_console at pl011 driver init.

Performs console setup for a match (as required by interface)
If no <options> are specified, then assume the h/w is already setup.

Returns 0 if console matches; otherwise non-zero to use default matching

.. This file was automatic generated / don't edit.


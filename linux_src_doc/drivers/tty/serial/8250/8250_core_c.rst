.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/8250/8250_core.c

.. _`serial8250_get_port`:

serial8250_get_port
===================

.. c:function:: struct uart_8250_port *serial8250_get_port(int line)

    retrieve struct uart_8250_port

    :param line:
        serial line number
    :type line: int

.. _`serial8250_get_port.description`:

Description
-----------

This function retrieves struct uart_8250_port for the specific line.
This struct *must* *not* be used to perform a 8250 or serial core operation
which is not accessible otherwise. Its only purpose is to make the struct
accessible to the runtime-pm callbacks for context suspend/restore.
The lock assumption made here is none because runtime-pm suspend/resume
callbacks should not be invoked if there is any operation performed on the
port.

.. _`univ8250_console_match`:

univ8250_console_match
======================

.. c:function:: int univ8250_console_match(struct console *co, char *name, int idx, char *options)

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

.. _`univ8250_console_match.only-attempts-to-match-console-command-lines-of-the-form`:

Only attempts to match console command lines of the form
--------------------------------------------------------

         console=uart[8250],io|mmio|mmio16|mmio32,<addr>[,<options>]
         console=uart[8250],0x<addr>[,<options>]
     This form is used to register an initial earlycon boot console and
     replace it with the serial8250_console at 8250 driver init.

     Performs console setup for a match (as required by interface)
     If no <options> are specified, then assume the h/w is already setup.

     Returns 0 if console matches; otherwise non-zero to use default matching

.. _`serial8250_suspend_port`:

serial8250_suspend_port
=======================

.. c:function:: void serial8250_suspend_port(int line)

    suspend one serial port

    :param line:
        serial line number
    :type line: int

.. _`serial8250_suspend_port.description`:

Description
-----------

     Suspend one serial port.

.. _`serial8250_resume_port`:

serial8250_resume_port
======================

.. c:function:: void serial8250_resume_port(int line)

    resume one serial port

    :param line:
        serial line number
    :type line: int

.. _`serial8250_resume_port.description`:

Description
-----------

     Resume one serial port.

.. _`serial8250_register_8250_port`:

serial8250_register_8250_port
=============================

.. c:function:: int serial8250_register_8250_port(struct uart_8250_port *up)

    register a serial port

    :param up:
        serial port template
    :type up: struct uart_8250_port \*

.. _`serial8250_register_8250_port.description`:

Description
-----------

     Configure the serial port specified by the request. If the
     port exists and is in use, it is hung up and unregistered
     first.

     The port is then probed and if necessary the IRQ is autodetected
     If this fails an error is returned.

     On success the port is ready to use and the line number is returned.

.. _`serial8250_unregister_port`:

serial8250_unregister_port
==========================

.. c:function:: void serial8250_unregister_port(int line)

    remove a 16x50 serial port at runtime

    :param line:
        serial line number
    :type line: int

.. _`serial8250_unregister_port.description`:

Description
-----------

     Remove one serial port.  This may not be called from interrupt
     context.  We hand the port back to the our control.

.. This file was automatic generated / don't edit.


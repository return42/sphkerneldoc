.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/serial_txx9.c

.. _`serial_txx9_register_port`:

serial_txx9_register_port
=========================

.. c:function:: int serial_txx9_register_port(struct uart_port *port)

    register a serial port

    :param struct uart_port \*port:
        serial port template

.. _`serial_txx9_register_port.description`:

Description
-----------

Configure the serial port specified by the request.

The port is then probed and if necessary the IRQ is autodetected
If this fails an error is returned.

On success the port is ready to use and the line number is returned.

.. _`serial_txx9_unregister_port`:

serial_txx9_unregister_port
===========================

.. c:function:: void serial_txx9_unregister_port(int line)

    remove a txx9 serial port at runtime

    :param int line:
        serial line number

.. _`serial_txx9_unregister_port.description`:

Description
-----------

Remove one serial port.  This may not be called from interrupt
context.  We hand the port back to the our control.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/pch_uart.c

.. _`pch_uart_driver_data`:

struct pch_uart_driver_data
===========================

.. c:type:: struct pch_uart_driver_data

    private data structure for UART-DMA

.. _`pch_uart_driver_data.definition`:

Definition
----------

.. code-block:: c

    struct pch_uart_driver_data {
        int port_type;
        int line_no;
    }

.. _`pch_uart_driver_data.members`:

Members
-------

port_type
    The type of UART port

line_no
    UART port line number (0, 1, 2...)

.. This file was automatic generated / don't edit.


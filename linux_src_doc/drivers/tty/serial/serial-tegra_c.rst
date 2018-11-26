.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/serial-tegra.c

.. _`tegra_uart_wait_cycle_time`:

tegra_uart_wait_cycle_time
==========================

.. c:function:: void tegra_uart_wait_cycle_time(struct tegra_uart_port *tup, unsigned int cycles)

    Wait for N UART clock periods

    :param tup:
        Tegra serial port data structure.
    :type tup: struct tegra_uart_port \*

    :param cycles:
        Number of clock periods to wait.
    :type cycles: unsigned int

.. _`tegra_uart_wait_cycle_time.description`:

Description
-----------

Tegra UARTs are clocked at 16X the baud/bit rate and hence the UART
clock speed is 16X the current baud rate.

.. This file was automatic generated / don't edit.


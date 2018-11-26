.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/men_z135_uart.c

.. _`men_z135_reg_set`:

men_z135_reg_set
================

.. c:function:: void men_z135_reg_set(struct men_z135_port *uart, u32 addr, u32 val)

    Set value in register

    :param uart:
        The UART port
    :type uart: struct men_z135_port \*

    :param addr:
        Register address
    :type addr: u32

    :param val:
        value to set
    :type val: u32

.. _`men_z135_reg_clr`:

men_z135_reg_clr
================

.. c:function:: void men_z135_reg_clr(struct men_z135_port *uart, u32 addr, u32 val)

    Unset value in register

    :param uart:
        The UART port
    :type uart: struct men_z135_port \*

    :param addr:
        Register address
    :type addr: u32

    :param val:
        value to clear
    :type val: u32

.. _`men_z135_handle_modem_status`:

men_z135_handle_modem_status
============================

.. c:function:: void men_z135_handle_modem_status(struct men_z135_port *uart)

    Handle change of modem status

    :param uart:
        *undescribed*
    :type uart: struct men_z135_port \*

.. _`men_z135_handle_modem_status.description`:

Description
-----------

Handle change of modem status register. This is done by reading the "delta"
versions of DCD (Data Carrier Detect) and CTS (Clear To Send).

.. _`get_rx_fifo_content`:

get_rx_fifo_content
===================

.. c:function:: u16 get_rx_fifo_content(struct men_z135_port *uart)

    Get the number of bytes in RX FIFO

    :param uart:
        The UART port
    :type uart: struct men_z135_port \*

.. _`get_rx_fifo_content.description`:

Description
-----------

Read RXC register from hardware and return current FIFO fill size.

.. _`men_z135_handle_rx`:

men_z135_handle_rx
==================

.. c:function:: void men_z135_handle_rx(struct men_z135_port *uart)

    RX tasklet routine

    :param uart:
        *undescribed*
    :type uart: struct men_z135_port \*

.. _`men_z135_handle_rx.description`:

Description
-----------

Copy from RX FIFO and acknowledge number of bytes copied.

.. _`men_z135_handle_tx`:

men_z135_handle_tx
==================

.. c:function:: void men_z135_handle_tx(struct men_z135_port *uart)

    TX tasklet routine

    :param uart:
        *undescribed*
    :type uart: struct men_z135_port \*

.. _`men_z135_intr`:

men_z135_intr
=============

.. c:function:: irqreturn_t men_z135_intr(int irq, void *data)

    Handle legacy IRQs

    :param irq:
        The IRQ number
    :type irq: int

    :param data:
        Pointer to UART port
    :type data: void \*

.. _`men_z135_intr.description`:

Description
-----------

Check IIR register to find the cause of the interrupt and handle it.
It is possible that multiple interrupts reason bits are set and reading
the IIR is a destructive read, so we always need to check for all possible
interrupts and handle them.

.. _`men_z135_request_irq`:

men_z135_request_irq
====================

.. c:function:: int men_z135_request_irq(struct men_z135_port *uart)

    Request IRQ for 16z135 core

    :param uart:
        z135 private uart port structure
    :type uart: struct men_z135_port \*

.. _`men_z135_request_irq.description`:

Description
-----------

Request an IRQ for 16z135 to use. First try using MSI, if it fails
fall back to using legacy interrupts.

.. _`men_z135_tx_empty`:

men_z135_tx_empty
=================

.. c:function:: unsigned int men_z135_tx_empty(struct uart_port *port)

    Handle tx_empty call

    :param port:
        The UART port
    :type port: struct uart_port \*

.. _`men_z135_tx_empty.description`:

Description
-----------

This function tests whether the TX FIFO and shifter for the port
described by \ ``port``\  is empty.

.. _`men_z135_set_mctrl`:

men_z135_set_mctrl
==================

.. c:function:: void men_z135_set_mctrl(struct uart_port *port, unsigned int mctrl)

    Set modem control lines

    :param port:
        The UART port
    :type port: struct uart_port \*

    :param mctrl:
        The modem control lines
    :type mctrl: unsigned int

.. _`men_z135_set_mctrl.description`:

Description
-----------

This function sets the modem control lines for a port described by \ ``port``\ 
to the state described by \ ``mctrl``\ 

.. _`men_z135_get_mctrl`:

men_z135_get_mctrl
==================

.. c:function:: unsigned int men_z135_get_mctrl(struct uart_port *port)

    Get modem control lines

    :param port:
        The UART port
    :type port: struct uart_port \*

.. _`men_z135_get_mctrl.description`:

Description
-----------

Retruns the current state of modem control inputs.

.. _`men_z135_stop_tx`:

men_z135_stop_tx
================

.. c:function:: void men_z135_stop_tx(struct uart_port *port)

    Stop transmitting characters

    :param port:
        The UART port
    :type port: struct uart_port \*

.. _`men_z135_stop_tx.description`:

Description
-----------

Stop transmitting characters. This might be due to CTS line becomming
inactive or the tty layer indicating we want to stop transmission due to
an XOFF character.

.. _`men_z135_start_tx`:

men_z135_start_tx
=================

.. c:function:: void men_z135_start_tx(struct uart_port *port)

    Start transmitting characters

    :param port:
        The UART port
    :type port: struct uart_port \*

.. _`men_z135_start_tx.description`:

Description
-----------

Start transmitting character. This actually doesn't transmit anything, but
fires off the TX tasklet.

.. _`men_z135_stop_rx`:

men_z135_stop_rx
================

.. c:function:: void men_z135_stop_rx(struct uart_port *port)

    Stop receiving characters

    :param port:
        The UART port
    :type port: struct uart_port \*

.. _`men_z135_stop_rx.description`:

Description
-----------

Stop receiving characters; the port is in the process of being closed.

.. _`men_z135_enable_ms`:

men_z135_enable_ms
==================

.. c:function:: void men_z135_enable_ms(struct uart_port *port)

    Enable Modem Status

    :param port:
        *undescribed*
    :type port: struct uart_port \*

.. _`men_z135_enable_ms.port`:

port
----


Enable Modem Status IRQ.

.. _`men_z135_probe`:

men_z135_probe
==============

.. c:function:: int men_z135_probe(struct mcb_device *mdev, const struct mcb_device_id *id)

    Probe a z135 instance

    :param mdev:
        The MCB device
    :type mdev: struct mcb_device \*

    :param id:
        The MCB device ID
    :type id: const struct mcb_device_id \*

.. _`men_z135_probe.description`:

Description
-----------

men_z135_probe does the basic setup of hardware resources and registers the
new uart port to the tty layer.

.. _`men_z135_remove`:

men_z135_remove
===============

.. c:function:: void men_z135_remove(struct mcb_device *mdev)

    Remove a z135 instance from the system

    :param mdev:
        The MCB device
    :type mdev: struct mcb_device \*

.. _`men_z135_init`:

men_z135_init
=============

.. c:function:: int men_z135_init( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`men_z135_init.description`:

Description
-----------

men_z135_init is the first routine called when the driver is loaded. All it
does is register with the legacy MEN Chameleon subsystem.

.. _`men_z135_exit`:

men_z135_exit
=============

.. c:function:: void __exit men_z135_exit( void)

    Driver Exit Routine

    :param void:
        no arguments
    :type void: 

.. _`men_z135_exit.description`:

Description
-----------

men_z135_exit is called just before the driver is removed from memory.

.. This file was automatic generated / don't edit.


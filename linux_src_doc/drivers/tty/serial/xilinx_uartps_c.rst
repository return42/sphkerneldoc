.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/xilinx_uartps.c

.. _`cdns_uart`:

struct cdns_uart
================

.. c:type:: struct cdns_uart

    device data

.. _`cdns_uart.definition`:

Definition
----------

.. code-block:: c

    struct cdns_uart {
        struct uart_port *port;
        struct clk *uartclk;
        struct clk *pclk;
        struct uart_driver *cdns_uart_driver;
        unsigned int baud;
        int id;
        struct notifier_block clk_rate_change_nb;
        u32 quirks;
    }

.. _`cdns_uart.members`:

Members
-------

port
    Pointer to the UART port

uartclk
    Reference clock

pclk
    APB clock

cdns_uart_driver
    Pointer to UART driver

baud
    Current baud rate

id
    Port ID

clk_rate_change_nb
    Notifier block for clock changes

quirks
    Flags for RXBS support.

.. _`cdns_uart_handle_rx`:

cdns_uart_handle_rx
===================

.. c:function:: void cdns_uart_handle_rx(void *dev_id, unsigned int isrstatus)

    Handle the received bytes along with Rx errors.

    :param dev_id:
        Id of the UART port
    :type dev_id: void \*

    :param isrstatus:
        The interrupt status register value as read
    :type isrstatus: unsigned int

.. _`cdns_uart_handle_rx.return`:

Return
------

None

.. _`cdns_uart_handle_tx`:

cdns_uart_handle_tx
===================

.. c:function:: void cdns_uart_handle_tx(void *dev_id)

    Handle the bytes to be Txed.

    :param dev_id:
        Id of the UART port
    :type dev_id: void \*

.. _`cdns_uart_handle_tx.return`:

Return
------

None

.. _`cdns_uart_isr`:

cdns_uart_isr
=============

.. c:function:: irqreturn_t cdns_uart_isr(int irq, void *dev_id)

    Interrupt handler

    :param irq:
        Irq number
    :type irq: int

    :param dev_id:
        Id of the port
    :type dev_id: void \*

.. _`cdns_uart_isr.return`:

Return
------

IRQHANDLED

.. _`cdns_uart_calc_baud_divs`:

cdns_uart_calc_baud_divs
========================

.. c:function:: unsigned int cdns_uart_calc_baud_divs(unsigned int clk, unsigned int baud, u32 *rbdiv, u32 *rcd, int *div8)

    Calculate baud rate divisors

    :param clk:
        UART module input clock
    :type clk: unsigned int

    :param baud:
        Desired baud rate
    :type baud: unsigned int

    :param rbdiv:
        BDIV value (return value)
    :type rbdiv: u32 \*

    :param rcd:
        CD value (return value)
    :type rcd: u32 \*

    :param div8:
        Value for clk_sel bit in mod (return value)
    :type div8: int \*

.. _`cdns_uart_calc_baud_divs.return`:

Return
------

baud rate, requested baud when possible, or actual baud when there
was too much error, zero if no valid divisors are found.

Formula to obtain baud rate is
baud_tx/rx rate = clk/CD \* (BDIV + 1)
input_clk = (Uart User Defined Clock or Apb Clock)
depends on UCLKEN in MR Reg
clk = input_clk or input_clk/8;
depends on CLKS in MR reg
CD and BDIV depends on values in
baud rate generate register
baud rate clock divisor register

.. _`cdns_uart_set_baud_rate`:

cdns_uart_set_baud_rate
=======================

.. c:function:: unsigned int cdns_uart_set_baud_rate(struct uart_port *port, unsigned int baud)

    Calculate and set the baud rate

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

    :param baud:
        Baud rate to set
    :type baud: unsigned int

.. _`cdns_uart_set_baud_rate.return`:

Return
------

baud rate, requested baud when possible, or actual baud when there
was too much error, zero if no valid divisors are found.

.. _`cdns_uart_clk_notifier_cb`:

cdns_uart_clk_notifier_cb
=========================

.. c:function:: int cdns_uart_clk_notifier_cb(struct notifier_block *nb, unsigned long event, void *data)

    Clock notifier callback

    :param nb:
        Notifier block
    :type nb: struct notifier_block \*

    :param event:
        Notify event
    :type event: unsigned long

    :param data:
        Notifier data
    :type data: void \*

.. _`cdns_uart_clk_notifier_cb.return`:

Return
------

NOTIFY_OK or NOTIFY_DONE on success, NOTIFY_BAD on error.

.. _`cdns_uart_start_tx`:

cdns_uart_start_tx
==================

.. c:function:: void cdns_uart_start_tx(struct uart_port *port)

    Start transmitting bytes

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_stop_tx`:

cdns_uart_stop_tx
=================

.. c:function:: void cdns_uart_stop_tx(struct uart_port *port)

    Stop TX

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_stop_rx`:

cdns_uart_stop_rx
=================

.. c:function:: void cdns_uart_stop_rx(struct uart_port *port)

    Stop RX

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_tx_empty`:

cdns_uart_tx_empty
==================

.. c:function:: unsigned int cdns_uart_tx_empty(struct uart_port *port)

    Check whether TX is empty

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_tx_empty.return`:

Return
------

TIOCSER_TEMT on success, 0 otherwise

.. _`cdns_uart_break_ctl`:

cdns_uart_break_ctl
===================

.. c:function:: void cdns_uart_break_ctl(struct uart_port *port, int ctl)

    Based on the input ctl we have to start or stop transmitting char breaks

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

    :param ctl:
        Value based on which start or stop decision is taken
    :type ctl: int

.. _`cdns_uart_set_termios`:

cdns_uart_set_termios
=====================

.. c:function:: void cdns_uart_set_termios(struct uart_port *port, struct ktermios *termios, struct ktermios *old)

    termios operations, handling data length, parity, stop bits, flow control, baud rate

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

    :param termios:
        Handle to the input termios structure
    :type termios: struct ktermios \*

    :param old:
        Values of the previously saved termios structure
    :type old: struct ktermios \*

.. _`cdns_uart_startup`:

cdns_uart_startup
=================

.. c:function:: int cdns_uart_startup(struct uart_port *port)

    Called when an application opens a cdns_uart port

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_startup.return`:

Return
------

0 on success, negative errno otherwise

.. _`cdns_uart_shutdown`:

cdns_uart_shutdown
==================

.. c:function:: void cdns_uart_shutdown(struct uart_port *port)

    Called when an application closes a cdns_uart port

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_type`:

cdns_uart_type
==============

.. c:function:: const char *cdns_uart_type(struct uart_port *port)

    Set UART type to cdns_uart port

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_type.return`:

Return
------

string on success, NULL otherwise

.. _`cdns_uart_verify_port`:

cdns_uart_verify_port
=====================

.. c:function:: int cdns_uart_verify_port(struct uart_port *port, struct serial_struct *ser)

    Verify the port params

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

    :param ser:
        Handle to the structure whose members are compared
    :type ser: struct serial_struct \*

.. _`cdns_uart_verify_port.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_uart_request_port`:

cdns_uart_request_port
======================

.. c:function:: int cdns_uart_request_port(struct uart_port *port)

    Claim the memory region attached to cdns_uart port, called when the driver adds a cdns_uart port via \ :c:func:`uart_add_one_port`\ 

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_request_port.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_uart_release_port`:

cdns_uart_release_port
======================

.. c:function:: void cdns_uart_release_port(struct uart_port *port)

    Release UART port

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_release_port.description`:

Description
-----------

Release the memory region attached to a cdns_uart port. Called when the
driver removes a cdns_uart port via \ :c:func:`uart_remove_one_port`\ .

.. _`cdns_uart_config_port`:

cdns_uart_config_port
=====================

.. c:function:: void cdns_uart_config_port(struct uart_port *port, int flags)

    Configure UART port

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

    :param flags:
        If any
    :type flags: int

.. _`cdns_uart_get_mctrl`:

cdns_uart_get_mctrl
===================

.. c:function:: unsigned int cdns_uart_get_mctrl(struct uart_port *port)

    Get the modem control state

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

.. _`cdns_uart_get_mctrl.return`:

Return
------

the modem control state

.. _`cdns_uart_console_putchar`:

cdns_uart_console_putchar
=========================

.. c:function:: void cdns_uart_console_putchar(struct uart_port *port, int ch)

    write the character to the FIFO buffer

    :param port:
        Handle to the uart port structure
    :type port: struct uart_port \*

    :param ch:
        Character to be written
    :type ch: int

.. _`cdns_uart_console_write`:

cdns_uart_console_write
=======================

.. c:function:: void cdns_uart_console_write(struct console *co, const char *s, unsigned int count)

    perform write operation

    :param co:
        Console handle
    :type co: struct console \*

    :param s:
        Pointer to character array
    :type s: const char \*

    :param count:
        No of characters
    :type count: unsigned int

.. _`cdns_uart_console_setup`:

cdns_uart_console_setup
=======================

.. c:function:: int cdns_uart_console_setup(struct console *co, char *options)

    Initialize the uart to default config

    :param co:
        Console handle
    :type co: struct console \*

    :param options:
        Initial settings of uart
    :type options: char \*

.. _`cdns_uart_console_setup.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_uart_suspend`:

cdns_uart_suspend
=================

.. c:function:: int cdns_uart_suspend(struct device *device)

    suspend event

    :param device:
        Pointer to the device structure
    :type device: struct device \*

.. _`cdns_uart_suspend.return`:

Return
------

0

.. _`cdns_uart_resume`:

cdns_uart_resume
================

.. c:function:: int cdns_uart_resume(struct device *device)

    Resume after a previous suspend

    :param device:
        Pointer to the device structure
    :type device: struct device \*

.. _`cdns_uart_resume.return`:

Return
------

0

.. _`cdns_uart_probe`:

cdns_uart_probe
===============

.. c:function:: int cdns_uart_probe(struct platform_device *pdev)

    Platform driver probe

    :param pdev:
        Pointer to the platform device structure
    :type pdev: struct platform_device \*

.. _`cdns_uart_probe.return`:

Return
------

0 on success, negative errno otherwise

.. _`cdns_uart_remove`:

cdns_uart_remove
================

.. c:function:: int cdns_uart_remove(struct platform_device *pdev)

    called when the platform driver is unregistered

    :param pdev:
        Pointer to the platform device structure
    :type pdev: struct platform_device \*

.. _`cdns_uart_remove.return`:

Return
------

0 on success, negative errno otherwise

.. This file was automatic generated / don't edit.


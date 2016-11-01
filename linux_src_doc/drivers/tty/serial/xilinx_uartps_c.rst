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
        unsigned int baud;
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

baud
    Current baud rate

clk_rate_change_nb
    Notifier block for clock changes

quirks
    *undescribed*

.. _`cdns_uart_handle_rx`:

cdns_uart_handle_rx
===================

.. c:function:: void cdns_uart_handle_rx(void *dev_id, unsigned int isrstatus)

    Handle the received bytes along with Rx errors.

    :param void \*dev_id:
        Id of the UART port

    :param unsigned int isrstatus:
        The interrupt status register value as read

.. _`cdns_uart_handle_rx.return`:

Return
------

None

.. _`cdns_uart_handle_tx`:

cdns_uart_handle_tx
===================

.. c:function:: void cdns_uart_handle_tx(void *dev_id)

    Handle the bytes to be Txed.

    :param void \*dev_id:
        Id of the UART port

.. _`cdns_uart_handle_tx.return`:

Return
------

None

.. _`cdns_uart_isr`:

cdns_uart_isr
=============

.. c:function:: irqreturn_t cdns_uart_isr(int irq, void *dev_id)

    Interrupt handler

    :param int irq:
        Irq number

    :param void \*dev_id:
        Id of the port

.. _`cdns_uart_isr.return`:

Return
------

IRQHANDLED

.. _`cdns_uart_calc_baud_divs`:

cdns_uart_calc_baud_divs
========================

.. c:function:: unsigned int cdns_uart_calc_baud_divs(unsigned int clk, unsigned int baud, u32 *rbdiv, u32 *rcd, int *div8)

    Calculate baud rate divisors

    :param unsigned int clk:
        UART module input clock

    :param unsigned int baud:
        Desired baud rate

    :param u32 \*rbdiv:
        BDIV value (return value)

    :param u32 \*rcd:
        CD value (return value)

    :param int \*div8:
        Value for clk_sel bit in mod (return value)

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

    :param struct uart_port \*port:
        Handle to the uart port structure

    :param unsigned int baud:
        Baud rate to set

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

    :param struct notifier_block \*nb:
        Notifier block

    :param unsigned long event:
        Notify event

    :param void \*data:
        Notifier data

.. _`cdns_uart_clk_notifier_cb.return`:

Return
------

NOTIFY_OK or NOTIFY_DONE on success, NOTIFY_BAD on error.

.. _`cdns_uart_start_tx`:

cdns_uart_start_tx
==================

.. c:function:: void cdns_uart_start_tx(struct uart_port *port)

    Start transmitting bytes

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_stop_tx`:

cdns_uart_stop_tx
=================

.. c:function:: void cdns_uart_stop_tx(struct uart_port *port)

    Stop TX

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_stop_rx`:

cdns_uart_stop_rx
=================

.. c:function:: void cdns_uart_stop_rx(struct uart_port *port)

    Stop RX

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_tx_empty`:

cdns_uart_tx_empty
==================

.. c:function:: unsigned int cdns_uart_tx_empty(struct uart_port *port)

    Check whether TX is empty

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_tx_empty.return`:

Return
------

TIOCSER_TEMT on success, 0 otherwise

.. _`cdns_uart_break_ctl`:

cdns_uart_break_ctl
===================

.. c:function:: void cdns_uart_break_ctl(struct uart_port *port, int ctl)

    Based on the input ctl we have to start or stop transmitting char breaks

    :param struct uart_port \*port:
        Handle to the uart port structure

    :param int ctl:
        Value based on which start or stop decision is taken

.. _`cdns_uart_set_termios`:

cdns_uart_set_termios
=====================

.. c:function:: void cdns_uart_set_termios(struct uart_port *port, struct ktermios *termios, struct ktermios *old)

    termios operations, handling data length, parity, stop bits, flow control, baud rate

    :param struct uart_port \*port:
        Handle to the uart port structure

    :param struct ktermios \*termios:
        Handle to the input termios structure

    :param struct ktermios \*old:
        Values of the previously saved termios structure

.. _`cdns_uart_startup`:

cdns_uart_startup
=================

.. c:function:: int cdns_uart_startup(struct uart_port *port)

    Called when an application opens a cdns_uart port

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_startup.return`:

Return
------

0 on success, negative errno otherwise

.. _`cdns_uart_shutdown`:

cdns_uart_shutdown
==================

.. c:function:: void cdns_uart_shutdown(struct uart_port *port)

    Called when an application closes a cdns_uart port

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_type`:

cdns_uart_type
==============

.. c:function:: const char *cdns_uart_type(struct uart_port *port)

    Set UART type to cdns_uart port

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_type.return`:

Return
------

string on success, NULL otherwise

.. _`cdns_uart_verify_port`:

cdns_uart_verify_port
=====================

.. c:function:: int cdns_uart_verify_port(struct uart_port *port, struct serial_struct *ser)

    Verify the port params

    :param struct uart_port \*port:
        Handle to the uart port structure

    :param struct serial_struct \*ser:
        Handle to the structure whose members are compared

.. _`cdns_uart_verify_port.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_uart_request_port`:

cdns_uart_request_port
======================

.. c:function:: int cdns_uart_request_port(struct uart_port *port)

    Claim the memory region attached to cdns_uart port, called when the driver adds a cdns_uart port via \ :c:func:`uart_add_one_port`\ 

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_request_port.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_uart_release_port`:

cdns_uart_release_port
======================

.. c:function:: void cdns_uart_release_port(struct uart_port *port)

    Release UART port

    :param struct uart_port \*port:
        Handle to the uart port structure

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

    :param struct uart_port \*port:
        Handle to the uart port structure

    :param int flags:
        If any

.. _`cdns_uart_get_mctrl`:

cdns_uart_get_mctrl
===================

.. c:function:: unsigned int cdns_uart_get_mctrl(struct uart_port *port)

    Get the modem control state

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_get_mctrl.return`:

Return
------

the modem control state

.. _`cdns_uart_get_port`:

cdns_uart_get_port
==================

.. c:function:: struct uart_port *cdns_uart_get_port(int id)

    Configure the port from platform device resource info

    :param int id:
        Port id

.. _`cdns_uart_get_port.return`:

Return
------

a pointer to a uart_port or NULL for failure

.. _`cdns_uart_console_wait_tx`:

cdns_uart_console_wait_tx
=========================

.. c:function:: void cdns_uart_console_wait_tx(struct uart_port *port)

    Wait for the TX to be full

    :param struct uart_port \*port:
        Handle to the uart port structure

.. _`cdns_uart_console_putchar`:

cdns_uart_console_putchar
=========================

.. c:function:: void cdns_uart_console_putchar(struct uart_port *port, int ch)

    write the character to the FIFO buffer

    :param struct uart_port \*port:
        Handle to the uart port structure

    :param int ch:
        Character to be written

.. _`cdns_uart_console_write`:

cdns_uart_console_write
=======================

.. c:function:: void cdns_uart_console_write(struct console *co, const char *s, unsigned int count)

    perform write operation

    :param struct console \*co:
        Console handle

    :param const char \*s:
        Pointer to character array

    :param unsigned int count:
        No of characters

.. _`cdns_uart_console_setup`:

cdns_uart_console_setup
=======================

.. c:function:: int cdns_uart_console_setup(struct console *co, char *options)

    Initialize the uart to default config

    :param struct console \*co:
        Console handle

    :param char \*options:
        Initial settings of uart

.. _`cdns_uart_console_setup.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_uart_console_init`:

cdns_uart_console_init
======================

.. c:function:: int cdns_uart_console_init( void)

    Initialization call

    :param  void:
        no arguments

.. _`cdns_uart_console_init.return`:

Return
------

0 on success, negative errno otherwise

.. _`cdns_uart_suspend`:

cdns_uart_suspend
=================

.. c:function:: int cdns_uart_suspend(struct device *device)

    suspend event

    :param struct device \*device:
        Pointer to the device structure

.. _`cdns_uart_suspend.return`:

Return
------

0

.. _`cdns_uart_resume`:

cdns_uart_resume
================

.. c:function:: int cdns_uart_resume(struct device *device)

    Resume after a previous suspend

    :param struct device \*device:
        Pointer to the device structure

.. _`cdns_uart_resume.return`:

Return
------

0

.. _`cdns_uart_probe`:

cdns_uart_probe
===============

.. c:function:: int cdns_uart_probe(struct platform_device *pdev)

    Platform driver probe

    :param struct platform_device \*pdev:
        Pointer to the platform device structure

.. _`cdns_uart_probe.return`:

Return
------

0 on success, negative errno otherwise

.. _`cdns_uart_remove`:

cdns_uart_remove
================

.. c:function:: int cdns_uart_remove(struct platform_device *pdev)

    called when the platform driver is unregistered

    :param struct platform_device \*pdev:
        Pointer to the platform device structure

.. _`cdns_uart_remove.return`:

Return
------

0 on success, negative errno otherwise

.. This file was automatic generated / don't edit.


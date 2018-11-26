.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/serial_core.c

.. _`uart_update_timeout`:

uart_update_timeout
===================

.. c:function:: void uart_update_timeout(struct uart_port *port, unsigned int cflag, unsigned int baud)

    update per-port FIFO timeout.

    :param port:
        uart_port structure describing the port
    :type port: struct uart_port \*

    :param cflag:
        termios cflag value
    :type cflag: unsigned int

    :param baud:
        speed of the port
    :type baud: unsigned int

.. _`uart_update_timeout.description`:

Description
-----------

     Set the port FIFO timeout value.  The \ ``cflag``\  value should
     reflect the actual hardware settings.

.. _`uart_get_baud_rate`:

uart_get_baud_rate
==================

.. c:function:: unsigned int uart_get_baud_rate(struct uart_port *port, struct ktermios *termios, struct ktermios *old, unsigned int min, unsigned int max)

    return baud rate for a particular port

    :param port:
        uart_port structure describing the port in question.
    :type port: struct uart_port \*

    :param termios:
        desired termios settings.
    :type termios: struct ktermios \*

    :param old:
        old termios (or NULL)
    :type old: struct ktermios \*

    :param min:
        minimum acceptable baud rate
    :type min: unsigned int

    :param max:
        maximum acceptable baud rate
    :type max: unsigned int

.. _`uart_get_baud_rate.description`:

Description
-----------

     Decode the termios structure into a numeric baud rate,
     taking account of the magic 38400 baud rate (with spd_*
     flags), and mapping the \ ``B0``\  rate to 9600 baud.

     If the new baud rate is invalid, try the old termios setting.
     If it's still invalid, we try 9600 baud.

     Update the \ ``termios``\  structure to reflect the baud rate
     we're actually going to be using. Don't do this for the case
     where B0 is requested ("hang up").

.. _`uart_get_divisor`:

uart_get_divisor
================

.. c:function:: unsigned int uart_get_divisor(struct uart_port *port, unsigned int baud)

    return uart clock divisor

    :param port:
        uart_port structure describing the port.
    :type port: struct uart_port \*

    :param baud:
        desired baud rate
    :type baud: unsigned int

.. _`uart_get_divisor.description`:

Description
-----------

     Calculate the uart clock divisor for the port.

.. _`uart_get_lsr_info`:

uart_get_lsr_info
=================

.. c:function:: int uart_get_lsr_info(struct tty_struct *tty, struct uart_state *state, unsigned int __user *value)

    get line status register info

    :param tty:
        tty associated with the UART
    :type tty: struct tty_struct \*

    :param state:
        UART being queried
    :type state: struct uart_state \*

    :param value:
        returned modem value
    :type value: unsigned int __user \*

.. _`uart_console_write`:

uart_console_write
==================

.. c:function:: void uart_console_write(struct uart_port *port, const char *s, unsigned int count, void (*putchar)(struct uart_port *, int))

    write a console message to a serial port

    :param port:
        the port to write the message
    :type port: struct uart_port \*

    :param s:
        array of characters
    :type s: const char \*

    :param count:
        number of characters in string to write
    :type count: unsigned int

    :param void (\*putchar)(struct uart_port \*, int):
        function to write character to port

.. _`uart_parse_earlycon`:

uart_parse_earlycon
===================

.. c:function:: int uart_parse_earlycon(char *p, unsigned char *iotype, resource_size_t *addr, char **options)

    Parse earlycon options

    :param p:
        ptr to 2nd field (ie., just beyond '<name>,')
    :type p: char \*

    :param iotype:
        ptr for decoded iotype (out)
    :type iotype: unsigned char \*

    :param addr:
        ptr for decoded mapbase/iobase (out)
    :type addr: resource_size_t \*

    :param options:
        ptr for <options> field; NULL if not present (out)
    :type options: char \*\*

.. _`uart_parse_earlycon.description`:

Description
-----------

     Decodes earlycon kernel command line parameters of the form
        earlycon=<name>,io|mmio|mmio16|mmio32|mmio32be|mmio32native,<addr>,<options>
        console=<name>,io|mmio|mmio16|mmio32|mmio32be|mmio32native,<addr>,<options>

     The optional form
        earlycon=<name>,0x<addr>,<options>
        console=<name>,0x<addr>,<options>
     is also accepted; the returned \ ``iotype``\  will be UPIO_MEM.

     Returns 0 on success or -EINVAL on failure

.. _`uart_parse_options`:

uart_parse_options
==================

.. c:function:: void uart_parse_options(const char *options, int *baud, int *parity, int *bits, int *flow)

    Parse serial port baud/parity/bits/flow control.

    :param options:
        pointer to option string
    :type options: const char \*

    :param baud:
        pointer to an 'int' variable for the baud rate.
    :type baud: int \*

    :param parity:
        pointer to an 'int' variable for the parity.
    :type parity: int \*

    :param bits:
        pointer to an 'int' variable for the number of data bits.
    :type bits: int \*

    :param flow:
        pointer to an 'int' variable for the flow control character.
    :type flow: int \*

.. _`uart_parse_options.description`:

Description
-----------

     uart_parse_options decodes a string containing the serial console
     options.  The format of the string is <baud><parity><bits><flow>,
     eg: 115200n8r

.. _`uart_set_options`:

uart_set_options
================

.. c:function:: int uart_set_options(struct uart_port *port, struct console *co, int baud, int parity, int bits, int flow)

    setup the serial console parameters

    :param port:
        pointer to the serial ports uart_port structure
    :type port: struct uart_port \*

    :param co:
        console pointer
    :type co: struct console \*

    :param baud:
        baud rate
    :type baud: int

    :param parity:
        parity character - 'n' (none), 'o' (odd), 'e' (even)
    :type parity: int

    :param bits:
        number of data bits
    :type bits: int

    :param flow:
        flow control character - 'r' (rts)
    :type flow: int

.. _`uart_change_pm`:

uart_change_pm
==============

.. c:function:: void uart_change_pm(struct uart_state *state, enum uart_pm_state pm_state)

    set power state of the port

    :param state:
        port descriptor
    :type state: struct uart_state \*

    :param pm_state:
        new state
    :type pm_state: enum uart_pm_state

.. _`uart_change_pm.description`:

Description
-----------

Locking: port->mutex has to be held

.. _`uart_register_driver`:

uart_register_driver
====================

.. c:function:: int uart_register_driver(struct uart_driver *drv)

    register a driver with the uart core layer

    :param drv:
        low level driver structure
    :type drv: struct uart_driver \*

.. _`uart_register_driver.description`:

Description
-----------

     Register a uart driver with the core driver.  We in turn register
     with the tty layer, and initialise the core driver per-port state.

     We have a proc file in /proc/tty/driver which is named after the
     normal driver.

     drv->port should be NULL, and the per-port structures should be
     registered using uart_add_one_port after this call has succeeded.

.. _`uart_unregister_driver`:

uart_unregister_driver
======================

.. c:function:: void uart_unregister_driver(struct uart_driver *drv)

    remove a driver from the uart core layer

    :param drv:
        low level driver structure
    :type drv: struct uart_driver \*

.. _`uart_unregister_driver.description`:

Description
-----------

     Remove all references to a driver from the core driver.  The low
     level driver must have removed all its ports via the
     \ :c:func:`uart_remove_one_port`\  if it registered them with \ :c:func:`uart_add_one_port`\ .
     (ie, drv->port == NULL)

.. _`uart_add_one_port`:

uart_add_one_port
=================

.. c:function:: int uart_add_one_port(struct uart_driver *drv, struct uart_port *uport)

    attach a driver-defined port structure

    :param drv:
        pointer to the uart low level driver structure for this port
    :type drv: struct uart_driver \*

    :param uport:
        uart port structure to use for this port.
    :type uport: struct uart_port \*

.. _`uart_add_one_port.description`:

Description
-----------

     This allows the driver to register its own uart_port structure
     with the core driver.  The main purpose is to allow the low
     level uart drivers to expand uart_port, rather than having yet
     more levels of structures.

.. _`uart_remove_one_port`:

uart_remove_one_port
====================

.. c:function:: int uart_remove_one_port(struct uart_driver *drv, struct uart_port *uport)

    detach a driver defined port structure

    :param drv:
        pointer to the uart low level driver structure for this port
    :type drv: struct uart_driver \*

    :param uport:
        uart port structure for this port
    :type uport: struct uart_port \*

.. _`uart_remove_one_port.description`:

Description
-----------

     This unhooks (and hangs up) the specified port structure from the
     core driver.  No further calls will be made to the low-level code
     for this port.

.. _`uart_handle_dcd_change`:

uart_handle_dcd_change
======================

.. c:function:: void uart_handle_dcd_change(struct uart_port *uport, unsigned int status)

    handle a change of carrier detect state

    :param uport:
        uart_port structure for the open port
    :type uport: struct uart_port \*

    :param status:
        new carrier detect status, nonzero if active
    :type status: unsigned int

.. _`uart_handle_dcd_change.description`:

Description
-----------

     Caller must hold uport->lock

.. _`uart_handle_cts_change`:

uart_handle_cts_change
======================

.. c:function:: void uart_handle_cts_change(struct uart_port *uport, unsigned int status)

    handle a change of clear-to-send state

    :param uport:
        uart_port structure for the open port
    :type uport: struct uart_port \*

    :param status:
        new clear to send status, nonzero if active
    :type status: unsigned int

.. _`uart_handle_cts_change.description`:

Description
-----------

     Caller must hold uport->lock

.. _`uart_insert_char`:

uart_insert_char
================

.. c:function:: void uart_insert_char(struct uart_port *port, unsigned int status, unsigned int overrun, unsigned int ch, unsigned int flag)

    push a char to the uart layer

    :param port:
        corresponding port
    :type port: struct uart_port \*

    :param status:
        state of the serial port RX buffer (LSR for 8250)
    :type status: unsigned int

    :param overrun:
        mask of overrun bits in \ ``status``\ 
    :type overrun: unsigned int

    :param ch:
        character to push
    :type ch: unsigned int

    :param flag:
        flag for the character (see TTY_NORMAL and friends)
    :type flag: unsigned int

.. _`uart_insert_char.description`:

Description
-----------

User is responsible to call tty_flip_buffer_push when they are done with
insertion.

.. _`uart_get_rs485_mode`:

uart_get_rs485_mode
===================

.. c:function:: void uart_get_rs485_mode(struct device *dev, struct serial_rs485 *rs485conf)

    retrieve rs485 properties for given uart

    :param dev:
        uart device
    :type dev: struct device \*

    :param rs485conf:
        output parameter
    :type rs485conf: struct serial_rs485 \*

.. _`uart_get_rs485_mode.description`:

Description
-----------

This function implements the device tree binding described in
Documentation/devicetree/bindings/serial/rs485.txt.

.. This file was automatic generated / don't edit.


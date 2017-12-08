.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/mux.c

.. _`get_mux_port_count`:

get_mux_port_count
==================

.. c:function:: int get_mux_port_count(struct parisc_device *dev)

    Get the number of available ports on the Mux.

    :param struct parisc_device \*dev:
        The parisc device.

.. _`get_mux_port_count.description`:

Description
-----------

This function is used to determine the number of ports the Mux
supports.  The IODC data reports the number of ports the Mux
can support, but there are cases where not all the Mux ports
are connected.  This function can override the IODC and
return the true port count.

.. _`mux_tx_empty`:

mux_tx_empty
============

.. c:function:: unsigned int mux_tx_empty(struct uart_port *port)

    Check if the transmitter fifo is empty.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_tx_empty.description`:

Description
-----------

This function test if the transmitter fifo for the port
described by 'port' is empty.  If it is empty, this function
should return TIOCSER_TEMT, otherwise return 0.

.. _`mux_set_mctrl`:

mux_set_mctrl
=============

.. c:function:: void mux_set_mctrl(struct uart_port *port, unsigned int mctrl)

    Set the current state of the modem control inputs.

    :param struct uart_port \*port:
        *undescribed*

    :param unsigned int mctrl:
        Modem control bits.

.. _`mux_set_mctrl.description`:

Description
-----------

The Serial MUX does not support CTS, DCD or DSR so this function
is ignored.

.. _`mux_get_mctrl`:

mux_get_mctrl
=============

.. c:function:: unsigned int mux_get_mctrl(struct uart_port *port)

    Returns the current state of modem control inputs.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_get_mctrl.description`:

Description
-----------

The Serial MUX does not support CTS, DCD or DSR so these lines are
treated as permanently active.

.. _`mux_stop_tx`:

mux_stop_tx
===========

.. c:function:: void mux_stop_tx(struct uart_port *port)

    Stop transmitting characters.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_stop_tx.description`:

Description
-----------

The Serial MUX does not support this function.

.. _`mux_start_tx`:

mux_start_tx
============

.. c:function:: void mux_start_tx(struct uart_port *port)

    Start transmitting characters.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_start_tx.description`:

Description
-----------

The Serial Mux does not support this function.

.. _`mux_stop_rx`:

mux_stop_rx
===========

.. c:function:: void mux_stop_rx(struct uart_port *port)

    Stop receiving characters.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_stop_rx.description`:

Description
-----------

The Serial Mux does not support this function.

.. _`mux_break_ctl`:

mux_break_ctl
=============

.. c:function:: void mux_break_ctl(struct uart_port *port, int break_state)

    Control the transmitssion of a break signal.

    :param struct uart_port \*port:
        Ptr to the uart_port.

    :param int break_state:
        Raise/Lower the break signal.

.. _`mux_break_ctl.description`:

Description
-----------

The Serial Mux does not support this function.

.. _`mux_write`:

mux_write
=========

.. c:function:: void mux_write(struct uart_port *port)

    Write chars to the mux fifo.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_write.description`:

Description
-----------

This function writes all the data from the uart buffer to
the mux fifo.

.. _`mux_read`:

mux_read
========

.. c:function:: void mux_read(struct uart_port *port)

    Read chars from the mux fifo.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_read.description`:

Description
-----------

This reads all available data from the mux's fifo and pushes
the data to the tty layer.

.. _`mux_startup`:

mux_startup
===========

.. c:function:: int mux_startup(struct uart_port *port)

    Initialize the port.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_startup.description`:

Description
-----------

Grab any resources needed for this port and start the
mux timer.

.. _`mux_shutdown`:

mux_shutdown
============

.. c:function:: void mux_shutdown(struct uart_port *port)

    Disable the port.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_shutdown.description`:

Description
-----------

Release any resources needed for the port.

.. _`mux_set_termios`:

mux_set_termios
===============

.. c:function:: void mux_set_termios(struct uart_port *port, struct ktermios *termios, struct ktermios *old)

    Chane port parameters.

    :param struct uart_port \*port:
        Ptr to the uart_port.

    :param struct ktermios \*termios:
        new termios settings.

    :param struct ktermios \*old:
        old termios settings.

.. _`mux_set_termios.description`:

Description
-----------

The Serial Mux does not support this function.

.. _`mux_type`:

mux_type
========

.. c:function:: const char *mux_type(struct uart_port *port)

    Describe the port.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_type.description`:

Description
-----------

Return a pointer to a string constant describing the
specified port.

.. _`mux_release_port`:

mux_release_port
================

.. c:function:: void mux_release_port(struct uart_port *port)

    Release memory and IO regions.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_release_port.description`:

Description
-----------

Release any memory and IO region resources currently in use by
the port.

.. _`mux_request_port`:

mux_request_port
================

.. c:function:: int mux_request_port(struct uart_port *port)

    Request memory and IO regions.

    :param struct uart_port \*port:
        Ptr to the uart_port.

.. _`mux_request_port.description`:

Description
-----------

Request any memory and IO region resources required by the port.
If any fail, no resources should be registered when this function
returns, and it should return -EBUSY on failure.

.. _`mux_config_port`:

mux_config_port
===============

.. c:function:: void mux_config_port(struct uart_port *port, int type)

    Perform port autoconfiguration.

    :param struct uart_port \*port:
        Ptr to the uart_port.

    :param int type:
        Bitmask of required configurations.

.. _`mux_config_port.description`:

Description
-----------

Perform any autoconfiguration steps for the port.  This function is
called if the UPF_BOOT_AUTOCONF flag is specified for the port.
[Note: This is required for now because of a bug in the Serial core.
rmk has already submitted a patch to linus, should be available for
2.5.47.]

.. _`mux_verify_port`:

mux_verify_port
===============

.. c:function:: int mux_verify_port(struct uart_port *port, struct serial_struct *ser)

    Verify the port information.

    :param struct uart_port \*port:
        Ptr to the uart_port.

    :param struct serial_struct \*ser:
        Ptr to the serial information.

.. _`mux_verify_port.description`:

Description
-----------

Verify the new serial port information contained within serinfo is
suitable for this port type.

.. _`mux_poll`:

mux_poll
========

.. c:function:: void mux_poll(struct timer_list *unused)

    Mux poll function.

    :param struct timer_list \*unused:
        Unused variable

.. _`mux_poll.description`:

Description
-----------

This function periodically polls the Serial MUX to check for new data.

.. _`mux_probe`:

mux_probe
=========

.. c:function:: int mux_probe(struct parisc_device *dev)

    Determine if the Serial Mux should claim this device.

    :param struct parisc_device \*dev:
        The parisc device.

.. _`mux_probe.description`:

Description
-----------

Deterimine if the Serial Mux should claim this chip (return 0)
or not (return 1).

.. _`mux_init`:

mux_init
========

.. c:function:: int mux_init( void)

    Serial MUX initialization procedure.

    :param  void:
        no arguments

.. _`mux_init.description`:

Description
-----------

Register the Serial MUX driver.

.. _`mux_exit`:

mux_exit
========

.. c:function:: void __exit mux_exit( void)

    Serial MUX cleanup procedure.

    :param  void:
        no arguments

.. _`mux_exit.description`:

Description
-----------

Unregister the Serial MUX driver from the tty layer.

.. This file was automatic generated / don't edit.


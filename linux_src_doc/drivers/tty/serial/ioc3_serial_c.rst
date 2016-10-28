.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/ioc3_serial.c

.. _`set_baud`:

set_baud
========

.. c:function:: int set_baud(struct ioc3_port *port, int baud)

    Baud rate setting code

    :param struct ioc3_port \*port:
        port to set

    :param int baud:
        baud rate to use

.. _`get_ioc3_port`:

get_ioc3_port
=============

.. c:function:: struct ioc3_port *get_ioc3_port(struct uart_port *the_port)

    given a uart port, return the control structure

    :param struct uart_port \*the_port:
        uart port to find

.. _`port_init`:

port_init
=========

.. c:function:: int inline port_init(struct ioc3_port *port)

    Initialize the sio and ioc3 hardware for a given port called per port from attach...

    :param struct ioc3_port \*port:
        port to initialize

.. _`enable_intrs`:

enable_intrs
============

.. c:function:: void enable_intrs(struct ioc3_port *port, uint32_t mask)

    enable interrupts

    :param struct ioc3_port \*port:
        port to enable

    :param uint32_t mask:
        mask to use

.. _`local_open`:

local_open
==========

.. c:function:: int local_open(struct ioc3_port *port)

    local open a port

    :param struct ioc3_port \*port:
        port to open

.. _`set_rx_timeout`:

set_rx_timeout
==============

.. c:function:: int set_rx_timeout(struct ioc3_port *port, int timeout)

    Set rx timeout and threshold values.

    :param struct ioc3_port \*port:
        port to use

    :param int timeout:
        timeout value in ticks

.. _`config_port`:

config_port
===========

.. c:function:: int config_port(struct ioc3_port *port, int baud, int byte_size, int stop_bits, int parenb, int parodd)

    config the hardware

    :param struct ioc3_port \*port:
        port to config

    :param int baud:
        baud rate for the port

    :param int byte_size:
        data size

    :param int stop_bits:
        number of stop bits

    :param int parenb:
        parity enable ?

    :param int parodd:
        odd parity ?

.. _`do_write`:

do_write
========

.. c:function:: int do_write(struct ioc3_port *port, char *buf, int len)

    Write bytes to the port.  Returns the number of bytes actually written. Called from transmit_chars

    :param struct ioc3_port \*port:
        port to use

    :param char \*buf:
        the stuff to write

    :param int len:
        how many bytes in 'buf'

.. _`disable_intrs`:

disable_intrs
=============

.. c:function:: void disable_intrs(struct ioc3_port *port, uint32_t mask)

    disable interrupts

    :param struct ioc3_port \*port:
        port to enable

    :param uint32_t mask:
        mask to use

.. _`set_notification`:

set_notification
================

.. c:function:: int set_notification(struct ioc3_port *port, int mask, int set_on)

    Modify event notification

    :param struct ioc3_port \*port:
        port to use

    :param int mask:
        events mask

    :param int set_on:
        set ?

.. _`set_mcr`:

set_mcr
=======

.. c:function:: int set_mcr(struct uart_port *the_port, int mask1, int mask2)

    set the master control reg

    :param struct uart_port \*the_port:
        port to use

    :param int mask1:
        mcr mask

    :param int mask2:
        shadow mask

.. _`ioc3_set_proto`:

ioc3_set_proto
==============

.. c:function:: int ioc3_set_proto(struct ioc3_port *port, int proto)

    set the protocol for the port

    :param struct ioc3_port \*port:
        port to use

    :param int proto:
        protocol to use

.. _`transmit_chars`:

transmit_chars
==============

.. c:function:: void transmit_chars(struct uart_port *the_port)

    upper level write, called with the_port->lock

    :param struct uart_port \*the_port:
        port to write

.. _`ioc3_change_speed`:

ioc3_change_speed
=================

.. c:function:: void ioc3_change_speed(struct uart_port *the_port, struct ktermios *new_termios, struct ktermios *old_termios)

    change the speed of the port

    :param struct uart_port \*the_port:
        port to change

    :param struct ktermios \*new_termios:
        new termios settings

    :param struct ktermios \*old_termios:
        old termios settings

.. _`ic3_startup_local`:

ic3_startup_local
=================

.. c:function:: int ic3_startup_local(struct uart_port *the_port)

    Start up the serial port - returns >= 0 if no errors

    :param struct uart_port \*the_port:
        Port to operate on

.. _`do_read`:

do_read
=======

.. c:function:: int do_read(struct uart_port *the_port, char *buf, int len)

    Read in bytes from the port.  Return the number of bytes actually read.

    :param struct uart_port \*the_port:
        port to use

    :param char \*buf:
        place to put the stuff we read

    :param int len:
        how big 'buf' is

.. _`receive_chars`:

receive_chars
=============

.. c:function:: int receive_chars(struct uart_port *the_port)

    upper level read.

    :param struct uart_port \*the_port:
        port to read from

.. _`ioc3uart_intr_one`:

ioc3uart_intr_one
=================

.. c:function:: int inline ioc3uart_intr_one(struct ioc3_submodule *is, struct ioc3_driver_data *idd, unsigned int pending)

    lowest level (per port) interrupt handler.

    :param struct ioc3_submodule \*is:
        submodule

    :param struct ioc3_driver_data \*idd:
        driver data

    :param unsigned int pending:
        interrupts to handle

.. _`ioc3uart_intr`:

ioc3uart_intr
=============

.. c:function:: int ioc3uart_intr(struct ioc3_submodule *is, struct ioc3_driver_data *idd, unsigned int pending)

    field all serial interrupts

    :param struct ioc3_submodule \*is:
        submodule

    :param struct ioc3_driver_data \*idd:
        driver data

    :param unsigned int pending:
        interrupts to handle

.. _`ic3_type`:

ic3_type
========

.. c:function:: const char *ic3_type(struct uart_port *the_port)

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_tx_empty`:

ic3_tx_empty
============

.. c:function:: unsigned int ic3_tx_empty(struct uart_port *the_port)

    Is the transmitter empty?

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_stop_tx`:

ic3_stop_tx
===========

.. c:function:: void ic3_stop_tx(struct uart_port *the_port)

    stop the transmitter

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_stop_rx`:

ic3_stop_rx
===========

.. c:function:: void ic3_stop_rx(struct uart_port *the_port)

    stop the receiver

    :param struct uart_port \*the_port:
        *undescribed*

.. _`null_void_function`:

null_void_function
==================

.. c:function:: void null_void_function(struct uart_port *the_port)

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_shutdown`:

ic3_shutdown
============

.. c:function:: void ic3_shutdown(struct uart_port *the_port)

    shut down the port - free irq and disable

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_set_mctrl`:

ic3_set_mctrl
=============

.. c:function:: void ic3_set_mctrl(struct uart_port *the_port, unsigned int mctrl)

    set control lines (dtr, rts, etc)

    :param struct uart_port \*the_port:
        *undescribed*

    :param unsigned int mctrl:
        Lines to set/unset

.. _`ic3_get_mctrl`:

ic3_get_mctrl
=============

.. c:function:: unsigned int ic3_get_mctrl(struct uart_port *the_port)

    get control line info

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_start_tx`:

ic3_start_tx
============

.. c:function:: void ic3_start_tx(struct uart_port *the_port)

    Start transmitter. Called with the_port->lock

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_break_ctl`:

ic3_break_ctl
=============

.. c:function:: void ic3_break_ctl(struct uart_port *the_port, int break_state)

    handle breaks

    :param struct uart_port \*the_port:
        *undescribed*

    :param int break_state:
        Break state

.. _`ic3_startup`:

ic3_startup
===========

.. c:function:: int ic3_startup(struct uart_port *the_port)

    Start up the serial port - always return 0 (We're always on)

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic3_set_termios`:

ic3_set_termios
===============

.. c:function:: void ic3_set_termios(struct uart_port *the_port, struct ktermios *termios, struct ktermios *old_termios)

    set termios stuff

    :param struct uart_port \*the_port:
        *undescribed*

    :param struct ktermios \*termios:
        Old

    :param struct ktermios \*old_termios:
        *undescribed*

.. _`ic3_request_port`:

ic3_request_port
================

.. c:function:: int ic3_request_port(struct uart_port *port)

    allocate resources for port - no op....

    :param struct uart_port \*port:
        port to operate on

.. _`ioc3_serial_core_attach`:

ioc3_serial_core_attach
=======================

.. c:function:: int ioc3_serial_core_attach(struct ioc3_submodule *is, struct ioc3_driver_data *idd)

    register with serial core This is done during pci probing

    :param struct ioc3_submodule \*is:
        submodule struct for this

    :param struct ioc3_driver_data \*idd:
        handle for this card

.. _`ioc3uart_remove`:

ioc3uart_remove
===============

.. c:function:: int ioc3uart_remove(struct ioc3_submodule *is, struct ioc3_driver_data *idd)

    register detach function

    :param struct ioc3_submodule \*is:
        submodule struct for this submodule

    :param struct ioc3_driver_data \*idd:
        ioc3 driver data for this submodule

.. _`ioc3uart_probe`:

ioc3uart_probe
==============

.. c:function:: int ioc3uart_probe(struct ioc3_submodule *is, struct ioc3_driver_data *idd)

    card probe function called from shim driver

    :param struct ioc3_submodule \*is:
        submodule struct for this submodule

    :param struct ioc3_driver_data \*idd:
        ioc3 driver data for this card

.. _`ioc3uart_init`:

ioc3uart_init
=============

.. c:function:: int ioc3uart_init( void)

    module init called,

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


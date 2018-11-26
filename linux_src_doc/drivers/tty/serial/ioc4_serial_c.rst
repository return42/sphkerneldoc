.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/ioc4_serial.c

.. _`write_ireg`:

write_ireg
==========

.. c:function:: void write_ireg(struct ioc4_soft *ioc4_soft, uint32_t val, int which, int type)

    write the interrupt regs

    :param ioc4_soft:
        ptr to soft struct for this port
    :type ioc4_soft: struct ioc4_soft \*

    :param val:
        value to write
    :type val: uint32_t

    :param which:
        which register
    :type which: int

    :param type:
        which ireg set
    :type type: int

.. _`set_baud`:

set_baud
========

.. c:function:: int set_baud(struct ioc4_port *port, int baud)

    Baud rate setting code

    :param port:
        port to set
    :type port: struct ioc4_port \*

    :param baud:
        baud rate to use
    :type baud: int

.. _`get_ioc4_port`:

get_ioc4_port
=============

.. c:function:: struct ioc4_port *get_ioc4_port(struct uart_port *the_port, int set)

    given a uart port, return the control structure

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

    :param set:
        set this port as current
    :type set: int

.. _`port_init`:

port_init
=========

.. c:function:: int port_init(struct ioc4_port *port)

    Initialize the sio and ioc4 hardware for a given port called per port from attach...

    :param port:
        port to initialize
    :type port: struct ioc4_port \*

.. _`handle_dma_error_intr`:

handle_dma_error_intr
=====================

.. c:function:: void handle_dma_error_intr(void *arg, uint32_t other_ir)

    service any pending DMA error interrupts for the given port - 2nd level called via sd_intr

    :param arg:
        handler arg
    :type arg: void \*

    :param other_ir:
        ioc4regs
    :type other_ir: uint32_t

.. _`intr_connect`:

intr_connect
============

.. c:function:: void intr_connect(struct ioc4_soft *soft, int type, uint32_t intrbits, ioc4_intr_func_f *intr, void *info)

    interrupt connect function

    :param soft:
        soft struct for this card
    :type soft: struct ioc4_soft \*

    :param type:
        interrupt type
    :type type: int

    :param intrbits:
        bit pattern to set
    :type intrbits: uint32_t

    :param intr:
        handler function
    :type intr: ioc4_intr_func_f \*

    :param info:
        handler arg
    :type info: void \*

.. _`ioc4_intr`:

ioc4_intr
=========

.. c:function:: irqreturn_t ioc4_intr(int irq, void *arg)

    Top level IOC4 interrupt handler.

    :param irq:
        irq value
    :type irq: int

    :param arg:
        handler arg
    :type arg: void \*

.. _`ioc4_attach_local`:

ioc4_attach_local
=================

.. c:function:: int ioc4_attach_local(struct ioc4_driver_data *idd)

    Device initialization. Called at \*\_attach() time for each IOC4 with serial ports in the system.

    :param idd:
        Master module data for this IOC4
    :type idd: struct ioc4_driver_data \*

.. _`enable_intrs`:

enable_intrs
============

.. c:function:: void enable_intrs(struct ioc4_port *port, uint32_t mask)

    enable interrupts

    :param port:
        port to enable
    :type port: struct ioc4_port \*

    :param mask:
        mask to use
    :type mask: uint32_t

.. _`local_open`:

local_open
==========

.. c:function:: int local_open(struct ioc4_port *port)

    local open a port

    :param port:
        port to open
    :type port: struct ioc4_port \*

.. _`set_rx_timeout`:

set_rx_timeout
==============

.. c:function:: int set_rx_timeout(struct ioc4_port *port, int timeout)

    Set rx timeout and threshold values.

    :param port:
        port to use
    :type port: struct ioc4_port \*

    :param timeout:
        timeout value in ticks
    :type timeout: int

.. _`config_port`:

config_port
===========

.. c:function:: int config_port(struct ioc4_port *port, int baud, int byte_size, int stop_bits, int parenb, int parodd)

    config the hardware

    :param port:
        port to config
    :type port: struct ioc4_port \*

    :param baud:
        baud rate for the port
    :type baud: int

    :param byte_size:
        data size
    :type byte_size: int

    :param stop_bits:
        number of stop bits
    :type stop_bits: int

    :param parenb:
        parity enable ?
    :type parenb: int

    :param parodd:
        odd parity ?
    :type parodd: int

.. _`do_write`:

do_write
========

.. c:function:: int do_write(struct ioc4_port *port, char *buf, int len)

    Write bytes to the port.  Returns the number of bytes actually written. Called from transmit_chars

    :param port:
        port to use
    :type port: struct ioc4_port \*

    :param buf:
        the stuff to write
    :type buf: char \*

    :param len:
        how many bytes in 'buf'
    :type len: int

.. _`disable_intrs`:

disable_intrs
=============

.. c:function:: void disable_intrs(struct ioc4_port *port, uint32_t mask)

    disable interrupts

    :param port:
        port to enable
    :type port: struct ioc4_port \*

    :param mask:
        mask to use
    :type mask: uint32_t

.. _`set_notification`:

set_notification
================

.. c:function:: int set_notification(struct ioc4_port *port, int mask, int set_on)

    Modify event notification

    :param port:
        port to use
    :type port: struct ioc4_port \*

    :param mask:
        events mask
    :type mask: int

    :param set_on:
        set ?
    :type set_on: int

.. _`set_mcr`:

set_mcr
=======

.. c:function:: int set_mcr(struct uart_port *the_port, int mask1, int mask2)

    set the master control reg

    :param the_port:
        port to use
    :type the_port: struct uart_port \*

    :param mask1:
        mcr mask
    :type mask1: int

    :param mask2:
        shadow mask
    :type mask2: int

.. _`ioc4_set_proto`:

ioc4_set_proto
==============

.. c:function:: int ioc4_set_proto(struct ioc4_port *port, int proto)

    set the protocol for the port

    :param port:
        port to use
    :type port: struct ioc4_port \*

    :param proto:
        protocol to use
    :type proto: int

.. _`transmit_chars`:

transmit_chars
==============

.. c:function:: void transmit_chars(struct uart_port *the_port)

    upper level write, called with ip_lock

    :param the_port:
        port to write
    :type the_port: struct uart_port \*

.. _`ioc4_change_speed`:

ioc4_change_speed
=================

.. c:function:: void ioc4_change_speed(struct uart_port *the_port, struct ktermios *new_termios, struct ktermios *old_termios)

    change the speed of the port

    :param the_port:
        port to change
    :type the_port: struct uart_port \*

    :param new_termios:
        new termios settings
    :type new_termios: struct ktermios \*

    :param old_termios:
        old termios settings
    :type old_termios: struct ktermios \*

.. _`ic4_startup_local`:

ic4_startup_local
=================

.. c:function:: int ic4_startup_local(struct uart_port *the_port)

    Start up the serial port - returns >= 0 if no errors

    :param the_port:
        Port to operate on
    :type the_port: struct uart_port \*

.. _`handle_intr`:

handle_intr
===========

.. c:function:: void handle_intr(void *arg, uint32_t sio_ir)

    service any interrupts for the given port - 2nd level called via sd_intr

    :param arg:
        handler arg
    :type arg: void \*

    :param sio_ir:
        ioc4regs
    :type sio_ir: uint32_t

.. _`do_read`:

do_read
=======

.. c:function:: int do_read(struct uart_port *the_port, unsigned char *buf, int len)

    Read in bytes from the port.  Return the number of bytes actually read.

    :param the_port:
        port to use
    :type the_port: struct uart_port \*

    :param buf:
        place to put the stuff we read
    :type buf: unsigned char \*

    :param len:
        how big 'buf' is
    :type len: int

.. _`receive_chars`:

receive_chars
=============

.. c:function:: void receive_chars(struct uart_port *the_port)

    upper level read. Called with ip_lock.

    :param the_port:
        port to read from
    :type the_port: struct uart_port \*

.. _`ic4_type`:

ic4_type
========

.. c:function:: const char *ic4_type(struct uart_port *the_port)

    What type of console are we?

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_tx_empty`:

ic4_tx_empty
============

.. c:function:: unsigned int ic4_tx_empty(struct uart_port *the_port)

    Is the transmitter empty?

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_stop_tx`:

ic4_stop_tx
===========

.. c:function:: void ic4_stop_tx(struct uart_port *the_port)

    stop the transmitter

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`null_void_function`:

null_void_function
==================

.. c:function:: void null_void_function(struct uart_port *the_port)

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_shutdown`:

ic4_shutdown
============

.. c:function:: void ic4_shutdown(struct uart_port *the_port)

    shut down the port - free irq and disable

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_set_mctrl`:

ic4_set_mctrl
=============

.. c:function:: void ic4_set_mctrl(struct uart_port *the_port, unsigned int mctrl)

    set control lines (dtr, rts, etc)

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

    :param mctrl:
        Lines to set/unset
    :type mctrl: unsigned int

.. _`ic4_get_mctrl`:

ic4_get_mctrl
=============

.. c:function:: unsigned int ic4_get_mctrl(struct uart_port *the_port)

    get control line info

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_start_tx`:

ic4_start_tx
============

.. c:function:: void ic4_start_tx(struct uart_port *the_port)

    Start transmitter, flush any output

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_break_ctl`:

ic4_break_ctl
=============

.. c:function:: void ic4_break_ctl(struct uart_port *the_port, int break_state)

    handle breaks

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

    :param break_state:
        Break state
    :type break_state: int

.. _`ic4_startup`:

ic4_startup
===========

.. c:function:: int ic4_startup(struct uart_port *the_port)

    Start up the serial port

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

.. _`ic4_set_termios`:

ic4_set_termios
===============

.. c:function:: void ic4_set_termios(struct uart_port *the_port, struct ktermios *termios, struct ktermios *old_termios)

    set termios stuff

    :param the_port:
        *undescribed*
    :type the_port: struct uart_port \*

    :param termios:
        Old
    :type termios: struct ktermios \*

    :param old_termios:
        *undescribed*
    :type old_termios: struct ktermios \*

.. _`ic4_request_port`:

ic4_request_port
================

.. c:function:: int ic4_request_port(struct uart_port *port)

    allocate resources for port - no op....

    :param port:
        port to operate on
    :type port: struct uart_port \*

.. _`ioc4_serial_remove_one`:

ioc4_serial_remove_one
======================

.. c:function:: int ioc4_serial_remove_one(struct ioc4_driver_data *idd)

    detach function

    :param idd:
        IOC4 master module data for this IOC4
    :type idd: struct ioc4_driver_data \*

.. _`ioc4_serial_core_attach`:

ioc4_serial_core_attach
=======================

.. c:function:: int ioc4_serial_core_attach(struct pci_dev *pdev, int port_type)

    register with serial core This is done during pci probing

    :param pdev:
        handle for this card
    :type pdev: struct pci_dev \*

    :param port_type:
        *undescribed*
    :type port_type: int

.. _`ioc4_serial_attach_one`:

ioc4_serial_attach_one
======================

.. c:function:: int ioc4_serial_attach_one(struct ioc4_driver_data *idd)

    register attach function called per card found from IOC4 master module.

    :param idd:
        Master module data for this IOC4
    :type idd: struct ioc4_driver_data \*

.. _`ioc4_serial_init`:

ioc4_serial_init
================

.. c:function:: int ioc4_serial_init( void)

    module init

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


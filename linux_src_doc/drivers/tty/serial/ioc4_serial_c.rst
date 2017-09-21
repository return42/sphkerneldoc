.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/ioc4_serial.c

.. _`write_ireg`:

write_ireg
==========

.. c:function:: void write_ireg(struct ioc4_soft *ioc4_soft, uint32_t val, int which, int type)

    write the interrupt regs

    :param struct ioc4_soft \*ioc4_soft:
        ptr to soft struct for this port

    :param uint32_t val:
        value to write

    :param int which:
        which register

    :param int type:
        which ireg set

.. _`set_baud`:

set_baud
========

.. c:function:: int set_baud(struct ioc4_port *port, int baud)

    Baud rate setting code

    :param struct ioc4_port \*port:
        port to set

    :param int baud:
        baud rate to use

.. _`get_ioc4_port`:

get_ioc4_port
=============

.. c:function:: struct ioc4_port *get_ioc4_port(struct uart_port *the_port, int set)

    given a uart port, return the control structure

    :param struct uart_port \*the_port:
        *undescribed*

    :param int set:
        set this port as current

.. _`port_init`:

port_init
=========

.. c:function:: int port_init(struct ioc4_port *port)

    Initialize the sio and ioc4 hardware for a given port called per port from attach...

    :param struct ioc4_port \*port:
        port to initialize

.. _`handle_dma_error_intr`:

handle_dma_error_intr
=====================

.. c:function:: void handle_dma_error_intr(void *arg, uint32_t other_ir)

    service any pending DMA error interrupts for the given port - 2nd level called via sd_intr

    :param void \*arg:
        handler arg

    :param uint32_t other_ir:
        ioc4regs

.. _`intr_connect`:

intr_connect
============

.. c:function:: void intr_connect(struct ioc4_soft *soft, int type, uint32_t intrbits, ioc4_intr_func_f *intr, void *info)

    interrupt connect function

    :param struct ioc4_soft \*soft:
        soft struct for this card

    :param int type:
        interrupt type

    :param uint32_t intrbits:
        bit pattern to set

    :param ioc4_intr_func_f \*intr:
        handler function

    :param void \*info:
        handler arg

.. _`ioc4_intr`:

ioc4_intr
=========

.. c:function:: irqreturn_t ioc4_intr(int irq, void *arg)

    Top level IOC4 interrupt handler.

    :param int irq:
        irq value

    :param void \*arg:
        handler arg

.. _`ioc4_attach_local`:

ioc4_attach_local
=================

.. c:function:: int ioc4_attach_local(struct ioc4_driver_data *idd)

    Device initialization. Called at \*\_attach() time for each IOC4 with serial ports in the system.

    :param struct ioc4_driver_data \*idd:
        Master module data for this IOC4

.. _`enable_intrs`:

enable_intrs
============

.. c:function:: void enable_intrs(struct ioc4_port *port, uint32_t mask)

    enable interrupts

    :param struct ioc4_port \*port:
        port to enable

    :param uint32_t mask:
        mask to use

.. _`local_open`:

local_open
==========

.. c:function:: int local_open(struct ioc4_port *port)

    local open a port

    :param struct ioc4_port \*port:
        port to open

.. _`set_rx_timeout`:

set_rx_timeout
==============

.. c:function:: int set_rx_timeout(struct ioc4_port *port, int timeout)

    Set rx timeout and threshold values.

    :param struct ioc4_port \*port:
        port to use

    :param int timeout:
        timeout value in ticks

.. _`config_port`:

config_port
===========

.. c:function:: int config_port(struct ioc4_port *port, int baud, int byte_size, int stop_bits, int parenb, int parodd)

    config the hardware

    :param struct ioc4_port \*port:
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

.. c:function:: int do_write(struct ioc4_port *port, char *buf, int len)

    Write bytes to the port.  Returns the number of bytes actually written. Called from transmit_chars

    :param struct ioc4_port \*port:
        port to use

    :param char \*buf:
        the stuff to write

    :param int len:
        how many bytes in 'buf'

.. _`disable_intrs`:

disable_intrs
=============

.. c:function:: void disable_intrs(struct ioc4_port *port, uint32_t mask)

    disable interrupts

    :param struct ioc4_port \*port:
        port to enable

    :param uint32_t mask:
        mask to use

.. _`set_notification`:

set_notification
================

.. c:function:: int set_notification(struct ioc4_port *port, int mask, int set_on)

    Modify event notification

    :param struct ioc4_port \*port:
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

.. _`ioc4_set_proto`:

ioc4_set_proto
==============

.. c:function:: int ioc4_set_proto(struct ioc4_port *port, int proto)

    set the protocol for the port

    :param struct ioc4_port \*port:
        port to use

    :param int proto:
        protocol to use

.. _`transmit_chars`:

transmit_chars
==============

.. c:function:: void transmit_chars(struct uart_port *the_port)

    upper level write, called with ip_lock

    :param struct uart_port \*the_port:
        port to write

.. _`ioc4_change_speed`:

ioc4_change_speed
=================

.. c:function:: void ioc4_change_speed(struct uart_port *the_port, struct ktermios *new_termios, struct ktermios *old_termios)

    change the speed of the port

    :param struct uart_port \*the_port:
        port to change

    :param struct ktermios \*new_termios:
        new termios settings

    :param struct ktermios \*old_termios:
        old termios settings

.. _`ic4_startup_local`:

ic4_startup_local
=================

.. c:function:: int ic4_startup_local(struct uart_port *the_port)

    Start up the serial port - returns >= 0 if no errors

    :param struct uart_port \*the_port:
        Port to operate on

.. _`handle_intr`:

handle_intr
===========

.. c:function:: void handle_intr(void *arg, uint32_t sio_ir)

    service any interrupts for the given port - 2nd level called via sd_intr

    :param void \*arg:
        handler arg

    :param uint32_t sio_ir:
        ioc4regs

.. _`do_read`:

do_read
=======

.. c:function:: int do_read(struct uart_port *the_port, unsigned char *buf, int len)

    Read in bytes from the port.  Return the number of bytes actually read.

    :param struct uart_port \*the_port:
        port to use

    :param unsigned char \*buf:
        place to put the stuff we read

    :param int len:
        how big 'buf' is

.. _`receive_chars`:

receive_chars
=============

.. c:function:: void receive_chars(struct uart_port *the_port)

    upper level read. Called with ip_lock.

    :param struct uart_port \*the_port:
        port to read from

.. _`ic4_type`:

ic4_type
========

.. c:function:: const char *ic4_type(struct uart_port *the_port)

    What type of console are we?

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_tx_empty`:

ic4_tx_empty
============

.. c:function:: unsigned int ic4_tx_empty(struct uart_port *the_port)

    Is the transmitter empty?

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_stop_tx`:

ic4_stop_tx
===========

.. c:function:: void ic4_stop_tx(struct uart_port *the_port)

    stop the transmitter

    :param struct uart_port \*the_port:
        *undescribed*

.. _`null_void_function`:

null_void_function
==================

.. c:function:: void null_void_function(struct uart_port *the_port)

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_shutdown`:

ic4_shutdown
============

.. c:function:: void ic4_shutdown(struct uart_port *the_port)

    shut down the port - free irq and disable

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_set_mctrl`:

ic4_set_mctrl
=============

.. c:function:: void ic4_set_mctrl(struct uart_port *the_port, unsigned int mctrl)

    set control lines (dtr, rts, etc)

    :param struct uart_port \*the_port:
        *undescribed*

    :param unsigned int mctrl:
        Lines to set/unset

.. _`ic4_get_mctrl`:

ic4_get_mctrl
=============

.. c:function:: unsigned int ic4_get_mctrl(struct uart_port *the_port)

    get control line info

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_start_tx`:

ic4_start_tx
============

.. c:function:: void ic4_start_tx(struct uart_port *the_port)

    Start transmitter, flush any output

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_break_ctl`:

ic4_break_ctl
=============

.. c:function:: void ic4_break_ctl(struct uart_port *the_port, int break_state)

    handle breaks

    :param struct uart_port \*the_port:
        *undescribed*

    :param int break_state:
        Break state

.. _`ic4_startup`:

ic4_startup
===========

.. c:function:: int ic4_startup(struct uart_port *the_port)

    Start up the serial port

    :param struct uart_port \*the_port:
        *undescribed*

.. _`ic4_set_termios`:

ic4_set_termios
===============

.. c:function:: void ic4_set_termios(struct uart_port *the_port, struct ktermios *termios, struct ktermios *old_termios)

    set termios stuff

    :param struct uart_port \*the_port:
        *undescribed*

    :param struct ktermios \*termios:
        Old

    :param struct ktermios \*old_termios:
        *undescribed*

.. _`ic4_request_port`:

ic4_request_port
================

.. c:function:: int ic4_request_port(struct uart_port *port)

    allocate resources for port - no op....

    :param struct uart_port \*port:
        port to operate on

.. _`ioc4_serial_remove_one`:

ioc4_serial_remove_one
======================

.. c:function:: int ioc4_serial_remove_one(struct ioc4_driver_data *idd)

    detach function

    :param struct ioc4_driver_data \*idd:
        IOC4 master module data for this IOC4

.. _`ioc4_serial_core_attach`:

ioc4_serial_core_attach
=======================

.. c:function:: int ioc4_serial_core_attach(struct pci_dev *pdev, int port_type)

    register with serial core This is done during pci probing

    :param struct pci_dev \*pdev:
        handle for this card

    :param int port_type:
        *undescribed*

.. _`ioc4_serial_attach_one`:

ioc4_serial_attach_one
======================

.. c:function:: int ioc4_serial_attach_one(struct ioc4_driver_data *idd)

    register attach function called per card found from IOC4 master module.

    :param struct ioc4_driver_data \*idd:
        Master module data for this IOC4

.. _`ioc4_serial_init`:

ioc4_serial_init
================

.. c:function:: int ioc4_serial_init( void)

    module init

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


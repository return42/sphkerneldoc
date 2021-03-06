.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/ifx6x60.c

.. _`mrdy_set_high`:

mrdy_set_high
=============

.. c:function:: void mrdy_set_high(struct ifx_spi_device *ifx)

    set MRDY GPIO

    :param ifx:
        device we are controlling
    :type ifx: struct ifx_spi_device \*

.. _`mrdy_set_low`:

mrdy_set_low
============

.. c:function:: void mrdy_set_low(struct ifx_spi_device *ifx)

    clear MRDY GPIO

    :param ifx:
        device we are controlling
    :type ifx: struct ifx_spi_device \*

.. _`ifx_spi_power_state_set`:

ifx_spi_power_state_set
=======================

.. c:function:: void ifx_spi_power_state_set(struct ifx_spi_device *ifx_dev, unsigned char val)

    :param ifx_dev:
        our SPI device
    :type ifx_dev: struct ifx_spi_device \*

    :param val:
        bits to set
    :type val: unsigned char

.. _`ifx_spi_power_state_set.description`:

Description
-----------

Set bit in power status and signal power system if status becomes non-0

.. _`ifx_spi_power_state_clear`:

ifx_spi_power_state_clear
=========================

.. c:function:: void ifx_spi_power_state_clear(struct ifx_spi_device *ifx_dev, unsigned char val)

    clear power bit

    :param ifx_dev:
        our SPI device
    :type ifx_dev: struct ifx_spi_device \*

    :param val:
        bits to clear
    :type val: unsigned char

.. _`ifx_spi_power_state_clear.description`:

Description
-----------

clear bit in power status and signal power system if status becomes 0

.. _`swap_buf_8`:

swap_buf_8
==========

.. c:function:: void swap_buf_8(unsigned char *buf, int len, void *end)

    :param buf:
        our buffer
    :type buf: unsigned char \*

    :param len:
        number of bytes (not words) in the buffer
    :type len: int

    :param end:
        end of buffer
    :type end: void \*

.. _`swap_buf_8.description`:

Description
-----------

Swap the contents of a buffer into big endian format

.. _`swap_buf_16`:

swap_buf_16
===========

.. c:function:: void swap_buf_16(unsigned char *buf, int len, void *end)

    :param buf:
        our buffer
    :type buf: unsigned char \*

    :param len:
        number of bytes (not words) in the buffer
    :type len: int

    :param end:
        end of buffer
    :type end: void \*

.. _`swap_buf_16.description`:

Description
-----------

Swap the contents of a buffer into big endian format

.. _`swap_buf_32`:

swap_buf_32
===========

.. c:function:: void swap_buf_32(unsigned char *buf, int len, void *end)

    :param buf:
        our buffer
    :type buf: unsigned char \*

    :param len:
        number of bytes (not words) in the buffer
    :type len: int

    :param end:
        end of buffer
    :type end: void \*

.. _`swap_buf_32.description`:

Description
-----------

Swap the contents of a buffer into big endian format

.. _`mrdy_assert`:

mrdy_assert
===========

.. c:function:: void mrdy_assert(struct ifx_spi_device *ifx_dev)

    assert MRDY line

    :param ifx_dev:
        our SPI device
    :type ifx_dev: struct ifx_spi_device \*

.. _`mrdy_assert.description`:

Description
-----------

Assert mrdy and set timer to wait for SRDY interrupt, if SRDY is low
now.

.. _`mrdy_assert.fixme`:

FIXME
-----

Can SRDY even go high as we are running this code ?

.. _`ifx_spi_timeout`:

ifx_spi_timeout
===============

.. c:function:: void ifx_spi_timeout(struct timer_list *t)

    SPI timeout

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ifx_spi_timeout.the-spi-has-timed-out`:

The SPI has timed out
---------------------

hang up the tty. Users will then see a hangup
and error events.

.. _`ifx_spi_tiocmget`:

ifx_spi_tiocmget
================

.. c:function:: int ifx_spi_tiocmget(struct tty_struct *tty)

    get modem lines

    :param tty:
        our tty device
    :type tty: struct tty_struct \*

.. _`ifx_spi_tiocmget.description`:

Description
-----------

Map the signal state into Linux modem flags and report the value
in Linux terms

.. _`ifx_spi_tiocmset`:

ifx_spi_tiocmset
================

.. c:function:: int ifx_spi_tiocmset(struct tty_struct *tty, unsigned int set, unsigned int clear)

    set modem bits

    :param tty:
        the tty structure
    :type tty: struct tty_struct \*

    :param set:
        bits to set
    :type set: unsigned int

    :param clear:
        bits to clear
    :type clear: unsigned int

.. _`ifx_spi_tiocmset.description`:

Description
-----------

The IFX6x60 only supports DTR and RTS. Set them accordingly
and flag that an update to the modem is needed.

.. _`ifx_spi_tiocmset.fixme`:

FIXME
-----

do we need to kick the tranfers when we do this ?

.. _`ifx_spi_open`:

ifx_spi_open
============

.. c:function:: int ifx_spi_open(struct tty_struct *tty, struct file *filp)

    called on tty open

    :param tty:
        our tty device
    :type tty: struct tty_struct \*

    :param filp:
        file handle being associated with the tty
    :type filp: struct file \*

.. _`ifx_spi_open.description`:

Description
-----------

Open the tty interface. We let the tty_port layer do all the work
for us.

.. _`ifx_spi_open.fixme`:

FIXME
-----

Remove single device assumption and saved_ifx_dev

.. _`ifx_spi_close`:

ifx_spi_close
=============

.. c:function:: void ifx_spi_close(struct tty_struct *tty, struct file *filp)

    called when our tty closes

    :param tty:
        the tty being closed
    :type tty: struct tty_struct \*

    :param filp:
        the file handle being closed
    :type filp: struct file \*

.. _`ifx_spi_close.description`:

Description
-----------

Perform the close of the tty. We use the tty_port layer to do all
our hard work.

.. _`ifx_spi_decode_spi_header`:

ifx_spi_decode_spi_header
=========================

.. c:function:: int ifx_spi_decode_spi_header(unsigned char *buffer, int *length, unsigned char *more, unsigned char *received_cts)

    decode received header

    :param buffer:
        the received data
    :type buffer: unsigned char \*

    :param length:
        decoded length
    :type length: int \*

    :param more:
        decoded more flag
    :type more: unsigned char \*

    :param received_cts:
        status of cts we received
    :type received_cts: unsigned char \*

.. _`ifx_spi_decode_spi_header.description`:

Description
-----------

Note how received_cts is handled -- if header is all F it is left
the same as it was, if header is all 0 it is set to 0 otherwise it is
taken from the incoming header.

.. _`ifx_spi_decode_spi_header.fixme`:

FIXME
-----

endianness

.. _`ifx_spi_setup_spi_header`:

ifx_spi_setup_spi_header
========================

.. c:function:: void ifx_spi_setup_spi_header(unsigned char *txbuffer, int tx_count, unsigned char more)

    set header fields

    :param txbuffer:
        pointer to start of SPI buffer
    :type txbuffer: unsigned char \*

    :param tx_count:
        bytes
    :type tx_count: int

    :param more:
        indicate if more to follow
    :type more: unsigned char

.. _`ifx_spi_setup_spi_header.description`:

Description
-----------

Format up an SPI header for a transfer

.. _`ifx_spi_setup_spi_header.fixme`:

FIXME
-----

endianness?

.. _`ifx_spi_prepare_tx_buffer`:

ifx_spi_prepare_tx_buffer
=========================

.. c:function:: int ifx_spi_prepare_tx_buffer(struct ifx_spi_device *ifx_dev)

    prepare transmit frame

    :param ifx_dev:
        our SPI device
    :type ifx_dev: struct ifx_spi_device \*

.. _`ifx_spi_prepare_tx_buffer.description`:

Description
-----------

The transmit buffr needs a header and various other bits of
information followed by as much data as we can pull from the FIFO
and transfer. This function formats up a suitable buffer in the
ifx_dev->tx_buffer

.. _`ifx_spi_prepare_tx_buffer.fixme`:

FIXME
-----

performance - should we wake the tty when the queue is half
empty ?

.. _`ifx_spi_write`:

ifx_spi_write
=============

.. c:function:: int ifx_spi_write(struct tty_struct *tty, const unsigned char *buf, int count)

    line discipline write

    :param tty:
        our tty device
    :type tty: struct tty_struct \*

    :param buf:
        pointer to buffer to write (kernel space)
    :type buf: const unsigned char \*

    :param count:
        size of buffer
    :type count: int

.. _`ifx_spi_write.description`:

Description
-----------

Write the characters we have been given into the FIFO. If the device
is not active then activate it, when the SRDY line is asserted back
this will commence I/O

.. _`ifx_spi_write_room`:

ifx_spi_write_room
==================

.. c:function:: int ifx_spi_write_room(struct tty_struct *tty)

    line discipline helper

    :param tty:
        our tty device
    :type tty: struct tty_struct \*

.. _`ifx_spi_write_room.description`:

Description
-----------

Report how much data we can accept before we drop bytes. As we use
a simple FIFO this is nice and easy.

.. _`ifx_spi_chars_in_buffer`:

ifx_spi_chars_in_buffer
=======================

.. c:function:: int ifx_spi_chars_in_buffer(struct tty_struct *tty)

    line discipline helper

    :param tty:
        our tty device
    :type tty: struct tty_struct \*

.. _`ifx_spi_chars_in_buffer.description`:

Description
-----------

Report how many characters we have buffered. In our case this is the
number of bytes sitting in our transmit FIFO.

.. _`ifx_spi_hangup`:

ifx_spi_hangup
==============

.. c:function:: void ifx_spi_hangup(struct tty_struct *tty)

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`ifx_spi_hangup.description`:

Description
-----------

tty port hang up. Called when tty_hangup processing is invoked either
by loss of carrier, or by software (eg vhangup). Serialized against
activate/shutdown by the tty layer.

.. _`ifx_port_activate`:

ifx_port_activate
=================

.. c:function:: int ifx_port_activate(struct tty_port *port, struct tty_struct *tty)

    :param port:
        our tty port
    :type port: struct tty_port \*

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`ifx_port_activate.description`:

Description
-----------

tty port activate method - called for first open. Serialized
with hangup and shutdown by the tty layer.

.. _`ifx_port_shutdown`:

ifx_port_shutdown
=================

.. c:function:: void ifx_port_shutdown(struct tty_port *port)

    :param port:
        our tty port
    :type port: struct tty_port \*

.. _`ifx_port_shutdown.description`:

Description
-----------

tty port shutdown method - called for last port close. Serialized
with hangup and activate by the tty layer.

.. _`ifx_spi_insert_flip_string`:

ifx_spi_insert_flip_string
==========================

.. c:function:: void ifx_spi_insert_flip_string(struct ifx_spi_device *ifx_dev, unsigned char *chars, size_t size)

    queue received data

    :param ifx_dev:
        *undescribed*
    :type ifx_dev: struct ifx_spi_device \*

    :param chars:
        buffer we have received
    :type chars: unsigned char \*

    :param size:
        number of chars reeived
    :type size: size_t

.. _`ifx_spi_insert_flip_string.description`:

Description
-----------

Queue bytes to the tty assuming the tty side is currently open. If
not the discard the data.

.. _`ifx_spi_complete`:

ifx_spi_complete
================

.. c:function:: void ifx_spi_complete(void *ctx)

    SPI transfer completed

    :param ctx:
        our SPI device
    :type ctx: void \*

.. _`ifx_spi_complete.description`:

Description
-----------

An SPI transfer has completed. Process any received data and kick off
any further transmits we can commence.

.. _`ifx_spi_io`:

ifx_spi_io
==========

.. c:function:: void ifx_spi_io(unsigned long data)

    I/O tasklet

    :param data:
        our SPI device
    :type data: unsigned long

.. _`ifx_spi_io.description`:

Description
-----------

Queue data for transmission if possible and then kick off the
transfer.

.. _`ifx_spi_free_port`:

ifx_spi_free_port
=================

.. c:function:: void ifx_spi_free_port(struct ifx_spi_device *ifx_dev)

    free up the tty side

    :param ifx_dev:
        IFX device going away
    :type ifx_dev: struct ifx_spi_device \*

.. _`ifx_spi_free_port.description`:

Description
-----------

Unregister and free up a port when the device goes away

.. _`ifx_spi_create_port`:

ifx_spi_create_port
===================

.. c:function:: int ifx_spi_create_port(struct ifx_spi_device *ifx_dev)

    create a new port

    :param ifx_dev:
        our spi device
    :type ifx_dev: struct ifx_spi_device \*

.. _`ifx_spi_create_port.description`:

Description
-----------

Allocate and initialise the tty port that goes with this interface
and add it to the tty layer so that it can be opened.

.. _`ifx_spi_handle_srdy`:

ifx_spi_handle_srdy
===================

.. c:function:: void ifx_spi_handle_srdy(struct ifx_spi_device *ifx_dev)

    handle SRDY

    :param ifx_dev:
        device asserting SRDY
    :type ifx_dev: struct ifx_spi_device \*

.. _`ifx_spi_handle_srdy.description`:

Description
-----------

Check our device state and see what we need to kick off when SRDY
is asserted. This usually means killing the timer and firing off the
I/O processing.

.. _`ifx_spi_srdy_interrupt`:

ifx_spi_srdy_interrupt
======================

.. c:function:: irqreturn_t ifx_spi_srdy_interrupt(int irq, void *dev)

    SRDY asserted

    :param irq:
        our IRQ number
    :type irq: int

    :param dev:
        our ifx device
    :type dev: void \*

.. _`ifx_spi_srdy_interrupt.description`:

Description
-----------

The modem asserted SRDY. Handle the srdy event

.. _`ifx_spi_reset_interrupt`:

ifx_spi_reset_interrupt
=======================

.. c:function:: irqreturn_t ifx_spi_reset_interrupt(int irq, void *dev)

    Modem has changed reset state

    :param irq:
        interrupt number
    :type irq: int

    :param dev:
        our device pointer
    :type dev: void \*

.. _`ifx_spi_reset_interrupt.description`:

Description
-----------

The modem has either entered or left reset state. Check the GPIO
line to see which.

.. _`ifx_spi_reset_interrupt.fixme`:

FIXME
-----

review locking on MR_INPROGRESS versus
parallel unsolicited reset/solicited reset

.. _`ifx_spi_free_device`:

ifx_spi_free_device
===================

.. c:function:: void ifx_spi_free_device(struct ifx_spi_device *ifx_dev)

    free device

    :param ifx_dev:
        device to free
    :type ifx_dev: struct ifx_spi_device \*

.. _`ifx_spi_free_device.description`:

Description
-----------

Free the IFX device

.. _`ifx_spi_reset`:

ifx_spi_reset
=============

.. c:function:: int ifx_spi_reset(struct ifx_spi_device *ifx_dev)

    reset modem

    :param ifx_dev:
        modem to reset
    :type ifx_dev: struct ifx_spi_device \*

.. _`ifx_spi_reset.description`:

Description
-----------

Perform a reset on the modem

.. _`ifx_spi_spi_probe`:

ifx_spi_spi_probe
=================

.. c:function:: int ifx_spi_spi_probe(struct spi_device *spi)

    probe callback

    :param spi:
        our possible matching SPI device
    :type spi: struct spi_device \*

.. _`ifx_spi_spi_probe.description`:

Description
-----------

Probe for a 6x60 modem on SPI bus. Perform any needed device and
GPIO setup.

.. _`ifx_spi_spi_probe.fixme`:

FIXME
-----

-       Support for multiple devices
-       Split out MID specific GPIO handling eventually

.. _`ifx_spi_spi_remove`:

ifx_spi_spi_remove
==================

.. c:function:: int ifx_spi_spi_remove(struct spi_device *spi)

    SPI device was removed

    :param spi:
        SPI device
    :type spi: struct spi_device \*

.. _`ifx_spi_spi_remove.fixme`:

FIXME
-----

We should be shutting the device down here not in
the module unload path.

.. _`ifx_spi_spi_shutdown`:

ifx_spi_spi_shutdown
====================

.. c:function:: void ifx_spi_spi_shutdown(struct spi_device *spi)

    called on SPI shutdown

    :param spi:
        SPI device
    :type spi: struct spi_device \*

.. _`ifx_spi_spi_shutdown.description`:

Description
-----------

No action needs to be taken here

.. _`ifx_spi_pm_suspend`:

ifx_spi_pm_suspend
==================

.. c:function:: int ifx_spi_pm_suspend(struct device *dev)

    suspend modem on system suspend

    :param dev:
        device being suspended
    :type dev: struct device \*

.. _`ifx_spi_pm_suspend.description`:

Description
-----------

Suspend the modem. No action needed on Intel MID platforms, may
need extending for other systems.

.. _`ifx_spi_pm_resume`:

ifx_spi_pm_resume
=================

.. c:function:: int ifx_spi_pm_resume(struct device *dev)

    resume modem on system resume

    :param dev:
        device being suspended
    :type dev: struct device \*

.. _`ifx_spi_pm_resume.description`:

Description
-----------

Allow the modem to resume. No action needed.

.. _`ifx_spi_pm_resume.fixme`:

FIXME
-----

do we need to reset anything here ?

.. _`ifx_spi_pm_runtime_resume`:

ifx_spi_pm_runtime_resume
=========================

.. c:function:: int ifx_spi_pm_runtime_resume(struct device *dev)

    suspend modem

    :param dev:
        device being suspended
    :type dev: struct device \*

.. _`ifx_spi_pm_runtime_resume.description`:

Description
-----------

Allow the modem to resume. No action needed.

.. _`ifx_spi_pm_runtime_suspend`:

ifx_spi_pm_runtime_suspend
==========================

.. c:function:: int ifx_spi_pm_runtime_suspend(struct device *dev)

    suspend modem

    :param dev:
        device being suspended
    :type dev: struct device \*

.. _`ifx_spi_pm_runtime_suspend.description`:

Description
-----------

Allow the modem to suspend and thus suspend to continue up the
device tree.

.. _`ifx_spi_pm_runtime_idle`:

ifx_spi_pm_runtime_idle
=======================

.. c:function:: int ifx_spi_pm_runtime_idle(struct device *dev)

    check if modem idle

    :param dev:
        our device
    :type dev: struct device \*

.. _`ifx_spi_pm_runtime_idle.description`:

Description
-----------

Check conditions and queue runtime suspend if idle.

.. _`ifx_spi_exit`:

ifx_spi_exit
============

.. c:function:: void __exit ifx_spi_exit( void)

    module exit

    :param void:
        no arguments
    :type void: 

.. _`ifx_spi_exit.description`:

Description
-----------

Unload the module.

.. _`ifx_spi_init`:

ifx_spi_init
============

.. c:function:: int ifx_spi_init( void)

    module entry point

    :param void:
        no arguments
    :type void: 

.. _`ifx_spi_init.description`:

Description
-----------

Initialise the SPI and tty interfaces for the IFX SPI driver
We need to initialize upper-edge spi driver after the tty
driver because otherwise the spi probe will race

.. This file was automatic generated / don't edit.


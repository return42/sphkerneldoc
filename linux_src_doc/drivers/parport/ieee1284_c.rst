.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parport/ieee1284.c

.. _`parport_wait_event`:

parport_wait_event
==================

.. c:function:: int parport_wait_event(struct parport *port, signed long timeout)

    wait for an event on a parallel port

    :param port:
        port to wait on
    :type port: struct parport \*

    :param timeout:
        time to wait (in jiffies)
    :type timeout: signed long

.. _`parport_wait_event.description`:

Description
-----------

     This function waits for up to \ ``timeout``\  jiffies for an
     interrupt to occur on a parallel port.  If the port timeout is
     set to zero, it returns immediately.

     If an interrupt occurs before the timeout period elapses, this
     function returns zero immediately.  If it times out, it returns
     one.  An error code less than zero indicates an error (most
     likely a pending signal), and the calling code should finish
     what it's doing as soon as it can.

.. _`parport_poll_peripheral`:

parport_poll_peripheral
=======================

.. c:function:: int parport_poll_peripheral(struct parport *port, unsigned char mask, unsigned char result, int usec)

    poll status lines

    :param port:
        port to watch
    :type port: struct parport \*

    :param mask:
        status lines to watch
    :type mask: unsigned char

    :param result:
        desired values of chosen status lines
    :type result: unsigned char

    :param usec:
        timeout
    :type usec: int

.. _`parport_poll_peripheral.description`:

Description
-----------

     This function busy-waits until the masked status lines have
     the desired values, or until the timeout period elapses.  The
     \ ``mask``\  and \ ``result``\  parameters are bitmasks, with the bits
     defined by the constants in parport.h: \ ``PARPORT_STATUS_BUSY``\ ,
     and so on.

     This function does not call \ :c:func:`schedule`\ ; instead it busy-waits
     using \ :c:func:`udelay`\ .  It currently has a resolution of 5usec.

     If the status lines take on the desired values before the
     timeout period elapses, \ :c:func:`parport_poll_peripheral`\  returns zero
     immediately.  A return value greater than zero indicates
     a timeout.  An error code (less than zero) indicates an error,
     most likely a signal that arrived, and the caller should
     finish what it is doing as soon as possible.

.. _`parport_wait_peripheral`:

parport_wait_peripheral
=======================

.. c:function:: int parport_wait_peripheral(struct parport *port, unsigned char mask, unsigned char result)

    wait for status lines to change in 35ms

    :param port:
        port to watch
    :type port: struct parport \*

    :param mask:
        status lines to watch
    :type mask: unsigned char

    :param result:
        desired values of chosen status lines
    :type result: unsigned char

.. _`parport_wait_peripheral.description`:

Description
-----------

     This function waits until the masked status lines have the
     desired values, or until 35ms have elapsed (see IEEE 1284-1994
     page 24 to 25 for why this value in particular is hardcoded).
     The \ ``mask``\  and \ ``result``\  parameters are bitmasks, with the bits
     defined by the constants in parport.h: \ ``PARPORT_STATUS_BUSY``\ ,
     and so on.

     The port is polled quickly to start off with, in anticipation
     of a fast response from the peripheral.  This fast polling
     time is configurable (using /proc), and defaults to 500usec.
     If the timeout for this port (see \ :c:func:`parport_set_timeout`\ ) is
     zero, the fast polling time is 35ms, and this function does
     not call \ :c:func:`schedule`\ .

     If the timeout for this port is non-zero, after the fast
     polling fails it uses \ :c:func:`parport_wait_event`\  to wait for up to
     10ms, waking up if an interrupt occurs.

.. _`parport_negotiate`:

parport_negotiate
=================

.. c:function:: int parport_negotiate(struct parport *port, int mode)

    negotiate an IEEE 1284 mode

    :param port:
        port to use
    :type port: struct parport \*

    :param mode:
        mode to negotiate to
    :type mode: int

.. _`parport_negotiate.description`:

Description
-----------

     Use this to negotiate to a particular IEEE 1284 transfer mode.
     The \ ``mode``\  parameter should be one of the constants in
     parport.h starting \ ``IEEE1284_MODE_xxx``\ .

     The return value is 0 if the peripheral has accepted the
     negotiation to the mode specified, -1 if the peripheral is not
     IEEE 1284 compliant (or not present), or 1 if the peripheral
     has rejected the negotiation.

.. _`parport_write`:

parport_write
=============

.. c:function:: ssize_t parport_write(struct parport *port, const void *buffer, size_t len)

    write a block of data to a parallel port

    :param port:
        port to write to
    :type port: struct parport \*

    :param buffer:
        data buffer (in kernel space)
    :type buffer: const void \*

    :param len:
        number of bytes of data to transfer
    :type len: size_t

.. _`parport_write.description`:

Description
-----------

     This will write up to \ ``len``\  bytes of \ ``buffer``\  to the port
     specified, using the IEEE 1284 transfer mode most recently
     negotiated to (using \ :c:func:`parport_negotiate`\ ), as long as that
     mode supports forward transfers (host to peripheral).

     It is the caller's responsibility to ensure that the first
     \ ``len``\  bytes of \ ``buffer``\  are valid.

     This function returns the number of bytes transferred (if zero
     or positive), or else an error code.

.. _`parport_read`:

parport_read
============

.. c:function:: ssize_t parport_read(struct parport *port, void *buffer, size_t len)

    read a block of data from a parallel port

    :param port:
        port to read from
    :type port: struct parport \*

    :param buffer:
        data buffer (in kernel space)
    :type buffer: void \*

    :param len:
        number of bytes of data to transfer
    :type len: size_t

.. _`parport_read.description`:

Description
-----------

     This will read up to \ ``len``\  bytes of \ ``buffer``\  to the port
     specified, using the IEEE 1284 transfer mode most recently
     negotiated to (using \ :c:func:`parport_negotiate`\ ), as long as that
     mode supports reverse transfers (peripheral to host).

     It is the caller's responsibility to ensure that the first
     \ ``len``\  bytes of \ ``buffer``\  are available to write to.

     This function returns the number of bytes transferred (if zero
     or positive), or else an error code.

.. _`parport_set_timeout`:

parport_set_timeout
===================

.. c:function:: long parport_set_timeout(struct pardevice *dev, long inactivity)

    set the inactivity timeout for a device

    :param dev:
        device on a port
    :type dev: struct pardevice \*

    :param inactivity:
        inactivity timeout (in jiffies)
    :type inactivity: long

.. _`parport_set_timeout.description`:

Description
-----------

     This sets the inactivity timeout for a particular device on a
     port.  This affects functions like \ :c:func:`parport_wait_peripheral`\ .
     The special value 0 means not to call \ :c:func:`schedule`\  while dealing
     with this device.

     The return value is the previous inactivity timeout.

     Any callers of \ :c:func:`parport_wait_event`\  for this device are woken
     up.

.. This file was automatic generated / don't edit.


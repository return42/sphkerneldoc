.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_api.c

.. _`__scif_flush`:

\__scif_flush
=============

.. c:function:: int __scif_flush(scif_epd_t epd)

    Wakes up any blocking accepts. The endpoint will no longer accept new connections.

    :param epd:
        The end point returned from \ :c:func:`scif_open`\ 
    :type epd: scif_epd_t

.. _`scif_accept`:

scif_accept
===========

.. c:function:: int scif_accept(scif_epd_t epd, struct scif_port_id *peer, scif_epd_t *newepd, int flags)

    Accept a connection request from the remote node

    :param epd:
        *undescribed*
    :type epd: scif_epd_t

    :param peer:
        *undescribed*
    :type peer: struct scif_port_id \*

    :param newepd:
        *undescribed*
    :type newepd: scif_epd_t \*

    :param flags:
        *undescribed*
    :type flags: int

.. _`scif_accept.description`:

Description
-----------

The function accepts a connection request from the remote node.  Successful
complete is indicate by a new end point being created and passed back
to the caller for future reference.

Upon successful complete a zero will be returned and the peer information
will be filled in.

If the end point is not in the listening state -EINVAL will be returned.

If during the connection sequence resource allocation fails the -ENOMEM
will be returned.

If the function is called with the ASYNC flag set and no connection requests
are pending it will return -EAGAIN.

If the remote side is not sending any connection requests the caller may
terminate this function with a signal.  If so a -EINTR will be returned.

.. _`scif_user_send`:

scif_user_send
==============

.. c:function:: int scif_user_send(scif_epd_t epd, void __user *msg, int len, int flags)

    Send data to connection queue

    :param epd:
        The end point returned from \ :c:func:`scif_open`\ 
    :type epd: scif_epd_t

    :param msg:
        Address to place data
    :type msg: void __user \*

    :param len:
        Length to receive
    :type len: int

    :param flags:
        blocking or non blocking
    :type flags: int

.. _`scif_user_send.description`:

Description
-----------

This function is called from the driver IOCTL entry point
only and is a wrapper for \_scif_send().

.. _`scif_user_recv`:

scif_user_recv
==============

.. c:function:: int scif_user_recv(scif_epd_t epd, void __user *msg, int len, int flags)

    Receive data from connection queue

    :param epd:
        The end point returned from \ :c:func:`scif_open`\ 
    :type epd: scif_epd_t

    :param msg:
        Address to place data
    :type msg: void __user \*

    :param len:
        Length to receive
    :type len: int

    :param flags:
        blocking or non blocking
    :type flags: int

.. _`scif_user_recv.description`:

Description
-----------

This function is called from the driver IOCTL entry point
only and is a wrapper for \_scif_recv().

.. _`scif_send`:

scif_send
=========

.. c:function:: int scif_send(scif_epd_t epd, void *msg, int len, int flags)

    Send data to connection queue

    :param epd:
        The end point returned from \ :c:func:`scif_open`\ 
    :type epd: scif_epd_t

    :param msg:
        Address to place data
    :type msg: void \*

    :param len:
        Length to receive
    :type len: int

    :param flags:
        blocking or non blocking
    :type flags: int

.. _`scif_send.description`:

Description
-----------

This function is called from the kernel mode only and is
a wrapper for \_scif_send().

.. _`scif_recv`:

scif_recv
=========

.. c:function:: int scif_recv(scif_epd_t epd, void *msg, int len, int flags)

    Receive data from connection queue

    :param epd:
        The end point returned from \ :c:func:`scif_open`\ 
    :type epd: scif_epd_t

    :param msg:
        Address to place data
    :type msg: void \*

    :param len:
        Length to receive
    :type len: int

    :param flags:
        blocking or non blocking
    :type flags: int

.. _`scif_recv.description`:

Description
-----------

This function is called from the kernel mode only and is
a wrapper for \_scif_recv().

.. _`scif_poll`:

scif_poll
=========

.. c:function:: int scif_poll(struct scif_pollepd *ufds, unsigned int nfds, long timeout_msecs)

    Kernel mode SCIF poll

    :param ufds:
        Array of scif_pollepd structures containing the end points
        and events to poll on
    :type ufds: struct scif_pollepd \*

    :param nfds:
        Size of the ufds array
    :type nfds: unsigned int

    :param timeout_msecs:
        Timeout in msecs, -ve implies infinite timeout
    :type timeout_msecs: long

.. _`scif_poll.description`:

Description
-----------

The code flow in this function is based on do_poll(..) in select.c

Returns the number of endpoints which have pending events or 0 in
the event of a timeout. If a signal is used for wake up, -EINTR is
returned.

.. This file was automatic generated / don't edit.


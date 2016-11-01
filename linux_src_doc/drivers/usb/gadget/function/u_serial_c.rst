.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/function/u_serial.c

.. _`gs_start_io`:

gs_start_io
===========

.. c:function:: int gs_start_io(struct gs_port *port)

    start USB I/O streams

    :param struct gs_port \*port:
        *undescribed*

.. _`gs_start_io.context`:

Context
-------

holding port_lock; port_tty and port_usb are non-null

.. _`gs_start_io.description`:

Description
-----------

We only start I/O when something is connected to both sides of
this port.  If nothing is listening on the host side, we may
be pointlessly filling up our TX buffers and FIFO.

.. _`gserial_connect`:

gserial_connect
===============

.. c:function:: int gserial_connect(struct gserial *gser, u8 port_num)

    notify TTY I/O glue that USB link is active

    :param struct gserial \*gser:
        the function, set up with endpoints and descriptors

    :param u8 port_num:
        which port is active

.. _`gserial_connect.context`:

Context
-------

any (usually from irq)

.. _`gserial_connect.description`:

Description
-----------

This is called activate endpoints and let the TTY layer know that
the connection is active ... not unlike "carrier detect".  It won't
necessarily start I/O queues; unless the TTY is held open by any
task, there would be no point.  However, the endpoints will be
activated so the USB host can perform I/O, subject to basic USB
hardware flow control.

Caller needs to have set up the endpoints and USB function in \ ``dev``\ 
before calling this, as well as the appropriate (speed-specific)
endpoint descriptors, and also have allocate \ ``port_num``\  by calling
\ ``gserial_alloc_line``\ ().

Returns negative errno or zero.
On success, ep->driver_data will be overwritten.

.. _`gserial_disconnect`:

gserial_disconnect
==================

.. c:function:: void gserial_disconnect(struct gserial *gser)

    notify TTY I/O glue that USB link is inactive

    :param struct gserial \*gser:
        the function, on which \ :c:func:`gserial_connect`\  was called

.. _`gserial_disconnect.context`:

Context
-------

any (usually from irq)

.. _`gserial_disconnect.description`:

Description
-----------

This is called to deactivate endpoints and let the TTY layer know
that the connection went inactive ... not unlike "hangup".

On return, the state is as if \ :c:func:`gserial_connect`\  had never been called;
there is no active USB I/O on these endpoints.

.. This file was automatic generated / don't edit.


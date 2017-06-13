.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/xenbus/xenbus_comms.c

.. _`xb_write`:

xb_write
========

.. c:function:: int xb_write(const void *data, unsigned int len)

    low level write

    :param const void \*data:
        buffer to send

    :param unsigned int len:
        length of buffer

.. _`xb_write.description`:

Description
-----------

Returns number of bytes written or -err.

.. _`xb_init_comms`:

xb_init_comms
=============

.. c:function:: int xb_init_comms( void)

    Set up interrupt handler off store event channel.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


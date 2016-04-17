.. -*- coding: utf-8; mode: rst -*-

===========
interface.c
===========


.. _`gigaset_if_receive`:

gigaset_if_receive
==================

.. c:function:: void gigaset_if_receive (struct cardstate *cs, unsigned char *buffer, size_t len)

    pass a received block of data to the tty device

    :param struct cardstate \*cs:
        device descriptor structure.

    :param unsigned char \*buffer:
        received data.

    :param size_t len:
        number of bytes received.



.. _`gigaset_if_receive.description`:

Description
-----------

Called by asyncdata/isocdata if a block of data received from the
device must be sent to userspace through the ttyG\* device.


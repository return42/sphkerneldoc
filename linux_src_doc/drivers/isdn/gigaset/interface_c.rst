.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/gigaset/interface.c

.. _`gigaset_if_receive`:

gigaset_if_receive
==================

.. c:function:: void gigaset_if_receive(struct cardstate *cs, unsigned char *buffer, size_t len)

    pass a received block of data to the tty device

    :param cs:
        device descriptor structure.
    :type cs: struct cardstate \*

    :param buffer:
        received data.
    :type buffer: unsigned char \*

    :param len:
        number of bytes received.
    :type len: size_t

.. _`gigaset_if_receive.description`:

Description
-----------

Called by asyncdata/isocdata if a block of data received from the
device must be sent to userspace through the ttyG\* device.

.. This file was automatic generated / don't edit.


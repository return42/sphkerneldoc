.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/gigaset/asyncdata.c

.. _`gigaset_m10x_input`:

gigaset_m10x_input
==================

.. c:function:: void gigaset_m10x_input(struct inbuf_t *inbuf)

    process a block of data received from the device

    :param struct inbuf_t \*inbuf:
        received data and device descriptor structure.

.. _`gigaset_m10x_input.description`:

Description
-----------

Called by hardware module {ser,usb}_gigaset with a block of received
bytes. Separates the bytes received over the serial data channel into
user data and command replies (locked/unlocked) according to the
current state of the interface.

.. _`gigaset_m10x_send_skb`:

gigaset_m10x_send_skb
=====================

.. c:function:: int gigaset_m10x_send_skb(struct bc_state *bcs, struct sk_buff *skb)

    queue an skb for sending

    :param struct bc_state \*bcs:
        B channel descriptor structure.

    :param struct sk_buff \*skb:
        data to send.

.. _`gigaset_m10x_send_skb.description`:

Description
-----------

Called by LL to encode and queue an skb for sending, and start
transmission if necessary.
Once the payload data has been transmitted completely, \ :c:func:`gigaset_skb_sent`\ 
will be called with the skb's link layer header preserved.

.. _`gigaset_m10x_send_skb.return-value`:

Return value
------------

number of bytes accepted for sending (skb->len) if ok,
error code < 0 (eg. -ENOMEM) on error

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/gigaset/isocdata.c

.. _`gigaset_isoc_send_skb`:

gigaset_isoc_send_skb
=====================

.. c:function:: int gigaset_isoc_send_skb(struct bc_state *bcs, struct sk_buff *skb)

    queue an skb for sending

    :param bcs:
        B channel descriptor structure.
    :type bcs: struct bc_state \*

    :param skb:
        data to send.
    :type skb: struct sk_buff \*

.. _`gigaset_isoc_send_skb.description`:

Description
-----------

Called by LL to queue an skb for sending, and start transmission if
necessary.
Once the payload data has been transmitted completely, \ :c:func:`gigaset_skb_sent`\ 
will be called with the skb's link layer header preserved.

.. _`gigaset_isoc_send_skb.return-value`:

Return value
------------

number of bytes accepted for sending (skb->len) if ok,
error code < 0 (eg. -ENODEV) on error

.. This file was automatic generated / don't edit.


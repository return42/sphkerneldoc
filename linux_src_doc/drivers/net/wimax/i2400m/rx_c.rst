.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wimax/i2400m/rx.c

.. _`i2400m_rx`:

i2400m_rx
=========

.. c:function:: int i2400m_rx(struct i2400m *i2400m, struct sk_buff *skb)

    Receive a buffer of data from the device

    :param i2400m:
        device descriptor
    :type i2400m: struct i2400m \*

    :param skb:
        skbuff where the data has been received
    :type skb: struct sk_buff \*

.. _`i2400m_rx.description`:

Description
-----------

Parse in a buffer of data that contains an RX message sent from the
device. See the file header for the format. Run all checks on the
buffer header, then run over each payload's descriptors, verify
their consistency and act on each payload's contents.  If
everything is successful, update the device's statistics.

.. _`i2400m_rx.note`:

Note
----

You need to set the skb to contain only the length of the
received buffer; for that, use skb_trim(skb, RECEIVED_SIZE).

.. _`i2400m_rx.return`:

Return
------


0 if ok, < 0 errno on error

If ok, this function owns now the skb and the caller DOESN'T have
to run \ :c:func:`kfree_skb`\  on it. However, on error, the caller still owns
the skb and it is responsible for releasing it.

.. This file was automatic generated / don't edit.


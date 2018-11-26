.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wimax/i2400m/tx.c

.. _`i2400m_tx`:

i2400m_tx
=========

.. c:function:: int i2400m_tx(struct i2400m *i2400m, const void *buf, size_t buf_len, enum i2400m_pt pl_type)

    send the data in a buffer to the device

    :param i2400m:
        *undescribed*
    :type i2400m: struct i2400m \*

    :param buf:
        pointer to the buffer to transmit
    :type buf: const void \*

    :param buf_len:
        buffer size
    :type buf_len: size_t

    :param pl_type:
        type of the payload we are sending.
    :type pl_type: enum i2400m_pt

.. _`i2400m_tx.return`:

Return
------

0 if ok, < 0 errno code on error (-ENOSPC, if there is no more
room for the message in the queue).

Appends the buffer to the TX FIFO and notifies the bus-specific
part of the driver that there is new data ready to transmit.
Once this function returns, the buffer has been copied, so it can
be reused.

The steps followed to append are explained in detail in the file
header.

Whenever we write to a message, we increase msg->size, so it
reflects exactly how big the message is. This is needed so that if
we concatenate two messages before they can be sent, the code that
sends the messages can find the boundaries (and it will replace the
size with the real barker before sending).

.. _`i2400m_tx.note`:

Note
----


Cold and warm reset payloads need to be sent as a single
payload, so we handle that.

.. _`i2400m_tx_msg_get`:

i2400m_tx_msg_get
=================

.. c:function:: struct i2400m_msg_hdr *i2400m_tx_msg_get(struct i2400m *i2400m, size_t *bus_size)

    Get the first TX message in the FIFO to start sending it

    :param i2400m:
        device descriptors
    :type i2400m: struct i2400m \*

    :param bus_size:
        where to place the size of the TX message
    :type bus_size: size_t \*

.. _`i2400m_tx_msg_get.description`:

Description
-----------

Called by the bus-specific driver to get the first TX message at
the FIF that is ready for transmission.

It sets the state in \ ``i2400m``\  to indicate the bus-specific driver is
transferring that message (i2400m->tx_msg_size).

Once the transfer is completed, call \ :c:func:`i2400m_tx_msg_sent`\ .

.. _`i2400m_tx_msg_get.notes`:

Notes
-----


The size of the TX message to be transmitted might be smaller than
that of the TX message in the FIFO (in case the header was
shorter). Hence, we copy it in \ ``bus_size``\ , for the bus layer to
use. We keep the message's size in i2400m->tx_msg_size so that
when the bus later is done transferring we know how much to
advance the fifo.

We collect statistics here as all the data is available and we
assume it is going to work [see \ :c:func:`i2400m_tx_msg_sent`\ ].

.. _`i2400m_tx_msg_sent`:

i2400m_tx_msg_sent
==================

.. c:function:: void i2400m_tx_msg_sent(struct i2400m *i2400m)

    indicate the transmission of a TX message

    :param i2400m:
        device descriptor
    :type i2400m: struct i2400m \*

.. _`i2400m_tx_msg_sent.description`:

Description
-----------

Called by the bus-specific driver when a message has been sent;
this pops it from the FIFO; and as there is space, start the queue
in case it was stopped.

Should be called even if the message send failed and we are
dropping this TX message.

.. _`i2400m_tx_setup`:

i2400m_tx_setup
===============

.. c:function:: int i2400m_tx_setup(struct i2400m *i2400m)

    Initialize the TX queue and infrastructure

    :param i2400m:
        *undescribed*
    :type i2400m: struct i2400m \*

.. _`i2400m_tx_setup.description`:

Description
-----------

Make sure we reset the TX sequence to zero, as when this function
is called, the firmware has been just restarted. Same rational
for tx_in, tx_out, tx_msg_size and tx_msg. We reset them since
the memory for TX queue is reallocated.

.. _`i2400m_tx_release`:

i2400m_tx_release
=================

.. c:function:: void i2400m_tx_release(struct i2400m *i2400m)

    Tear down the TX queue and infrastructure

    :param i2400m:
        *undescribed*
    :type i2400m: struct i2400m \*

.. This file was automatic generated / don't edit.


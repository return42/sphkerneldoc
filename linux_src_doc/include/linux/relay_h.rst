.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/relay.h

.. _`relay_write`:

relay_write
===========

.. c:function:: void relay_write(struct rchan *chan, const void *data, size_t length)

    write data into the channel

    :param chan:
        relay channel
    :type chan: struct rchan \*

    :param data:
        data to be written
    :type data: const void \*

    :param length:
        number of bytes to write
    :type length: size_t

.. _`relay_write.description`:

Description
-----------

Writes data into the current cpu's channel buffer.

Protects the buffer by disabling interrupts.  Use this
if you might be logging from interrupt context.  Try
\__relay_write() if you know you won't be logging from
interrupt context.

.. _`__relay_write`:

\__relay_write
==============

.. c:function:: void __relay_write(struct rchan *chan, const void *data, size_t length)

    write data into the channel

    :param chan:
        relay channel
    :type chan: struct rchan \*

    :param data:
        data to be written
    :type data: const void \*

    :param length:
        number of bytes to write
    :type length: size_t

.. _`__relay_write.description`:

Description
-----------

Writes data into the current cpu's channel buffer.

Protects the buffer by disabling preemption.  Use
\ :c:func:`relay_write`\  if you might be logging from interrupt
context.

.. _`relay_reserve`:

relay_reserve
=============

.. c:function:: void *relay_reserve(struct rchan *chan, size_t length)

    reserve slot in channel buffer

    :param chan:
        relay channel
    :type chan: struct rchan \*

    :param length:
        number of bytes to reserve
    :type length: size_t

.. _`relay_reserve.description`:

Description
-----------

Returns pointer to reserved slot, NULL if full.

Reserves a slot in the current cpu's channel buffer.
Does not protect the buffer at all - caller must provide
appropriate synchronization.

.. _`subbuf_start_reserve`:

subbuf_start_reserve
====================

.. c:function:: void subbuf_start_reserve(struct rchan_buf *buf, size_t length)

    reserve bytes at the start of a sub-buffer

    :param buf:
        relay channel buffer
    :type buf: struct rchan_buf \*

    :param length:
        number of bytes to reserve
    :type length: size_t

.. _`subbuf_start_reserve.description`:

Description
-----------

Helper function used to reserve bytes at the beginning of
a sub-buffer in the \ :c:func:`subbuf_start`\  callback.

.. This file was automatic generated / don't edit.


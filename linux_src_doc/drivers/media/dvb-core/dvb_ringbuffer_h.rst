.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_ringbuffer.h

.. _`dvb_ringbuffer`:

struct dvb_ringbuffer
=====================

.. c:type:: struct dvb_ringbuffer

    Describes a ring buffer used at DVB framework

.. _`dvb_ringbuffer.definition`:

Definition
----------

.. code-block:: c

    struct dvb_ringbuffer {
        u8 *data;
        ssize_t size;
        ssize_t pread;
        ssize_t pwrite;
        int error;
        wait_queue_head_t queue;
        spinlock_t lock;
    }

.. _`dvb_ringbuffer.members`:

Members
-------

data
    Area were the ringbuffer data is written

size
    size of the ringbuffer

pread
    next position to read

pwrite
    next position to write

error
    used by ringbuffer clients to indicate that an error happened.

queue
    Wait queue used by ringbuffer clients to indicate when buffer
    was filled

lock
    Spinlock used to protect the ringbuffer

.. _`dvb_ringbuffer_init`:

dvb_ringbuffer_init
===================

.. c:function:: void dvb_ringbuffer_init(struct dvb_ringbuffer *rbuf, void *data, size_t len)

    initialize ring buffer, lock and queue

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

    :param void \*data:
        pointer to the buffer where the data will be stored

    :param size_t len:
        bytes from ring buffer into \ ``buf``\ 

.. _`dvb_ringbuffer_empty`:

dvb_ringbuffer_empty
====================

.. c:function:: int dvb_ringbuffer_empty(struct dvb_ringbuffer *rbuf)

    test whether buffer is empty

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

.. _`dvb_ringbuffer_free`:

dvb_ringbuffer_free
===================

.. c:function:: ssize_t dvb_ringbuffer_free(struct dvb_ringbuffer *rbuf)

    returns the number of free bytes in the buffer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

.. _`dvb_ringbuffer_free.return`:

Return
------

number of free bytes in the buffer

.. _`dvb_ringbuffer_avail`:

dvb_ringbuffer_avail
====================

.. c:function:: ssize_t dvb_ringbuffer_avail(struct dvb_ringbuffer *rbuf)

    returns the number of bytes waiting in the buffer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

.. _`dvb_ringbuffer_avail.return`:

Return
------

number of bytes waiting in the buffer

.. _`dvb_ringbuffer_reset`:

dvb_ringbuffer_reset
====================

.. c:function:: void dvb_ringbuffer_reset(struct dvb_ringbuffer *rbuf)

    resets the ringbuffer to initial state

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

.. _`dvb_ringbuffer_reset.description`:

Description
-----------

Resets the read and write pointers to zero and flush the buffer.

This counts as a read and write operation

.. _`dvb_ringbuffer_flush`:

dvb_ringbuffer_flush
====================

.. c:function:: void dvb_ringbuffer_flush(struct dvb_ringbuffer *rbuf)

    flush buffer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

.. _`dvb_ringbuffer_flush_spinlock_wakeup`:

dvb_ringbuffer_flush_spinlock_wakeup
====================================

.. c:function:: void dvb_ringbuffer_flush_spinlock_wakeup(struct dvb_ringbuffer *rbuf)

    flush buffer protected by spinlock and wake-up waiting task(s)

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

.. _`dvb_ringbuffer_peek`:

DVB_RINGBUFFER_PEEK
===================

.. c:function::  DVB_RINGBUFFER_PEEK( rbuf,  offs)

    peek at byte \ ``offs``\  in the buffer

    :param  rbuf:
        pointer to struct dvb_ringbuffer

    :param  offs:
        offset inside the ringbuffer

.. _`dvb_ringbuffer_skip`:

DVB_RINGBUFFER_SKIP
===================

.. c:function::  DVB_RINGBUFFER_SKIP( rbuf,  num)

    advance read ptr by \ ``num``\  bytes

    :param  rbuf:
        pointer to struct dvb_ringbuffer

    :param  num:
        number of bytes to advance

.. _`dvb_ringbuffer_read_user`:

dvb_ringbuffer_read_user
========================

.. c:function:: ssize_t dvb_ringbuffer_read_user(struct dvb_ringbuffer *rbuf, u8 __user *buf, size_t len)

    Reads a buffer into a user pointer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

    :param u8 __user \*buf:
        pointer to the buffer where the data will be stored

    :param size_t len:
        bytes from ring buffer into \ ``buf``\ 

.. _`dvb_ringbuffer_read_user.description`:

Description
-----------

This variant assumes that the buffer is a memory at the userspace. So,
it will internally call \ :c:func:`copy_to_user`\ .

.. _`dvb_ringbuffer_read_user.return`:

Return
------

number of bytes transferred or -EFAULT

.. _`dvb_ringbuffer_read`:

dvb_ringbuffer_read
===================

.. c:function:: void dvb_ringbuffer_read(struct dvb_ringbuffer *rbuf, u8 *buf, size_t len)

    Reads a buffer into a pointer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

    :param u8 \*buf:
        pointer to the buffer where the data will be stored

    :param size_t len:
        bytes from ring buffer into \ ``buf``\ 

.. _`dvb_ringbuffer_read.description`:

Description
-----------

This variant assumes that the buffer is a memory at the Kernel space

.. _`dvb_ringbuffer_read.return`:

Return
------

number of bytes transferred or -EFAULT

.. _`dvb_ringbuffer_write_byte`:

DVB_RINGBUFFER_WRITE_BYTE
=========================

.. c:function::  DVB_RINGBUFFER_WRITE_BYTE( rbuf,  byte)

    write single byte to ring buffer

    :param  rbuf:
        pointer to struct dvb_ringbuffer

    :param  byte:
        byte to write

.. _`dvb_ringbuffer_write`:

dvb_ringbuffer_write
====================

.. c:function:: ssize_t dvb_ringbuffer_write(struct dvb_ringbuffer *rbuf, const u8 *buf, size_t len)

    Writes a buffer into the ringbuffer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

    :param const u8 \*buf:
        pointer to the buffer where the data will be read

    :param size_t len:
        bytes from ring buffer into \ ``buf``\ 

.. _`dvb_ringbuffer_write.description`:

Description
-----------

This variant assumes that the buffer is a memory at the Kernel space

.. _`dvb_ringbuffer_write.return`:

Return
------

number of bytes transferred or -EFAULT

.. _`dvb_ringbuffer_write_user`:

dvb_ringbuffer_write_user
=========================

.. c:function:: ssize_t dvb_ringbuffer_write_user(struct dvb_ringbuffer *rbuf, const u8 __user *buf, size_t len)

    Writes a buffer received via a user pointer

    :param struct dvb_ringbuffer \*rbuf:
        pointer to struct dvb_ringbuffer

    :param const u8 __user \*buf:
        pointer to the buffer where the data will be read

    :param size_t len:
        bytes from ring buffer into \ ``buf``\ 

.. _`dvb_ringbuffer_write_user.description`:

Description
-----------

This variant assumes that the buffer is a memory at the userspace. So,
it will internally call \ :c:func:`copy_from_user`\ .

.. _`dvb_ringbuffer_write_user.return`:

Return
------

number of bytes transferred or -EFAULT

.. _`dvb_ringbuffer_pkt_write`:

dvb_ringbuffer_pkt_write
========================

.. c:function:: ssize_t dvb_ringbuffer_pkt_write(struct dvb_ringbuffer *rbuf, u8 *buf, size_t len)

    Write a packet into the ringbuffer.

    :param struct dvb_ringbuffer \*rbuf:
        Ringbuffer to write to.

    :param u8 \*buf:
        Buffer to write.

    :param size_t len:
        Length of buffer (currently limited to 65535 bytes max).

.. _`dvb_ringbuffer_pkt_write.return`:

Return
------

Number of bytes written, or -EFAULT, -ENOMEM, -EVINAL.

.. _`dvb_ringbuffer_pkt_read_user`:

dvb_ringbuffer_pkt_read_user
============================

.. c:function:: ssize_t dvb_ringbuffer_pkt_read_user(struct dvb_ringbuffer *rbuf, size_t idx, int offset, u8 __user *buf, size_t len)

    Read from a packet in the ringbuffer.

    :param struct dvb_ringbuffer \*rbuf:
        Ringbuffer concerned.

    :param size_t idx:
        Packet index as returned by \ :c:func:`dvb_ringbuffer_pkt_next`\ .

    :param int offset:
        Offset into packet to read from.

    :param u8 __user \*buf:
        Destination buffer for data.

    :param size_t len:
        Size of destination buffer.

.. _`dvb_ringbuffer_pkt_read_user.return`:

Return
------

Number of bytes read, or -EFAULT.

.. note::

   unlike \ :c:func:`dvb_ringbuffer_read`\ , this does **NOT** update the read pointer
   in the ringbuffer. You must use \ :c:func:`dvb_ringbuffer_pkt_dispose`\  to mark a
   packet as no longer required.

.. _`dvb_ringbuffer_pkt_read`:

dvb_ringbuffer_pkt_read
=======================

.. c:function:: ssize_t dvb_ringbuffer_pkt_read(struct dvb_ringbuffer *rbuf, size_t idx, int offset, u8 *buf, size_t len)

    Read from a packet in the ringbuffer.

    :param struct dvb_ringbuffer \*rbuf:
        Ringbuffer concerned.

    :param size_t idx:
        Packet index as returned by \ :c:func:`dvb_ringbuffer_pkt_next`\ .

    :param int offset:
        Offset into packet to read from.

    :param u8 \*buf:
        Destination buffer for data.

    :param size_t len:
        Size of destination buffer.

.. _`dvb_ringbuffer_pkt_read.note`:

Note
----

unlike \ :c:func:`dvb_ringbuffer_read_user`\ , this DOES update the read pointer
in the ringbuffer.

.. _`dvb_ringbuffer_pkt_read.return`:

Return
------

Number of bytes read, or -EFAULT.

.. _`dvb_ringbuffer_pkt_dispose`:

dvb_ringbuffer_pkt_dispose
==========================

.. c:function:: void dvb_ringbuffer_pkt_dispose(struct dvb_ringbuffer *rbuf, size_t idx)

    Dispose of a packet in the ring buffer.

    :param struct dvb_ringbuffer \*rbuf:
        Ring buffer concerned.

    :param size_t idx:
        Packet index as returned by \ :c:func:`dvb_ringbuffer_pkt_next`\ .

.. _`dvb_ringbuffer_pkt_next`:

dvb_ringbuffer_pkt_next
=======================

.. c:function:: ssize_t dvb_ringbuffer_pkt_next(struct dvb_ringbuffer *rbuf, size_t idx, size_t *pktlen)

    Get the index of the next packet in a ringbuffer.

    :param struct dvb_ringbuffer \*rbuf:
        Ringbuffer concerned.

    :param size_t idx:
        Previous packet index, or -1 to return the first packet index.

    :param size_t \*pktlen:
        On success, will be updated to contain the length of the packet
        in bytes.
        returns Packet index (if >=0), or -1 if no packets available.

.. This file was automatic generated / don't edit.


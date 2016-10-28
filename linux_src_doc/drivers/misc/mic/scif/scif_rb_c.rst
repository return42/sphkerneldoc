.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_rb.c

.. _`scif_rb_init`:

scif_rb_init
============

.. c:function:: void scif_rb_init(struct scif_rb *rb, u32 *read_ptr, u32 *write_ptr, void *rb_base, u8 size)

    Initializes the ring buffer

    :param struct scif_rb \*rb:
        ring buffer

    :param u32 \*read_ptr:
        A pointer to the read offset

    :param u32 \*write_ptr:
        A pointer to the write offset

    :param void \*rb_base:
        A pointer to the base of the ring buffer

    :param u8 size:
        The size of the ring buffer in powers of two

.. _`scif_rb_space`:

scif_rb_space
=============

.. c:function:: u32 scif_rb_space(struct scif_rb *rb)

    Query space available for writing to the RB

    :param struct scif_rb \*rb:
        ring buffer

.. _`scif_rb_space.return`:

Return
------

size available for writing to RB in bytes.

.. _`scif_rb_write`:

scif_rb_write
=============

.. c:function:: int scif_rb_write(struct scif_rb *rb, void *msg, u32 size)

    Write a message to the RB

    :param struct scif_rb \*rb:
        ring buffer

    :param void \*msg:
        buffer to send the message.  Must be at least size bytes long

    :param u32 size:
        the size (in bytes) to be copied to the RB

.. _`scif_rb_write.description`:

Description
-----------

This API does not block if there isn't enough space in the RB.

.. _`scif_rb_write.return`:

Return
------

0 on success or -ENOMEM on failure

.. _`scif_rb_commit`:

scif_rb_commit
==============

.. c:function:: void scif_rb_commit(struct scif_rb *rb)

    To submit the message to let the peer fetch it

    :param struct scif_rb \*rb:
        ring buffer

.. _`scif_rb_get`:

scif_rb_get
===========

.. c:function:: void *scif_rb_get(struct scif_rb *rb, u32 size)

    To get next message from the ring buffer

    :param struct scif_rb \*rb:
        ring buffer

    :param u32 size:
        Number of bytes to be read

.. _`scif_rb_get.return`:

Return
------

NULL if no bytes to be read from the ring buffer, otherwise the
pointer to the next byte

.. _`scif_rb_update_read_ptr`:

scif_rb_update_read_ptr
=======================

.. c:function:: void scif_rb_update_read_ptr(struct scif_rb *rb)

    :param struct scif_rb \*rb:
        ring buffer

.. _`scif_rb_count`:

scif_rb_count
=============

.. c:function:: u32 scif_rb_count(struct scif_rb *rb, u32 size)

    :param struct scif_rb \*rb:
        ring buffer

    :param u32 size:
        Number of bytes expected to be read

.. _`scif_rb_count.return`:

Return
------

number of bytes that can be read from the RB

.. This file was automatic generated / don't edit.


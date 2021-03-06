.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_buffer.c

.. _`tty_buffer_lock_exclusive`:

tty_buffer_lock_exclusive
=========================

.. c:function:: void tty_buffer_lock_exclusive(struct tty_port *port)

    gain exclusive access to buffer tty_buffer_unlock_exclusive     -       release exclusive access

    :param port:
        *undescribed*
    :type port: struct tty_port \*

.. _`tty_buffer_lock_exclusive.description`:

Description
-----------

\ ``port``\  - tty_port owning the flip buffer

Guarantees safe use of the line discipline's \ :c:func:`receive_buf`\  method by
excluding the buffer work and any pending flush from using the flip
buffer. Data can continue to be added concurrently to the flip buffer
from the driver side.

On release, the buffer work is restarted if there is data in the
flip buffer

.. _`tty_buffer_space_avail`:

tty_buffer_space_avail
======================

.. c:function:: int tty_buffer_space_avail(struct tty_port *port)

    return unused buffer space \ ``port``\  - tty_port owning the flip buffer

    :param port:
        *undescribed*
    :type port: struct tty_port \*

.. _`tty_buffer_space_avail.description`:

Description
-----------

Returns the # of bytes which can be written by the driver without
reaching the buffer limit.

.. _`tty_buffer_space_avail.note`:

Note
----

this does not guarantee that memory is available to write
the returned # of bytes (use \ :c:func:`tty_prepare_flip_string_xxx`\  to
pre-allocate if memory guarantee is required).

.. _`tty_buffer_free_all`:

tty_buffer_free_all
===================

.. c:function:: void tty_buffer_free_all(struct tty_port *port)

    free buffers used by a tty

    :param port:
        *undescribed*
    :type port: struct tty_port \*

.. _`tty_buffer_free_all.description`:

Description
-----------

Remove all the buffers pending on a tty whether queued with data
or in the free ring. Must be called when the tty is no longer in use

.. _`tty_buffer_alloc`:

tty_buffer_alloc
================

.. c:function:: struct tty_buffer *tty_buffer_alloc(struct tty_port *port, size_t size)

    allocate a tty buffer

    :param port:
        *undescribed*
    :type port: struct tty_port \*

    :param size:
        desired size (characters)
    :type size: size_t

.. _`tty_buffer_alloc.description`:

Description
-----------

Allocate a new tty buffer to hold the desired number of characters.
We round our buffers off in 256 character chunks to get better
allocation behaviour.
Return NULL if out of memory or the allocation would exceed the
per device queue

.. _`tty_buffer_free`:

tty_buffer_free
===============

.. c:function:: void tty_buffer_free(struct tty_port *port, struct tty_buffer *b)

    free a tty buffer

    :param port:
        *undescribed*
    :type port: struct tty_port \*

    :param b:
        the buffer to free
    :type b: struct tty_buffer \*

.. _`tty_buffer_free.description`:

Description
-----------

Free a tty buffer, or add it to the free list according to our
internal strategy

.. _`tty_buffer_flush`:

tty_buffer_flush
================

.. c:function:: void tty_buffer_flush(struct tty_struct *tty, struct tty_ldisc *ld)

    flush full tty buffers

    :param tty:
        tty to flush
    :type tty: struct tty_struct \*

    :param ld:
        optional ldisc ptr (must be referenced)
    :type ld: struct tty_ldisc \*

.. _`tty_buffer_flush.description`:

Description
-----------

flush all the buffers containing receive data. If ld != NULL,
flush the ldisc input buffer.

.. _`tty_buffer_flush.locking`:

Locking
-------

takes buffer lock to ensure single-threaded flip buffer
'consumer'

.. _`__tty_buffer_request_room`:

\__tty_buffer_request_room
==========================

.. c:function:: int __tty_buffer_request_room(struct tty_port *port, size_t size, int flags)

    grow tty buffer if needed

    :param port:
        *undescribed*
    :type port: struct tty_port \*

    :param size:
        size desired
    :type size: size_t

    :param flags:
        buffer flags if new buffer allocated (default = 0)
    :type flags: int

.. _`__tty_buffer_request_room.description`:

Description
-----------

Make at least size bytes of linear space available for the tty
buffer. If we fail return the size we managed to find.

Will change over to a new buffer if the current buffer is encoded as
TTY_NORMAL (so has no flags buffer) and the new buffer requires
a flags buffer.

.. _`tty_insert_flip_string_fixed_flag`:

tty_insert_flip_string_fixed_flag
=================================

.. c:function:: int tty_insert_flip_string_fixed_flag(struct tty_port *port, const unsigned char *chars, char flag, size_t size)

    Add characters to the tty buffer

    :param port:
        tty port
    :type port: struct tty_port \*

    :param chars:
        characters
    :type chars: const unsigned char \*

    :param flag:
        flag value for each character
    :type flag: char

    :param size:
        size
    :type size: size_t

.. _`tty_insert_flip_string_fixed_flag.description`:

Description
-----------

Queue a series of bytes to the tty buffering. All the characters
passed are marked with the supplied flag. Returns the number added.

.. _`tty_insert_flip_string_flags`:

tty_insert_flip_string_flags
============================

.. c:function:: int tty_insert_flip_string_flags(struct tty_port *port, const unsigned char *chars, const char *flags, size_t size)

    Add characters to the tty buffer

    :param port:
        tty port
    :type port: struct tty_port \*

    :param chars:
        characters
    :type chars: const unsigned char \*

    :param flags:
        flag bytes
    :type flags: const char \*

    :param size:
        size
    :type size: size_t

.. _`tty_insert_flip_string_flags.description`:

Description
-----------

Queue a series of bytes to the tty buffering. For each character
the flags array indicates the status of the character. Returns the
number added.

.. _`__tty_insert_flip_char`:

\__tty_insert_flip_char
=======================

.. c:function:: int __tty_insert_flip_char(struct tty_port *port, unsigned char ch, char flag)

    Add one character to the tty buffer

    :param port:
        tty port
    :type port: struct tty_port \*

    :param ch:
        character
    :type ch: unsigned char

    :param flag:
        flag byte
    :type flag: char

.. _`__tty_insert_flip_char.description`:

Description
-----------

Queue a single byte to the tty buffering, with an optional flag.
This is the slow path of tty_insert_flip_char.

.. _`tty_schedule_flip`:

tty_schedule_flip
=================

.. c:function:: void tty_schedule_flip(struct tty_port *port)

    push characters to ldisc

    :param port:
        tty port to push from
    :type port: struct tty_port \*

.. _`tty_schedule_flip.description`:

Description
-----------

Takes any pending buffers and transfers their ownership to the
ldisc side of the queue. It then schedules those characters for
processing by the line discipline.

.. _`tty_prepare_flip_string`:

tty_prepare_flip_string
=======================

.. c:function:: int tty_prepare_flip_string(struct tty_port *port, unsigned char **chars, size_t size)

    make room for characters

    :param port:
        tty port
    :type port: struct tty_port \*

    :param chars:
        return pointer for character write area
    :type chars: unsigned char \*\*

    :param size:
        desired size
    :type size: size_t

.. _`tty_prepare_flip_string.description`:

Description
-----------

Prepare a block of space in the buffer for data. Returns the length
available and buffer pointer to the space which is now allocated and
accounted for as ready for normal characters. This is used for drivers
that need their own block copy routines into the buffer. There is no
guarantee the buffer is a DMA target!

.. _`tty_ldisc_receive_buf`:

tty_ldisc_receive_buf
=====================

.. c:function:: int tty_ldisc_receive_buf(struct tty_ldisc *ld, const unsigned char *p, char *f, int count)

    forward data to line discipline

    :param ld:
        line discipline to process input
    :type ld: struct tty_ldisc \*

    :param p:
        char buffer
    :type p: const unsigned char \*

    :param f:
        TTY\_\* flags buffer
    :type f: char \*

    :param count:
        number of bytes to process
    :type count: int

.. _`tty_ldisc_receive_buf.description`:

Description
-----------

Callers other than \ :c:func:`flush_to_ldisc`\  need to exclude the kworker
from concurrent use of the line discipline, see \ :c:func:`paste_selection`\ .

Returns the number of bytes processed

.. _`flush_to_ldisc`:

flush_to_ldisc
==============

.. c:function:: void flush_to_ldisc(struct work_struct *work)

    :param work:
        tty structure passed from work queue.
    :type work: struct work_struct \*

.. _`flush_to_ldisc.description`:

Description
-----------

This routine is called out of the software interrupt to flush data
from the buffer chain to the line discipline.

The receive_buf method is single threaded for each tty instance.

.. _`flush_to_ldisc.locking`:

Locking
-------

takes buffer lock to ensure single-threaded flip buffer
'consumer'

.. _`tty_flip_buffer_push`:

tty_flip_buffer_push
====================

.. c:function:: void tty_flip_buffer_push(struct tty_port *port)

    terminal

    :param port:
        tty port to push
    :type port: struct tty_port \*

.. _`tty_flip_buffer_push.description`:

Description
-----------

Queue a push of the terminal flip buffers to the line discipline.
Can be called from IRQ/atomic context.

In the event of the queue being busy for flipping the work will be
held off and retried later.

.. _`tty_buffer_init`:

tty_buffer_init
===============

.. c:function:: void tty_buffer_init(struct tty_port *port)

    prepare a tty buffer structure

    :param port:
        *undescribed*
    :type port: struct tty_port \*

.. _`tty_buffer_init.description`:

Description
-----------

Set up the initial state of the buffer management for a tty device.
Must be called before the other tty buffer functions are used.

.. _`tty_buffer_set_limit`:

tty_buffer_set_limit
====================

.. c:function:: int tty_buffer_set_limit(struct tty_port *port, int limit)

    change the tty buffer memory limit

    :param port:
        tty port to change
    :type port: struct tty_port \*

    :param limit:
        *undescribed*
    :type limit: int

.. _`tty_buffer_set_limit.description`:

Description
-----------

Change the tty buffer memory limit.
Must be called before the other tty buffer functions are used.

.. This file was automatic generated / don't edit.


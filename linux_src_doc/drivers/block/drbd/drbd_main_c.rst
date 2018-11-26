.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_main.c

.. _`tl_release`:

tl_release
==========

.. c:function:: void tl_release(struct drbd_connection *connection, unsigned int barrier_nr, unsigned int set_size)

    mark as BARRIER_ACKED all requests in the corresponding transfer log epoch

    :param connection:
        DRBD connection.
    :type connection: struct drbd_connection \*

    :param barrier_nr:
        Expected identifier of the DRBD write barrier packet.
    :type barrier_nr: unsigned int

    :param set_size:
        Expected number of requests before that barrier.
    :type set_size: unsigned int

.. _`tl_release.description`:

Description
-----------

In case the passed barrier_nr or set_size does not match the oldest
epoch of not yet barrier-acked requests, this function will cause a
termination of the connection.

.. _`_tl_restart`:

\_tl_restart
============

.. c:function:: void _tl_restart(struct drbd_connection *connection, enum drbd_req_event what)

    Walks the transfer log, and applies an action to all requests

    :param connection:
        DRBD connection to operate on.
    :type connection: struct drbd_connection \*

    :param what:
        The action/event to perform with all request objects
    :type what: enum drbd_req_event

.. _`_tl_restart.description`:

Description
-----------

\ ``what``\  might be one of CONNECTION_LOST_WHILE_PENDING, RESEND, FAIL_FROZEN_DISK_IO,
RESTART_FROZEN_DISK_IO.

.. _`tl_clear`:

tl_clear
========

.. c:function:: void tl_clear(struct drbd_connection *connection)

    Clears all requests and \ :c:type:`struct drbd_tl_epoch <drbd_tl_epoch>`\  objects out of the TL

    :param connection:
        *undescribed*
    :type connection: struct drbd_connection \*

.. _`tl_clear.description`:

Description
-----------

This is called after the connection to the peer was lost. The storage covered
by the requests on the transfer gets marked as our of sync. Called from the
receiver thread and the worker thread.

.. _`tl_abort_disk_io`:

tl_abort_disk_io
================

.. c:function:: void tl_abort_disk_io(struct drbd_device *device)

    Abort disk I/O for all requests for a certain device in the TL

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_calc_cpu_mask`:

drbd_calc_cpu_mask
==================

.. c:function:: void drbd_calc_cpu_mask(cpumask_var_t *cpu_mask)

    Generate CPU masks, spread over all CPUs

    :param cpu_mask:
        *undescribed*
    :type cpu_mask: cpumask_var_t \*

.. _`drbd_calc_cpu_mask.description`:

Description
-----------

Forces all threads of a resource onto the same CPU. This is beneficial for
DRBD's performance. May be overwritten by user's configuration.

.. _`drbd_thread_current_set_cpu`:

drbd_thread_current_set_cpu
===========================

.. c:function:: void drbd_thread_current_set_cpu(struct drbd_thread *thi)

    modifies the cpu mask of the \_current\_ thread

    :param thi:
        drbd_thread object
    :type thi: struct drbd_thread \*

.. _`drbd_thread_current_set_cpu.description`:

Description
-----------

call in the "main loop" of \_all\_ threads, no need for any mutex, current won't die
prematurely.

.. _`drbd_header_size`:

drbd_header_size
================

.. c:function:: unsigned int drbd_header_size(struct drbd_connection *connection)

    size of a packet header

    :param connection:
        *undescribed*
    :type connection: struct drbd_connection \*

.. _`drbd_header_size.description`:

Description
-----------

The header size is a multiple of 8, so any payload following the header is
word aligned on 64-bit architectures.  (The bitmap send and receive code
relies on this.)

.. _`drbd_send_current_state`:

drbd_send_current_state
=======================

.. c:function:: int drbd_send_current_state(struct drbd_peer_device *peer_device)

    Sends the drbd state to the peer

    :param peer_device:
        DRBD peer device.
    :type peer_device: struct drbd_peer_device \*

.. _`drbd_send_state`:

drbd_send_state
===============

.. c:function:: int drbd_send_state(struct drbd_peer_device *peer_device, union drbd_state state)

    After a state change, sends the new state to the peer

    :param peer_device:
        DRBD peer device.
    :type peer_device: struct drbd_peer_device \*

    :param state:
        the state to send, not necessarily the current state.
    :type state: union drbd_state

.. _`drbd_send_state.description`:

Description
-----------

Each state change queues an "after_state_ch" work, which will eventually
send the resulting new state to the peer. If more state changes happen
between queuing and processing of the after_state_ch work, we still
want to send each intermediary state in the order it occurred.

.. _`send_bitmap_rle_or_plain`:

send_bitmap_rle_or_plain
========================

.. c:function:: int send_bitmap_rle_or_plain(struct drbd_device *device, struct bm_xfer_ctx *c)

    :param device:
        *undescribed*
    :type device: struct drbd_device \*

    :param c:
        *undescribed*
    :type c: struct bm_xfer_ctx \*

.. _`send_bitmap_rle_or_plain.description`:

Description
-----------

Return 0 when done, 1 when another iteration is needed, and a negative error
code upon failure.

.. _`_drbd_send_ack`:

\_drbd_send_ack
===============

.. c:function:: int _drbd_send_ack(struct drbd_peer_device *peer_device, enum drbd_packet cmd, u64 sector, u32 blksize, u64 block_id)

    Sends an ack packet

    :param peer_device:
        *undescribed*
    :type peer_device: struct drbd_peer_device \*

    :param cmd:
        Packet command code.
    :type cmd: enum drbd_packet

    :param sector:
        sector, needs to be in big endian byte order
    :type sector: u64

    :param blksize:
        size in byte, needs to be in big endian byte order
    :type blksize: u32

    :param block_id:
        Id, big endian byte order
    :type block_id: u64

.. _`drbd_send_ack`:

drbd_send_ack
=============

.. c:function:: int drbd_send_ack(struct drbd_peer_device *peer_device, enum drbd_packet cmd, struct drbd_peer_request *peer_req)

    Sends an ack packet

    :param peer_device:
        *undescribed*
    :type peer_device: struct drbd_peer_device \*

    :param cmd:
        packet command code
    :type cmd: enum drbd_packet

    :param peer_req:
        peer request
    :type peer_req: struct drbd_peer_request \*

.. _`drbd_send_all`:

drbd_send_all
=============

.. c:function:: int drbd_send_all(struct drbd_connection *connection, struct socket *sock, void *buffer, size_t size, unsigned msg_flags)

    Send an entire buffer

    :param connection:
        *undescribed*
    :type connection: struct drbd_connection \*

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param buffer:
        *undescribed*
    :type buffer: void \*

    :param size:
        *undescribed*
    :type size: size_t

    :param msg_flags:
        *undescribed*
    :type msg_flags: unsigned

.. _`drbd_send_all.description`:

Description
-----------

Returns 0 upon success and a negative error value otherwise.

.. _`drbd_congested`:

drbd_congested
==============

.. c:function:: int drbd_congested(void *congested_data, int bdi_bits)

    Callback for the flusher thread

    :param congested_data:
        User data
    :type congested_data: void \*

    :param bdi_bits:
        Bits the BDI flusher thread is currently interested in
    :type bdi_bits: int

.. _`drbd_congested.description`:

Description
-----------

Returns 1<<WB_async_congested and/or 1<<WB_sync_congested if we are congested.

.. _`drbd_md_sync`:

drbd_md_sync
============

.. c:function:: void drbd_md_sync(struct drbd_device *device)

    Writes the meta data super block if the MD_DIRTY flag bit is set

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_md_read`:

drbd_md_read
============

.. c:function:: int drbd_md_read(struct drbd_device *device, struct drbd_backing_dev *bdev)

    Reads in the meta data super block

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param bdev:
        Device from which the meta data should be read in.
    :type bdev: struct drbd_backing_dev \*

.. _`drbd_md_read.description`:

Description
-----------

Return NO_ERROR on success, and an enum drbd_ret_code in case
something goes wrong.

Called exactly once during \ :c:func:`drbd_adm_attach`\ , while still being D_DISKLESS,
even before \ ``bdev``\  is assigned to \ ``device->ldev``\ .

.. _`drbd_md_mark_dirty_`:

drbd_md_mark_dirty_
===================

.. c:function:: void drbd_md_mark_dirty_(struct drbd_device *device, unsigned int line, const char *func)

    Mark meta data super block as dirty

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param line:
        *undescribed*
    :type line: unsigned int

    :param func:
        *undescribed*
    :type func: const char \*

.. _`drbd_md_mark_dirty_.description`:

Description
-----------

Call this function if you change anything that should be written to
the meta-data super block. This function sets MD_DIRTY, and starts a
timer that ensures that within five seconds you have to call \ :c:func:`drbd_md_sync`\ .

.. _`drbd_uuid_new_current`:

drbd_uuid_new_current
=====================

.. c:function:: void drbd_uuid_new_current(struct drbd_device *device)

    Creates a new current UUID

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_uuid_new_current.description`:

Description
-----------

Creates a new current UUID, and rotates the old current UUID into
the bitmap slot. Causes an incremental resync upon next connect.

.. _`drbd_bmio_set_n_write`:

drbd_bmio_set_n_write
=====================

.. c:function:: int drbd_bmio_set_n_write(struct drbd_device *device)

    io_fn for \ :c:func:`drbd_queue_bitmap_io`\  or \ :c:func:`drbd_bitmap_io`\ 

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_bmio_set_n_write.description`:

Description
-----------

Sets all bits in the bitmap and writes the whole bitmap to stable storage.

.. _`drbd_bmio_clear_n_write`:

drbd_bmio_clear_n_write
=======================

.. c:function:: int drbd_bmio_clear_n_write(struct drbd_device *device)

    io_fn for \ :c:func:`drbd_queue_bitmap_io`\  or \ :c:func:`drbd_bitmap_io`\ 

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_bmio_clear_n_write.description`:

Description
-----------

Clears all bits in the bitmap and writes the whole bitmap to stable storage.

.. _`drbd_queue_bitmap_io`:

drbd_queue_bitmap_io
====================

.. c:function:: void drbd_queue_bitmap_io(struct drbd_device *device, int (*io_fn)(struct drbd_device *), void (*done)(struct drbd_device *, int), char *why, enum bm_flag flags)

    Queues an IO operation on the whole bitmap

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param int (\*io_fn)(struct drbd_device \*):
        IO callback to be called when bitmap IO is possible

    :param void (\*done)(struct drbd_device \*, int):
        callback to be called after the bitmap IO was performed

    :param why:
        Descriptive text of the reason for doing the IO
    :type why: char \*

    :param flags:
        *undescribed*
    :type flags: enum bm_flag

.. _`drbd_queue_bitmap_io.description`:

Description
-----------

While IO on the bitmap happens we freeze application IO thus we ensure
that \ :c:func:`drbd_set_out_of_sync`\  can not be called. This function MAY ONLY be
called from worker context. It MUST NOT be used while a previous such
work is still pending!

Its worker function encloses the call of \ :c:func:`io_fn`\  by \ :c:func:`get_ldev`\  and
\ :c:func:`put_ldev`\ .

.. _`drbd_bitmap_io`:

drbd_bitmap_io
==============

.. c:function:: int drbd_bitmap_io(struct drbd_device *device, int (*io_fn)(struct drbd_device *), char *why, enum bm_flag flags)

    Does an IO operation on the whole bitmap

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param int (\*io_fn)(struct drbd_device \*):
        IO callback to be called when bitmap IO is possible

    :param why:
        Descriptive text of the reason for doing the IO
    :type why: char \*

    :param flags:
        *undescribed*
    :type flags: enum bm_flag

.. _`drbd_bitmap_io.description`:

Description
-----------

freezes application IO while that the actual IO operations runs. This
functions MAY NOT be called from worker context.

.. _`drbd_wait_misc`:

drbd_wait_misc
==============

.. c:function:: int drbd_wait_misc(struct drbd_device *device, struct drbd_interval *i)

    wait for a request to make progress

    :param device:
        device associated with the request
    :type device: struct drbd_device \*

    :param i:
        the struct drbd_interval embedded in struct drbd_request or
        struct drbd_peer_request
    :type i: struct drbd_interval \*

.. This file was automatic generated / don't edit.


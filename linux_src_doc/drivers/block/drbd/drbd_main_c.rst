.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_main.c

.. _`tl_release`:

tl_release
==========

.. c:function:: void tl_release(struct drbd_connection *connection, unsigned int barrier_nr, unsigned int set_size)

    mark as BARRIER_ACKED all requests in the corresponding transfer log epoch

    :param struct drbd_connection \*connection:
        DRBD connection.

    :param unsigned int barrier_nr:
        Expected identifier of the DRBD write barrier packet.

    :param unsigned int set_size:
        Expected number of requests before that barrier.

.. _`tl_release.description`:

Description
-----------

In case the passed barrier_nr or set_size does not match the oldest
epoch of not yet barrier-acked requests, this function will cause a
termination of the connection.

.. _`_tl_restart`:

_tl_restart
===========

.. c:function:: void _tl_restart(struct drbd_connection *connection, enum drbd_req_event what)

    Walks the transfer log, and applies an action to all requests

    :param struct drbd_connection \*connection:
        DRBD connection to operate on.

    :param enum drbd_req_event what:
        The action/event to perform with all request objects

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

    :param struct drbd_connection \*connection:
        *undescribed*

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

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_calc_cpu_mask`:

drbd_calc_cpu_mask
==================

.. c:function:: void drbd_calc_cpu_mask(cpumask_var_t *cpu_mask)

    Generate CPU masks, spread over all CPUs

    :param cpumask_var_t \*cpu_mask:
        *undescribed*

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

    :param struct drbd_thread \*thi:
        drbd_thread object

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

    :param struct drbd_connection \*connection:
        *undescribed*

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

    :param struct drbd_peer_device \*peer_device:
        DRBD peer device.

.. _`drbd_send_state`:

drbd_send_state
===============

.. c:function:: int drbd_send_state(struct drbd_peer_device *peer_device, union drbd_state state)

    After a state change, sends the new state to the peer

    :param struct drbd_peer_device \*peer_device:
        DRBD peer device.

    :param union drbd_state state:
        the state to send, not necessarily the current state.

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

    :param struct drbd_device \*device:
        *undescribed*

    :param struct bm_xfer_ctx \*c:
        *undescribed*

.. _`send_bitmap_rle_or_plain.description`:

Description
-----------

Return 0 when done, 1 when another iteration is needed, and a negative error
code upon failure.

.. _`_drbd_send_ack`:

_drbd_send_ack
==============

.. c:function:: int _drbd_send_ack(struct drbd_peer_device *peer_device, enum drbd_packet cmd, u64 sector, u32 blksize, u64 block_id)

    Sends an ack packet

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

    :param enum drbd_packet cmd:
        Packet command code.

    :param u64 sector:
        sector, needs to be in big endian byte order

    :param u32 blksize:
        size in byte, needs to be in big endian byte order

    :param u64 block_id:
        Id, big endian byte order

.. _`drbd_send_ack`:

drbd_send_ack
=============

.. c:function:: int drbd_send_ack(struct drbd_peer_device *peer_device, enum drbd_packet cmd, struct drbd_peer_request *peer_req)

    Sends an ack packet

    :param struct drbd_peer_device \*peer_device:
        *undescribed*

    :param enum drbd_packet cmd:
        packet command code

    :param struct drbd_peer_request \*peer_req:
        peer request

.. _`drbd_send_all`:

drbd_send_all
=============

.. c:function:: int drbd_send_all(struct drbd_connection *connection, struct socket *sock, void *buffer, size_t size, unsigned msg_flags)

    Send an entire buffer

    :param struct drbd_connection \*connection:
        *undescribed*

    :param struct socket \*sock:
        *undescribed*

    :param void \*buffer:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param unsigned msg_flags:
        *undescribed*

.. _`drbd_send_all.description`:

Description
-----------

Returns 0 upon success and a negative error value otherwise.

.. _`drbd_congested`:

drbd_congested
==============

.. c:function:: int drbd_congested(void *congested_data, int bdi_bits)

    Callback for the flusher thread

    :param void \*congested_data:
        User data

    :param int bdi_bits:
        Bits the BDI flusher thread is currently interested in

.. _`drbd_congested.description`:

Description
-----------

Returns 1<<WB_async_congested and/or 1<<WB_sync_congested if we are congested.

.. _`drbd_md_sync`:

drbd_md_sync
============

.. c:function:: void drbd_md_sync(struct drbd_device *device)

    Writes the meta data super block if the MD_DIRTY flag bit is set

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_md_read`:

drbd_md_read
============

.. c:function:: int drbd_md_read(struct drbd_device *device, struct drbd_backing_dev *bdev)

    Reads in the meta data super block

    :param struct drbd_device \*device:
        DRBD device.

    :param struct drbd_backing_dev \*bdev:
        Device from which the meta data should be read in.

.. _`drbd_md_read.description`:

Description
-----------

Return NO_ERROR on success, and an enum drbd_ret_code in case
something goes wrong.

Called exactly once during \ :c:func:`drbd_adm_attach`\ , while still being D_DISKLESS,
even before \ ``bdev``\  is assigned to \ ``device``\ ->ldev.

.. _`drbd_md_mark_dirty_`:

drbd_md_mark_dirty_
===================

.. c:function:: void drbd_md_mark_dirty_(struct drbd_device *device, unsigned int line, const char *func)

    Mark meta data super block as dirty

    :param struct drbd_device \*device:
        DRBD device.

    :param unsigned int line:
        *undescribed*

    :param const char \*func:
        *undescribed*

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

    :param struct drbd_device \*device:
        DRBD device.

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

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_bmio_set_n_write.description`:

Description
-----------

Sets all bits in the bitmap and writes the whole bitmap to stable storage.

.. _`drbd_bmio_clear_n_write`:

drbd_bmio_clear_n_write
=======================

.. c:function:: int drbd_bmio_clear_n_write(struct drbd_device *device)

    io_fn for \ :c:func:`drbd_queue_bitmap_io`\  or \ :c:func:`drbd_bitmap_io`\ 

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_bmio_clear_n_write.description`:

Description
-----------

Clears all bits in the bitmap and writes the whole bitmap to stable storage.

.. _`drbd_queue_bitmap_io`:

drbd_queue_bitmap_io
====================

.. c:function:: void drbd_queue_bitmap_io(struct drbd_device *device, int (*io_fn)(struct drbd_device *), void (*done)(struct drbd_device *, int), char *why, enum bm_flag flags)

    Queues an IO operation on the whole bitmap

    :param struct drbd_device \*device:
        DRBD device.

    :param int (\*io_fn)(struct drbd_device \*):
        IO callback to be called when bitmap IO is possible

    :param void (\*done)(struct drbd_device \*, int):
        callback to be called after the bitmap IO was performed

    :param char \*why:
        Descriptive text of the reason for doing the IO

    :param enum bm_flag flags:
        *undescribed*

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

    :param struct drbd_device \*device:
        DRBD device.

    :param int (\*io_fn)(struct drbd_device \*):
        IO callback to be called when bitmap IO is possible

    :param char \*why:
        Descriptive text of the reason for doing the IO

    :param enum bm_flag flags:
        *undescribed*

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

    :param struct drbd_device \*device:
        device associated with the request

    :param struct drbd_interval \*i:
        the struct drbd_interval embedded in struct drbd_request or
        struct drbd_peer_request

.. This file was automatic generated / don't edit.


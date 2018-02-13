.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/dvb_vb2.h

.. _`dvb_buf_type`:

enum dvb_buf_type
=================

.. c:type:: enum dvb_buf_type

    types of Digital TV memory-mapped buffers

.. _`dvb_buf_type.definition`:

Definition
----------

.. code-block:: c

    enum dvb_buf_type {
        DVB_BUF_TYPE_CAPTURE
    };

.. _`dvb_buf_type.constants`:

Constants
---------

DVB_BUF_TYPE_CAPTURE
    buffer is filled by the Kernel,
    with a received Digital TV stream

.. _`dvb_vb2_states`:

enum dvb_vb2_states
===================

.. c:type:: enum dvb_vb2_states

    states to control VB2 state machine

.. _`dvb_vb2_states.definition`:

Definition
----------

.. code-block:: c

    enum dvb_vb2_states {
        DVB_VB2_STATE_NONE,
        DVB_VB2_STATE_INIT,
        DVB_VB2_STATE_REQBUFS,
        DVB_VB2_STATE_STREAMON
    };

.. _`dvb_vb2_states.constants`:

Constants
---------

DVB_VB2_STATE_NONE
    VB2 engine not initialized yet, init failed or VB2 was released.

DVB_VB2_STATE_INIT
    VB2 engine initialized.

DVB_VB2_STATE_REQBUFS
    Buffers were requested

DVB_VB2_STATE_STREAMON
    VB2 is streaming. Callers should not check it directly. Instead,
    they should use \ :c:func:`dvb_vb2_is_streaming`\ .

.. _`dvb_vb2_states.note`:

Note
----


Callers should not touch at the state machine directly. This
is handled inside dvb_vb2.c.

.. _`dvb_buffer`:

struct dvb_buffer
=================

.. c:type:: struct dvb_buffer

    video buffer information for v4l2.

.. _`dvb_buffer.definition`:

Definition
----------

.. code-block:: c

    struct dvb_buffer {
        struct vb2_buffer vb;
        struct list_head list;
    }

.. _`dvb_buffer.members`:

Members
-------

vb
    embedded struct \ :c:type:`struct vb2_buffer <vb2_buffer>`\ .

list
    list of \ :c:type:`struct dvb_buffer <dvb_buffer>`\ .

.. _`dvb_vb2_ctx`:

struct dvb_vb2_ctx
==================

.. c:type:: struct dvb_vb2_ctx

    control struct for VB2 handler

.. _`dvb_vb2_ctx.definition`:

Definition
----------

.. code-block:: c

    struct dvb_vb2_ctx {
        struct vb2_queue vb_q;
        struct mutex mutex;
        spinlock_t slock;
        struct list_head dvb_q;
        struct dvb_buffer *buf;
        int offset;
        int remain;
        int state;
        int buf_siz;
        int buf_cnt;
        int nonblocking;
        char name[DVB_VB2_NAME_MAX + 1];
    }

.. _`dvb_vb2_ctx.members`:

Members
-------

vb_q
    pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

mutex
    mutex to serialize vb2 operations. Used by
    vb2 core \ ``wait_prepare``\  and \ ``wait_finish``\  operations.

slock
    spin lock used to protect buffer filling at dvb_vb2.c.

dvb_q
    List of buffers that are not filled yet.

buf
    Pointer to the buffer that are currently being filled.

offset
    index to the next position at the \ ``buf``\  to be filled.

remain
    How many bytes are left to be filled at \ ``buf``\ .

state
    bitmask of buffer states as defined by \ :c:type:`enum dvb_vb2_states <dvb_vb2_states>`\ .

buf_siz
    size of each VB2 buffer.

buf_cnt
    number of VB2 buffers.

nonblocking
    If different than zero, device is operating on non-blocking
    mode.

name
    name of the device type. Currently, it can either be
    "dvr" or "demux_filter".

.. _`dvb_vb2_init`:

dvb_vb2_init
============

.. c:function:: int dvb_vb2_init(struct dvb_vb2_ctx *ctx, const char *name, int non_blocking)

    initializes VB2 handler

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param const char \*name:
        name for the VB2 handler

    :param int non_blocking:
        if not zero, it means that the device is at non-blocking mode

.. _`dvb_vb2_release`:

dvb_vb2_release
===============

.. c:function:: int dvb_vb2_release(struct dvb_vb2_ctx *ctx)

    Releases the VB2 handler allocated resources and put \ ``ctx``\  at DVB_VB2_STATE_NONE state.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

.. _`dvb_vb2_is_streaming`:

dvb_vb2_is_streaming
====================

.. c:function:: int dvb_vb2_is_streaming(struct dvb_vb2_ctx *ctx)

    checks if the VB2 handler is streaming

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

.. _`dvb_vb2_is_streaming.return`:

Return
------

0 if not streaming, 1 otherwise.

.. _`dvb_vb2_fill_buffer`:

dvb_vb2_fill_buffer
===================

.. c:function:: int dvb_vb2_fill_buffer(struct dvb_vb2_ctx *ctx, const unsigned char *src, int len)

    fills a VB2 buffer

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param const unsigned char \*src:
        place where the data is stored

    :param int len:
        number of bytes to be copied from \ ``src``\ 

.. _`dvb_vb2_poll`:

dvb_vb2_poll
============

.. c:function:: __poll_t dvb_vb2_poll(struct dvb_vb2_ctx *ctx, struct file *file, poll_table *wait)

    Wrapper to \ :c:func:`vb2_core_streamon`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct file \*file:
        &struct file argument passed to the poll
        file operation handler.

    :param poll_table \*wait:
        &poll_table wait argument passed to the poll
        file operation handler.

.. _`dvb_vb2_poll.description`:

Description
-----------

Implements poll \ :c:func:`syscall`\  logic.

.. _`dvb_vb2_stream_on`:

dvb_vb2_stream_on
=================

.. c:function:: int dvb_vb2_stream_on(struct dvb_vb2_ctx *ctx)

    Wrapper to \ :c:func:`vb2_core_streamon`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

.. _`dvb_vb2_stream_on.description`:

Description
-----------

Starts dvb streaming

.. _`dvb_vb2_stream_off`:

dvb_vb2_stream_off
==================

.. c:function:: int dvb_vb2_stream_off(struct dvb_vb2_ctx *ctx)

    Wrapper to \ :c:func:`vb2_core_streamoff`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

.. _`dvb_vb2_stream_off.description`:

Description
-----------

Stops dvb streaming

.. _`dvb_vb2_reqbufs`:

dvb_vb2_reqbufs
===============

.. c:function:: int dvb_vb2_reqbufs(struct dvb_vb2_ctx *ctx, struct dmx_requestbuffers *req)

    Wrapper to \ :c:func:`vb2_core_reqbufs`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct dmx_requestbuffers \*req:
        &struct dmx_requestbuffers passed from userspace in
        order to handle \ :c:type:`struct DMX_REQBUFS <DMX_REQBUFS>`\ .

.. _`dvb_vb2_reqbufs.description`:

Description
-----------

Initiate streaming by requesting a number of buffers. Also used to
free previously requested buffers, is ``req->count`` is zero.

.. _`dvb_vb2_querybuf`:

dvb_vb2_querybuf
================

.. c:function:: int dvb_vb2_querybuf(struct dvb_vb2_ctx *ctx, struct dmx_buffer *b)

    Wrapper to \ :c:func:`vb2_core_querybuf`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct dmx_buffer \*b:
        &struct dmx_buffer passed from userspace in
        order to handle \ :c:type:`struct DMX_QUERYBUF <DMX_QUERYBUF>`\ .

.. _`dvb_vb2_querybuf.description`:

Description
-----------



.. _`dvb_vb2_expbuf`:

dvb_vb2_expbuf
==============

.. c:function:: int dvb_vb2_expbuf(struct dvb_vb2_ctx *ctx, struct dmx_exportbuffer *exp)

    Wrapper to \ :c:func:`vb2_core_expbuf`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct dmx_exportbuffer \*exp:
        &struct dmx_exportbuffer passed from userspace in
        order to handle \ :c:type:`struct DMX_EXPBUF <DMX_EXPBUF>`\ .

.. _`dvb_vb2_expbuf.description`:

Description
-----------

Export a buffer as a file descriptor.

.. _`dvb_vb2_qbuf`:

dvb_vb2_qbuf
============

.. c:function:: int dvb_vb2_qbuf(struct dvb_vb2_ctx *ctx, struct dmx_buffer *b)

    Wrapper to \ :c:func:`vb2_core_qbuf`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct dmx_buffer \*b:
        &struct dmx_buffer passed from userspace in
        order to handle \ :c:type:`struct DMX_QBUF <DMX_QBUF>`\ .

.. _`dvb_vb2_qbuf.description`:

Description
-----------

Queue a Digital TV buffer as requested by userspace

.. _`dvb_vb2_dqbuf`:

dvb_vb2_dqbuf
=============

.. c:function:: int dvb_vb2_dqbuf(struct dvb_vb2_ctx *ctx, struct dmx_buffer *b)

    Wrapper to \ :c:func:`vb2_core_dqbuf`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct dmx_buffer \*b:
        &struct dmx_buffer passed from userspace in
        order to handle \ :c:type:`struct DMX_DQBUF <DMX_DQBUF>`\ .

.. _`dvb_vb2_dqbuf.description`:

Description
-----------

Dequeue a Digital TV buffer to the userspace

.. _`dvb_vb2_mmap`:

dvb_vb2_mmap
============

.. c:function:: int dvb_vb2_mmap(struct dvb_vb2_ctx *ctx, struct vm_area_struct *vma)

    Wrapper to \ :c:func:`vb2_mmap`\  for Digital TV buffer handling.

    :param struct dvb_vb2_ctx \*ctx:
        control struct for VB2 handler

    :param struct vm_area_struct \*vma:
        pointer to \ :c:type:`struct vm_area_struct <vm_area_struct>`\  with the vma passed
        to the mmap file operation handler in the driver.

.. _`dvb_vb2_mmap.description`:

Description
-----------

map Digital TV video buffers into application address space.

.. This file was automatic generated / don't edit.


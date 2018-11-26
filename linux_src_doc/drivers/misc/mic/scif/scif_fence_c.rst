.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_fence.c

.. _`scif_recv_mark`:

scif_recv_mark
==============

.. c:function:: void scif_recv_mark(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_MARK request

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_mark.description`:

Description
-----------

The peer has requested a mark.

.. _`scif_recv_mark_resp`:

scif_recv_mark_resp
===================

.. c:function:: void scif_recv_mark_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_MARK_(N)ACK messages.

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_mark_resp.description`:

Description
-----------

The peer has responded to a SCIF_MARK message.

.. _`scif_recv_wait`:

scif_recv_wait
==============

.. c:function:: void scif_recv_wait(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_WAIT request

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_wait.description`:

Description
-----------

The peer has requested waiting on a fence.

.. _`scif_recv_wait_resp`:

scif_recv_wait_resp
===================

.. c:function:: void scif_recv_wait_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_WAIT_(N)ACK messages.

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_wait_resp.description`:

Description
-----------

The peer has responded to a SCIF_WAIT message.

.. _`scif_recv_sig_local`:

scif_recv_sig_local
===================

.. c:function:: void scif_recv_sig_local(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_SIG_LOCAL request

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_sig_local.description`:

Description
-----------

The peer has requested a signal on a local offset.

.. _`scif_recv_sig_remote`:

scif_recv_sig_remote
====================

.. c:function:: void scif_recv_sig_remote(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_SIGNAL_REMOTE request

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_sig_remote.description`:

Description
-----------

The peer has requested a signal on a remote offset.

.. _`scif_recv_sig_resp`:

scif_recv_sig_resp
==================

.. c:function:: void scif_recv_sig_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_SIG_(N)ACK messages.

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_recv_sig_resp.description`:

Description
-----------

The peer has responded to a signal request.

.. _`scif_rma_handle_remote_fences`:

scif_rma_handle_remote_fences
=============================

.. c:function:: void scif_rma_handle_remote_fences( void)

    :param void:
        no arguments
    :type void: 

.. _`scif_rma_handle_remote_fences.description`:

Description
-----------

This routine services remote fence requests.

.. _`scif_send_fence_mark`:

scif_send_fence_mark
====================

.. c:function:: int scif_send_fence_mark(scif_epd_t epd, int *out_mark)

    :param epd:
        end point descriptor.
    :type epd: scif_epd_t

    :param out_mark:
        Output DMA mark reported by peer.
    :type out_mark: int \*

.. _`scif_send_fence_mark.description`:

Description
-----------

Send a remote fence mark request.

.. _`scif_send_fence_wait`:

scif_send_fence_wait
====================

.. c:function:: int scif_send_fence_wait(scif_epd_t epd, int mark)

    :param epd:
        end point descriptor.
    :type epd: scif_epd_t

    :param mark:
        DMA mark to wait for.
    :type mark: int

.. _`scif_send_fence_wait.description`:

Description
-----------

Send a remote fence wait request.

.. _`scif_send_fence_signal`:

scif_send_fence_signal
======================

.. c:function:: int scif_send_fence_signal(scif_epd_t epd, off_t roff, u64 rval, off_t loff, u64 lval, int flags)

    \ ``epd``\  - endpoint descriptor \ ``loff``\  - local offset \ ``lval``\  - local value to write to loffset \ ``roff``\  - remote offset \ ``rval``\  - remote value to write to roffset \ ``flags``\  - flags

    :param epd:
        *undescribed*
    :type epd: scif_epd_t

    :param roff:
        *undescribed*
    :type roff: off_t

    :param rval:
        *undescribed*
    :type rval: u64

    :param loff:
        *undescribed*
    :type loff: off_t

    :param lval:
        *undescribed*
    :type lval: u64

    :param flags:
        *undescribed*
    :type flags: int

.. _`scif_send_fence_signal.description`:

Description
-----------

Sends a remote fence signal request

.. This file was automatic generated / don't edit.


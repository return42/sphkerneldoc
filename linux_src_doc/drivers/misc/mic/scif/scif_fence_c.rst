.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_fence.c

.. _`scif_recv_mark`:

scif_recv_mark
==============

.. c:function:: void scif_recv_mark(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_MARK request

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_mark.description`:

Description
-----------

The peer has requested a mark.

.. _`scif_recv_mark_resp`:

scif_recv_mark_resp
===================

.. c:function:: void scif_recv_mark_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_MARK_(N)ACK messages.

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_mark_resp.description`:

Description
-----------

The peer has responded to a SCIF_MARK message.

.. _`scif_recv_wait`:

scif_recv_wait
==============

.. c:function:: void scif_recv_wait(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_WAIT request

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_wait.description`:

Description
-----------

The peer has requested waiting on a fence.

.. _`scif_recv_wait_resp`:

scif_recv_wait_resp
===================

.. c:function:: void scif_recv_wait_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_WAIT_(N)ACK messages.

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_wait_resp.description`:

Description
-----------

The peer has responded to a SCIF_WAIT message.

.. _`scif_recv_sig_local`:

scif_recv_sig_local
===================

.. c:function:: void scif_recv_sig_local(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_SIG_LOCAL request

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_sig_local.description`:

Description
-----------

The peer has requested a signal on a local offset.

.. _`scif_recv_sig_remote`:

scif_recv_sig_remote
====================

.. c:function:: void scif_recv_sig_remote(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_SIGNAL_REMOTE request

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_sig_remote.description`:

Description
-----------

The peer has requested a signal on a remote offset.

.. _`scif_recv_sig_resp`:

scif_recv_sig_resp
==================

.. c:function:: void scif_recv_sig_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Handle SCIF_SIG_(N)ACK messages.

    :param struct scif_dev \*scifdev:
        *undescribed*

    :param struct scifmsg \*msg:
        Interrupt message

.. _`scif_recv_sig_resp.description`:

Description
-----------

The peer has responded to a signal request.

.. _`scif_rma_handle_remote_fences`:

scif_rma_handle_remote_fences
=============================

.. c:function:: void scif_rma_handle_remote_fences( void)

    :param  void:
        no arguments

.. _`scif_rma_handle_remote_fences.description`:

Description
-----------

This routine services remote fence requests.

.. _`scif_send_fence_mark`:

scif_send_fence_mark
====================

.. c:function:: int scif_send_fence_mark(scif_epd_t epd, int *out_mark)

    :param scif_epd_t epd:
        end point descriptor.

    :param int \*out_mark:
        Output DMA mark reported by peer.

.. _`scif_send_fence_mark.description`:

Description
-----------

Send a remote fence mark request.

.. _`scif_send_fence_wait`:

scif_send_fence_wait
====================

.. c:function:: int scif_send_fence_wait(scif_epd_t epd, int mark)

    :param scif_epd_t epd:
        end point descriptor.

    :param int mark:
        DMA mark to wait for.

.. _`scif_send_fence_wait.description`:

Description
-----------

Send a remote fence wait request.

.. _`scif_send_fence_signal`:

scif_send_fence_signal
======================

.. c:function:: int scif_send_fence_signal(scif_epd_t epd, off_t roff, u64 rval, off_t loff, u64 lval, int flags)

    \ ``epd``\  - endpoint descriptor \ ``loff``\  - local offset \ ``lval``\  - local value to write to loffset \ ``roff``\  - remote offset \ ``rval``\  - remote value to write to roffset \ ``flags``\  - flags

    :param scif_epd_t epd:
        *undescribed*

    :param off_t roff:
        *undescribed*

    :param u64 rval:
        *undescribed*

    :param off_t loff:
        *undescribed*

    :param u64 lval:
        *undescribed*

    :param int flags:
        *undescribed*

.. _`scif_send_fence_signal.description`:

Description
-----------

Sends a remote fence signal request

.. This file was automatic generated / don't edit.


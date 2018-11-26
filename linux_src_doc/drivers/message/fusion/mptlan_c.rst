.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/message/fusion/mptlan.c

.. _`lan_reply`:

lan_reply
=========

.. c:function:: int lan_reply(MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf, MPT_FRAME_HDR *reply)

    Handle all data sent from the hardware.

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param mf:
        Pointer to original MPT request frame (NULL if TurboReply)
    :type mf: MPT_FRAME_HDR \*

    :param reply:
        Pointer to MPT reply frame
    :type reply: MPT_FRAME_HDR \*

.. _`lan_reply.description`:

Description
-----------

Returns 1 indicating original alloc'd request frame ptr
should be freed, or 0 if it shouldn't.

.. This file was automatic generated / don't edit.


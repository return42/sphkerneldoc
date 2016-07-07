.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/message/fusion/mptlan.c

.. _`lan_reply`:

lan_reply
=========

.. c:function:: int lan_reply(MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf, MPT_FRAME_HDR *reply)

    Handle all data sent from the hardware.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param MPT_FRAME_HDR \*mf:
        Pointer to original MPT request frame (NULL if TurboReply)

    :param MPT_FRAME_HDR \*reply:
        Pointer to MPT reply frame

.. _`lan_reply.description`:

Description
-----------

Returns 1 indicating original alloc'd request frame ptr
should be freed, or 0 if it shouldn't.

.. This file was automatic generated / don't edit.


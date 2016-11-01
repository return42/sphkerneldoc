.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorbus/visorchannel.c

.. _`visorchannel_get_uuid`:

visorchannel_get_uuid
=====================

.. c:function:: uuid_le visorchannel_get_uuid(struct visorchannel *channel)

    queries the UUID of the designated channel

    :param struct visorchannel \*channel:
        the channel to query

.. _`visorchannel_get_uuid.return`:

Return
------

the UUID of the provided channel

.. _`visorchannel_signalremove`:

visorchannel_signalremove
=========================

.. c:function:: int visorchannel_signalremove(struct visorchannel *channel, u32 queue, void *msg)

    removes a message from the designated channel/queue

    :param struct visorchannel \*channel:
        the channel the message will be removed from

    :param u32 queue:
        the queue the message will be removed from

    :param void \*msg:
        the message to remove

.. _`visorchannel_signalremove.return`:

Return
------

integer error code indicating the status of the removal

.. _`visorchannel_signalempty`:

visorchannel_signalempty
========================

.. c:function:: bool visorchannel_signalempty(struct visorchannel *channel, u32 queue)

    checks if the designated channel/queue contains any messages

    :param struct visorchannel \*channel:
        the channel to query

    :param u32 queue:
        the queue in the channel to query

.. _`visorchannel_signalempty.return`:

Return
------

boolean indicating whether any messages in the designated
channel/queue are present

.. _`visorchannel_create_guts`:

visorchannel_create_guts
========================

.. c:function:: struct visorchannel *visorchannel_create_guts(u64 physaddr, unsigned long channel_bytes, gfp_t gfp, uuid_le guid, bool needs_lock)

    creates the struct visorchannel abstraction for a data area in memory, but does NOT modify this data area

    :param u64 physaddr:
        physical address of start of channel

    :param unsigned long channel_bytes:
        size of the channel in bytes; this may 0 if the channel has
        already been initialized in memory (which is true for all
        channels provided to guest environments by the s-Par
        back-end), in which case the actual channel size will be
        read from the channel header in memory

    :param gfp_t gfp:
        gfp_t to use when allocating memory for the data struct

    :param uuid_le guid:
        uuid that identifies channel type; this may 0 if the channel
        has already been initialized in memory (which is true for all
        channels provided to guest environments by the s-Par
        back-end), in which case the actual channel guid will be
        read from the channel header in memory

    :param bool needs_lock:
        must specify true if you have multiple threads of execution
        that will be calling visorchannel methods of this
        visorchannel at the same time

.. _`visorchannel_create_guts.return`:

Return
------

pointer to visorchannel that was created if successful,
otherwise NULL

.. _`visorchannel_signalinsert`:

visorchannel_signalinsert
=========================

.. c:function:: int visorchannel_signalinsert(struct visorchannel *channel, u32 queue, void *msg)

    inserts a message into the designated channel/queue

    :param struct visorchannel \*channel:
        the channel the message will be added to

    :param u32 queue:
        the queue the message will be added to

    :param void \*msg:
        the message to insert

.. _`visorchannel_signalinsert.return`:

Return
------

integer error code indicating the status of the insertion

.. This file was automatic generated / don't edit.


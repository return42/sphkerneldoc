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


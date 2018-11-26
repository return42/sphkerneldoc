.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_epd.c

.. _`scif_cnctreq`:

scif_cnctreq
============

.. c:function:: void scif_cnctreq(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CNCT_REQ interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_cnctreq.description`:

Description
-----------

This message is initiated by the remote node to request a connection
to the local node.  This function looks for an end point in the
listen state on the requested port id.

If it finds a listening port it places the connect request on the
listening end points queue and wakes up any pending accept calls.

If it does not find a listening end point it sends a connection
reject message to the remote node.

.. _`scif_cnctgnt`:

scif_cnctgnt
============

.. c:function:: void scif_cnctgnt(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CNCT_GNT interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_cnctgnt.description`:

Description
-----------

An \ :c:func:`accept`\  on the remote node has occurred and sent this message
to indicate success.  Place the end point in the MAPPING state and
save the remote nodes memory information.  Then wake up the connect
request so it can finish.

.. _`scif_cnctgnt_ack`:

scif_cnctgnt_ack
================

.. c:function:: void scif_cnctgnt_ack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CNCT_GNTACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_cnctgnt_ack.description`:

Description
-----------

The remote connection request has finished mapping the local memory.
Place the connection in the connected state and wake up the pending
\ :c:func:`accept`\  call.

.. _`scif_cnctgnt_nack`:

scif_cnctgnt_nack
=================

.. c:function:: void scif_cnctgnt_nack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CNCT_GNTNACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_cnctgnt_nack.description`:

Description
-----------

The remote connection request failed to map the local memory it was sent.
Place the end point in the CLOSING state to indicate it and wake up
the pending \ :c:func:`accept`\ ;

.. _`scif_cnctrej`:

scif_cnctrej
============

.. c:function:: void scif_cnctrej(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CNCT_REJ interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_cnctrej.description`:

Description
-----------

The remote end has rejected the connection request.  Set the end
point back to the bound state and wake up the pending \ :c:func:`connect`\ .

.. _`scif_discnct`:

scif_discnct
============

.. c:function:: void scif_discnct(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_DISCNCT interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_discnct.description`:

Description
-----------

The remote node has indicated \ :c:func:`close`\  has been called on its end
point.  Remove the local end point from the connected list, set its
state to disconnected and ensure accesses to the remote node are
shutdown.

When all accesses to the remote end have completed then send a
DISCNT_ACK to indicate it can remove its resources and complete
the close routine.

.. _`scif_discnt_ack`:

scif_discnt_ack
===============

.. c:function:: void scif_discnt_ack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_DISCNT_ACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_discnt_ack.description`:

Description
-----------

Remote side has indicated it has not more references to local resources

.. _`scif_clientsend`:

scif_clientsend
===============

.. c:function:: void scif_clientsend(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CLIENT_SEND interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_clientsend.description`:

Description
-----------

Remote side is confirming send or receive interrupt handling is complete.

.. _`scif_clientrcvd`:

scif_clientrcvd
===============

.. c:function:: void scif_clientrcvd(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_CLIENT_RCVD interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_clientrcvd.description`:

Description
-----------

Remote side is confirming send or receive interrupt handling is complete.

.. This file was automatic generated / don't edit.


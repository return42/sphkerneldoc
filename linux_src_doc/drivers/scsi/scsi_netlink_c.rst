.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_netlink.c

.. _`scsi_nl_rcv_msg`:

scsi_nl_rcv_msg
===============

.. c:function:: void scsi_nl_rcv_msg(struct sk_buff *skb)

    Receive message handler.

    :param struct sk_buff \*skb:
        socket receive buffer

.. _`scsi_nl_rcv_msg.description`:

Description
-----------

Extracts message from a receive buffer.
   Validates message header and calls appropriate transport message handler

.. _`scsi_netlink_init`:

scsi_netlink_init
=================

.. c:function:: void scsi_netlink_init( void)

    Called by SCSI subsystem to initialize the SCSI transport netlink interface

    :param  void:
        no arguments

.. _`scsi_netlink_exit`:

scsi_netlink_exit
=================

.. c:function:: void scsi_netlink_exit( void)

    Called by SCSI subsystem to disable the SCSI transport netlink interface

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


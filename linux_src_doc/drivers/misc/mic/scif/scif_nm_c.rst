.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_nm.c

.. _`scif_invalidate_ep`:

scif_invalidate_ep
==================

.. c:function:: void scif_invalidate_ep(int node)

    Set state for all connected endpoints to disconnected and wake up all send/recv waitqueues

    :param node:
        *undescribed*
    :type node: int

.. _`scif_disconnect_node`:

scif_disconnect_node
====================

.. c:function:: void scif_disconnect_node(u32 node_id, bool mgmt_initiated)

    :param node_id:
        source node id.
    :type node_id: u32

    :param mgmt_initiated:
        Disconnection initiated from the mgmt node
    :type mgmt_initiated: bool

.. _`scif_disconnect_node.description`:

Description
-----------

Disconnect a node from the scif network.

.. This file was automatic generated / don't edit.


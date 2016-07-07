.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_nm.c

.. _`scif_invalidate_ep`:

scif_invalidate_ep
==================

.. c:function:: void scif_invalidate_ep(int node)

    Set state for all connected endpoints to disconnected and wake up all send/recv waitqueues

    :param int node:
        *undescribed*

.. _`scif_disconnect_node`:

scif_disconnect_node
====================

.. c:function:: void scif_disconnect_node(u32 node_id, bool mgmt_initiated)

    :param u32 node_id:
        source node id.

    :param bool mgmt_initiated:
        Disconnection initiated from the mgmt node

.. _`scif_disconnect_node.description`:

Description
-----------

Disconnect a node from the scif network.

.. This file was automatic generated / don't edit.


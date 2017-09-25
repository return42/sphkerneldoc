.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/remote_node_table.h

.. _`sci_remote_node_table`:

struct sci_remote_node_table
============================

.. c:type:: struct sci_remote_node_table


.. _`sci_remote_node_table.definition`:

Definition
----------

.. code-block:: c

    struct sci_remote_node_table {
        u16 available_nodes_array_size;
        u16 group_array_size;
        u32 available_remote_nodes[(SCI_MAX_REMOTE_DEVICES / SCIC_SDS_REMOTE_NODES_PER_DWORD) + ((SCI_MAX_REMOTE_DEVICES % SCIC_SDS_REMOTE_NODES_PER_DWORD) != 0)];
        u32 remote_node_groups[SCU_STP_REMOTE_NODE_COUNT][(SCI_MAX_REMOTE_DEVICES / (32 * SCU_STP_REMOTE_NODE_COUNT)) + ((SCI_MAX_REMOTE_DEVICES % (32 * SCU_STP_REMOTE_NODE_COUNT)) != 0)];
    }

.. _`sci_remote_node_table.members`:

Members
-------

available_nodes_array_size
    *undescribed*

group_array_size
    *undescribed*

available_remote_nodes
    *undescribed*

remote_node_groups
    *undescribed*

.. _`sci_remote_node_table.description`:

Description
-----------



.. This file was automatic generated / don't edit.


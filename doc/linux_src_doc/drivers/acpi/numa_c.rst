.. -*- coding: utf-8; mode: rst -*-

======
numa.c
======


.. _`acpi_map_pxm_to_online_node`:

acpi_map_pxm_to_online_node
===========================

.. c:function:: int acpi_map_pxm_to_online_node (int pxm)

    Map proximity ID to online node

    :param int pxm:
        ACPI proximity ID



.. _`acpi_map_pxm_to_online_node.description`:

Description
-----------

This is similar to :c:func:`acpi_map_pxm_to_node`, but always returns an online
node.  When the mapped node from a given proximity ID is offline, it
looks up the node distance table and returns the nearest online node.

ACPI device drivers, which are called after the NUMA initialization has
completed in the kernel, can call this interface to obtain their device
NUMA topology from ACPI tables.  Such drivers do not have to deal with
offline nodes.  A node may be offline when a device proximity ID is
unique, SRAT memory entry does not exist, or NUMA is disabled, ex.
"numa=off" on x86.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/mm/numa.c

.. _`numa_add_memblk`:

numa_add_memblk
===============

.. c:function:: int numa_add_memblk(int nid, u64 start, u64 end)

    Set node id to memblk

    :param nid:
        NUMA node ID of the new memblk
    :type nid: int

    :param start:
        Start address of the new memblk
    :type start: u64

    :param end:
        End address of the new memblk
    :type end: u64

.. _`numa_add_memblk.return`:

Return
------

0 on success, -errno on failure.

.. _`setup_node_data`:

setup_node_data
===============

.. c:function:: void setup_node_data(int nid, u64 start_pfn, u64 end_pfn)

    :param nid:
        *undescribed*
    :type nid: int

    :param start_pfn:
        *undescribed*
    :type start_pfn: u64

    :param end_pfn:
        *undescribed*
    :type end_pfn: u64

.. _`numa_free_distance`:

numa_free_distance
==================

.. c:function:: void numa_free_distance( void)

    :param void:
        no arguments
    :type void: 

.. _`numa_free_distance.description`:

Description
-----------

The current table is freed.

.. _`numa_set_distance`:

numa_set_distance
=================

.. c:function:: void numa_set_distance(int from, int to, int distance)

    Set inter node NUMA distance from node to node.

    :param from:
        the 'from' node to set distance
    :type from: int

    :param to:
        the 'to'  node to set distance
    :type to: int

    :param distance:
        NUMA distance
    :type distance: int

.. _`numa_set_distance.description`:

Description
-----------

Set the distance from node \ ``from``\  to \ ``to``\  to \ ``distance``\ .
If distance table doesn't exist, a warning is printed.

If \ ``from``\  or \ ``to``\  is higher than the highest known node or lower than zero
or \ ``distance``\  doesn't make sense, the call is ignored.

.. _`__node_distance`:

\__node_distance
================

.. c:function:: int __node_distance(int from, int to)

    :param from:
        *undescribed*
    :type from: int

    :param to:
        *undescribed*
    :type to: int

.. _`dummy_numa_init`:

dummy_numa_init
===============

.. c:function:: int dummy_numa_init( void)

    Fallback dummy NUMA init

    :param void:
        no arguments
    :type void: 

.. _`dummy_numa_init.description`:

Description
-----------

Used if there's no underlying NUMA architecture, NUMA initialization
fails, or NUMA is disabled on the command line.

Must online at least one node (node 0) and add memory blocks that cover all
allowed memory. It is unlikely that this function fails.

.. _`arm64_numa_init`:

arm64_numa_init
===============

.. c:function:: void arm64_numa_init( void)

    Initialize NUMA

    :param void:
        no arguments
    :type void: 

.. _`arm64_numa_init.description`:

Description
-----------

Try each configured NUMA initialization method until one succeeds.  The
last fallback is dummy single node config encomapssing whole memory.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/mm/numa.c

.. _`numa_add_memblk`:

numa_add_memblk
===============

.. c:function:: int numa_add_memblk(int nid, u64 start, u64 end)

    Set node id to memblk

    :param int nid:
        NUMA node ID of the new memblk

    :param u64 start:
        Start address of the new memblk

    :param u64 end:
        End address of the new memblk

.. _`numa_add_memblk.return`:

Return
------

0 on success, -errno on failure.

.. _`setup_node_data`:

setup_node_data
===============

.. c:function:: void setup_node_data(int nid, u64 start_pfn, u64 end_pfn)

    :param int nid:
        *undescribed*

    :param u64 start_pfn:
        *undescribed*

    :param u64 end_pfn:
        *undescribed*

.. _`numa_free_distance`:

numa_free_distance
==================

.. c:function:: void numa_free_distance( void)

    :param  void:
        no arguments

.. _`numa_free_distance.description`:

Description
-----------

The current table is freed.

.. _`numa_set_distance`:

numa_set_distance
=================

.. c:function:: void numa_set_distance(int from, int to, int distance)

    Set inter node NUMA distance from node to node.

    :param int from:
        the 'from' node to set distance

    :param int to:
        the 'to'  node to set distance

    :param int distance:
        NUMA distance

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

    :param int from:
        *undescribed*

    :param int to:
        *undescribed*

.. _`dummy_numa_init`:

dummy_numa_init
===============

.. c:function:: int dummy_numa_init( void)

    Fallback dummy NUMA init

    :param  void:
        no arguments

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

    :param  void:
        no arguments

.. _`arm64_numa_init.description`:

Description
-----------

Try each configured NUMA initialization method until one succeeds.  The
last fallback is dummy single node config encomapssing whole memory.

.. This file was automatic generated / don't edit.


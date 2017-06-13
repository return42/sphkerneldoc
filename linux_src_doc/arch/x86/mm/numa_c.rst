.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/numa.c

.. _`numa_remove_memblk_from`:

numa_remove_memblk_from
=======================

.. c:function:: void numa_remove_memblk_from(int idx, struct numa_meminfo *mi)

    Remove one numa_memblk from a numa_meminfo

    :param int idx:
        Index of memblk to remove

    :param struct numa_meminfo \*mi:
        numa_meminfo to remove memblk from

.. _`numa_remove_memblk_from.description`:

Description
-----------

Remove \ ``idx``\ 'th numa_memblk from \ ``mi``\  by shifting \ ``mi``\ ->blk[] and
decrementing \ ``mi``\ ->nr_blks.

.. _`numa_add_memblk`:

numa_add_memblk
===============

.. c:function:: int numa_add_memblk(int nid, u64 start, u64 end)

    Add one numa_memblk to numa_meminfo

    :param int nid:
        NUMA node ID of the new memblk

    :param u64 start:
        Start address of the new memblk

    :param u64 end:
        End address of the new memblk

.. _`numa_add_memblk.description`:

Description
-----------

Add a new memblk to the default numa_meminfo.

.. _`numa_add_memblk.return`:

Return
------

0 on success, -errno on failure.

.. _`numa_cleanup_meminfo`:

numa_cleanup_meminfo
====================

.. c:function:: int numa_cleanup_meminfo(struct numa_meminfo *mi)

    Cleanup a numa_meminfo

    :param struct numa_meminfo \*mi:
        numa_meminfo to clean up

.. _`numa_cleanup_meminfo.description`:

Description
-----------

Sanitize \ ``mi``\  by merging and removing unnecessary memblks.  Also check for
conflicts and clear unused memblks.

.. _`numa_cleanup_meminfo.return`:

Return
------

0 on success, -errno on failure.

.. _`numa_reset_distance`:

numa_reset_distance
===================

.. c:function:: void numa_reset_distance( void)

    Reset NUMA distance table

    :param  void:
        no arguments

.. _`numa_reset_distance.description`:

Description
-----------

The current table is freed.  The next \ :c:func:`numa_set_distance`\  call will
create a new one.

.. _`numa_set_distance`:

numa_set_distance
=================

.. c:function:: void numa_set_distance(int from, int to, int distance)

    Set NUMA distance from one NUMA to another

    :param int from:
        the 'from' node to set distance

    :param int to:
        the 'to'  node to set distance

    :param int distance:
        NUMA distance

.. _`numa_set_distance.description`:

Description
-----------

Set the distance from node \ ``from``\  to \ ``to``\  to \ ``distance``\ .  If distance table
doesn't exist, one which is large enough to accommodate all the currently
known nodes will be created.

If such table cannot be allocated, a warning is printed and further
calls are ignored until the distance table is reset with
\ :c:func:`numa_reset_distance`\ .

If \ ``from``\  or \ ``to``\  is higher than the highest known node or lower than zero
at the time of table creation or \ ``distance``\  doesn't make sense, the call
is ignored.
This is to allow simplification of specific NUMA config implementations.

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

Must online at least one node and add memory blocks that cover all
allowed memory.  This function must not fail.

.. _`x86_numa_init`:

x86_numa_init
=============

.. c:function:: void x86_numa_init( void)

    Initialize NUMA

    :param  void:
        no arguments

.. _`x86_numa_init.description`:

Description
-----------

Try each configured NUMA initialization method until one succeeds.  The
last fallback is dummy single node config encomapssing whole memory and
never fails.

.. This file was automatic generated / don't edit.


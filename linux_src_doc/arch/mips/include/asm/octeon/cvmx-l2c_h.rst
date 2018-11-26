.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-l2c.h

.. _`cvmx_l2c_config_perf`:

cvmx_l2c_config_perf
====================

.. c:function:: void cvmx_l2c_config_perf(uint32_t counter, enum cvmx_l2c_event event, uint32_t clear_on_read)

    occurrences.

    :param counter:
        The counter to configure. Range 0..3.
    :type counter: uint32_t

    :param event:
        The type of L2 Cache event occurrence to count.
    :type event: enum cvmx_l2c_event

    :param clear_on_read:
        When asserted, any read of the performance counter
        clears the counter.
    :type clear_on_read: uint32_t

.. _`cvmx_l2c_config_perf.description`:

Description
-----------

\ ``note``\  The routine does not clear the counter.

.. _`cvmx_l2c_read_perf`:

cvmx_l2c_read_perf
==================

.. c:function:: uint64_t cvmx_l2c_read_perf(uint32_t counter)

    before reading, but this routine does not enforce this requirement.

    :param counter:
        The counter to configure. Range 0..3.
    :type counter: uint32_t

.. _`cvmx_l2c_read_perf.description`:

Description
-----------

Returns The current counter value.

.. _`cvmx_l2c_get_core_way_partition`:

cvmx_l2c_get_core_way_partition
===============================

.. c:function:: int cvmx_l2c_get_core_way_partition(uint32_t core)

    :param core:
        The core processor of interest.
    :type core: uint32_t

.. _`cvmx_l2c_get_core_way_partition.description`:

Description
-----------

Returns    The mask specifying the partitioning. 0 bits in mask indicates
the cache 'ways' that a core can evict from.
-1 on error

.. _`cvmx_l2c_set_core_way_partition`:

cvmx_l2c_set_core_way_partition
===============================

.. c:function:: int cvmx_l2c_set_core_way_partition(uint32_t core, uint32_t mask)

    :param core:
        The core that the partitioning applies to.
    :type core: uint32_t

    :param mask:
        The partitioning of the ways expressed as a binary
        mask. A 0 bit allows the core to evict cache lines from
        a way, while a 1 bit blocks the core from evicting any
        lines from that way. There must be at least one allowed
        way (0 bit) in the mask.
    :type mask: uint32_t

.. _`cvmx_l2c_set_core_way_partition.description`:

Description
-----------

\ ``note``\  If any ways are blocked for all cores and the HW blocks, then
those ways will never have any cache lines evicted from them.
All cores and the hardware blocks are free to read from all
ways regardless of the partitioning.

.. _`cvmx_l2c_get_hw_way_partition`:

cvmx_l2c_get_hw_way_partition
=============================

.. c:function:: int cvmx_l2c_get_hw_way_partition( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_l2c_get_hw_way_partition.description`:

Description
-----------

Returns    The mask specifying the reserved way. 0 bits in mask indicates
the cache 'ways' that a core can evict from.
-1 on error

.. _`cvmx_l2c_set_hw_way_partition`:

cvmx_l2c_set_hw_way_partition
=============================

.. c:function:: int cvmx_l2c_set_hw_way_partition(uint32_t mask)

    :param mask:
        The partitioning of the ways expressed as a binary
        mask. A 0 bit allows the core to evict cache lines from
        a way, while a 1 bit blocks the core from evicting any
        lines from that way. There must be at least one allowed
        way (0 bit) in the mask.
    :type mask: uint32_t

.. _`cvmx_l2c_set_hw_way_partition.description`:

Description
-----------

\ ``note``\  If any ways are blocked for all cores and the HW blocks, then
those ways will never have any cache lines evicted from them.
All cores and the hardware blocks are free to read from all
ways regardless of the partitioning.

.. _`cvmx_l2c_lock_line`:

cvmx_l2c_lock_line
==================

.. c:function:: int cvmx_l2c_lock_line(uint64_t addr)

    :param addr:
        physical address of line to lock
    :type addr: uint64_t

.. _`cvmx_l2c_lock_line.description`:

Description
-----------

Returns 0 on success,
1 if line not locked.

.. _`cvmx_l2c_lock_mem_region`:

cvmx_l2c_lock_mem_region
========================

.. c:function:: int cvmx_l2c_lock_mem_region(uint64_t start, uint64_t len)

    :param start:
        Physical address of the start of the region to lock
    :type start: uint64_t

    :param len:
        Length (in bytes) of region to lock
    :type len: uint64_t

.. _`cvmx_l2c_lock_mem_region.description`:

Description
-----------

Note that if not all lines can be locked, that means that all
but one of the ways (associations) available to the locking
core are locked.  Having only 1 association available for
normal caching may have a significant adverse affect on performance.
Care should be taken to ensure that enough of the L2 cache is left
unlocked to allow for normal caching of DRAM.

Returns Number of requested lines that where not locked.
0 on success (all locked)

.. _`cvmx_l2c_unlock_line`:

cvmx_l2c_unlock_line
====================

.. c:function:: int cvmx_l2c_unlock_line(uint64_t address)

    :param address:
        Physical address to unlock
    :type address: uint64_t

.. _`cvmx_l2c_unlock_line.important`:

IMPORTANT
---------

Must only be run by one core at a time due to use
of L2C debug features.
Note that this function will flush a matching but unlocked cache line.
(If address is not in L2, no lines are flushed.)

.. _`cvmx_l2c_unlock_line.returns-0`:

Returns 0
---------

line not unlocked
1: line unlocked

.. _`cvmx_l2c_unlock_mem_region`:

cvmx_l2c_unlock_mem_region
==========================

.. c:function:: int cvmx_l2c_unlock_mem_region(uint64_t start, uint64_t len)

    :param start:
        start physical address
    :type start: uint64_t

    :param len:
        length (in bytes) to unlock
    :type len: uint64_t

.. _`cvmx_l2c_unlock_mem_region.description`:

Description
-----------

Returns Number of locked lines that the call unlocked

.. _`cvmx_l2c_get_tag`:

cvmx_l2c_get_tag
================

.. c:function:: union cvmx_l2c_tag cvmx_l2c_get_tag(uint32_t association, uint32_t index)

    :param association:
        Which association to read line from
    :type association: uint32_t

    :param index:
        Which way to read from.
    :type index: uint32_t

.. _`cvmx_l2c_get_tag.description`:

Description
-----------

Returns l2c tag structure for line requested.

.. _`cvmx_l2c_address_to_index`:

cvmx_l2c_address_to_index
=========================

.. c:function:: uint32_t cvmx_l2c_address_to_index(uint64_t addr)

    :param addr:
        physical address
    :type addr: uint64_t

.. _`cvmx_l2c_address_to_index.description`:

Description
-----------

Returns L2 cache index

.. _`cvmx_l2c_flush`:

cvmx_l2c_flush
==============

.. c:function:: void cvmx_l2c_flush( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_l2c_flush.important`:

IMPORTANT
---------

Must only be run by one core at a time due to use
of L2C debug features.

.. _`cvmx_l2c_get_num_sets`:

cvmx_l2c_get_num_sets
=====================

.. c:function:: int cvmx_l2c_get_num_sets( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_l2c_get_num_sets.description`:

Description
-----------

Returns

.. _`cvmx_l2c_get_set_bits`:

cvmx_l2c_get_set_bits
=====================

.. c:function:: int cvmx_l2c_get_set_bits( void)

    Returns

    :param void:
        no arguments
    :type void: 

.. _`cvmx_l2c_get_num_assoc`:

cvmx_l2c_get_num_assoc
======================

.. c:function:: int cvmx_l2c_get_num_assoc( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_l2c_get_num_assoc.description`:

Description
-----------

Returns

.. _`cvmx_l2c_flush_line`:

cvmx_l2c_flush_line
===================

.. c:function:: void cvmx_l2c_flush_line(uint32_t assoc, uint32_t index)

    This should only be called from one core at a time, as this routine sets the core to the 'debug' core in order to flush the line.

    :param assoc:
        Association (or way) to flush
    :type assoc: uint32_t

    :param index:
        Index to flush
    :type index: uint32_t

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/region_devs.c

.. _`nd_region_to_nstype`:

nd_region_to_nstype
===================

.. c:function:: int nd_region_to_nstype(struct nd_region *nd_region)

    region to an integer namespace type

    :param nd_region:
        region-device to interrogate
    :type nd_region: struct nd_region \*

.. _`nd_region_to_nstype.description`:

Description
-----------

This is the 'nstype' attribute of a region as well, an input to the
MODALIAS for namespace devices, and bit number for a nvdimm_bus to match
namespace devices with namespace drivers.

.. _`nd_region_acquire_lane`:

nd_region_acquire_lane
======================

.. c:function:: unsigned int nd_region_acquire_lane(struct nd_region *nd_region)

    allocate and lock a lane

    :param nd_region:
        region id and number of lanes possible
    :type nd_region: struct nd_region \*

.. _`nd_region_acquire_lane.description`:

Description
-----------

A lane correlates to a BLK-data-window and/or a log slot in the BTT.
We optimize for the common case where there are 256 lanes, one
per-cpu.  For larger systems we need to lock to share lanes.  For now
this implementation assumes the cost of maintaining an allocator for
free lanes is on the order of the lock hold time, so it implements a
static lane = cpu % num_lanes mapping.

In the case of a BTT instance on top of a BLK namespace a lane may be
acquired recursively.  We lock on the first instance.

In the case of a BTT instance on top of PMEM, we only acquire a lane
for the BTT metadata updates.

.. _`nvdimm_flush`:

nvdimm_flush
============

.. c:function:: void nvdimm_flush(struct nd_region *nd_region)

    flush any posted write queues between the cpu and pmem media

    :param nd_region:
        blk or interleaved pmem region
    :type nd_region: struct nd_region \*

.. _`nvdimm_has_flush`:

nvdimm_has_flush
================

.. c:function:: int nvdimm_has_flush(struct nd_region *nd_region)

    determine write flushing requirements

    :param nd_region:
        blk or interleaved pmem region
    :type nd_region: struct nd_region \*

.. _`nvdimm_has_flush.description`:

Description
-----------

Returns 1 if writes require flushing
Returns 0 if writes do not require flushing
Returns -ENXIO if flushing capability can not be determined

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/namespace_devs.c

.. _`nd_is_uuid_unique`:

nd_is_uuid_unique
=================

.. c:function:: bool nd_is_uuid_unique(struct device *dev, u8 *uuid)

    verify that no other namespace has \ ``uuid``\ 

    :param dev:
        any device on a nvdimm_bus
    :type dev: struct device \*

    :param uuid:
        uuid to check
    :type uuid: u8 \*

.. _`shrink_dpa_allocation`:

shrink_dpa_allocation
=====================

.. c:function:: int shrink_dpa_allocation(struct nd_region *nd_region, struct nd_label_id *label_id, resource_size_t n)

    for each dimm in region free n bytes for label_id

    :param nd_region:
        the set of dimms to reclaim \ ``n``\  bytes from
    :type nd_region: struct nd_region \*

    :param label_id:
        unique identifier for the namespace consuming this dpa range
    :type label_id: struct nd_label_id \*

    :param n:
        number of bytes per-dimm to release
    :type n: resource_size_t

.. _`shrink_dpa_allocation.description`:

Description
-----------

Assumes resources are ordered.  Starting from the end try to
\ :c:func:`adjust_resource`\  the allocation to \ ``n``\ , but if \ ``n``\  is larger than the
allocation delete it and find the 'new' last allocation in the label
set.

.. _`space_valid`:

space_valid
===========

.. c:function:: void space_valid(struct nd_region *nd_region, struct nvdimm_drvdata *ndd, struct nd_label_id *label_id, struct resource *prev, struct resource *next, struct resource *exist, resource_size_t n, struct resource *valid)

    validate free dpa space against constraints

    :param nd_region:
        hosting region of the free space
    :type nd_region: struct nd_region \*

    :param ndd:
        dimm device data for debug
    :type ndd: struct nvdimm_drvdata \*

    :param label_id:
        namespace id to allocate space
    :type label_id: struct nd_label_id \*

    :param prev:
        potential allocation that precedes free space
    :type prev: struct resource \*

    :param next:
        allocation that follows the given free space range
    :type next: struct resource \*

    :param exist:
        first allocation with same id in the mapping
    :type exist: struct resource \*

    :param n:
        range that must satisfied for pmem allocations
    :type n: resource_size_t

    :param valid:
        free space range to validate
    :type valid: struct resource \*

.. _`space_valid.description`:

Description
-----------

BLK-space is valid as long as it does not precede a PMEM
allocation in a given region. PMEM-space must be contiguous
and adjacent to an existing existing allocation (if one
exists).  If reserving PMEM any space is valid.

.. _`grow_dpa_allocation`:

grow_dpa_allocation
===================

.. c:function:: int grow_dpa_allocation(struct nd_region *nd_region, struct nd_label_id *label_id, resource_size_t n)

    for each dimm allocate n bytes for \ ``label_id``\ 

    :param nd_region:
        the set of dimms to allocate \ ``n``\  more bytes from
    :type nd_region: struct nd_region \*

    :param label_id:
        unique identifier for the namespace consuming this dpa range
    :type label_id: struct nd_label_id \*

    :param n:
        number of bytes per-dimm to add to the existing allocation
    :type n: resource_size_t

.. _`grow_dpa_allocation.description`:

Description
-----------

Assumes resources are ordered.  For BLK regions, first consume
BLK-only available DPA free space, then consume PMEM-aliased DPA
space starting at the highest DPA.  For PMEM regions start
allocations from the start of an interleave set and end at the first
BLK allocation or the end of the interleave set, whichever comes
first.

.. _`namespace_update_uuid`:

namespace_update_uuid
=====================

.. c:function:: int namespace_update_uuid(struct nd_region *nd_region, struct device *dev, u8 *new_uuid, u8 **old_uuid)

    check for a unique uuid and whether we're "renaming"

    :param nd_region:
        parent region so we can updates all dimms in the set
    :type nd_region: struct nd_region \*

    :param dev:
        namespace type for generating label_id
    :type dev: struct device \*

    :param new_uuid:
        incoming uuid
    :type new_uuid: u8 \*

    :param old_uuid:
        reference to the uuid storage location in the namespace object
    :type old_uuid: u8 \*\*

.. _`create_namespace_pmem`:

create_namespace_pmem
=====================

.. c:function:: struct device *create_namespace_pmem(struct nd_region *nd_region, struct nd_namespace_index *nsindex, struct nd_namespace_label *nd_label)

    validate interleave set labelling, retrieve label0

    :param nd_region:
        region with mappings to validate
    :type nd_region: struct nd_region \*

    :param nsindex:
        *undescribed*
    :type nsindex: struct nd_namespace_index \*

    :param nd_label:
        target pmem namespace label to evaluate
    :type nd_label: struct nd_namespace_label \*

.. This file was automatic generated / don't edit.


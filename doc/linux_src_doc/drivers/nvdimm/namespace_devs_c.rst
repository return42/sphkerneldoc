.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/namespace_devs.c

.. _`nd_is_uuid_unique`:

nd_is_uuid_unique
=================

.. c:function:: bool nd_is_uuid_unique(struct device *dev, u8 *uuid)

    verify that no other namespace has \ ``uuid``\ 

    :param struct device \*dev:
        any device on a nvdimm_bus

    :param u8 \*uuid:
        uuid to check

.. _`shrink_dpa_allocation`:

shrink_dpa_allocation
=====================

.. c:function:: int shrink_dpa_allocation(struct nd_region *nd_region, struct nd_label_id *label_id, resource_size_t n)

    for each dimm in region free n bytes for label_id

    :param struct nd_region \*nd_region:
        the set of dimms to reclaim \ ``n``\  bytes from

    :param struct nd_label_id \*label_id:
        unique identifier for the namespace consuming this dpa range

    :param resource_size_t n:
        number of bytes per-dimm to release

.. _`shrink_dpa_allocation.description`:

Description
-----------

Assumes resources are ordered.  Starting from the end try to
\ :c:func:`adjust_resource`\  the allocation to \ ``n``\ , but if \ ``n``\  is larger than the
allocation delete it and find the 'new' last allocation in the label
set.

.. _`grow_dpa_allocation`:

grow_dpa_allocation
===================

.. c:function:: int grow_dpa_allocation(struct nd_region *nd_region, struct nd_label_id *label_id, resource_size_t n)

    for each dimm allocate n bytes for \ ``label_id``\ 

    :param struct nd_region \*nd_region:
        the set of dimms to allocate \ ``n``\  more bytes from

    :param struct nd_label_id \*label_id:
        unique identifier for the namespace consuming this dpa range

    :param resource_size_t n:
        number of bytes per-dimm to add to the existing allocation

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

    :param struct nd_region \*nd_region:
        parent region so we can updates all dimms in the set

    :param struct device \*dev:
        namespace type for generating label_id

    :param u8 \*new_uuid:
        incoming uuid

    :param u8 \*\*old_uuid:
        reference to the uuid storage location in the namespace object

.. _`find_pmem_label_set`:

find_pmem_label_set
===================

.. c:function:: int find_pmem_label_set(struct nd_region *nd_region, struct nd_namespace_pmem *nspm)

    validate interleave set labelling, retrieve label0

    :param struct nd_region \*nd_region:
        region with mappings to validate

    :param struct nd_namespace_pmem \*nspm:
        *undescribed*

.. This file was automatic generated / don't edit.


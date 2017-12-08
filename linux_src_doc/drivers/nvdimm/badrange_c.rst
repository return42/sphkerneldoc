.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/badrange.c

.. _`__add_badblock_range`:

__add_badblock_range
====================

.. c:function:: void __add_badblock_range(struct badblocks *bb, u64 ns_offset, u64 len)

    Convert a physical address range to bad sectors

    :param struct badblocks \*bb:
        badblocks instance to populate

    :param u64 ns_offset:
        namespace offset where the error range begins (in bytes)

    :param u64 len:
        number of bytes of badrange to be added

.. _`__add_badblock_range.description`:

Description
-----------

This assumes that the range provided with (ns_offset, len) is within
the bounds of physical addresses for this namespace, i.e. lies in the
interval [ns_start, ns_start + ns_size)

.. _`nvdimm_badblocks_populate`:

nvdimm_badblocks_populate
=========================

.. c:function:: void nvdimm_badblocks_populate(struct nd_region *nd_region, struct badblocks *bb, const struct resource *res)

    Convert a list of badranges to badblocks

    :param struct nd_region \*nd_region:
        *undescribed*

    :param struct badblocks \*bb:
        badblocks instance to populate

    :param const struct resource \*res:
        resource range to consider

.. _`nvdimm_badblocks_populate.description`:

Description
-----------

The badrange list generated during bus initialization may contain
multiple, possibly overlapping physical address ranges.  Compare each
of these ranges to the resource range currently being initialized,
and add badblocks entries for all matching sub-ranges

.. This file was automatic generated / don't edit.


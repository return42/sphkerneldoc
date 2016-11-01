.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/core.c

.. _`devm_nvdimm_memremap`:

devm_nvdimm_memremap
====================

.. c:function:: void *devm_nvdimm_memremap(struct device *dev, resource_size_t offset, size_t size, unsigned long flags)

    map a resource that is shared across regions

    :param struct device \*dev:
        device that will own a reference to the shared mapping

    :param resource_size_t offset:
        physical base address of the mapping

    :param size_t size:
        mapping size

    :param unsigned long flags:
        memremap flags, or, if zero, perform an ioremap instead

.. _`nd_uuid_store`:

nd_uuid_store
=============

.. c:function:: int nd_uuid_store(struct device *dev, u8 **uuid_out, const char *buf, size_t len)

    common implementation for writing 'uuid' sysfs attributes

    :param struct device \*dev:
        container device for the uuid property

    :param u8 \*\*uuid_out:
        uuid buffer to replace

    :param const char \*buf:
        raw sysfs buffer to parse

    :param size_t len:
        *undescribed*

.. _`nd_uuid_store.description`:

Description
-----------

Enforce that uuids can only be changed while the device is disabled
(driver detached)

.. _`nd_uuid_store.locking`:

LOCKING
-------

expects \ :c:func:`device_lock`\  is held on entry

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
        number of bytes of poison to be added

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

    Convert a list of poison ranges to badblocks

    :param struct nd_region \*nd_region:
        *undescribed*

    :param struct badblocks \*bb:
        badblocks instance to populate

    :param const struct resource \*res:
        resource range to consider

.. _`nvdimm_badblocks_populate.description`:

Description
-----------

The poison list generated during bus initialization may contain
multiple, possibly overlapping physical address ranges.  Compare each
of these ranges to the resource range currently being initialized,
and add badblocks entries for all matching sub-ranges

.. This file was automatic generated / don't edit.


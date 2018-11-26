.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/core.c

.. _`devm_nvdimm_memremap`:

devm_nvdimm_memremap
====================

.. c:function:: void *devm_nvdimm_memremap(struct device *dev, resource_size_t offset, size_t size, unsigned long flags)

    map a resource that is shared across regions

    :param dev:
        device that will own a reference to the shared mapping
    :type dev: struct device \*

    :param offset:
        physical base address of the mapping
    :type offset: resource_size_t

    :param size:
        mapping size
    :type size: size_t

    :param flags:
        memremap flags, or, if zero, perform an ioremap instead
    :type flags: unsigned long

.. _`nd_uuid_store`:

nd_uuid_store
=============

.. c:function:: int nd_uuid_store(struct device *dev, u8 **uuid_out, const char *buf, size_t len)

    common implementation for writing 'uuid' sysfs attributes

    :param dev:
        container device for the uuid property
    :type dev: struct device \*

    :param uuid_out:
        uuid buffer to replace
    :type uuid_out: u8 \*\*

    :param buf:
        raw sysfs buffer to parse
    :type buf: const char \*

    :param len:
        *undescribed*
    :type len: size_t

.. _`nd_uuid_store.description`:

Description
-----------

Enforce that uuids can only be changed while the device is disabled
(driver detached)

.. _`nd_uuid_store.locking`:

LOCKING
-------

expects \ :c:func:`device_lock`\  is held on entry

.. This file was automatic generated / don't edit.


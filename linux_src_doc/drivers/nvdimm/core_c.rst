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

.. This file was automatic generated / don't edit.


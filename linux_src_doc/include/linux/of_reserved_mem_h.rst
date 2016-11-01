.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/of_reserved_mem.h

.. _`of_reserved_mem_device_init`:

of_reserved_mem_device_init
===========================

.. c:function:: int of_reserved_mem_device_init(struct device *dev)

    assign reserved memory region to given device

    :param struct device \*dev:
        Pointer to the device to configure

.. _`of_reserved_mem_device_init.description`:

Description
-----------

This function assigns respective DMA-mapping operations based on the first
reserved memory region specified by 'memory-region' property in device tree
node of the given device.

Returns error code or zero on success.

.. This file was automatic generated / don't edit.


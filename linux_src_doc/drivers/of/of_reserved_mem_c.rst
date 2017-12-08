.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_reserved_mem.c

.. _`fdt_reserved_mem_save_node`:

fdt_reserved_mem_save_node
==========================

.. c:function:: void fdt_reserved_mem_save_node(unsigned long node, const char *uname, phys_addr_t base, phys_addr_t size)

    save fdt node for second pass initialization

    :param unsigned long node:
        *undescribed*

    :param const char \*uname:
        *undescribed*

    :param phys_addr_t base:
        *undescribed*

    :param phys_addr_t size:
        *undescribed*

.. _`__reserved_mem_alloc_size`:

__reserved_mem_alloc_size
=========================

.. c:function:: int __reserved_mem_alloc_size(unsigned long node, const char *uname, phys_addr_t *res_base, phys_addr_t *res_size)

    allocate reserved memory described by 'size', 'align' and 'alloc-ranges' properties

    :param unsigned long node:
        *undescribed*

    :param const char \*uname:
        *undescribed*

    :param phys_addr_t \*res_base:
        *undescribed*

    :param phys_addr_t \*res_size:
        *undescribed*

.. _`__reserved_mem_init_node`:

__reserved_mem_init_node
========================

.. c:function:: int __reserved_mem_init_node(struct reserved_mem *rmem)

    call region specific reserved memory init code

    :param struct reserved_mem \*rmem:
        *undescribed*

.. _`fdt_init_reserved_mem`:

fdt_init_reserved_mem
=====================

.. c:function:: void fdt_init_reserved_mem( void)

    allocate and init all saved reserved memory regions

    :param  void:
        no arguments

.. _`of_reserved_mem_device_init_by_idx`:

of_reserved_mem_device_init_by_idx
==================================

.. c:function:: int of_reserved_mem_device_init_by_idx(struct device *dev, struct device_node *np, int idx)

    assign reserved memory region to given device

    :param struct device \*dev:
        Pointer to the device to configure

    :param struct device_node \*np:
        Pointer to the device_node with 'reserved-memory' property

    :param int idx:
        Index of selected region

.. _`of_reserved_mem_device_init_by_idx.description`:

Description
-----------

This function assigns respective DMA-mapping operations based on reserved
memory region specified by 'memory-region' property in \ ``np``\  node to the \ ``dev``\ 
device. When driver needs to use more than one reserved memory region, it
should allocate child devices and initialize regions by name for each of
child device.

Returns error code or zero on success.

.. _`of_reserved_mem_device_release`:

of_reserved_mem_device_release
==============================

.. c:function:: void of_reserved_mem_device_release(struct device *dev)

    release reserved memory device structures

    :param struct device \*dev:
        Pointer to the device to deconfigure

.. _`of_reserved_mem_device_release.description`:

Description
-----------

This function releases structures allocated for memory region handling for
the given device.

.. _`of_reserved_mem_lookup`:

of_reserved_mem_lookup
======================

.. c:function:: struct reserved_mem *of_reserved_mem_lookup(struct device_node *np)

    acquire reserved_mem from a device node

    :param struct device_node \*np:
        node pointer of the desired reserved-memory region

.. _`of_reserved_mem_lookup.description`:

Description
-----------

This function allows drivers to acquire a reference to the reserved_mem
struct based on a device node handle.

Returns a reserved_mem reference, or NULL on error.

.. This file was automatic generated / don't edit.


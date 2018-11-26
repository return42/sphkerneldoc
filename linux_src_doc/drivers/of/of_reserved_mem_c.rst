.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_reserved_mem.c

.. _`fdt_reserved_mem_save_node`:

fdt_reserved_mem_save_node
==========================

.. c:function:: void fdt_reserved_mem_save_node(unsigned long node, const char *uname, phys_addr_t base, phys_addr_t size)

    save fdt node for second pass initialization

    :param node:
        *undescribed*
    :type node: unsigned long

    :param uname:
        *undescribed*
    :type uname: const char \*

    :param base:
        *undescribed*
    :type base: phys_addr_t

    :param size:
        *undescribed*
    :type size: phys_addr_t

.. _`__reserved_mem_alloc_size`:

\__reserved_mem_alloc_size
==========================

.. c:function:: int __reserved_mem_alloc_size(unsigned long node, const char *uname, phys_addr_t *res_base, phys_addr_t *res_size)

    allocate reserved memory described by 'size', 'align' and 'alloc-ranges' properties

    :param node:
        *undescribed*
    :type node: unsigned long

    :param uname:
        *undescribed*
    :type uname: const char \*

    :param res_base:
        *undescribed*
    :type res_base: phys_addr_t \*

    :param res_size:
        *undescribed*
    :type res_size: phys_addr_t \*

.. _`__reserved_mem_init_node`:

\__reserved_mem_init_node
=========================

.. c:function:: int __reserved_mem_init_node(struct reserved_mem *rmem)

    call region specific reserved memory init code

    :param rmem:
        *undescribed*
    :type rmem: struct reserved_mem \*

.. _`fdt_init_reserved_mem`:

fdt_init_reserved_mem
=====================

.. c:function:: void fdt_init_reserved_mem( void)

    allocate and init all saved reserved memory regions

    :param void:
        no arguments
    :type void: 

.. _`of_reserved_mem_device_init_by_idx`:

of_reserved_mem_device_init_by_idx
==================================

.. c:function:: int of_reserved_mem_device_init_by_idx(struct device *dev, struct device_node *np, int idx)

    assign reserved memory region to given device

    :param dev:
        Pointer to the device to configure
    :type dev: struct device \*

    :param np:
        Pointer to the device_node with 'reserved-memory' property
    :type np: struct device_node \*

    :param idx:
        Index of selected region
    :type idx: int

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

    :param dev:
        Pointer to the device to deconfigure
    :type dev: struct device \*

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

    :param np:
        node pointer of the desired reserved-memory region
    :type np: struct device_node \*

.. _`of_reserved_mem_lookup.description`:

Description
-----------

This function allows drivers to acquire a reference to the reserved_mem
struct based on a device node handle.

Returns a reserved_mem reference, or NULL on error.

.. This file was automatic generated / don't edit.


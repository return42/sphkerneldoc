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

.. _`of_reserved_mem_device_init`:

of_reserved_mem_device_init
===========================

.. c:function:: int of_reserved_mem_device_init(struct device *dev)

    assign reserved memory region to given device

    :param struct device \*dev:
        *undescribed*

.. _`of_reserved_mem_device_init.description`:

Description
-----------

This function assign memory region pointed by "memory-region" device tree
property to the given device.

.. _`of_reserved_mem_device_release`:

of_reserved_mem_device_release
==============================

.. c:function:: void of_reserved_mem_device_release(struct device *dev)

    release reserved memory device structures

    :param struct device \*dev:
        *undescribed*

.. _`of_reserved_mem_device_release.description`:

Description
-----------

This function releases structures allocated for memory region handling for
the given device.

.. This file was automatic generated / don't edit.

.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/dma-mapping.h

.. _`arm_dma_alloc`:

arm_dma_alloc
=============

.. c:function:: void *arm_dma_alloc(struct device *dev, size_t size, dma_addr_t *handle, gfp_t gfp, unsigned long attrs)

    allocate consistent memory for DMA

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param size:
        required memory size
    :type size: size_t

    :param handle:
        bus-specific DMA address
    :type handle: dma_addr_t \*

    :param gfp:
        *undescribed*
    :type gfp: gfp_t

    :param attrs:
        optinal attributes that specific mapping properties
    :type attrs: unsigned long

.. _`arm_dma_alloc.description`:

Description
-----------

Allocate some memory for a device for performing DMA.  This function
allocates pages, and will return the CPU-viewed address, and sets \ ``handle``\ 
to be the device-viewed address.

.. _`arm_dma_free`:

arm_dma_free
============

.. c:function:: void arm_dma_free(struct device *dev, size_t size, void *cpu_addr, dma_addr_t handle, unsigned long attrs)

    free memory allocated by arm_dma_alloc

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param size:
        size of memory originally requested in dma_alloc_coherent
    :type size: size_t

    :param cpu_addr:
        CPU-view address returned from dma_alloc_coherent
    :type cpu_addr: void \*

    :param handle:
        device-view address returned from dma_alloc_coherent
    :type handle: dma_addr_t

    :param attrs:
        optinal attributes that specific mapping properties
    :type attrs: unsigned long

.. _`arm_dma_free.description`:

Description
-----------

Free (and unmap) a DMA buffer previously allocated by
\ :c:func:`arm_dma_alloc`\ .

References to memory and mappings associated with cpu_addr/handle
during and after this call executing are illegal.

.. _`arm_dma_mmap`:

arm_dma_mmap
============

.. c:function:: int arm_dma_mmap(struct device *dev, struct vm_area_struct *vma, void *cpu_addr, dma_addr_t dma_addr, size_t size, unsigned long attrs)

    map a coherent DMA allocation into user space

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param vma:
        vm_area_struct describing requested user mapping
    :type vma: struct vm_area_struct \*

    :param cpu_addr:
        kernel CPU-view address returned from dma_alloc_coherent
    :type cpu_addr: void \*

    :param dma_addr:
        *undescribed*
    :type dma_addr: dma_addr_t

    :param size:
        size of memory originally requested in dma_alloc_coherent
    :type size: size_t

    :param attrs:
        optinal attributes that specific mapping properties
    :type attrs: unsigned long

.. _`arm_dma_mmap.description`:

Description
-----------

Map a coherent DMA buffer previously allocated by dma_alloc_coherent
into user space.  The coherent DMA buffer must not be freed by the
driver until the user space mapping has been released.

.. _`dmabounce_register_dev`:

dmabounce_register_dev
======================

.. c:function:: int dmabounce_register_dev(int (*)(struct device *, dma_addr_t, size_t), unsigned long, unsigned long, int (*)(struct device *, dma_addr_t, size_t))

    :param int (\*)(struct device \*, dma_addr_t, size_t):
        *undescribed*

    :param long:
        *undescribed*
    :type long: unsigned

    :param long:
        *undescribed*
    :type long: unsigned

    :param int (\*)(struct device \*, dma_addr_t, size_t):
        *undescribed*

.. _`dmabounce_register_dev.description`:

Description
-----------

This function should be called by low-level platform code to register
a device as requireing DMA buffer bouncing. The function will allocate
appropriate DMA pools for the device.

.. _`dmabounce_unregister_dev`:

dmabounce_unregister_dev
========================

.. c:function:: void dmabounce_unregister_dev(struct device *)

    :param :
        *undescribed*
    :type : struct device \*

.. _`dmabounce_unregister_dev.description`:

Description
-----------

This function should be called by low-level platform code when device
that was previously registered with dmabounce_register_dev is removed
from the system.

.. This file was automatic generated / don't edit.


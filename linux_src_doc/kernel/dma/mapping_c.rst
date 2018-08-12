.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/dma/mapping.c

.. _`dmam_alloc_coherent`:

dmam_alloc_coherent
===================

.. c:function:: void *dmam_alloc_coherent(struct device *dev, size_t size, dma_addr_t *dma_handle, gfp_t gfp)

    Managed \ :c:func:`dma_alloc_coherent`\ 

    :param struct device \*dev:
        Device to allocate coherent memory for

    :param size_t size:
        Size of allocation

    :param dma_addr_t \*dma_handle:
        Out argument for allocated DMA handle

    :param gfp_t gfp:
        Allocation flags

.. _`dmam_alloc_coherent.description`:

Description
-----------

Managed \ :c:func:`dma_alloc_coherent`\ .  Memory allocated using this function
will be automatically released on driver detach.

.. _`dmam_alloc_coherent.return`:

Return
------

Pointer to allocated memory on success, NULL on failure.

.. _`dmam_free_coherent`:

dmam_free_coherent
==================

.. c:function:: void dmam_free_coherent(struct device *dev, size_t size, void *vaddr, dma_addr_t dma_handle)

    Managed \ :c:func:`dma_free_coherent`\ 

    :param struct device \*dev:
        Device to free coherent memory for

    :param size_t size:
        Size of allocation

    :param void \*vaddr:
        Virtual address of the memory to free

    :param dma_addr_t dma_handle:
        DMA handle of the memory to free

.. _`dmam_free_coherent.description`:

Description
-----------

Managed \ :c:func:`dma_free_coherent`\ .

.. _`dmam_alloc_attrs`:

dmam_alloc_attrs
================

.. c:function:: void *dmam_alloc_attrs(struct device *dev, size_t size, dma_addr_t *dma_handle, gfp_t gfp, unsigned long attrs)

    Managed \ :c:func:`dma_alloc_attrs`\ 

    :param struct device \*dev:
        Device to allocate non_coherent memory for

    :param size_t size:
        Size of allocation

    :param dma_addr_t \*dma_handle:
        Out argument for allocated DMA handle

    :param gfp_t gfp:
        Allocation flags

    :param unsigned long attrs:
        Flags in the DMA_ATTR_* namespace.

.. _`dmam_alloc_attrs.description`:

Description
-----------

Managed \ :c:func:`dma_alloc_attrs`\ .  Memory allocated using this function will be
automatically released on driver detach.

.. _`dmam_alloc_attrs.return`:

Return
------

Pointer to allocated memory on success, NULL on failure.

.. _`dmam_declare_coherent_memory`:

dmam_declare_coherent_memory
============================

.. c:function:: int dmam_declare_coherent_memory(struct device *dev, phys_addr_t phys_addr, dma_addr_t device_addr, size_t size, int flags)

    Managed \ :c:func:`dma_declare_coherent_memory`\ 

    :param struct device \*dev:
        Device to declare coherent memory for

    :param phys_addr_t phys_addr:
        Physical address of coherent memory to be declared

    :param dma_addr_t device_addr:
        Device address of coherent memory to be declared

    :param size_t size:
        Size of coherent memory to be declared

    :param int flags:
        Flags

.. _`dmam_declare_coherent_memory.description`:

Description
-----------

Managed \ :c:func:`dma_declare_coherent_memory`\ .

.. _`dmam_declare_coherent_memory.return`:

Return
------

0 on success, -errno on failure.

.. _`dmam_release_declared_memory`:

dmam_release_declared_memory
============================

.. c:function:: void dmam_release_declared_memory(struct device *dev)

    Managed \ :c:func:`dma_release_declared_memory`\ .

    :param struct device \*dev:
        Device to release declared coherent memory for

.. _`dmam_release_declared_memory.description`:

Description
-----------

Managed \ :c:func:`dmam_release_declared_memory`\ .

.. This file was automatic generated / don't edit.


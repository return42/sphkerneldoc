.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/p2pdma.c

.. _`pci_p2pdma_add_resource`:

pci_p2pdma_add_resource
=======================

.. c:function:: int pci_p2pdma_add_resource(struct pci_dev *pdev, int bar, size_t size, u64 offset)

    add memory for use as p2p memory

    :param pdev:
        the device to add the memory to
    :type pdev: struct pci_dev \*

    :param bar:
        PCI BAR to add
    :type bar: int

    :param size:
        size of the memory to add, may be zero to use the whole BAR
    :type size: size_t

    :param offset:
        offset into the PCI BAR
    :type offset: u64

.. _`pci_p2pdma_add_resource.description`:

Description
-----------

The memory will be given ZONE_DEVICE struct pages so that it may
be used with any DMA request.

.. _`pci_p2pdma_distance_many`:

pci_p2pdma_distance_many
========================

.. c:function:: int pci_p2pdma_distance_many(struct pci_dev *provider, struct device **clients, int num_clients, bool verbose)

    Determive the cumulative distance between a p2pdma provider and the clients in use.

    :param provider:
        p2pdma provider to check against the client list
    :type provider: struct pci_dev \*

    :param clients:
        array of devices to check (NULL-terminated)
    :type clients: struct device \*\*

    :param num_clients:
        number of clients in the array
    :type num_clients: int

    :param verbose:
        if true, print warnings for devices when we return -1
    :type verbose: bool

.. _`pci_p2pdma_distance_many.description`:

Description
-----------

Returns -1 if any of the clients are not compatible (behind the same
root port as the provider), otherwise returns a positive number where
a lower number is the preferrable choice. (If there's one client
that's the same as the provider it will return 0, which is best choice).

For now, "compatible" means the provider and the clients are all behind
the same PCI root port. This cuts out cases that may work but is safest
for the user. Future work can expand this to white-list root complexes that
can safely forward between each ports.

.. _`pci_has_p2pmem`:

pci_has_p2pmem
==============

.. c:function:: bool pci_has_p2pmem(struct pci_dev *pdev)

    check if a given PCI device has published any p2pmem

    :param pdev:
        PCI device to check
    :type pdev: struct pci_dev \*

.. _`pci_p2pmem_find_many`:

pci_p2pmem_find_many
====================

.. c:function:: struct pci_dev *pci_p2pmem_find_many(struct device **clients, int num_clients)

    find a peer-to-peer DMA memory device compatible with the specified list of clients and shortest distance (as determined by \ :c:func:`pci_p2pmem_dma`\ )

    :param clients:
        array of devices to check (NULL-terminated)
    :type clients: struct device \*\*

    :param num_clients:
        number of client devices in the list
    :type num_clients: int

.. _`pci_p2pmem_find_many.description`:

Description
-----------

If multiple devices are behind the same switch, the one "closest" to the
client devices in use will be chosen first. (So if one of the providers are
the same as one of the clients, that provider will be used ahead of any
other providers that are unrelated). If multiple providers are an equal
distance away, one will be chosen at random.

Returns a pointer to the PCI device with a reference taken (use pci_dev_put
to return the reference) or NULL if no compatible device is found. The
found provider will also be assigned to the client list.

.. _`pci_alloc_p2pmem`:

pci_alloc_p2pmem
================

.. c:function:: void *pci_alloc_p2pmem(struct pci_dev *pdev, size_t size)

    allocate peer-to-peer DMA memory

    :param pdev:
        the device to allocate memory from
    :type pdev: struct pci_dev \*

    :param size:
        number of bytes to allocate
    :type size: size_t

.. _`pci_alloc_p2pmem.description`:

Description
-----------

Returns the allocated memory or NULL on error.

.. _`pci_free_p2pmem`:

pci_free_p2pmem
===============

.. c:function:: void pci_free_p2pmem(struct pci_dev *pdev, void *addr, size_t size)

    free peer-to-peer DMA memory

    :param pdev:
        the device the memory was allocated from
    :type pdev: struct pci_dev \*

    :param addr:
        address of the memory that was allocated
    :type addr: void \*

    :param size:
        number of bytes that was allocated
    :type size: size_t

.. _`pci_p2pmem_virt_to_bus`:

pci_p2pmem_virt_to_bus
======================

.. c:function:: pci_bus_addr_t pci_p2pmem_virt_to_bus(struct pci_dev *pdev, void *addr)

    return the PCI bus address for a given virtual address obtained with \ :c:func:`pci_alloc_p2pmem`\ 

    :param pdev:
        the device the memory was allocated from
    :type pdev: struct pci_dev \*

    :param addr:
        address of the memory that was allocated
    :type addr: void \*

.. _`pci_p2pmem_alloc_sgl`:

pci_p2pmem_alloc_sgl
====================

.. c:function:: struct scatterlist *pci_p2pmem_alloc_sgl(struct pci_dev *pdev, unsigned int *nents, u32 length)

    allocate peer-to-peer DMA memory in a scatterlist

    :param pdev:
        the device to allocate memory from
    :type pdev: struct pci_dev \*

    :param nents:
        the number of SG entries in the list
    :type nents: unsigned int \*

    :param length:
        number of bytes to allocate
    :type length: u32

.. _`pci_p2pmem_alloc_sgl.description`:

Description
-----------

Returns 0 on success

.. _`pci_p2pmem_free_sgl`:

pci_p2pmem_free_sgl
===================

.. c:function:: void pci_p2pmem_free_sgl(struct pci_dev *pdev, struct scatterlist *sgl)

    free a scatterlist allocated by \ :c:func:`pci_p2pmem_alloc_sgl`\ 

    :param pdev:
        the device to allocate memory from
    :type pdev: struct pci_dev \*

    :param sgl:
        the allocated scatterlist
    :type sgl: struct scatterlist \*

.. _`pci_p2pmem_publish`:

pci_p2pmem_publish
==================

.. c:function:: void pci_p2pmem_publish(struct pci_dev *pdev, bool publish)

    publish the peer-to-peer DMA memory for use by other devices with \ :c:func:`pci_p2pmem_find`\ 

    :param pdev:
        the device with peer-to-peer DMA memory to publish
    :type pdev: struct pci_dev \*

    :param publish:
        set to true to publish the memory, false to unpublish it
    :type publish: bool

.. _`pci_p2pmem_publish.description`:

Description
-----------

Published memory can be used by other PCI device drivers for
peer-2-peer DMA operations. Non-published memory is reserved for
exlusive use of the device driver that registers the peer-to-peer
memory.

.. _`pci_p2pdma_map_sg`:

pci_p2pdma_map_sg
=================

.. c:function:: int pci_p2pdma_map_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    map a PCI peer-to-peer scatterlist for DMA

    :param dev:
        device doing the DMA request
    :type dev: struct device \*

    :param sg:
        scatter list to map
    :type sg: struct scatterlist \*

    :param nents:
        elements in the scatterlist
    :type nents: int

    :param dir:
        DMA direction
    :type dir: enum dma_data_direction

.. _`pci_p2pdma_map_sg.description`:

Description
-----------

Scatterlists mapped with this function should not be unmapped in any way.

Returns the number of SG entries mapped or 0 on error.

.. _`pci_p2pdma_enable_store`:

pci_p2pdma_enable_store
=======================

.. c:function:: int pci_p2pdma_enable_store(const char *page, struct pci_dev **p2p_dev, bool *use_p2pdma)

    parse a configfs/sysfs attribute store to enable p2pdma

    :param page:
        contents of the value to be stored
    :type page: const char \*

    :param p2p_dev:
        returns the PCI device that was selected to be used
        (if one was specified in the stored value)
    :type p2p_dev: struct pci_dev \*\*

    :param use_p2pdma:
        returns whether to enable p2pdma or not
    :type use_p2pdma: bool \*

.. _`pci_p2pdma_enable_store.description`:

Description
-----------

Parses an attribute value to decide whether to enable p2pdma.
The value can select a PCI device (using it's full BDF device
name) or a boolean (in any format \ :c:func:`strtobool`\  accepts). A false
value disables p2pdma, a true value expects the caller
to automatically find a compatible device and specifying a PCI device
expects the caller to use the specific provider.

\ :c:func:`pci_p2pdma_enable_show`\  should be used as the show operation for
the attribute.

Returns 0 on success

.. _`pci_p2pdma_enable_show`:

pci_p2pdma_enable_show
======================

.. c:function:: ssize_t pci_p2pdma_enable_show(char *page, struct pci_dev *p2p_dev, bool use_p2pdma)

    show a configfs/sysfs attribute indicating whether p2pdma is enabled

    :param page:
        contents of the stored value
    :type page: char \*

    :param p2p_dev:
        the selected p2p device (NULL if no device is selected)
    :type p2p_dev: struct pci_dev \*

    :param use_p2pdma:
        whether p2pdme has been enabled
    :type use_p2pdma: bool

.. _`pci_p2pdma_enable_show.description`:

Description
-----------

Attributes that use \ :c:func:`pci_p2pdma_enable_store`\  should use this function
to show the value of the attribute.

Returns 0 on success

.. This file was automatic generated / don't edit.


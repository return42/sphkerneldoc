.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/devres.c

.. _`devm_ioremap`:

devm_ioremap
============

.. c:function:: void __iomem *devm_ioremap(struct device *dev, resource_size_t offset, resource_size_t size)

    Managed \ :c:func:`ioremap`\ 

    :param struct device \*dev:
        Generic device to remap IO address for

    :param resource_size_t offset:
        BUS offset to map

    :param resource_size_t size:
        Size of map

.. _`devm_ioremap.description`:

Description
-----------

Managed \ :c:func:`ioremap`\ .  Map is automatically unmapped on driver detach.

.. _`devm_ioremap_nocache`:

devm_ioremap_nocache
====================

.. c:function:: void __iomem *devm_ioremap_nocache(struct device *dev, resource_size_t offset, resource_size_t size)

    Managed \ :c:func:`ioremap_nocache`\ 

    :param struct device \*dev:
        Generic device to remap IO address for

    :param resource_size_t offset:
        BUS offset to map

    :param resource_size_t size:
        Size of map

.. _`devm_ioremap_nocache.description`:

Description
-----------

Managed \ :c:func:`ioremap_nocache`\ .  Map is automatically unmapped on driver
detach.

.. _`devm_ioremap_wc`:

devm_ioremap_wc
===============

.. c:function:: void __iomem *devm_ioremap_wc(struct device *dev, resource_size_t offset, resource_size_t size)

    Managed \ :c:func:`ioremap_wc`\ 

    :param struct device \*dev:
        Generic device to remap IO address for

    :param resource_size_t offset:
        BUS offset to map

    :param resource_size_t size:
        Size of map

.. _`devm_ioremap_wc.description`:

Description
-----------

Managed \ :c:func:`ioremap_wc`\ .  Map is automatically unmapped on driver detach.

.. _`devm_iounmap`:

devm_iounmap
============

.. c:function:: void devm_iounmap(struct device *dev, void __iomem *addr)

    Managed \ :c:func:`iounmap`\ 

    :param struct device \*dev:
        Generic device to unmap for

    :param void __iomem \*addr:
        Address to unmap

.. _`devm_iounmap.description`:

Description
-----------

Managed \ :c:func:`iounmap`\ .  \ ``addr``\  must have been mapped using devm_ioremap\*().

.. _`devm_ioremap_resource`:

devm_ioremap_resource
=====================

.. c:function:: void __iomem *devm_ioremap_resource(struct device *dev, struct resource *res)

    check, request region, and ioremap resource

    :param struct device \*dev:
        generic device to handle the resource for

    :param struct resource \*res:
        resource to be handled

.. _`devm_ioremap_resource.description`:

Description
-----------

Checks that a resource is a valid memory region, requests the memory
region and ioremaps it. All operations are managed and will be undone
on driver detach.

Returns a pointer to the remapped memory or an \ :c:func:`ERR_PTR`\  encoded error code
on failure. Usage example:

res = platform_get_resource(pdev, IORESOURCE_MEM, 0);
base = devm_ioremap_resource(\ :c:type:`pdev->dev <pdev>`\ , res);
if (IS_ERR(base))
return PTR_ERR(base);

.. _`devm_ioport_map`:

devm_ioport_map
===============

.. c:function:: void __iomem *devm_ioport_map(struct device *dev, unsigned long port, unsigned int nr)

    Managed \ :c:func:`ioport_map`\ 

    :param struct device \*dev:
        Generic device to map ioport for

    :param unsigned long port:
        Port to map

    :param unsigned int nr:
        Number of ports to map

.. _`devm_ioport_map.description`:

Description
-----------

Managed \ :c:func:`ioport_map`\ .  Map is automatically unmapped on driver
detach.

.. _`devm_ioport_unmap`:

devm_ioport_unmap
=================

.. c:function:: void devm_ioport_unmap(struct device *dev, void __iomem *addr)

    Managed \ :c:func:`ioport_unmap`\ 

    :param struct device \*dev:
        Generic device to unmap for

    :param void __iomem \*addr:
        Address to unmap

.. _`devm_ioport_unmap.description`:

Description
-----------

Managed \ :c:func:`ioport_unmap`\ .  \ ``addr``\  must have been mapped using
\ :c:func:`devm_ioport_map`\ .

.. _`pcim_iomap_table`:

pcim_iomap_table
================

.. c:function:: void __iomem * const *pcim_iomap_table(struct pci_dev *pdev)

    access iomap allocation table

    :param struct pci_dev \*pdev:
        PCI device to access iomap table for

.. _`pcim_iomap_table.description`:

Description
-----------

Access iomap allocation table for \ ``dev``\ .  If iomap table doesn't
exist and \ ``pdev``\  is managed, it will be allocated.  All iomaps
recorded in the iomap table are automatically unmapped on driver
detach.

This function might sleep when the table is first allocated but can
be safely called without context and guaranteed to succed once
allocated.

.. _`pcim_iomap`:

pcim_iomap
==========

.. c:function:: void __iomem *pcim_iomap(struct pci_dev *pdev, int bar, unsigned long maxlen)

    Managed \ :c:func:`pcim_iomap`\ 

    :param struct pci_dev \*pdev:
        PCI device to iomap for

    :param int bar:
        BAR to iomap

    :param unsigned long maxlen:
        Maximum length of iomap

.. _`pcim_iomap.description`:

Description
-----------

Managed \ :c:func:`pci_iomap`\ .  Map is automatically unmapped on driver
detach.

.. _`pcim_iounmap`:

pcim_iounmap
============

.. c:function:: void pcim_iounmap(struct pci_dev *pdev, void __iomem *addr)

    Managed \ :c:func:`pci_iounmap`\ 

    :param struct pci_dev \*pdev:
        PCI device to iounmap for

    :param void __iomem \*addr:
        Address to unmap

.. _`pcim_iounmap.description`:

Description
-----------

Managed \ :c:func:`pci_iounmap`\ .  \ ``addr``\  must have been mapped using \ :c:func:`pcim_iomap`\ .

.. _`pcim_iomap_regions`:

pcim_iomap_regions
==================

.. c:function:: int pcim_iomap_regions(struct pci_dev *pdev, int mask, const char *name)

    Request and iomap PCI BARs

    :param struct pci_dev \*pdev:
        PCI device to map IO resources for

    :param int mask:
        Mask of BARs to request and iomap

    :param const char \*name:
        Name used when requesting regions

.. _`pcim_iomap_regions.description`:

Description
-----------

Request and iomap regions specified by \ ``mask``\ .

.. _`pcim_iomap_regions_request_all`:

pcim_iomap_regions_request_all
==============================

.. c:function:: int pcim_iomap_regions_request_all(struct pci_dev *pdev, int mask, const char *name)

    Request all BARs and iomap specified ones

    :param struct pci_dev \*pdev:
        PCI device to map IO resources for

    :param int mask:
        Mask of BARs to iomap

    :param const char \*name:
        Name used when requesting regions

.. _`pcim_iomap_regions_request_all.description`:

Description
-----------

Request all PCI BARs and iomap regions specified by \ ``mask``\ .

.. _`pcim_iounmap_regions`:

pcim_iounmap_regions
====================

.. c:function:: void pcim_iounmap_regions(struct pci_dev *pdev, int mask)

    Unmap and release PCI BARs

    :param struct pci_dev \*pdev:
        PCI device to map IO resources for

    :param int mask:
        Mask of BARs to unmap and release

.. _`pcim_iounmap_regions.description`:

Description
-----------

Unmap and release regions specified by \ ``mask``\ .

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_pci.c

.. _`drm_pci_alloc`:

drm_pci_alloc
=============

.. c:function:: drm_dma_handle_t *drm_pci_alloc(struct drm_device *dev, size_t size, size_t align)

    Allocate a PCI consistent memory block, for DMA.

    :param struct drm_device \*dev:
        DRM device

    :param size_t size:
        size of block to allocate

    :param size_t align:
        alignment of block

.. _`drm_pci_alloc.description`:

Description
-----------

FIXME: This is a needless abstraction of the Linux dma-api and should be
removed.

.. _`drm_pci_alloc.return`:

Return
------

A handle to the allocated memory block on success or NULL on
failure.

.. _`drm_pci_free`:

drm_pci_free
============

.. c:function:: void drm_pci_free(struct drm_device *dev, drm_dma_handle_t *dmah)

    Free a PCI consistent memory block

    :param struct drm_device \*dev:
        DRM device

    :param drm_dma_handle_t \*dmah:
        handle to memory block

.. _`drm_pci_free.description`:

Description
-----------

FIXME: This is a needless abstraction of the Linux dma-api and should be
removed.

.. _`drm_irq_by_busid`:

drm_irq_by_busid
================

.. c:function:: int drm_irq_by_busid(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Get interrupt from bus ID

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        IOCTL parameter pointing to a drm_irq_busid structure

    :param struct drm_file \*file_priv:
        DRM file private.

.. _`drm_irq_by_busid.description`:

Description
-----------

Finds the PCI device with the specified bus id and gets its IRQ number.
This IOCTL is deprecated, and will now return EINVAL for any busid not equal
to that of the device that this DRM instance attached to.

.. _`drm_irq_by_busid.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_get_pci_dev`:

drm_get_pci_dev
===============

.. c:function:: int drm_get_pci_dev(struct pci_dev *pdev, const struct pci_device_id *ent, struct drm_driver *driver)

    Register a PCI device with the DRM subsystem

    :param struct pci_dev \*pdev:
        PCI device

    :param const struct pci_device_id \*ent:
        entry from the PCI ID table that matches \ ``pdev``\ 

    :param struct drm_driver \*driver:
        DRM device driver

.. _`drm_get_pci_dev.description`:

Description
-----------

Attempt to gets inter module "drm" information. If we are first
then register the character device and inter module information.
Try and register, if we fail to register, backout previous work.

.. _`drm_get_pci_dev.note`:

NOTE
----

This function is deprecated, please use \ :c:func:`drm_dev_alloc`\  and
\ :c:func:`drm_dev_register`\  instead and remove your \ :c:type:`drm_driver.load <drm_driver>`\  callback.

.. _`drm_get_pci_dev.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_legacy_pci_init`:

drm_legacy_pci_init
===================

.. c:function:: int drm_legacy_pci_init(struct drm_driver *driver, struct pci_driver *pdriver)

    shadow-attach a legacy DRM PCI driver

    :param struct drm_driver \*driver:
        DRM device driver

    :param struct pci_driver \*pdriver:
        PCI device driver

.. _`drm_legacy_pci_init.description`:

Description
-----------

This is only used by legacy dri1 drivers and deprecated.

.. _`drm_legacy_pci_init.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_legacy_pci_exit`:

drm_legacy_pci_exit
===================

.. c:function:: void drm_legacy_pci_exit(struct drm_driver *driver, struct pci_driver *pdriver)

    unregister shadow-attach legacy DRM driver

    :param struct drm_driver \*driver:
        DRM device driver

    :param struct pci_driver \*pdriver:
        PCI device driver

.. _`drm_legacy_pci_exit.description`:

Description
-----------

Unregister a DRM driver shadow-attached through \ :c:func:`drm_legacy_pci_init`\ . This
is deprecated and only used by dri1 drivers.

.. This file was automatic generated / don't edit.


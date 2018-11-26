.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virtio/virtio_pci_modern.c

.. _`virtio_pci_find_capability`:

virtio_pci_find_capability
==========================

.. c:function:: int virtio_pci_find_capability(struct pci_dev *dev, u8 cfg_type, u32 ioresource_types, int *bars)

    walk capabilities to find device info.

    :param dev:
        the pci device
    :type dev: struct pci_dev \*

    :param cfg_type:
        the VIRTIO_PCI_CAP\_\* value we seek
    :type cfg_type: u8

    :param ioresource_types:
        IORESOURCE_MEM and/or IORESOURCE_IO.
    :type ioresource_types: u32

    :param bars:
        *undescribed*
    :type bars: int \*

.. _`virtio_pci_find_capability.description`:

Description
-----------

Returns offset of the capability, or 0.

.. This file was automatic generated / don't edit.


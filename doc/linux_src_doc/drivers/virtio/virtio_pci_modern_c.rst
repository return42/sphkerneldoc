.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virtio/virtio_pci_modern.c

.. _`virtio_pci_find_capability`:

virtio_pci_find_capability
==========================

.. c:function:: int virtio_pci_find_capability(struct pci_dev *dev, u8 cfg_type, u32 ioresource_types, int *bars)

    walk capabilities to find device info.

    :param struct pci_dev \*dev:
        the pci device

    :param u8 cfg_type:
        the VIRTIO_PCI_CAP\_\* value we seek

    :param u32 ioresource_types:
        IORESOURCE_MEM and/or IORESOURCE_IO.

    :param int \*bars:
        *undescribed*

.. _`virtio_pci_find_capability.description`:

Description
-----------

Returns offset of the capability, or 0.

.. This file was automatic generated / don't edit.


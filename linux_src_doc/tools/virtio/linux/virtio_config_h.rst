.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/virtio/linux/virtio_config.h

.. _`__virtio_set_bit`:

\__virtio_set_bit
=================

.. c:function:: void __virtio_set_bit(struct virtio_device *vdev, unsigned int fbit)

    helper to set feature bits. For use by transports.

    :param vdev:
        the device
    :type vdev: struct virtio_device \*

    :param fbit:
        the feature bit
    :type fbit: unsigned int

.. _`__virtio_clear_bit`:

\__virtio_clear_bit
===================

.. c:function:: void __virtio_clear_bit(struct virtio_device *vdev, unsigned int fbit)

    helper to clear feature bits. For use by transports.

    :param vdev:
        the device
    :type vdev: struct virtio_device \*

    :param fbit:
        the feature bit
    :type fbit: unsigned int

.. _`virtio_has_iommu_quirk`:

virtio_has_iommu_quirk
======================

.. c:function:: bool virtio_has_iommu_quirk(const struct virtio_device *vdev)

    determine whether this device has the iommu quirk

    :param vdev:
        the device
    :type vdev: const struct virtio_device \*

.. This file was automatic generated / don't edit.


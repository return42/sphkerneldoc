.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/virtio/linux/virtio_config.h

.. _`__virtio_set_bit`:

__virtio_set_bit
================

.. c:function:: void __virtio_set_bit(struct virtio_device *vdev, unsigned int fbit)

    helper to set feature bits. For use by transports.

    :param struct virtio_device \*vdev:
        the device

    :param unsigned int fbit:
        the feature bit

.. _`__virtio_clear_bit`:

__virtio_clear_bit
==================

.. c:function:: void __virtio_clear_bit(struct virtio_device *vdev, unsigned int fbit)

    helper to clear feature bits. For use by transports.

    :param struct virtio_device \*vdev:
        the device

    :param unsigned int fbit:
        the feature bit

.. This file was automatic generated / don't edit.


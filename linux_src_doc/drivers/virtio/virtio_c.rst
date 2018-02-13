.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virtio/virtio.c

.. _`register_virtio_device`:

register_virtio_device
======================

.. c:function:: int register_virtio_device(struct virtio_device *dev)

    register virtio device

    :param struct virtio_device \*dev:
        virtio device to be registered

.. _`register_virtio_device.description`:

Description
-----------

On error, the caller must call put_device on &@dev->dev (and not kfree),
as another code path may have obtained a reference to \ ``dev``\ .

.. _`register_virtio_device.return`:

Return
------

0 on suceess, -error on failure

.. This file was automatic generated / don't edit.


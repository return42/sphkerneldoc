.. -*- coding: utf-8; mode: rst -*-

===================
remoteproc_virtio.c
===================


.. _`rproc_vq_interrupt`:

rproc_vq_interrupt
==================

.. c:function:: irqreturn_t rproc_vq_interrupt (struct rproc *rproc, int notifyid)

    tell remoteproc that a virtqueue is interrupted

    :param struct rproc \*rproc:
        handle to the remote processor

    :param int notifyid:
        index of the signalled virtqueue (unique per this ``rproc``\ )



.. _`rproc_vq_interrupt.description`:

Description
-----------

This function should be called by the platform-specific rproc driver,
when the remote processor signals that a specific virtqueue has pending
messages available.

Returns IRQ_NONE if no message was found in the ``notifyid`` virtqueue,
and otherwise returns IRQ_HANDLED.



.. _`rproc_add_virtio_dev`:

rproc_add_virtio_dev
====================

.. c:function:: int rproc_add_virtio_dev (struct rproc_vdev *rvdev, int id)

    register an rproc-induced virtio device

    :param struct rproc_vdev \*rvdev:
        the remote vdev

    :param int id:

        *undescribed*



.. _`rproc_add_virtio_dev.description`:

Description
-----------

This function registers a virtio device. This vdev's partent is
the rproc device.

Returns 0 on success or an appropriate error value otherwise.



.. _`rproc_remove_virtio_dev`:

rproc_remove_virtio_dev
=======================

.. c:function:: void rproc_remove_virtio_dev (struct rproc_vdev *rvdev)

    remove an rproc-induced virtio device

    :param struct rproc_vdev \*rvdev:
        the remote vdev



.. _`rproc_remove_virtio_dev.description`:

Description
-----------

This function unregisters an existing virtio device.


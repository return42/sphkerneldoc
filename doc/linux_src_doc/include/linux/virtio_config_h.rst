.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/virtio_config.h

.. _`vq_callback_t`:

vq_callback_t
=============

.. c:function:: void vq_callback_t(struct virtqueue *)

    operations for configuring a virtio device

    :param struct virtqueue \*:
        *undescribed*

.. _`vq_callback_t.vdev`:

vdev
----

the virtio_device

the virtio_device

the virtio_device
Returns the config generation counter

the virtio_device
Returns the status byte

the virtio_device

the virtio device
After this, status and feature negotiation must be done again
Device must not be reset from its vq/config callbacks, or in
parallel with being added/removed.

the virtio_device

the virtio_device
Returns the first 32 feature bits (all we currently need).

the virtio_device

the virtio_device
This returns a pointer to the bus name a la pci_name from which
the caller can then copy.

.. _`vq_callback_t.offset`:

offset
------

the offset of the configuration field

the offset of the configuration field

.. _`vq_callback_t.buf`:

buf
---

the buffer to write the field value into.

the buffer to read the field value from.

.. _`vq_callback_t.len`:

len
---

the length of the buffer

the length of the buffer

.. _`vq_callback_t.status`:

status
------

the new status byte

.. _`vq_callback_t.nvqs`:

nvqs
----

the number of virtqueues to find

.. _`vq_callback_t.vqs`:

vqs
---

on success, includes new virtqueues

.. _`vq_callback_t.callbacks`:

callbacks
---------

array of callbacks, for each virtqueue
include a NULL entry for vqs that do not need a callback

.. _`vq_callback_t.names`:

names
-----

array of virtqueue names (mainly for debugging)
include a NULL entry for vqs unused by driver
Returns 0 on success or error status

.. _`vq_callback_t.this-gives-the-final-feature-bits-for-the-device`:

This gives the final feature bits for the device
------------------------------------------------

it can change
the dev->feature bits if it wants.
Returns 0 on success or error status

.. _`__virtio_test_bit`:

__virtio_test_bit
=================

.. c:function:: bool __virtio_test_bit(const struct virtio_device *vdev, unsigned int fbit)

    helper to test feature bits. For use by transports. Devices should normally use virtio_has_feature, which includes more checks.

    :param const struct virtio_device \*vdev:
        the device

    :param unsigned int fbit:
        the feature bit

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

.. _`virtio_has_feature`:

virtio_has_feature
==================

.. c:function:: bool virtio_has_feature(const struct virtio_device *vdev, unsigned int fbit)

    helper to determine if this device has this feature.

    :param const struct virtio_device \*vdev:
        the device

    :param unsigned int fbit:
        the feature bit

.. _`virtio_device_ready`:

virtio_device_ready
===================

.. c:function:: void virtio_device_ready(struct virtio_device *dev)

    enable vq use in probe function

    :param struct virtio_device \*dev:
        *undescribed*

.. _`virtio_device_ready.description`:

Description
-----------

Driver must call this to use vqs in the probe function.

.. _`virtio_device_ready.note`:

Note
----

vqs are enabled automatically after probe returns.

.. _`virtqueue_set_affinity`:

virtqueue_set_affinity
======================

.. c:function:: int virtqueue_set_affinity(struct virtqueue *vq, int cpu)

    setting affinity for a virtqueue

    :param struct virtqueue \*vq:
        the virtqueue

    :param int cpu:
        the cpu no.

.. _`virtqueue_set_affinity.description`:

Description
-----------

Pay attention the function are best-effort: the affinity hint may not be set
due to config support, irq type and sharing.

.. This file was automatic generated / don't edit.


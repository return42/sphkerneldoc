.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/xen-blkfront.c

.. _`blkfront_probe`:

blkfront_probe
==============

.. c:function:: int blkfront_probe(struct xenbus_device *dev, const struct xenbus_device_id *id)

    structures and the ring buffer for communication with the backend, and inform the backend of the appropriate details for those.  Switch to Initialised state.

    :param struct xenbus_device \*dev:
        *undescribed*

    :param const struct xenbus_device_id \*id:
        *undescribed*

.. _`blkfront_resume`:

blkfront_resume
===============

.. c:function:: int blkfront_resume(struct xenbus_device *dev)

    driver restart.  We tear down our blkif structure and recreate it, but leave the device-layer structures intact so that this is transparent to the rest of the kernel.

    :param struct xenbus_device \*dev:
        *undescribed*

.. _`blkback_changed`:

blkback_changed
===============

.. c:function:: void blkback_changed(struct xenbus_device *dev, enum xenbus_state backend_state)

    :param struct xenbus_device \*dev:
        *undescribed*

    :param enum xenbus_state backend_state:
        *undescribed*

.. This file was automatic generated / don't edit.


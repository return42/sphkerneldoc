.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/xen-netfront.c

.. _`netfront_probe`:

netfront_probe
==============

.. c:function:: int netfront_probe(struct xenbus_device *dev, const struct xenbus_device_id *id)

    structures and the ring buffers for communication with the backend, and inform the backend of the appropriate details for those.

    :param struct xenbus_device \*dev:
        *undescribed*

    :param const struct xenbus_device_id \*id:
        *undescribed*

.. _`netfront_resume`:

netfront_resume
===============

.. c:function:: int netfront_resume(struct xenbus_device *dev)

    driver restart.  We tear down our netif structure and recreate it, but leave the device-layer structures intact so that this is transparent to the rest of the kernel.

    :param struct xenbus_device \*dev:
        *undescribed*

.. _`netback_changed`:

netback_changed
===============

.. c:function:: void netback_changed(struct xenbus_device *dev, enum xenbus_state backend_state)

    :param struct xenbus_device \*dev:
        *undescribed*

    :param enum xenbus_state backend_state:
        *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/umc-dev.c

.. _`umc_device_create`:

umc_device_create
=================

.. c:function:: struct umc_dev *umc_device_create(struct device *parent, int n)

    allocate a child UMC device

    :param parent:
        parent of the new UMC device.
    :type parent: struct device \*

    :param n:
        index of the new device.
    :type n: int

.. _`umc_device_create.description`:

Description
-----------

The new UMC device will have a bus ID of the parent with '-n'
appended.

.. _`umc_device_register`:

umc_device_register
===================

.. c:function:: int umc_device_register(struct umc_dev *umc)

    register a UMC device

    :param umc:
        pointer to the UMC device
    :type umc: struct umc_dev \*

.. _`umc_device_register.description`:

Description
-----------

The memory resource for the UMC device is acquired and the device
registered with the system.

.. _`umc_device_unregister`:

umc_device_unregister
=====================

.. c:function:: void umc_device_unregister(struct umc_dev *umc)

    unregister a UMC device

    :param umc:
        pointer to the UMC device
    :type umc: struct umc_dev \*

.. _`umc_device_unregister.description`:

Description
-----------

First we unregister the device, make sure the driver can do it's
resource release thing and then we try to release any left over
resources. We take a ref to the device, to make sure it doesn't
disappear under our feet.

.. This file was automatic generated / don't edit.


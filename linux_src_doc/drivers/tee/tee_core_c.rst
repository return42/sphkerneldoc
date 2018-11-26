.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/tee_core.c

.. _`tee_device_alloc`:

tee_device_alloc
================

.. c:function:: struct tee_device *tee_device_alloc(const struct tee_desc *teedesc, struct device *dev, struct tee_shm_pool *pool, void *driver_data)

    Allocate a new struct tee_device instance

    :param teedesc:
        Descriptor for this driver
    :type teedesc: const struct tee_desc \*

    :param dev:
        Parent device for this device
    :type dev: struct device \*

    :param pool:
        Shared memory pool, NULL if not used
    :type pool: struct tee_shm_pool \*

    :param driver_data:
        Private driver data for this device
    :type driver_data: void \*

.. _`tee_device_alloc.description`:

Description
-----------

Allocates a new struct tee_device instance. The device is
removed by \ :c:func:`tee_device_unregister`\ .

\ ``returns``\  a pointer to a 'struct tee_device' or an ERR_PTR on failure

.. _`tee_device_register`:

tee_device_register
===================

.. c:function:: int tee_device_register(struct tee_device *teedev)

    Registers a TEE device

    :param teedev:
        Device to register
    :type teedev: struct tee_device \*

.. _`tee_device_register.description`:

Description
-----------

\ :c:func:`tee_device_unregister`\  need to be called to remove the \ ``teedev``\  if
this function fails.

\ ``returns``\  < 0 on failure

.. _`tee_device_unregister`:

tee_device_unregister
=====================

.. c:function:: void tee_device_unregister(struct tee_device *teedev)

    Removes a TEE device

    :param teedev:
        Device to unregister
    :type teedev: struct tee_device \*

.. _`tee_device_unregister.description`:

Description
-----------

This function should be called to remove the \ ``teedev``\  even if
\ :c:func:`tee_device_register`\  hasn't been called yet. Does nothing if
\ ``teedev``\  is NULL.

.. _`tee_get_drvdata`:

tee_get_drvdata
===============

.. c:function:: void *tee_get_drvdata(struct tee_device *teedev)

    Return driver_data pointer

    :param teedev:
        Device containing the driver_data pointer
        \ ``returns``\  the driver_data pointer supplied to \ :c:func:`tee_register`\ .
    :type teedev: struct tee_device \*

.. This file was automatic generated / don't edit.


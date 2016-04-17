.. -*- coding: utf-8; mode: rst -*-

===========
sdio_func.h
===========


.. _`sdio_device`:

SDIO_DEVICE
===========

.. c:function:: SDIO_DEVICE ( vend,  dev)

    macro used to describe a specific SDIO device

    :param vend:
        the 16 bit manufacturer code

    :param dev:
        the 16 bit function id



.. _`sdio_device.description`:

Description
-----------

This macro is used to create a struct sdio_device_id that matches a
specific device. The class field will be set to SDIO_ANY_ID.



.. _`sdio_device_class`:

SDIO_DEVICE_CLASS
=================

.. c:function:: SDIO_DEVICE_CLASS ( dev_class)

    macro used to describe a specific SDIO device class

    :param dev_class:
        the 8 bit standard interface code



.. _`sdio_device_class.description`:

Description
-----------

This macro is used to create a struct sdio_device_id that matches a
specific standard SDIO function type.  The vendor and device fields will
be set to SDIO_ANY_ID.


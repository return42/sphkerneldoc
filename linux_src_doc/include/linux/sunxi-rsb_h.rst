.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sunxi-rsb.h

.. _`sunxi_rsb_device`:

struct sunxi_rsb_device
=======================

.. c:type:: struct sunxi_rsb_device

    Basic representation of an RSB device

.. _`sunxi_rsb_device.definition`:

Definition
----------

.. code-block:: c

    struct sunxi_rsb_device {
        struct device dev;
        struct sunxi_rsb *rsb;
        int irq;
        u8 rtaddr;
        u16 hwaddr;
    }

.. _`sunxi_rsb_device.members`:

Members
-------

dev
    Driver model representation of the device.

rsb
    *undescribed*

irq
    *undescribed*

rtaddr
    This device's runtime address

hwaddr
    This device's hardware address

.. _`sunxi_rsb_driver`:

struct sunxi_rsb_driver
=======================

.. c:type:: struct sunxi_rsb_driver

    RSB slave device driver

.. _`sunxi_rsb_driver.definition`:

Definition
----------

.. code-block:: c

    struct sunxi_rsb_driver {
        struct device_driver driver;
        int (*probe)(struct sunxi_rsb_device *rdev);
        int (*remove)(struct sunxi_rsb_device *rdev);
    }

.. _`sunxi_rsb_driver.members`:

Members
-------

driver
    RSB device drivers should initialize name and owner field of
    this structure.

probe
    binds this driver to a RSB device.

remove
    unbinds this driver from the RSB device.

.. _`sunxi_rsb_driver_unregister`:

sunxi_rsb_driver_unregister
===========================

.. c:function:: void sunxi_rsb_driver_unregister(struct sunxi_rsb_driver *rdrv)

    unregister an RSB client driver

    :param rdrv:
        the driver to unregister
    :type rdrv: struct sunxi_rsb_driver \*

.. _`devm_regmap_init_sunxi_rsb`:

devm_regmap_init_sunxi_rsb
==========================

.. c:function::  devm_regmap_init_sunxi_rsb( rdev,  config)

    Initialise managed register map

    :param rdev:
        Device that will be interacted with
    :type rdev: 

    :param config:
        Configuration for register map
    :type config: 

.. _`devm_regmap_init_sunxi_rsb.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. This file was automatic generated / don't edit.


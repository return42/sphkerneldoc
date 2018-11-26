.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/uwb/umc.h

.. _`umc_dev`:

struct umc_dev
==============

.. c:type:: struct umc_dev

    UMC capability device

.. _`umc_dev.definition`:

Definition
----------

.. code-block:: c

    struct umc_dev {
        u16 version;
        u8 cap_id;
        u8 bar;
        struct resource resource;
        unsigned irq;
        struct device dev;
    }

.. _`umc_dev.members`:

Members
-------

version
    version of the specification this capability conforms to.

cap_id
    capability ID.

bar
    PCI Bar (64 bit) where the resource lies

resource
    register space resource.

irq
    interrupt line.

dev
    *undescribed*

.. _`umc_driver`:

struct umc_driver
=================

.. c:type:: struct umc_driver

    UMC capability driver

.. _`umc_driver.definition`:

Definition
----------

.. code-block:: c

    struct umc_driver {
        char *name;
        u8 cap_id;
        int (*match)(struct umc_driver *, struct umc_dev *);
        const void *match_data;
        int (*probe)(struct umc_dev *);
        void (*remove)(struct umc_dev *);
        int (*pre_reset)(struct umc_dev *);
        int (*post_reset)(struct umc_dev *);
        struct device_driver driver;
    }

.. _`umc_driver.members`:

Members
-------

name
    *undescribed*

cap_id
    supported capability ID.

match
    driver specific capability matching function.

match_data
    driver specific data for \ :c:func:`match`\  (e.g., a
    table of pci_device_id's if \ :c:func:`umc_match_pci_id`\  is used).

probe
    *undescribed*

remove
    *undescribed*

pre_reset
    *undescribed*

post_reset
    *undescribed*

driver
    *undescribed*

.. _`umc_driver_register`:

umc_driver_register
===================

.. c:function::  umc_driver_register( umc_drv)

    register a UMC capabiltity driver.

    :param umc_drv:
        pointer to the driver.
    :type umc_drv: 

.. _`umc_parent_pci_dev`:

umc_parent_pci_dev
==================

.. c:function:: struct pci_dev *umc_parent_pci_dev(struct umc_dev *umc_dev)

    return the UMC's parent PCI device or NULL if none

    :param umc_dev:
        UMC device whose parent PCI device we are looking for
    :type umc_dev: struct umc_dev \*

.. _`umc_parent_pci_dev.description`:

Description
-----------

DIRTY!!! DON'T RELY ON THIS

.. _`umc_parent_pci_dev.fixme`:

FIXME
-----

This is as dirty as it gets, but we need some way to check
the correct type of umc_dev->parent (so that for example, we can
cast to pci_dev). Casting to pci_dev is necessary because at some
point we need to request resources from the device. Mapping is
easily over come (ioremap and stuff are bus agnostic), but hooking
up to some error handlers (such as pci error handlers) might need
this.

THIS might (probably will) be removed in the future, so don't count
on it.

.. _`umc_dev_get`:

umc_dev_get
===========

.. c:function:: struct umc_dev *umc_dev_get(struct umc_dev *umc_dev)

    reference a UMC device.

    :param umc_dev:
        Pointer to UMC device.
    :type umc_dev: struct umc_dev \*

.. _`umc_dev_get.note`:

NOTE
----

we are assuming in this whole scheme that the parent device
is referenced at \_probe() time and unreferenced at \_remove()
time by the parent's subsystem.

.. _`umc_dev_put`:

umc_dev_put
===========

.. c:function:: void umc_dev_put(struct umc_dev *umc_dev)

    unreference a UMC device.

    :param umc_dev:
        Pointer to UMC device.
    :type umc_dev: struct umc_dev \*

.. _`umc_set_drvdata`:

umc_set_drvdata
===============

.. c:function:: void umc_set_drvdata(struct umc_dev *umc_dev, void *data)

    set UMC device's driver data.

    :param umc_dev:
        Pointer to UMC device.
    :type umc_dev: struct umc_dev \*

    :param data:
        Data to set.
    :type data: void \*

.. _`umc_get_drvdata`:

umc_get_drvdata
===============

.. c:function:: void *umc_get_drvdata(struct umc_dev *umc_dev)

    recover UMC device's driver data.

    :param umc_dev:
        Pointer to UMC device.
    :type umc_dev: struct umc_dev \*

.. This file was automatic generated / don't edit.


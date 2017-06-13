.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/vme.h

.. _`vme_dev`:

struct vme_dev
==============

.. c:type:: struct vme_dev

    Structure representing a VME device

.. _`vme_dev.definition`:

Definition
----------

.. code-block:: c

    struct vme_dev {
        int num;
        struct vme_bridge *bridge;
        struct device dev;
        struct list_head drv_list;
        struct list_head bridge_list;
    }

.. _`vme_dev.members`:

Members
-------

num
    The device number

bridge
    Pointer to the bridge device this device is on

dev
    Internal device structure

drv_list
    List of devices (per driver)

bridge_list
    List of devices (per bridge)

.. _`vme_driver`:

struct vme_driver
=================

.. c:type:: struct vme_driver

    Structure representing a VME driver

.. _`vme_driver.definition`:

Definition
----------

.. code-block:: c

    struct vme_driver {
        const char *name;
        int (*match)(struct vme_dev *);
        int (*probe)(struct vme_dev *);
        int (*remove)(struct vme_dev *);
        struct device_driver driver;
        struct list_head devices;
    }

.. _`vme_driver.members`:

Members
-------

name
    Driver name, should be unique among VME drivers and usually the same
    as the module name.

match
    Callback used to determine whether probe should be run.

probe
    Callback for device binding, called when new device is detected.

remove
    Callback, called on device removal.

driver
    Underlying generic device driver structure.

devices
    List of VME devices (struct vme_dev) associated with this driver.

.. This file was automatic generated / don't edit.


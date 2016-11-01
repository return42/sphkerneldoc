.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mcb.h

.. _`mcb_bus`:

struct mcb_bus
==============

.. c:type:: struct mcb_bus

    MEN Chameleon Bus

.. _`mcb_bus.definition`:

Definition
----------

.. code-block:: c

    struct mcb_bus {
        struct device dev;
        struct device *carrier;
        int bus_nr;
        u8 revision;
        char model;
        u8 minor;
        char name[CHAMELEON_FILENAME_LEN + 1];
        int (*get_irq)(struct mcb_device *dev);
    }

.. _`mcb_bus.members`:

Members
-------

dev
    bus device

carrier
    pointer to carrier device

bus_nr
    mcb bus number

revision
    the FPGA's revision number

model
    the FPGA's model number

minor
    *undescribed*

get_irq
    callback to get IRQ number

.. _`mcb_device`:

struct mcb_device
=================

.. c:type:: struct mcb_device

    MEN Chameleon Bus device

.. _`mcb_device.definition`:

Definition
----------

.. code-block:: c

    struct mcb_device {
        struct device dev;
        struct mcb_bus *bus;
        bool is_added;
        struct mcb_driver *driver;
        u16 id;
        int inst;
        int group;
        int var;
        int bar;
        int rev;
        struct resource irq;
        struct resource mem;
        struct device *dma_dev;
    }

.. _`mcb_device.members`:

Members
-------

dev
    device in kernel representation

bus
    mcb bus the device is plugged to

is_added
    flag to check if device is added to bus

driver
    associated mcb_driver

id
    mcb device id

inst
    instance in Chameleon table

group
    group in Chameleon table

var
    variant in Chameleon table

bar
    BAR in Chameleon table

rev
    revision in Chameleon table

irq
    IRQ resource

mem
    *undescribed*

dma_dev
    *undescribed*

.. _`mcb_driver`:

struct mcb_driver
=================

.. c:type:: struct mcb_driver

    MEN Chameleon Bus device driver

.. _`mcb_driver.definition`:

Definition
----------

.. code-block:: c

    struct mcb_driver {
        struct device_driver driver;
        const struct mcb_device_id *id_table;
        int (*probe)(struct mcb_device *mdev, const struct mcb_device_id *id);
        void (*remove)(struct mcb_device *mdev);
        void (*shutdown)(struct mcb_device *mdev);
    }

.. _`mcb_driver.members`:

Members
-------

driver
    device_driver

id_table
    mcb id table

probe
    probe callback

remove
    remove callback

shutdown
    shutdown callback

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/ccwdev.h

.. _`ccw_device`:

struct ccw_device
=================

.. c:type:: struct ccw_device

    channel attached device

.. _`ccw_device.definition`:

Definition
----------

.. code-block:: c

    struct ccw_device {
        spinlock_t *ccwlock;
        struct ccw_device_id id;
        struct ccw_driver *drv;
        struct device dev;
        int online;
        void (*handler) (struct ccw_device *, unsigned long, struct irb *);
    }

.. _`ccw_device.members`:

Members
-------

ccwlock
    pointer to device lock

id
    id of this device

drv
    ccw driver for this device

dev
    embedded device structure

online
    online status of device

handler
    interrupt handler

.. _`ccw_device.description`:

Description
-----------

\ ``handler``\  is a member of the device rather than the driver since a driver
can have different interrupt handlers for different ccw devices
(multi-subchannel drivers).

.. _`ccw_driver`:

struct ccw_driver
=================

.. c:type:: struct ccw_driver

    device driver for channel attached devices

.. _`ccw_driver.definition`:

Definition
----------

.. code-block:: c

    struct ccw_driver {
        struct ccw_device_id *ids;
        int (*probe) (struct ccw_device *);
        void (*remove) (struct ccw_device *);
        int (*set_online) (struct ccw_device *);
        int (*set_offline) (struct ccw_device *);
        int (*notify) (struct ccw_device *, int);
        void (*path_event) (struct ccw_device *, int *);
        void (*shutdown) (struct ccw_device *);
        int (*prepare) (struct ccw_device *);
        void (*complete) (struct ccw_device *);
        int (*freeze)(struct ccw_device *);
        int (*thaw) (struct ccw_device *);
        int (*restore)(struct ccw_device *);
        enum uc_todo (*uc_handler) (struct ccw_device *, struct irb *);
        struct device_driver driver;
        enum interruption_class int_class;
    }

.. _`ccw_driver.members`:

Members
-------

ids
    ids supported by this driver

probe
    function called on probe

remove
    function called on remove

set_online
    called when setting device online

set_offline
    called when setting device offline

notify
    notify driver of device state changes

path_event
    notify driver of channel path events

shutdown
    called at device shutdown

prepare
    prepare for pm state transition

complete
    undo work done in \ ``prepare``\ 

freeze
    callback for freezing during hibernation snapshotting

thaw
    undo work done in \ ``freeze``\ 

restore
    callback for restoring after hibernation

uc_handler
    callback for unit check handler

driver
    embedded device driver structure

int_class
    interruption class to use for accounting interrupts

.. This file was automatic generated / don't edit.


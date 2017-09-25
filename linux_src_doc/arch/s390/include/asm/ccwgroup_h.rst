.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/ccwgroup.h

.. _`ccwgroup_device`:

struct ccwgroup_device
======================

.. c:type:: struct ccwgroup_device

    ccw group device

.. _`ccwgroup_device.definition`:

Definition
----------

.. code-block:: c

    struct ccwgroup_device {
        enum {
            CCWGROUP_OFFLINE,CCWGROUP_ONLINE, } state;
            atomic_t onoff;
            struct mutex reg_mutex;
            unsigned int count;
            struct device dev;
            struct work_struct ungroup_work;
            struct ccw_device *cdev[0];
    }

.. _`ccwgroup_device.members`:

Members
-------

state
    online/offline state

onoff
    *undescribed*

reg_mutex
    *undescribed*

count
    number of attached slave devices

dev
    embedded device structure

ungroup_work
    work to be done when a ccwgroup notifier has action
    type \ ``BUS_NOTIFY_UNBIND_DRIVER``\ 

cdev
    variable number of slave devices, allocated as needed

.. _`ccwgroup_driver`:

struct ccwgroup_driver
======================

.. c:type:: struct ccwgroup_driver

    driver for ccw group devices

.. _`ccwgroup_driver.definition`:

Definition
----------

.. code-block:: c

    struct ccwgroup_driver {
        int (*setup) (struct ccwgroup_device *);
        void (*remove) (struct ccwgroup_device *);
        int (*set_online) (struct ccwgroup_device *);
        int (*set_offline) (struct ccwgroup_device *);
        void (*shutdown)(struct ccwgroup_device *);
        int (*prepare) (struct ccwgroup_device *);
        void (*complete) (struct ccwgroup_device *);
        int (*freeze)(struct ccwgroup_device *);
        int (*thaw) (struct ccwgroup_device *);
        int (*restore)(struct ccwgroup_device *);
        struct device_driver driver;
    }

.. _`ccwgroup_driver.members`:

Members
-------

setup
    function called during device creation to setup the device

remove
    function called on remove

set_online
    function called when device is set online

set_offline
    function called when device is set offline

shutdown
    function called when device is shut down

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

driver
    embedded driver structure

.. This file was automatic generated / don't edit.


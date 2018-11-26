.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/typec_altmode.h

.. _`typec_altmode`:

struct typec_altmode
====================

.. c:type:: struct typec_altmode

    USB Type-C alternate mode device

.. _`typec_altmode.definition`:

Definition
----------

.. code-block:: c

    struct typec_altmode {
        struct device dev;
        u16 svid;
        int mode;
        u32 vdo;
        unsigned int active:1;
        char *desc;
        const struct typec_altmode_ops *ops;
    }

.. _`typec_altmode.members`:

Members
-------

dev
    Driver model's view of this device

svid
    Standard or Vendor ID (SVID) of the alternate mode

mode
    Index of the Mode

vdo
    VDO returned by Discover Modes USB PD command

active
    Tells has the mode been entered or not

desc
    Optional human readable description of the mode

ops
    Operations vector from the driver

.. _`typec_altmode_ops`:

struct typec_altmode_ops
========================

.. c:type:: struct typec_altmode_ops

    Alternate mode specific operations vector

.. _`typec_altmode_ops.definition`:

Definition
----------

.. code-block:: c

    struct typec_altmode_ops {
        int (*enter)(struct typec_altmode *altmode);
        int (*exit)(struct typec_altmode *altmode);
        void (*attention)(struct typec_altmode *altmode, u32 vdo);
        int (*vdm)(struct typec_altmode *altmode, const u32 hdr, const u32 *vdo, int cnt);
        int (*notify)(struct typec_altmode *altmode, unsigned long conf, void *data);
        int (*activate)(struct typec_altmode *altmode, int activate);
    }

.. _`typec_altmode_ops.members`:

Members
-------

enter
    Operations to be executed with Enter Mode Command

exit
    Operations to be executed with Exit Mode Command

attention
    Callback for Attention Command

vdm
    Callback for SVID specific commands

notify
    Communication channel for platform and the alternate mode

activate
    User callback for Enter/Exit Mode

.. _`typec_altmode_get_orientation`:

typec_altmode_get_orientation
=============================

.. c:function:: enum typec_orientation typec_altmode_get_orientation(struct typec_altmode *altmode)

    Get cable plug orientation

    :param altmode:
        *undescribed*
    :type altmode: struct typec_altmode \*

.. _`typec_altmode_get_orientation.altmode`:

altmode
-------

Handle to the alternate mode

.. _`typec_altmode_driver`:

struct typec_altmode_driver
===========================

.. c:type:: struct typec_altmode_driver

    USB Type-C alternate mode device driver

.. _`typec_altmode_driver.definition`:

Definition
----------

.. code-block:: c

    struct typec_altmode_driver {
        const struct typec_device_id *id_table;
        int (*probe)(struct typec_altmode *altmode);
        void (*remove)(struct typec_altmode *altmode);
        struct device_driver driver;
    }

.. _`typec_altmode_driver.members`:

Members
-------

id_table
    Null terminated array of SVIDs

probe
    Callback for device binding

remove
    Callback for device unbinding

driver
    Device driver model driver

.. _`typec_altmode_driver.description`:

Description
-----------

These drivers will be bind to the partner alternate mode devices. They will
handle all SVID specific communication.

.. This file was automatic generated / don't edit.


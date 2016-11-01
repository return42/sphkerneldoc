.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/extcon.h

.. _`extcon_dev`:

struct extcon_dev
=================

.. c:type:: struct extcon_dev

    An extcon device represents one external connector.

.. _`extcon_dev.definition`:

Definition
----------

.. code-block:: c

    struct extcon_dev {
        const char *name;
        const unsigned int *supported_cable;
        const u32 *mutually_exclusive;
        struct device dev;
        struct raw_notifier_head *nh;
        struct list_head entry;
        int max_supported;
        spinlock_t lock;
        u32 state;
        struct device_type extcon_dev_type;
        struct extcon_cable *cables;
        struct attribute_group attr_g_muex;
        struct attribute **attrs_muex;
        struct device_attribute *d_attrs_muex;
    }

.. _`extcon_dev.members`:

Members
-------

name
    The name of this extcon device. Parent device name is
    used if NULL.

supported_cable
    Array of supported cable names ending with EXTCON_NONE.
    If supported_cable is NULL, cable name related APIs
    are disabled.

mutually_exclusive
    Array of mutually exclusive set of cables that cannot
    be attached simultaneously. The array should be
    ending with NULL or be NULL (no mutually exclusive
    cables). For example, if it is { 0x7, 0x30, 0}, then,
    {0, 1}, {0, 1, 2}, {0, 2}, {1, 2}, or {4, 5} cannot
    be attached simulataneously. {0x7, 0} is equivalent to
    {0x3, 0x6, 0x5, 0}. If it is {0xFFFFFFFF, 0}, there
    can be no simultaneous connections.

dev
    Device of this extcon.

nh
    Notifier for the state change events from this extcon

entry
    To support list of extcon devices so that users can
    search for extcon devices based on the extcon name.

max_supported
    Internal value to store the number of cables.

lock
    *undescribed*

state
    Attach/detach state of this extcon. Do not provide at
    register-time.

extcon_dev_type
    Device_type struct to provide attribute_groups
    customized for each extcon device.

cables
    Sysfs subdirectories. Each represents one cable.

attr_g_muex
    *undescribed*

attrs_muex
    *undescribed*

d_attrs_muex
    *undescribed*

.. _`extcon_dev.description`:

Description
-----------

In most cases, users only need to provide "User initializing data" of
this struct when registering an extcon. In some exceptional cases,
optional callbacks may be needed. However, the values in "internal data"
are overwritten by register function.

.. This file was automatic generated / don't edit.


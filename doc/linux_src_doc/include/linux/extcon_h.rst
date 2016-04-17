.. -*- coding: utf-8; mode: rst -*-

========
extcon.h
========


.. _`extcon_dev`:

struct extcon_dev
=================

.. c:type:: extcon_dev

    An extcon device represents one external connector.


.. _`extcon_dev.definition`:

Definition
----------

.. code-block:: c

  struct extcon_dev {
    const char * name;
    const unsigned int * supported_cable;
    const u32 * mutually_exclusive;
    struct device dev;
    struct raw_notifier_head * nh;
    struct list_head entry;
    int max_supported;
    u32 state;
    struct device_type extcon_dev_type;
    struct extcon_cable * cables;
  };


.. _`extcon_dev.members`:

Members
-------

:``name``:
    The name of this extcon device. Parent device name is
    used if NULL.

:``supported_cable``:
    Array of supported cable names ending with EXTCON_NONE.
    If supported_cable is NULL, cable name related APIs
    are disabled.

:``mutually_exclusive``:
    Array of mutually exclusive set of cables that cannot
    be attached simultaneously. The array should be
    ending with NULL or be NULL (no mutually exclusive
    cables). For example, if it is { 0x7, 0x30, 0}, then,
    {0, 1}, {0, 1, 2}, {0, 2}, {1, 2}, or {4, 5} cannot
    be attached simulataneously. {0x7, 0} is equivalent to
    {0x3, 0x6, 0x5, 0}. If it is {0xFFFFFFFF, 0}, there
    can be no simultaneous connections.

:``dev``:
    Device of this extcon.

:``nh``:
    Notifier for the state change events from this extcon

:``entry``:
    To support list of extcon devices so that users can
    search for extcon devices based on the extcon name.

:``max_supported``:
    Internal value to store the number of cables.

:``state``:
    Attach/detach state of this extcon. Do not provide at
    register-time.

:``extcon_dev_type``:
    Device_type struct to provide attribute_groups
    customized for each extcon device.

:``cables``:
    Sysfs subdirectories. Each represents one cable.




.. _`extcon_dev.description`:

Description
-----------

In most cases, users only need to provide "User initializing data" of
this struct when registering an extcon. In some exceptional cases,
optional callbacks may be needed. However, the values in "internal data"
are overwritten by register function.



.. _`extcon_cable`:

struct extcon_cable
===================

.. c:type:: extcon_cable

    An internal data for each cable of extcon device.


.. _`extcon_cable.definition`:

Definition
----------

.. code-block:: c

  struct extcon_cable {
    struct extcon_dev * edev;
    int cable_index;
    struct attribute_group attr_g;
    struct device_attribute attr_name;
    struct device_attribute attr_state;
    struct attribute * attrs[3];
  };


.. _`extcon_cable.members`:

Members
-------

:``edev``:
    The extcon device

:``cable_index``:
    Index of this cable in the edev

:``attr_g``:
    Attribute group for the cable

:``attr_name``:
    "name" sysfs entry

:``attr_state``:
    "state" sysfs entry

:``attrs[3]``:
    Array pointing to attr_name and attr_state for attr_g




.. _`extcon_specific_cable_nb`:

struct extcon_specific_cable_nb
===============================

.. c:type:: extcon_specific_cable_nb

    An internal data for extcon_register_interest().


.. _`extcon_specific_cable_nb.definition`:

Definition
----------

.. code-block:: c

  struct extcon_specific_cable_nb {
    struct notifier_block * user_nb;
    int cable_index;
    struct extcon_dev * edev;
    unsigned long previous_value;
  };


.. _`extcon_specific_cable_nb.members`:

Members
-------

:``user_nb``:
    user provided notifier block for events from
    a specific cable.

:``cable_index``:
    the target cable.

:``edev``:
    the target extcon device.

:``previous_value``:
    the saved previous event value.



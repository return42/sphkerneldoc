.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/rfkill.h

.. _`rfkill_type`:

enum rfkill_type
================

.. c:type:: enum rfkill_type

    type of rfkill switch.

.. _`rfkill_type.definition`:

Definition
----------

.. code-block:: c

    enum rfkill_type {
        RFKILL_TYPE_ALL,
        RFKILL_TYPE_WLAN,
        RFKILL_TYPE_BLUETOOTH,
        RFKILL_TYPE_UWB,
        RFKILL_TYPE_WIMAX,
        RFKILL_TYPE_WWAN,
        RFKILL_TYPE_GPS,
        RFKILL_TYPE_FM,
        RFKILL_TYPE_NFC,
        NUM_RFKILL_TYPES
    };

.. _`rfkill_type.constants`:

Constants
---------

RFKILL_TYPE_ALL
    toggles all switches (requests only - not a switch type)

RFKILL_TYPE_WLAN
    switch is on a 802.11 wireless network device.

RFKILL_TYPE_BLUETOOTH
    switch is on a bluetooth device.

RFKILL_TYPE_UWB
    switch is on a ultra wideband device.

RFKILL_TYPE_WIMAX
    switch is on a WiMAX device.

RFKILL_TYPE_WWAN
    switch is on a wireless WAN device.

RFKILL_TYPE_GPS
    switch is on a GPS device.

RFKILL_TYPE_FM
    switch is on a FM radio device.

RFKILL_TYPE_NFC
    switch is on an NFC device.

NUM_RFKILL_TYPES
    number of defined rfkill types

.. _`rfkill_operation`:

enum rfkill_operation
=====================

.. c:type:: enum rfkill_operation

    operation types

.. _`rfkill_operation.definition`:

Definition
----------

.. code-block:: c

    enum rfkill_operation {
        RFKILL_OP_ADD,
        RFKILL_OP_DEL,
        RFKILL_OP_CHANGE,
        RFKILL_OP_CHANGE_ALL
    };

.. _`rfkill_operation.constants`:

Constants
---------

RFKILL_OP_ADD
    a device was added

RFKILL_OP_DEL
    a device was removed

RFKILL_OP_CHANGE
    a device's state changed -- userspace changes one device

RFKILL_OP_CHANGE_ALL
    userspace changes all devices (of a type, or all)
    into a state, also updating the default state used for devices that
    are hot-plugged later.

.. _`rfkill_event`:

struct rfkill_event
===================

.. c:type:: struct rfkill_event

    events for userspace on /dev/rfkill

.. _`rfkill_event.definition`:

Definition
----------

.. code-block:: c

    struct rfkill_event {
        __u32 idx;
        __u8 type;
        __u8 op;
        __u8 soft, hard;
    }

.. _`rfkill_event.members`:

Members
-------

idx
    index of dev rfkill

type
    type of the rfkill struct

op
    operation code

soft
    soft state (0/1)

hard
    hard state (0/1)

.. _`rfkill_event.description`:

Description
-----------

Structure used for userspace communication on /dev/rfkill,
used for events from the kernel and control to the kernel.

.. This file was automatic generated / don't edit.


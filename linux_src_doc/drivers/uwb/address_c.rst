.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/address.c

.. _`uwb_rc_dev_addr_mgmt`:

uwb_rc_dev_addr_mgmt
====================

.. c:function:: int uwb_rc_dev_addr_mgmt(struct uwb_rc *rc, u8 bmOperationType, const u8 *baAddr, struct uwb_rc_evt_dev_addr_mgmt *reply)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param bmOperationType:
        Set/get, MAC/DEV (see WUSB1.0[8.6.2.2])
    :type bmOperationType: u8

    :param baAddr:
        address buffer--assumed to have enough data to hold
        the address type requested.
    :type baAddr: const u8 \*

    :param reply:
        Pointer to reply buffer (can be stack allocated)
    :type reply: struct uwb_rc_evt_dev_addr_mgmt \*

.. _`uwb_rc_dev_addr_mgmt.description`:

Description
-----------

\ ``cmd``\  has to be allocated because USB cannot grok USB or vmalloc
buffers depending on your combination of host architecture.

.. _`uwb_rc_addr_set`:

uwb_rc_addr_set
===============

.. c:function:: int uwb_rc_addr_set(struct uwb_rc *rc, const void *_addr, enum uwb_addr_type type)

    :param rc:
        UWB Radio Controller
    :type rc: struct uwb_rc \*

    :param _addr:
        Pointer to address to write [assumed to be either a
        'struct uwb_mac_addr \*' or a 'struct uwb_dev_addr \*'].
    :type _addr: const void \*

    :param type:
        Type of address to set (UWB_ADDR_DEV or UWB_ADDR_MAC).
    :type type: enum uwb_addr_type

.. _`uwb_rc_addr_set.some-anal-retentivity-here`:

Some anal retentivity here
--------------------------

even if both 'struct
uwb_{dev,mac}_addr' have the actual byte array in the same offset
and I could just pass \_addr to \ :c:func:`hwarc_cmd_dev_addr_mgmt`\ , I prefer
to use some syntatic sugar in case someday we decide to change the
format of the structs. The compiler will optimize it out anyway.

.. _`uwb_rc_addr_get`:

uwb_rc_addr_get
===============

.. c:function:: int uwb_rc_addr_get(struct uwb_rc *rc, void *_addr, enum uwb_addr_type type)

    :param rc:
        UWB Radio Controller
    :type rc: struct uwb_rc \*

    :param _addr:
        Where to write the address data [assumed to be either a
        'struct uwb_mac_addr \*' or a 'struct uwb_dev_addr \*'].
    :type _addr: void \*

    :param type:
        Type of address to get (UWB_ADDR_DEV or UWB_ADDR_MAC).
    :type type: enum uwb_addr_type

.. _`uwb_rc_addr_get.description`:

Description
-----------

See comment in \ :c:func:`uwb_rc_addr_set`\  about anal retentivity in the
type handling of the address variables.

.. _`uwb_rc_dev_addr_assign`:

uwb_rc_dev_addr_assign
======================

.. c:function:: int uwb_rc_dev_addr_assign(struct uwb_rc *rc)

    assigned a generated DevAddr to a radio controller

    :param rc:
        the (local) radio controller device requiring a new DevAddr
    :type rc: struct uwb_rc \*

.. _`uwb_rc_dev_addr_assign.a-new-devaddr-is-required-when`:

A new DevAddr is required when
------------------------------

- first setting up a radio controller
- if the hardware reports a DevAddr conflict

The DevAddr is randomly generated in the generated DevAddr range
[0x100, 0xfeff]. The number of devices in a beacon group is limited
by mMaxBPLength (96) so this address space will never be exhausted.

[ECMA-368] 17.1.1, 17.16.

.. _`uwbd_evt_handle_rc_dev_addr_conflict`:

uwbd_evt_handle_rc_dev_addr_conflict
====================================

.. c:function:: int uwbd_evt_handle_rc_dev_addr_conflict(struct uwb_event *evt)

    handle a DEV_ADDR_CONFLICT event

    :param evt:
        the DEV_ADDR_CONFLICT notification from the radio controller
    :type evt: struct uwb_event \*

.. _`uwbd_evt_handle_rc_dev_addr_conflict.description`:

Description
-----------

A new (non-conflicting) DevAddr is assigned to the radio controller.

[ECMA-368] 17.1.1.1.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/beacon.c

.. _`uwb_dev_get_by_devaddr`:

uwb_dev_get_by_devaddr
======================

.. c:function:: struct uwb_dev *uwb_dev_get_by_devaddr(struct uwb_rc *rc, const struct uwb_dev_addr *devaddr)

    get a UWB device with a specific DevAddr

    :param rc:
        the radio controller that saw the device
    :type rc: struct uwb_rc \*

    :param devaddr:
        DevAddr of the UWB device to find
    :type devaddr: const struct uwb_dev_addr \*

.. _`uwb_dev_get_by_devaddr.description`:

Description
-----------

There may be more than one matching device (in the case of a
DevAddr conflict), but only the first one is returned.

.. _`uwb_dev_get_by_macaddr`:

uwb_dev_get_by_macaddr
======================

.. c:function:: struct uwb_dev *uwb_dev_get_by_macaddr(struct uwb_rc *rc, const struct uwb_mac_addr *macaddr)

    get a UWB device with a specific EUI-48

    :param rc:
        the radio controller that saw the device
    :type rc: struct uwb_rc \*

    :param macaddr:
        *undescribed*
    :type macaddr: const struct uwb_mac_addr \*

.. _`uwbd_evt_handle_rc_bp_slot_change`:

uwbd_evt_handle_rc_bp_slot_change
=================================

.. c:function:: int uwbd_evt_handle_rc_bp_slot_change(struct uwb_event *evt)

    handle a BP_SLOT_CHANGE event

    :param evt:
        the BP_SLOT_CHANGE notification from the radio controller
    :type evt: struct uwb_event \*

.. _`uwbd_evt_handle_rc_bp_slot_change.description`:

Description
-----------

If the event indicates that no beacon period slots were available
then radio controller has transitioned to a non-beaconing state.
Otherwise, simply save the current beacon slot.

.. This file was automatic generated / don't edit.


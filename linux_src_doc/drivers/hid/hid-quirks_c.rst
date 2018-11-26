.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-quirks.c

.. _`hid_exists_dquirk`:

hid_exists_dquirk
=================

.. c:function:: struct hid_device_id *hid_exists_dquirk(const struct hid_device *hdev)

    find any dynamic quirks for a HID device

    :param hdev:
        the HID device to match
    :type hdev: const struct hid_device \*

.. _`hid_exists_dquirk.description`:

Description
-----------

Scans dquirks_list for a matching dynamic quirk and returns
the pointer to the relevant struct hid_device_id if found.
Must be called with a read lock held on dquirks_lock.

.. _`hid_exists_dquirk.return`:

Return
------

NULL if no quirk found, struct hid_device_id \* if found.

.. _`hid_modify_dquirk`:

hid_modify_dquirk
=================

.. c:function:: int hid_modify_dquirk(const struct hid_device_id *id, const unsigned long quirks)

    add/replace a HID quirk

    :param id:
        the HID device to match
    :type id: const struct hid_device_id \*

    :param quirks:
        the unsigned long quirks value to add/replace
    :type quirks: const unsigned long

.. _`hid_modify_dquirk.description`:

Description
-----------

If an dynamic quirk exists in memory for this device, replace its
quirks value with what was provided.  Otherwise, add the quirk
to the dynamic quirks list.

.. _`hid_modify_dquirk.return`:

Return
------

0 OK, -error on failure.

.. _`hid_remove_all_dquirks`:

hid_remove_all_dquirks
======================

.. c:function:: void hid_remove_all_dquirks(__u16 bus)

    remove all runtime HID quirks from memory

    :param bus:
        bus to match against. Use HID_BUS_ANY if all need to be removed.
    :type bus: __u16

.. _`hid_remove_all_dquirks.description`:

Description
-----------

Free all memory associated with dynamic quirks - called before
module unload.

.. _`hid_quirks_init`:

hid_quirks_init
===============

.. c:function:: int hid_quirks_init(char **quirks_param, __u16 bus, int count)

    apply HID quirks specified at module load time

    :param quirks_param:
        *undescribed*
    :type quirks_param: char \*\*

    :param bus:
        *undescribed*
    :type bus: __u16

    :param count:
        *undescribed*
    :type count: int

.. _`hid_quirks_exit`:

hid_quirks_exit
===============

.. c:function:: void hid_quirks_exit(__u16 bus)

    release memory associated with dynamic_quirks

    :param bus:
        a bus to match against
    :type bus: __u16

.. _`hid_quirks_exit.description`:

Description
-----------

Release all memory associated with dynamic quirks for a given bus.
Called upon module unload.
Use HID_BUS_ANY to remove all dynamic quirks.

.. _`hid_quirks_exit.return`:

Return
------

nothing

.. _`hid_gets_squirk`:

hid_gets_squirk
===============

.. c:function:: unsigned long hid_gets_squirk(const struct hid_device *hdev)

    return any static quirks for a HID device

    :param hdev:
        the HID device to match
    :type hdev: const struct hid_device \*

.. _`hid_gets_squirk.description`:

Description
-----------

Given a HID device, return a pointer to the quirked hid_device_id entry
associated with that device.

.. _`hid_gets_squirk.return`:

Return
------

the quirks.

.. _`hid_lookup_quirk`:

hid_lookup_quirk
================

.. c:function:: unsigned long hid_lookup_quirk(const struct hid_device *hdev)

    return any quirks associated with a HID device

    :param hdev:
        the HID device to look for
    :type hdev: const struct hid_device \*

.. _`hid_lookup_quirk.description`:

Description
-----------

Given a HID device, return any quirks associated with that device.

.. _`hid_lookup_quirk.return`:

Return
------

an unsigned long quirks value.

.. This file was automatic generated / don't edit.


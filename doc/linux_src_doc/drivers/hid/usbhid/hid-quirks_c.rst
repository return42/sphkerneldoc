.. -*- coding: utf-8; mode: rst -*-

============
hid-quirks.c
============


.. _`usbhid_exists_dquirk`:

usbhid_exists_dquirk
====================

.. c:function:: struct hid_blacklist *usbhid_exists_dquirk (const u16 idVendor, const u16 idProduct)

    :param const u16 idVendor:
        the 16-bit USB vendor ID, in native byteorder

    :param const u16 idProduct:
        the 16-bit USB product ID, in native byteorder



.. _`usbhid_exists_dquirk.description`:

Description
-----------

Scans dquirks_list for a matching dynamic quirk and returns
the pointer to the relevant struct hid_blacklist if found.
Must be called with a read lock held on dquirks_rwsem.



.. _`usbhid_exists_dquirk.returns`:

Returns
-------

NULL if no quirk found, struct hid_blacklist * if found.



.. _`usbhid_modify_dquirk`:

usbhid_modify_dquirk
====================

.. c:function:: int usbhid_modify_dquirk (const u16 idVendor, const u16 idProduct, const u32 quirks)

    :param const u16 idVendor:
        the 16-bit USB vendor ID, in native byteorder

    :param const u16 idProduct:
        the 16-bit USB product ID, in native byteorder

    :param const u32 quirks:
        the u32 quirks value to add/replace



.. _`usbhid_modify_dquirk.description`:

Description
-----------

If an dynamic quirk exists in memory for this (idVendor,
idProduct) pair, replace its quirks value with what was
provided.  Otherwise, add the quirk to the dynamic quirks list.



.. _`usbhid_modify_dquirk.returns`:

Returns
-------

0 OK, -error on failure.



.. _`usbhid_remove_all_dquirks`:

usbhid_remove_all_dquirks
=========================

.. c:function:: void usbhid_remove_all_dquirks ( void)

    :param void:
        no arguments



.. _`usbhid_remove_all_dquirks.description`:

Description
-----------

Free all memory associated with dynamic quirks - called before
module unload.



.. _`usbhid_quirks_init`:

usbhid_quirks_init
==================

.. c:function:: int usbhid_quirks_init (char **quirks_param)

    :param char \*\*quirks_param:

        *undescribed*



.. _`usbhid_quirks_exit`:

usbhid_quirks_exit
==================

.. c:function:: void usbhid_quirks_exit ( void)

    :param void:
        no arguments



.. _`usbhid_quirks_exit.description`:

Description
-----------

Release all memory associated with dynamic quirks.  Called upon
module unload.



.. _`usbhid_quirks_exit.returns`:

Returns
-------

nothing



.. _`usbhid_exists_squirk`:

usbhid_exists_squirk
====================

.. c:function:: const struct hid_blacklist *usbhid_exists_squirk (const u16 idVendor, const u16 idProduct)

    :param const u16 idVendor:
        the 16-bit USB vendor ID, in native byteorder

    :param const u16 idProduct:
        the 16-bit USB product ID, in native byteorder



.. _`usbhid_exists_squirk.description`:

Description
-----------

Given a USB vendor ID and product ID, return a pointer to
the hid_blacklist entry associated with that device.



.. _`usbhid_exists_squirk.returns`:

Returns
-------

pointer if quirk found, or NULL if no quirks found.



.. _`usbhid_lookup_quirk`:

usbhid_lookup_quirk
===================

.. c:function:: u32 usbhid_lookup_quirk (const u16 idVendor, const u16 idProduct)

    :param const u16 idVendor:
        the 16-bit USB vendor ID, in native byteorder

    :param const u16 idProduct:
        the 16-bit USB product ID, in native byteorder



.. _`usbhid_lookup_quirk.description`:

Description
-----------

Given a USB vendor ID and product ID, return any quirks associated
with that device.



.. _`usbhid_lookup_quirk.returns`:

Returns
-------

a u32 quirks value.


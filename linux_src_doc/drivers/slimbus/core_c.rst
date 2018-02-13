.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/slimbus/core.c

.. _`slim_unregister_controller`:

slim_unregister_controller
==========================

.. c:function:: int slim_unregister_controller(struct slim_controller *ctrl)

    Controller tear-down.

    :param struct slim_controller \*ctrl:
        Controller to tear-down.

.. _`slim_report_absent`:

slim_report_absent
==================

.. c:function:: void slim_report_absent(struct slim_device *sbdev)

    Controller calls this function when a device reports absent, OR when the device cannot be communicated with

    :param struct slim_device \*sbdev:
        Device that cannot be reached, or sent report absent

.. _`slim_get_device`:

slim_get_device
===============

.. c:function:: struct slim_device *slim_get_device(struct slim_controller *ctrl, struct slim_eaddr *e_addr)

    get handle to a device.

    :param struct slim_controller \*ctrl:
        Controller on which this device will be added/queried

    :param struct slim_eaddr \*e_addr:
        Enumeration address of the device to be queried

.. _`slim_get_device.return`:

Return
------

pointer to a device if it has already reported. Creates a new
device and returns pointer to it if the device has not yet enumerated.

.. _`slim_device_report_present`:

slim_device_report_present
==========================

.. c:function:: int slim_device_report_present(struct slim_controller *ctrl, struct slim_eaddr *e_addr, u8 *laddr)

    Report enumerated device.

    :param struct slim_controller \*ctrl:
        Controller with which device is enumerated.

    :param struct slim_eaddr \*e_addr:
        Enumeration address of the device.

    :param u8 \*laddr:
        Return logical address (if valid flag is false)

.. _`slim_device_report_present.description`:

Description
-----------

Called by controller in response to REPORT_PRESENT. Framework will assign
a logical address to this enumeration address.
Function returns -EXFULL to indicate that all logical addresses are already
taken.

.. _`slim_get_logical_addr`:

slim_get_logical_addr
=====================

.. c:function:: int slim_get_logical_addr(struct slim_device *sbdev)

    get/allocate logical address of a SLIMbus device.

    :param struct slim_device \*sbdev:
        client handle requesting the address.

.. _`slim_get_logical_addr.return`:

Return
------

zero if a logical address is valid or a new logical address
has been assigned. error code in case of error.

.. This file was automatic generated / don't edit.


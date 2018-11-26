.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/slimbus/core.c

.. _`slim_unregister_controller`:

slim_unregister_controller
==========================

.. c:function:: int slim_unregister_controller(struct slim_controller *ctrl)

    Controller tear-down.

    :param ctrl:
        Controller to tear-down.
    :type ctrl: struct slim_controller \*

.. _`slim_report_absent`:

slim_report_absent
==================

.. c:function:: void slim_report_absent(struct slim_device *sbdev)

    Controller calls this function when a device reports absent, OR when the device cannot be communicated with

    :param sbdev:
        Device that cannot be reached, or sent report absent
    :type sbdev: struct slim_device \*

.. _`slim_get_device`:

slim_get_device
===============

.. c:function:: struct slim_device *slim_get_device(struct slim_controller *ctrl, struct slim_eaddr *e_addr)

    get handle to a device.

    :param ctrl:
        Controller on which this device will be added/queried
    :type ctrl: struct slim_controller \*

    :param e_addr:
        Enumeration address of the device to be queried
    :type e_addr: struct slim_eaddr \*

.. _`slim_get_device.return`:

Return
------

pointer to a device if it has already reported. Creates a new
device and returns pointer to it if the device has not yet enumerated.

.. _`of_slim_get_device`:

of_slim_get_device
==================

.. c:function:: struct slim_device *of_slim_get_device(struct slim_controller *ctrl, struct device_node *np)

    get handle to a device using dt node.

    :param ctrl:
        Controller on which this device will be added/queried
    :type ctrl: struct slim_controller \*

    :param np:
        node pointer to device
    :type np: struct device_node \*

.. _`of_slim_get_device.return`:

Return
------

pointer to a device if it has already reported. Creates a new
device and returns pointer to it if the device has not yet enumerated.

.. _`slim_device_report_present`:

slim_device_report_present
==========================

.. c:function:: int slim_device_report_present(struct slim_controller *ctrl, struct slim_eaddr *e_addr, u8 *laddr)

    Report enumerated device.

    :param ctrl:
        Controller with which device is enumerated.
    :type ctrl: struct slim_controller \*

    :param e_addr:
        Enumeration address of the device.
    :type e_addr: struct slim_eaddr \*

    :param laddr:
        Return logical address (if valid flag is false)
    :type laddr: u8 \*

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

    :param sbdev:
        client handle requesting the address.
    :type sbdev: struct slim_device \*

.. _`slim_get_logical_addr.return`:

Return
------

zero if a logical address is valid or a new logical address
has been assigned. error code in case of error.

.. This file was automatic generated / don't edit.


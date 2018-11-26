.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/usb-acpi.c

.. _`usb_acpi_power_manageable`:

usb_acpi_power_manageable
=========================

.. c:function:: bool usb_acpi_power_manageable(struct usb_device *hdev, int index)

    check whether usb port has acpi power resource.

    :param hdev:
        USB device belonging to the usb hub
    :type hdev: struct usb_device \*

    :param index:
        port index based zero
    :type index: int

.. _`usb_acpi_power_manageable.description`:

Description
-----------

Return true if the port has acpi power resource and false if no.

.. _`usb_acpi_set_power_state`:

usb_acpi_set_power_state
========================

.. c:function:: int usb_acpi_set_power_state(struct usb_device *hdev, int index, bool enable)

    control usb port's power via acpi power resource

    :param hdev:
        USB device belonging to the usb hub
    :type hdev: struct usb_device \*

    :param index:
        port index based zero
    :type index: int

    :param enable:
        power state expected to be set
    :type enable: bool

.. _`usb_acpi_set_power_state.description`:

Description
-----------

Notice to use \ :c:func:`usb_acpi_power_manageable`\  to check whether the usb port
has acpi power resource before invoking this function.

Returns 0 on success, else negative errno.

.. This file was automatic generated / don't edit.


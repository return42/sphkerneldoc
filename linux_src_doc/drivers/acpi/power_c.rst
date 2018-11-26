.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/power.c

.. _`acpi_device_sleep_wake`:

acpi_device_sleep_wake
======================

.. c:function:: int acpi_device_sleep_wake(struct acpi_device *dev, int enable, int sleep_state, int dev_state)

    execute \_DSW (Device Sleep Wake) or (deprecated in ACPI 3.0) \_PSW (Power State Wake)

    :param dev:
        Device to handle.
    :type dev: struct acpi_device \*

    :param enable:
        0 - disable, 1 - enable the wake capabilities of the device.
    :type enable: int

    :param sleep_state:
        Target sleep state of the system.
    :type sleep_state: int

    :param dev_state:
        Target power state of the device.
    :type dev_state: int

.. _`acpi_device_sleep_wake.description`:

Description
-----------

Execute \_DSW (Device Sleep Wake) or (deprecated in ACPI 3.0) \_PSW (Power
State Wake) for the device, if present.  On failure reset the device's
wakeup.flags.valid flag.

.. _`acpi_device_sleep_wake.return-value`:

RETURN VALUE
------------

0 if either \_DSW or \_PSW has been successfully executed
0 if neither \_DSW nor \_PSW has been found
-ENODEV if the execution of either \_DSW or \_PSW has failed

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

========
wakeup.c
========


.. _`acpi_enable_wakeup_devices`:

acpi_enable_wakeup_devices
==========================

.. c:function:: void acpi_enable_wakeup_devices (u8 sleep_state)

    Enable wake-up device GPEs.

    :param u8 sleep_state:
        ACPI system sleep state.



.. _`acpi_enable_wakeup_devices.description`:

Description
-----------

Enable wakeup device power of devices with the state.enable flag set and set
the wakeup enable mask bits in the GPE registers that correspond to wakeup
devices.



.. _`acpi_disable_wakeup_devices`:

acpi_disable_wakeup_devices
===========================

.. c:function:: void acpi_disable_wakeup_devices (u8 sleep_state)

    Disable devices' wakeup capability.

    :param u8 sleep_state:
        ACPI system sleep state.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/acpi/sleep.c

.. _`x86_acpi_enter_sleep_state`:

x86_acpi_enter_sleep_state
==========================

.. c:function:: acpi_status asmlinkage __visible x86_acpi_enter_sleep_state(u8 state)

    enter sleep state

    :param state:
        Sleep state to enter.
    :type state: u8

.. _`x86_acpi_enter_sleep_state.description`:

Description
-----------

Wrapper around \ :c:func:`acpi_enter_sleep_state`\  to be called by assmebly.

.. _`x86_acpi_suspend_lowlevel`:

x86_acpi_suspend_lowlevel
=========================

.. c:function:: int x86_acpi_suspend_lowlevel( void)

    save kernel state

    :param void:
        no arguments
    :type void: 

.. _`x86_acpi_suspend_lowlevel.description`:

Description
-----------

Create an identity mapped page table and copy the wakeup routine to
low memory.

.. This file was automatic generated / don't edit.


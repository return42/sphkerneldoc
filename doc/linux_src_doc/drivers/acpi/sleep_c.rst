.. -*- coding: utf-8; mode: rst -*-

=======
sleep.c
=======


.. _`acpi_pm_freeze`:

acpi_pm_freeze
==============

.. c:function:: int acpi_pm_freeze ( void)

    Disable the GPEs and suspend EC transactions.

    :param void:
        no arguments



.. _`acpi_pm_pre_suspend`:

acpi_pm_pre_suspend
===================

.. c:function:: int acpi_pm_pre_suspend ( void)

    Enable wakeup devices, "freeze" EC and save NVS.

    :param void:
        no arguments



.. _`__acpi_pm_prepare`:

__acpi_pm_prepare
=================

.. c:function:: int __acpi_pm_prepare ( void)

    Prepare the platform to enter the target state.

    :param void:
        no arguments



.. _`__acpi_pm_prepare.description`:

Description
-----------


If necessary, set the firmware waking vector and do arch-specific
nastiness to get the wakeup code to the waking vector.



.. _`acpi_pm_prepare`:

acpi_pm_prepare
===============

.. c:function:: int acpi_pm_prepare ( void)

    Prepare the platform to enter the target sleep state and disable the GPEs.

    :param void:
        no arguments



.. _`acpi_pm_finish`:

acpi_pm_finish
==============

.. c:function:: void acpi_pm_finish ( void)

    Instruct the platform to leave a sleep state.

    :param void:
        no arguments



.. _`acpi_pm_finish.description`:

Description
-----------


This is called after we wake back up (or if entering the sleep state
failed).



.. _`acpi_pm_start`:

acpi_pm_start
=============

.. c:function:: void acpi_pm_start (u32 acpi_state)

    Start system PM transition.

    :param u32 acpi_state:

        *undescribed*



.. _`acpi_pm_end`:

acpi_pm_end
===========

.. c:function:: void acpi_pm_end ( void)

    Finish up system PM transition.

    :param void:
        no arguments



.. _`acpi_suspend_begin`:

acpi_suspend_begin
==================

.. c:function:: int acpi_suspend_begin (suspend_state_t pm_state)

    Set the target system sleep state to the state associated with given @pm_state, if supported.

    :param suspend_state_t pm_state:

        *undescribed*



.. _`acpi_suspend_enter`:

acpi_suspend_enter
==================

.. c:function:: int acpi_suspend_enter (suspend_state_t pm_state)

    Actually enter a sleep state.

    :param suspend_state_t pm_state:
        ignored



.. _`acpi_suspend_enter.description`:

Description
-----------

Flush caches and go to sleep. For STR we have to call arch-specific
assembly, which in turn call :c:func:`acpi_enter_sleep_state`.
It's unfortunate, but it works. Please fix if you're feeling frisky.



.. _`acpi_suspend_begin_old`:

acpi_suspend_begin_old
======================

.. c:function:: int acpi_suspend_begin_old (suspend_state_t pm_state)

    Set the target system sleep state to the state associated with given @pm_state, if supported, and execute the _PTS control method. This function is used if the pre-ACPI 2.0 suspend ordering has been requested.

    :param suspend_state_t pm_state:

        *undescribed*



.. _`acpi_hibernation_begin_old`:

acpi_hibernation_begin_old
==========================

.. c:function:: int acpi_hibernation_begin_old ( void)

    Set the target system sleep state to ACPI_STATE_S4 and execute the _PTS control method. This function is used if the pre-ACPI 2.0 suspend ordering has been requested.

    :param void:
        no arguments


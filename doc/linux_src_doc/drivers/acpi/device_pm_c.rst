.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/device_pm.c

.. _`acpi_power_state_string`:

acpi_power_state_string
=======================

.. c:function:: const char *acpi_power_state_string(int state)

    String representation of ACPI device power state.

    :param int state:
        ACPI device power state to return the string representation of.

.. _`acpi_device_get_power`:

acpi_device_get_power
=====================

.. c:function:: int acpi_device_get_power(struct acpi_device *device, int *state)

    Get power state of an ACPI device.

    :param struct acpi_device \*device:
        Device to get the power state of.

    :param int \*state:
        Place to store the power state of the device.

.. _`acpi_device_get_power.description`:

Description
-----------

This function does not update the device's power.state field, but it may
update its parent's power.state field (when the parent's power state is
unknown and the device's power state turns out to be D0).

.. _`acpi_device_set_power`:

acpi_device_set_power
=====================

.. c:function:: int acpi_device_set_power(struct acpi_device *device, int state)

    Set power state of an ACPI device.

    :param struct acpi_device \*device:
        Device to set the power state of.

    :param int state:
        New power state to set.

.. _`acpi_device_set_power.description`:

Description
-----------

Callers must ensure that the device is power manageable before using this
function.

.. _`acpi_device_fix_up_power`:

acpi_device_fix_up_power
========================

.. c:function:: int acpi_device_fix_up_power(struct acpi_device *device)

    Force device with missing \_PSC into D0.

    :param struct acpi_device \*device:
        Device object whose power state is to be fixed up.

.. _`acpi_device_fix_up_power.description`:

Description
-----------

Devices without power resources and \_PSC, but having \_PS0 and \_PS3 defined,
are assumed to be put into D0 by the BIOS.  However, in some cases that may
not be the case and this function should be used then.

.. _`acpi_add_pm_notifier`:

acpi_add_pm_notifier
====================

.. c:function:: acpi_status acpi_add_pm_notifier(struct acpi_device *adev, struct device *dev, void (*work_func)(struct work_struct *work))

    Register PM notify handler for given ACPI device.

    :param struct acpi_device \*adev:
        ACPI device to add the notify handler for.

    :param struct device \*dev:
        Device to generate a wakeup event for while handling the notification.

    :param void (\*work_func)(struct work_struct \*work):
        Work function to execute when handling the notification.

.. _`acpi_add_pm_notifier.note`:

NOTE
----

\ ``adev``\  need not be a run-wake or wakeup device to be a valid source of
PM wakeup events.  For example, wakeup events may be generated for bridges
if one of the devices below the bridge is signaling wakeup, even if the
bridge itself doesn't have a wakeup GPE associated with it.

.. _`acpi_remove_pm_notifier`:

acpi_remove_pm_notifier
=======================

.. c:function:: acpi_status acpi_remove_pm_notifier(struct acpi_device *adev)

    Unregister PM notifier from given ACPI device.

    :param struct acpi_device \*adev:
        ACPI device to remove the notifier from.

.. _`acpi_dev_pm_get_state`:

acpi_dev_pm_get_state
=====================

.. c:function:: int acpi_dev_pm_get_state(struct device *dev, struct acpi_device *adev, u32 target_state, int *d_min_p, int *d_max_p)

    Get preferred power state of ACPI device.

    :param struct device \*dev:
        Device whose preferred target power state to return.

    :param struct acpi_device \*adev:
        ACPI device node corresponding to \ ``dev``\ .

    :param u32 target_state:
        System state to match the resultant device state.

    :param int \*d_min_p:
        Location to store the highest power state available to the device.

    :param int \*d_max_p:
        Location to store the lowest power state available to the device.

.. _`acpi_dev_pm_get_state.description`:

Description
-----------

Find the lowest power (highest number) and highest power (lowest number) ACPI
device power states that the device can be in while the system is in the
state represented by \ ``target_state``\ .  Store the integer numbers representing
those stats in the memory locations pointed to by \ ``d_max_p``\  and \ ``d_min_p``\ ,
respectively.

Callers must ensure that \ ``dev``\  and \ ``adev``\  are valid pointers and that \ ``adev``\ 
actually corresponds to \ ``dev``\  before using this function.

Returns 0 on success or -ENODATA when one of the ACPI methods fails or
returns a value that doesn't make sense.  The memory locations pointed to by
\ ``d_max_p``\  and \ ``d_min_p``\  are only modified on success.

.. _`acpi_pm_device_sleep_state`:

acpi_pm_device_sleep_state
==========================

.. c:function:: int acpi_pm_device_sleep_state(struct device *dev, int *d_min_p, int d_max_in)

    Get preferred power state of ACPI device.

    :param struct device \*dev:
        Device whose preferred target power state to return.

    :param int \*d_min_p:
        Location to store the upper limit of the allowed states range.

    :param int d_max_in:
        Deepest low-power state to take into consideration.

.. _`acpi_pm_device_sleep_state.return-value`:

Return value
------------

Preferred power state of the device on success, -ENODEV
if there's no 'struct acpi_device' for \ ``dev``\ , -EINVAL if \ ``d_max_in``\  is
incorrect, or -ENODATA on ACPI method failure.

The caller must ensure that \ ``dev``\  is valid before using this function.

.. _`acpi_pm_notify_work_func`:

acpi_pm_notify_work_func
========================

.. c:function:: void acpi_pm_notify_work_func(struct work_struct *work)

    ACPI devices wakeup notification work function.

    :param struct work_struct \*work:
        Work item to handle.

.. _`acpi_device_wakeup`:

acpi_device_wakeup
==================

.. c:function:: int acpi_device_wakeup(struct acpi_device *adev, u32 target_state, bool enable)

    Enable/disable wakeup functionality for device.

    :param struct acpi_device \*adev:
        ACPI device to enable/disable wakeup functionality for.

    :param u32 target_state:
        State the system is transitioning into.

    :param bool enable:
        Whether to enable or disable the wakeup functionality.

.. _`acpi_device_wakeup.description`:

Description
-----------

Enable/disable the GPE associated with \ ``adev``\  so that it can generate
wakeup signals for the device in response to external (remote) events and
enable/disable device wakeup power.

Callers must ensure that \ ``adev``\  is a valid ACPI device node before executing
this function.

.. _`acpi_pm_device_run_wake`:

acpi_pm_device_run_wake
=======================

.. c:function:: int acpi_pm_device_run_wake(struct device *phys_dev, bool enable)

    Enable/disable remote wakeup for given device.

    :param struct device \*phys_dev:
        *undescribed*

    :param bool enable:
        Whether to enable or disable the wakeup functionality.

.. _`acpi_pm_device_sleep_wake`:

acpi_pm_device_sleep_wake
=========================

.. c:function:: int acpi_pm_device_sleep_wake(struct device *dev, bool enable)

    Enable or disable device to wake up the system.

    :param struct device \*dev:
        Device to enable/desible to wake up the system from sleep states.

    :param bool enable:
        Whether to enable or disable \ ``dev``\  to wake up the system.

.. _`acpi_dev_pm_low_power`:

acpi_dev_pm_low_power
=====================

.. c:function:: int acpi_dev_pm_low_power(struct device *dev, struct acpi_device *adev, u32 system_state)

    Put ACPI device into a low-power state.

    :param struct device \*dev:
        Device to put into a low-power state.

    :param struct acpi_device \*adev:
        ACPI device node corresponding to \ ``dev``\ .

    :param u32 system_state:
        System state to choose the device state for.

.. _`acpi_dev_pm_full_power`:

acpi_dev_pm_full_power
======================

.. c:function:: int acpi_dev_pm_full_power(struct acpi_device *adev)

    Put ACPI device into the full-power state.

    :param struct acpi_device \*adev:
        ACPI device node to put into the full-power state.

.. _`acpi_dev_runtime_suspend`:

acpi_dev_runtime_suspend
========================

.. c:function:: int acpi_dev_runtime_suspend(struct device *dev)

    Put device into a low-power state using ACPI.

    :param struct device \*dev:
        Device to put into a low-power state.

.. _`acpi_dev_runtime_suspend.description`:

Description
-----------

Put the given device into a runtime low-power state using the standard ACPI
mechanism.  Set up remote wakeup if desired, choose the state to put the
device into (this checks if remote wakeup is expected to work too), and set
the power state of the device.

.. _`acpi_dev_runtime_resume`:

acpi_dev_runtime_resume
=======================

.. c:function:: int acpi_dev_runtime_resume(struct device *dev)

    Put device into the full-power state using ACPI.

    :param struct device \*dev:
        Device to put into the full-power state.

.. _`acpi_dev_runtime_resume.description`:

Description
-----------

Put the given device into the full-power state using the standard ACPI
mechanism at run time.  Set the power state of the device to ACPI D0 and
disable remote wakeup.

.. _`acpi_subsys_runtime_suspend`:

acpi_subsys_runtime_suspend
===========================

.. c:function:: int acpi_subsys_runtime_suspend(struct device *dev)

    Suspend device using ACPI.

    :param struct device \*dev:
        Device to suspend.

.. _`acpi_subsys_runtime_suspend.description`:

Description
-----------

Carry out the generic runtime suspend procedure for \ ``dev``\  and use ACPI to put
it into a runtime low-power state.

.. _`acpi_subsys_runtime_resume`:

acpi_subsys_runtime_resume
==========================

.. c:function:: int acpi_subsys_runtime_resume(struct device *dev)

    Resume device using ACPI.

    :param struct device \*dev:
        Device to Resume.

.. _`acpi_subsys_runtime_resume.description`:

Description
-----------

Use ACPI to put the given device into the full-power state and carry out the
generic runtime resume procedure for it.

.. _`acpi_dev_suspend_late`:

acpi_dev_suspend_late
=====================

.. c:function:: int acpi_dev_suspend_late(struct device *dev)

    Put device into a low-power state using ACPI.

    :param struct device \*dev:
        Device to put into a low-power state.

.. _`acpi_dev_suspend_late.description`:

Description
-----------

Put the given device into a low-power state during system transition to a
sleep state using the standard ACPI mechanism.  Set up system wakeup if
desired, choose the state to put the device into (this checks if system
wakeup is expected to work too), and set the power state of the device.

.. _`acpi_dev_resume_early`:

acpi_dev_resume_early
=====================

.. c:function:: int acpi_dev_resume_early(struct device *dev)

    Put device into the full-power state using ACPI.

    :param struct device \*dev:
        Device to put into the full-power state.

.. _`acpi_dev_resume_early.description`:

Description
-----------

Put the given device into the full-power state using the standard ACPI
mechanism during system transition to the working state.  Set the power
state of the device to ACPI D0 and disable remote wakeup.

.. _`acpi_subsys_prepare`:

acpi_subsys_prepare
===================

.. c:function:: int acpi_subsys_prepare(struct device *dev)

    Prepare device for system transition to a sleep state.

    :param struct device \*dev:
        Device to prepare.

.. _`acpi_subsys_suspend`:

acpi_subsys_suspend
===================

.. c:function:: int acpi_subsys_suspend(struct device *dev)

    Run the device driver's suspend callback.

    :param struct device \*dev:
        Device to handle.

.. _`acpi_subsys_suspend.description`:

Description
-----------

Follow PCI and resume devices suspended at run time before running their
system suspend callbacks.

.. _`acpi_subsys_suspend_late`:

acpi_subsys_suspend_late
========================

.. c:function:: int acpi_subsys_suspend_late(struct device *dev)

    Suspend device using ACPI.

    :param struct device \*dev:
        Device to suspend.

.. _`acpi_subsys_suspend_late.description`:

Description
-----------

Carry out the generic late suspend procedure for \ ``dev``\  and use ACPI to put
it into a low-power state during system transition into a sleep state.

.. _`acpi_subsys_resume_early`:

acpi_subsys_resume_early
========================

.. c:function:: int acpi_subsys_resume_early(struct device *dev)

    Resume device using ACPI.

    :param struct device \*dev:
        Device to Resume.

.. _`acpi_subsys_resume_early.description`:

Description
-----------

Use ACPI to put the given device into the full-power state and carry out the
generic early resume procedure for it during system transition into the
working state.

.. _`acpi_subsys_freeze`:

acpi_subsys_freeze
==================

.. c:function:: int acpi_subsys_freeze(struct device *dev)

    Run the device driver's freeze callback.

    :param struct device \*dev:
        Device to handle.

.. _`acpi_dev_pm_detach`:

acpi_dev_pm_detach
==================

.. c:function:: void acpi_dev_pm_detach(struct device *dev, bool power_off)

    Remove ACPI power management from the device.

    :param struct device \*dev:
        Device to take care of.

    :param bool power_off:
        Whether or not to try to remove power from the device.

.. _`acpi_dev_pm_detach.description`:

Description
-----------

Remove the device from the general ACPI PM domain and remove its wakeup
notifier.  If \ ``power_off``\  is set, additionally remove power from the device if
possible.

Callers must ensure proper synchronization of this function with power
management callbacks.

.. _`acpi_dev_pm_attach`:

acpi_dev_pm_attach
==================

.. c:function:: int acpi_dev_pm_attach(struct device *dev, bool power_on)

    Prepare device for ACPI power management.

    :param struct device \*dev:
        Device to prepare.

    :param bool power_on:
        Whether or not to power on the device.

.. _`acpi_dev_pm_attach.description`:

Description
-----------

If \ ``dev``\  has a valid ACPI handle that has a valid struct acpi_device object
attached to it, install a wakeup notification handler for the device and
add it to the general ACPI PM domain.  If \ ``power_on``\  is set, the device will
be put into the ACPI D0 state before the function returns.

This assumes that the \ ``dev``\ 's bus type uses generic power management callbacks
(or doesn't use any power management callbacks at all).

Callers must ensure proper synchronization of this function with power
management callbacks.

.. This file was automatic generated / don't edit.


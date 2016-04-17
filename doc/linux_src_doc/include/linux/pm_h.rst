.. -*- coding: utf-8; mode: rst -*-

====
pm.h
====


.. _`dev_pm_ops`:

struct dev_pm_ops
=================

.. c:type:: dev_pm_ops

    device PM callbacks


.. _`dev_pm_ops.definition`:

Definition
----------

.. code-block:: c

  struct dev_pm_ops {
    int (* prepare) (struct device *dev);
    void (* complete) (struct device *dev);
    int (* suspend) (struct device *dev);
    int (* resume) (struct device *dev);
    int (* freeze) (struct device *dev);
    int (* thaw) (struct device *dev);
    int (* poweroff) (struct device *dev);
    int (* restore) (struct device *dev);
    int (* suspend_late) (struct device *dev);
    int (* resume_early) (struct device *dev);
    int (* freeze_late) (struct device *dev);
    int (* thaw_early) (struct device *dev);
    int (* poweroff_late) (struct device *dev);
    int (* restore_early) (struct device *dev);
    int (* suspend_noirq) (struct device *dev);
    int (* resume_noirq) (struct device *dev);
    int (* freeze_noirq) (struct device *dev);
    int (* thaw_noirq) (struct device *dev);
    int (* poweroff_noirq) (struct device *dev);
    int (* restore_noirq) (struct device *dev);
    int (* runtime_suspend) (struct device *dev);
    int (* runtime_resume) (struct device *dev);
    int (* runtime_idle) (struct device *dev);
  };


.. _`dev_pm_ops.members`:

Members
-------

:``prepare``:
    The principal role of this callback is to prevent new children of
    the device from being registered after it has returned (the driver's
    subsystem and generally the rest of the kernel is supposed to prevent
    new calls to the probe method from being made too once @:c:func:`prepare` has
    succeeded).  If @:c:func:`prepare` detects a situation it cannot handle (e.g.
    registration of a child already in progress), it may return -EAGAIN, so
    that the PM core can execute it once again (e.g. after a new child has
    been registered) to recover from the race condition.
    This method is executed for all kinds of suspend transitions and is

:``complete``:
    Undo the changes made by @:c:func:`prepare`.  This method is executed for
    all kinds of resume transitions, following one of the resume callbacks:
    @:c:func:`resume`, @:c:func:`thaw`, @:c:func:`restore`.  Also called if the state transition
    fails before the driver's suspend callback: @:c:func:`suspend`, @:c:func:`freeze` or
    @:c:func:`poweroff`, can be executed (e.g. if the suspend callback fails for one
    of the other devices that the PM core has unsuccessfully attempted to
    suspend earlier).
    The PM core executes subsystem-level @:c:func:`complete` after it has executed
    the appropriate resume callbacks for all devices.  If the corresponding
    @:c:func:`prepare` at the beginning of the suspend transition returned a
    positive number and the device was left in runtime suspend (without
    executing any suspend and resume callbacks for it), @:c:func:`complete` will be
    the only callback executed for the device during resume.  In that case,
    @:c:func:`complete` must be prepared to do whatever is necessary to ensure the
    proper functioning of the device after the system resume.  To this end,
    @:c:func:`complete` can check the power.direct_complete flag of the device to
    learn whether (unset) or not (set) the previous suspend and resume
    callbacks have been executed for it.

:``suspend``:
    Executed before putting the system into a sleep state in which the
    contents of main memory are preserved.  The exact action to perform
    depends on the device's subsystem (PM domain, device type, class or bus
    type), but generally the device must be quiescent after subsystem-level
    @:c:func:`suspend` has returned, so that it doesn't do any I/O or DMA.
    Subsystem-level @:c:func:`suspend` is executed for all devices after invoking
    subsystem-level @:c:func:`prepare` for all of them.

:``resume``:
    Executed after waking the system up from a sleep state in which the
    contents of main memory were preserved.  The exact action to perform
    depends on the device's subsystem, but generally the driver is expected
    to start working again, responding to hardware events and software
    requests (the device itself may be left in a low-power state, waiting
    for a runtime resume to occur).  The state of the device at the time its
    driver's @:c:func:`resume` callback is run depends on the platform and subsystem
    the device belongs to.  On most platforms, there are no restrictions on
    availability of resources like clocks during @:c:func:`resume`.
    Subsystem-level @:c:func:`resume` is executed for all devices after invoking
    subsystem-level @:c:func:`resume_noirq` for all of them.

:``freeze``:
    Hibernation-specific, executed before creating a hibernation image.
    Analogous to @:c:func:`suspend`, but it should not enable the device to signal
    wakeup events or change its power state.  The majority of subsystems
    (with the notable exception of the PCI bus type) expect the driver-level
    @:c:func:`freeze` to save the device settings in memory to be used by @:c:func:`restore`
    during the subsequent resume from hibernation.
    Subsystem-level @:c:func:`freeze` is executed for all devices after invoking
    subsystem-level @:c:func:`prepare` for all of them.

:``thaw``:
    Hibernation-specific, executed after creating a hibernation image OR
    if the creation of an image has failed.  Also executed after a failing
    attempt to restore the contents of main memory from such an image.
    Undo the changes made by the preceding @:c:func:`freeze`, so the device can be
    operated in the same way as immediately before the call to @:c:func:`freeze`.
    Subsystem-level @:c:func:`thaw` is executed for all devices after invoking
    subsystem-level @:c:func:`thaw_noirq` for all of them.  It also may be executed
    directly after @:c:func:`freeze` in case of a transition error.

:``poweroff``:
    Hibernation-specific, executed after saving a hibernation image.
    Analogous to @:c:func:`suspend`, but it need not save the device's settings in
    memory.
    Subsystem-level @:c:func:`poweroff` is executed for all devices after invoking
    subsystem-level @:c:func:`prepare` for all of them.

:``restore``:
    Hibernation-specific, executed after restoring the contents of main
    memory from a hibernation image, analogous to @:c:func:`resume`.

:``suspend_late``:
    Continue operations started by @:c:func:`suspend`.  For a number of
    devices @:c:func:`suspend_late` may point to the same callback routine as the
    runtime suspend callback.

:``resume_early``:
    Prepare to execute @:c:func:`resume`.  For a number of devices
    @:c:func:`resume_early` may point to the same callback routine as the runtime
    resume callback.

:``freeze_late``:
    Continue operations started by @:c:func:`freeze`.  Analogous to
    @:c:func:`suspend_late`, but it should not enable the device to signal wakeup
    events or change its power state.

:``thaw_early``:
    Prepare to execute @:c:func:`thaw`.  Undo the changes made by the
    preceding @:c:func:`freeze_late`.

:``poweroff_late``:
    Continue operations started by @:c:func:`poweroff`.  Analogous to
    @:c:func:`suspend_late`, but it need not save the device's settings in memory.

:``restore_early``:
    Prepare to execute @:c:func:`restore`, analogous to @:c:func:`resume_early`.

:``suspend_noirq``:
    Complete the actions started by @:c:func:`suspend`.  Carry out any
    additional operations required for suspending the device that might be
    racing with its driver's interrupt handler, which is guaranteed not to
    run while @:c:func:`suspend_noirq` is being executed.
    It generally is expected that the device will be in a low-power state
    (appropriate for the target system sleep state) after subsystem-level
    @:c:func:`suspend_noirq` has returned successfully.  If the device can generate
    system wakeup signals and is enabled to wake up the system, it should be
    configured to do so at that time.  However, depending on the platform
    and device's subsystem, @:c:func:`suspend` or @:c:func:`suspend_late` may be allowed to
    put the device into the low-power state and configure it to generate
    wakeup signals, in which case it generally is not necessary to define
    @:c:func:`suspend_noirq`.

:``resume_noirq``:
    Prepare for the execution of @:c:func:`resume` by carrying out any
    operations required for resuming the device that might be racing with
    its driver's interrupt handler, which is guaranteed not to run while
    @:c:func:`resume_noirq` is being executed.

:``freeze_noirq``:
    Complete the actions started by @:c:func:`freeze`.  Carry out any
    additional operations required for freezing the device that might be
    racing with its driver's interrupt handler, which is guaranteed not to
    run while @:c:func:`freeze_noirq` is being executed.
    The power state of the device should not be changed by either @:c:func:`freeze`,
    or @:c:func:`freeze_late`, or @:c:func:`freeze_noirq` and it should not be configured to
    signal system wakeup by any of these callbacks.

:``thaw_noirq``:
    Prepare for the execution of @:c:func:`thaw` by carrying out any
    operations required for thawing the device that might be racing with its
    driver's interrupt handler, which is guaranteed not to run while
    @:c:func:`thaw_noirq` is being executed.

:``poweroff_noirq``:
    Complete the actions started by @:c:func:`poweroff`.  Analogous to
    @:c:func:`suspend_noirq`, but it need not save the device's settings in memory.

:``restore_noirq``:
    Prepare for the execution of @:c:func:`restore` by carrying out any
    operations required for thawing the device that might be racing with its
    driver's interrupt handler, which is guaranteed not to run while
    @:c:func:`restore_noirq` is being executed.  Analogous to @:c:func:`resume_noirq`.

:``runtime_suspend``:
    Prepare the device for a condition in which it won't be
    able to communicate with the CPU(s) and RAM due to power management.
    This need not mean that the device should be put into a low-power state.
    For example, if the device is behind a link which is about to be turned
    off, the device may remain at full power.  If the device does go to low
    power and is capable of generating runtime wakeup events, remote wakeup
    (i.e., a hardware mechanism allowing the device to request a change of
    its power state via an interrupt) should be enabled for it.

:``runtime_resume``:
    Put the device into the fully active state in response to a
    wakeup event generated by hardware or at the request of software.  If
    necessary, put the device into the full-power state and restore its
    registers, so that it is fully operational.

:``runtime_idle``:
    Device appears to be inactive and it might be put into a
    low-power state if all of the necessary conditions are satisfied.
    Check these conditions, and return 0 if it's appropriate to let the PM
    core queue a suspend request for the device.




.. _`dev_pm_ops.description`:

Description
-----------

Refer to Documentation/power/runtime_pm.txt for more information about the
role of the above callbacks in device runtime power management.



.. _`dev_pm_ops.followed-by-one-of-the-suspend-callbacks`:

followed by one of the suspend callbacks
----------------------------------------

@:c:func:`suspend`, @:c:func:`freeze`, or
@:c:func:`poweroff`.  If the transition is a suspend to memory or standby (that
is, not related to hibernation), the return value of @:c:func:`prepare` may be
used to indicate to the PM core to leave the device in runtime suspend
if applicable.  Namely, if @:c:func:`prepare` returns a positive number, the PM
core will understand that as a declaration that the device appears to be
runtime-suspended and it may be left in that state during the entire
transition and during the subsequent resume if all of its descendants
are left in runtime suspend too.  If that happens, @:c:func:`complete` will be
executed directly after @:c:func:`prepare` and it must ensure the proper
functioning of the device after the system resume.
The PM core executes subsystem-level @:c:func:`prepare` for all devices before
starting to invoke suspend callbacks for any of them, so generally
devices may be assumed to be functional or to respond to runtime resume
requests while @:c:func:`prepare` is being executed.  However, device drivers
may NOT assume anything about the availability of user space at that
time and it is NOT valid to request firmware from within @:c:func:`prepare`
(it's too late to do that).  It also is NOT valid to allocate
substantial amounts of memory from @:c:func:`prepare` in the GFP_KERNEL mode.
[To work around these limitations, drivers may register suspend and
hibernation notifiers to be executed before the freezing of tasks.]



.. _`dev_pm_ops.description`:

Description
-----------

Refer to Documentation/power/runtime_pm.txt for more information about the
role of the above callbacks in device runtime power management.



.. _`dev_pm_ops.description`:

Description
-----------

Refer to Documentation/power/runtime_pm.txt for more information about the
role of the above callbacks in device runtime power management.



.. _`pm_event_invalid`:

PM_EVENT_INVALID
================

.. c:function:: PM_EVENT_INVALID ()



.. _`pm_event_invalid.description`:

Description
-----------


The following PM_EVENT_ messages are defined for the internal use of the PM
core, in order to provide a mechanism allowing the high level suspend and
hibernation code to convey the necessary information to the device PM core



.. _`pm_event_invalid.code`:

code
----


ON                No transition.

FREEZE        System is going to hibernate, call ->:c:func:`prepare` and ->:c:func:`freeze`
for all devices.

SUSPEND        System is going to suspend, call ->:c:func:`prepare` and ->:c:func:`suspend`
for all devices.

HIBERNATE        Hibernation image has been saved, call ->:c:func:`prepare` and
->:c:func:`poweroff` for all devices.

QUIESCE        Contents of main memory are going to be restored from a (loaded)
hibernation image, call ->:c:func:`prepare` and ->:c:func:`freeze` for all
devices.

RESUME        System is resuming, call ->:c:func:`resume` and ->:c:func:`complete` for all
devices.

THAW                Hibernation image has been created, call ->:c:func:`thaw` and
->:c:func:`complete` for all devices.

RESTORE        Contents of main memory have been restored from a hibernation
image, call ->:c:func:`restore` and ->:c:func:`complete` for all devices.

RECOVER        Creation of a hibernation image or restoration of the main
memory contents from a hibernation image has failed, call
->:c:func:`thaw` and ->:c:func:`complete` for all devices.

The following PM_EVENT_ messages are defined for internal use by
kernel subsystems.  They are never issued by the PM core.

USER_SUSPEND                Manual selective suspend was issued by userspace.

USER_RESUME                Manual selective resume was issued by userspace.

REMOTE_WAKEUP        Remote-wakeup request was received from the device.

AUTO_SUSPEND                Automatic (device idle) runtime suspend was
initiated by the subsystem.

AUTO_RESUME                Automatic (device needed) runtime resume was
requested by a driver.


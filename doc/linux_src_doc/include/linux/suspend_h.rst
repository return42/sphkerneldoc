.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/suspend.h

.. _`platform_suspend_ops`:

struct platform_suspend_ops
===========================

.. c:type:: struct platform_suspend_ops

    Callbacks for managing platform dependent system sleep states.

.. _`platform_suspend_ops.definition`:

Definition
----------

.. code-block:: c

    struct platform_suspend_ops {
        int (* valid) (suspend_state_t state);
        int (* begin) (suspend_state_t state);
        int (* prepare) (void);
        int (* prepare_late) (void);
        int (* enter) (suspend_state_t state);
        void (* wake) (void);
        void (* finish) (void);
        bool (* suspend_again) (void);
        void (* end) (void);
        void (* recover) (void);
    }

.. _`platform_suspend_ops.members`:

Members
-------

valid
    Callback to determine if given system sleep state is supported by
    the platform.
    Valid (ie. supported) states are advertised in /sys/power/state.  Note
    that it still may be impossible to enter given system sleep state if the
    conditions aren't right.
    There is the \ ``suspend_valid_only_mem``\  function available that can be
    assigned to this if the platform only supports mem sleep.

begin
    Initialise a transition to given system sleep state.
    @\ :c:func:`begin`\  is executed right prior to suspending devices.  The information
    conveyed to the platform code by @\ :c:func:`begin`\  should be disregarded by it as
    soon as @\ :c:func:`end`\  is executed.  If @\ :c:func:`begin`\  fails (ie. returns nonzero),
    @\ :c:func:`prepare`\ , @\ :c:func:`enter`\  and @\ :c:func:`finish`\  will not be called by the PM core.
    This callback is optional.  However, if it is implemented, the argument
    passed to @\ :c:func:`enter`\  is redundant and should be ignored.

prepare
    Prepare the platform for entering the system sleep state indicated
    by @\ :c:func:`begin`\ .
    @\ :c:func:`prepare`\  is called right after devices have been suspended (ie. the
    appropriate .\ :c:func:`suspend`\  method has been executed for each device) and
    before device drivers' late suspend callbacks are executed.  It returns
    0 on success or a negative error code otherwise, in which case the
    system cannot enter the desired sleep state (@\ :c:func:`prepare_late`\ , @\ :c:func:`enter`\ ,
    and @\ :c:func:`wake`\  will not be called in that case).

prepare_late
    Finish preparing the platform for entering the system sleep
    state indicated by @\ :c:func:`begin`\ .
    \ ``prepare_late``\  is called before disabling nonboot CPUs and after
    device drivers' late suspend callbacks have been executed.  It returns
    0 on success or a negative error code otherwise, in which case the
    system cannot enter the desired sleep state (@\ :c:func:`enter`\  will not be
    executed).

enter
    Enter the system sleep state indicated by @\ :c:func:`begin`\  or represented by
    the argument if @\ :c:func:`begin`\  is not implemented.
    This callback is mandatory.  It returns 0 on success or a negative
    error code otherwise, in which case the system cannot enter the desired
    sleep state.

wake
    Called when the system has just left a sleep state, right after
    the nonboot CPUs have been enabled and before device drivers' early
    resume callbacks are executed.
    This callback is optional, but should be implemented by the platforms
    that implement @\ :c:func:`prepare_late`\ .  If implemented, it is always called
    after \ ``prepare_late``\  and @\ :c:func:`enter`\ , even if one of them fails.

finish
    Finish wake-up of the platform.
    \ ``finish``\  is called right prior to calling device drivers' regular suspend
    callbacks.
    This callback is optional, but should be implemented by the platforms
    that implement @\ :c:func:`prepare`\ .  If implemented, it is always called after
    @\ :c:func:`enter`\  and @\ :c:func:`wake`\ , even if any of them fails.  It is executed after
    a failing \ ``prepare``\ .

suspend_again
    Returns whether the system should suspend again (true) or
    not (false). If the platform wants to poll sensors or execute some
    code during suspended without invoking userspace and most of devices,
    suspend_again callback is the place assuming that periodic-wakeup or
    alarm-wakeup is already setup. This allows to execute some codes while
    being kept suspended in the view of userland and devices.

end
    Called by the PM core right after resuming devices, to indicate to
    the platform that the system has returned to the working state or
    the transition to the sleep state has been aborted.
    This callback is optional, but should be implemented by the platforms
    that implement @\ :c:func:`begin`\ .  Accordingly, platforms implementing @\ :c:func:`begin`\ 
    should also provide a @\ :c:func:`end`\  which cleans up transitions aborted before
    @\ :c:func:`enter`\ .

recover
    Recover the platform from a suspend failure.
    Called by the PM core if the suspending of devices fails.
    This callback is optional and should only be implemented by platforms
    which require special recovery actions in that situation.

.. _`suspend_set_ops`:

suspend_set_ops
===============

.. c:function:: void suspend_set_ops(const struct platform_suspend_ops *ops)

    set platform dependent suspend operations

    :param const struct platform_suspend_ops \*ops:
        The new suspend operations to set.

.. _`arch_suspend_disable_irqs`:

arch_suspend_disable_irqs
=========================

.. c:function:: void arch_suspend_disable_irqs( void)

    disable IRQs for suspend

    :param  void:
        no arguments

.. _`arch_suspend_disable_irqs.description`:

Description
-----------

Disables IRQs (in the default case). This is a weak symbol in the common
code and thus allows architectures to override it if more needs to be
done. Not called for suspend to disk.

.. _`arch_suspend_enable_irqs`:

arch_suspend_enable_irqs
========================

.. c:function:: void arch_suspend_enable_irqs( void)

    enable IRQs after suspend

    :param  void:
        no arguments

.. _`arch_suspend_enable_irqs.description`:

Description
-----------

Enables IRQs (in the default case). This is a weak symbol in the common
code and thus allows architectures to override it if more needs to be
done. Not called for suspend to disk.

.. _`platform_hibernation_ops`:

struct platform_hibernation_ops
===============================

.. c:type:: struct platform_hibernation_ops

    hibernation platform support

.. _`platform_hibernation_ops.definition`:

Definition
----------

.. code-block:: c

    struct platform_hibernation_ops {
        int (* begin) (void);
        void (* end) (void);
        int (* pre_snapshot) (void);
        void (* finish) (void);
        int (* prepare) (void);
        int (* enter) (void);
        void (* leave) (void);
        int (* pre_restore) (void);
        void (* restore_cleanup) (void);
        void (* recover) (void);
    }

.. _`platform_hibernation_ops.members`:

Members
-------

begin
    Tell the platform driver that we're starting hibernation.
    Called right after shrinking memory and before freezing devices.

end
    Called by the PM core right after resuming devices, to indicate to
    the platform that the system has returned to the working state.

pre_snapshot
    Prepare the platform for creating the hibernation image.
    Called right after devices have been frozen and before the nonboot
    CPUs are disabled (runs with IRQs on).

finish
    Restore the previous state of the platform after the hibernation
    image has been created \*or\* put the platform into the normal operation
    mode after the hibernation (the same method is executed in both cases).
    Called right after the nonboot CPUs have been enabled and before
    thawing devices (runs with IRQs on).

prepare
    Prepare the platform for entering the low power state.
    Called right after the hibernation image has been saved and before
    devices are prepared for entering the low power state.

enter
    Put the system into the low power state after the hibernation image
    has been saved to disk.
    Called after the nonboot CPUs have been disabled and all of the low
    level devices have been shut down (runs with IRQs off).

leave
    Perform the first stage of the cleanup after the system sleep state
    indicated by @\ :c:func:`set_target`\  has been left.
    Called right after the control has been passed from the boot kernel to
    the image kernel, before the nonboot CPUs are enabled and before devices
    are resumed.  Executed with interrupts disabled.

pre_restore
    Prepare system for the restoration from a hibernation image.
    Called right after devices have been frozen and before the nonboot
    CPUs are disabled (runs with IRQs on).

restore_cleanup
    Clean up after a failing image restoration.
    Called right after the nonboot CPUs have been enabled and before
    thawing devices (runs with IRQs on).

recover
    Recover the platform from a failure to suspend devices.
    Called by the PM core if the suspending of devices during hibernation
    fails.  This callback is optional and should only be implemented by
    platforms which require special recovery actions in that situation.

.. _`platform_hibernation_ops.description`:

Description
-----------

The methods in this structure allow a platform to carry out special
operations required by it during a hibernation transition.

All the methods below, except for @\ :c:func:`recover`\ , must be implemented.

.. This file was automatic generated / don't edit.


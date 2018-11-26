.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/hibernate.c

.. _`hibernation_set_ops`:

hibernation_set_ops
===================

.. c:function:: void hibernation_set_ops(const struct platform_hibernation_ops *ops)

    Set the global hibernate operations.

    :param ops:
        Hibernation operations to use in subsequent hibernation transitions.
    :type ops: const struct platform_hibernation_ops \*

.. _`platform_begin`:

platform_begin
==============

.. c:function:: int platform_begin(int platform_mode)

    Call platform to start hibernation.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_end`:

platform_end
============

.. c:function:: void platform_end(int platform_mode)

    Call platform to finish transition to the working state.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_pre_snapshot`:

platform_pre_snapshot
=====================

.. c:function:: int platform_pre_snapshot(int platform_mode)

    Call platform to prepare the machine for hibernation.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_pre_snapshot.description`:

Description
-----------

Use the platform driver to prepare the system for creating a hibernate image,
if so configured, and return an error code if that fails.

.. _`platform_leave`:

platform_leave
==============

.. c:function:: void platform_leave(int platform_mode)

    Call platform to prepare a transition to the working state.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_leave.description`:

Description
-----------

Use the platform driver prepare to prepare the machine for switching to the
normal mode of operation.

This routine is called on one CPU with interrupts disabled.

.. _`platform_finish`:

platform_finish
===============

.. c:function:: void platform_finish(int platform_mode)

    Call platform to switch the system to the working state.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_finish.description`:

Description
-----------

Use the platform driver to switch the machine to the normal mode of
operation.

This routine must be called after \ :c:func:`platform_prepare`\ .

.. _`platform_pre_restore`:

platform_pre_restore
====================

.. c:function:: int platform_pre_restore(int platform_mode)

    Prepare for hibernate image restoration.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_pre_restore.description`:

Description
-----------

Use the platform driver to prepare the system for resume from a hibernation
image.

If the restore fails after this function has been called,
\ :c:func:`platform_restore_cleanup`\  must be called.

.. _`platform_restore_cleanup`:

platform_restore_cleanup
========================

.. c:function:: void platform_restore_cleanup(int platform_mode)

    Switch to the working state after failing restore.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`platform_restore_cleanup.description`:

Description
-----------

Use the platform driver to switch the system to the normal mode of operation
after a failing restore.

If \ :c:func:`platform_pre_restore`\  has been called before the failing restore, this
function must be called too, regardless of the result of
\ :c:func:`platform_pre_restore`\ .

.. _`platform_recover`:

platform_recover
================

.. c:function:: void platform_recover(int platform_mode)

    Recover from a failure to suspend devices.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`swsusp_show_speed`:

swsusp_show_speed
=================

.. c:function:: void swsusp_show_speed(ktime_t start, ktime_t stop, unsigned nr_pages, char *msg)

    Print time elapsed between two events during hibernation.

    :param start:
        Starting event.
    :type start: ktime_t

    :param stop:
        Final event.
    :type stop: ktime_t

    :param nr_pages:
        Number of memory pages processed between \ ``start``\  and \ ``stop``\ .
    :type nr_pages: unsigned

    :param msg:
        Additional diagnostic message to print.
    :type msg: char \*

.. _`create_image`:

create_image
============

.. c:function:: int create_image(int platform_mode)

    Create a hibernation image.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: int

.. _`create_image.description`:

Description
-----------

Execute device drivers' "late" and "noirq" freeze callbacks, create a
hibernation image and run the drivers' "noirq" and "early" thaw callbacks.

Control reappears in this routine after the subsequent restore.

.. _`hibernation_snapshot`:

hibernation_snapshot
====================

.. c:function:: int hibernation_snapshot(int platform_mode)

    Quiesce devices and create a hibernation image.

    :param platform_mode:
        If set, use platform driver to prepare for the transition.
    :type platform_mode: int

.. _`hibernation_snapshot.description`:

Description
-----------

This routine must be called with system_transition_mutex held.

.. _`resume_target_kernel`:

resume_target_kernel
====================

.. c:function:: int resume_target_kernel(bool platform_mode)

    Restore system state from a hibernation image.

    :param platform_mode:
        Whether or not to use the platform driver.
    :type platform_mode: bool

.. _`resume_target_kernel.description`:

Description
-----------

Execute device drivers' "noirq" and "late" freeze callbacks, restore the
contents of highmem that have not been restored yet from the image and run
the low-level code that will restore the remaining contents of memory and
switch to the just restored target kernel.

.. _`hibernation_restore`:

hibernation_restore
===================

.. c:function:: int hibernation_restore(int platform_mode)

    Quiesce devices and restore from a hibernation image.

    :param platform_mode:
        If set, use platform driver to prepare for the transition.
    :type platform_mode: int

.. _`hibernation_restore.description`:

Description
-----------

This routine must be called with system_transition_mutex held.  If it is
successful, control reappears in the restored target kernel in
\ :c:func:`hibernation_snapshot`\ .

.. _`hibernation_platform_enter`:

hibernation_platform_enter
==========================

.. c:function:: int hibernation_platform_enter( void)

    Power off the system using the platform driver.

    :param void:
        no arguments
    :type void: 

.. _`power_down`:

power_down
==========

.. c:function:: void power_down( void)

    Shut the machine down for hibernation.

    :param void:
        no arguments
    :type void: 

.. _`power_down.description`:

Description
-----------

Use the platform driver, if configured, to put the system into the sleep
state corresponding to hibernation, or try to power it off or reboot,
depending on the value of hibernation_mode.

.. _`hibernate`:

hibernate
=========

.. c:function:: int hibernate( void)

    Carry out system hibernation, including saving the image.

    :param void:
        no arguments
    :type void: 

.. _`software_resume`:

software_resume
===============

.. c:function:: int software_resume( void)

    Resume from a saved hibernation image.

    :param void:
        no arguments
    :type void: 

.. _`software_resume.description`:

Description
-----------

This routine is called as a late initcall, when all devices have been
discovered and initialized already.

The image reading code is called to see if there is a hibernation image
available for reading.  If that is the case, devices are quiesced and the
contents of memory is restored from the saved image.

If this is successful, control reappears in the restored target kernel in
\ :c:func:`hibernation_snapshot`\  which returns to \ :c:func:`hibernate`\ .  Otherwise, the routine
attempts to recover gracefully and make the kernel return to the normal mode
of operation.

.. This file was automatic generated / don't edit.


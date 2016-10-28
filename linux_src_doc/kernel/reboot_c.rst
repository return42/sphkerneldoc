.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/reboot.c

.. _`emergency_restart`:

emergency_restart
=================

.. c:function:: void emergency_restart( void)

    reboot the system

    :param  void:
        no arguments

.. _`emergency_restart.description`:

Description
-----------

Without shutting down any hardware or taking any locks
reboot the system.  This is called when we know we are in
trouble so this is our best effort to reboot.  This is
safe to call in interrupt context.

.. _`register_reboot_notifier`:

register_reboot_notifier
========================

.. c:function:: int register_reboot_notifier(struct notifier_block *nb)

    Register function to be called at reboot time

    :param struct notifier_block \*nb:
        Info about notifier function to be called

.. _`register_reboot_notifier.description`:

Description
-----------

Registers a function with the list of functions
to be called at reboot time.

Currently always returns zero, as \ :c:func:`blocking_notifier_chain_register`\ 
always returns zero.

.. _`unregister_reboot_notifier`:

unregister_reboot_notifier
==========================

.. c:function:: int unregister_reboot_notifier(struct notifier_block *nb)

    Unregister previously registered reboot notifier

    :param struct notifier_block \*nb:
        Hook to be unregistered

.. _`unregister_reboot_notifier.description`:

Description
-----------

Unregisters a previously registered reboot
notifier function.

Returns zero on success, or \ ``-ENOENT``\  on failure.

.. _`register_restart_handler`:

register_restart_handler
========================

.. c:function:: int register_restart_handler(struct notifier_block *nb)

    Register function to be called to reset the system

    :param struct notifier_block \*nb:
        Handler priority. Handlers should follow the
        following guidelines for setting priorities.
        0:      Restart handler of last resort,
        with limited restart capabilities
        128:    Default restart handler; use if no other
        restart handler is expected to be available,
        and/or if restart functionality is
        sufficient to restart the entire system
        255:    Highest priority restart handler, will
        preempt all other restart handlers

.. _`register_restart_handler.description`:

Description
-----------

Registers a function with code to be called to restart the
system.

Registered functions will be called from machine_restart as last
step of the restart sequence (if the architecture specific
machine_restart function calls do_kernel_restart - see below
for details).
Registered functions are expected to restart the system immediately.
If more than one function is registered, the restart handler priority
selects which function will be called first.

Restart handlers are expected to be registered from non-architecture
code, typically from drivers. A typical use case would be a system
where restart functionality is provided through a watchdog. Multiple
restart handlers may exist; for example, one restart handler might
restart the entire system, while another only restarts the CPU.
In such cases, the restart handler which only restarts part of the
hardware is expected to register with low priority to ensure that
it only runs if no other means to restart the system is available.

Currently always returns zero, as \ :c:func:`atomic_notifier_chain_register`\ 
always returns zero.

.. _`unregister_restart_handler`:

unregister_restart_handler
==========================

.. c:function:: int unregister_restart_handler(struct notifier_block *nb)

    Unregister previously registered restart handler

    :param struct notifier_block \*nb:
        Hook to be unregistered

.. _`unregister_restart_handler.description`:

Description
-----------

Unregisters a previously registered restart handler function.

Returns zero on success, or \ ``-ENOENT``\  on failure.

.. _`do_kernel_restart`:

do_kernel_restart
=================

.. c:function:: void do_kernel_restart(char *cmd)

    Execute kernel restart handler call chain

    :param char \*cmd:
        *undescribed*

.. _`do_kernel_restart.description`:

Description
-----------

Calls functions registered with register_restart_handler.

Expected to be called from machine_restart as last step of the restart
sequence.

Restarts the system immediately if a restart handler function has been
registered. Otherwise does nothing.

.. _`kernel_restart`:

kernel_restart
==============

.. c:function:: void kernel_restart(char *cmd)

    reboot the system

    :param char \*cmd:
        pointer to buffer containing command to execute for restart
        or \ ``NULL``\ 

.. _`kernel_restart.description`:

Description
-----------

Shutdown everything and perform a clean reboot.
This is not safe to call in interrupt context.

.. _`kernel_halt`:

kernel_halt
===========

.. c:function:: void kernel_halt( void)

    halt the system

    :param  void:
        no arguments

.. _`kernel_halt.description`:

Description
-----------

Shutdown everything and perform a clean system halt.

.. _`kernel_power_off`:

kernel_power_off
================

.. c:function:: void kernel_power_off( void)

    power_off the system

    :param  void:
        no arguments

.. _`kernel_power_off.description`:

Description
-----------

Shutdown everything and perform a clean system power_off.

.. _`orderly_poweroff`:

orderly_poweroff
================

.. c:function:: void orderly_poweroff(bool force)

    Trigger an orderly system poweroff

    :param bool force:
        force poweroff if command execution fails

.. _`orderly_poweroff.description`:

Description
-----------

This may be called from any context to trigger a system shutdown.
If the orderly shutdown fails, it will force an immediate shutdown.

.. _`orderly_reboot`:

orderly_reboot
==============

.. c:function:: void orderly_reboot( void)

    Trigger an orderly system reboot

    :param  void:
        no arguments

.. _`orderly_reboot.description`:

Description
-----------

This may be called from any context to trigger a system reboot.
If the orderly reboot fails, it will force an immediate reboot.

.. This file was automatic generated / don't edit.


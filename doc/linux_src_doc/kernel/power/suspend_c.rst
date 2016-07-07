.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/suspend.c

.. _`suspend_set_ops`:

suspend_set_ops
===============

.. c:function:: void suspend_set_ops(const struct platform_suspend_ops *ops)

    Set the global suspend method table.

    :param const struct platform_suspend_ops \*ops:
        Suspend operations to use.

.. _`suspend_valid_only_mem`:

suspend_valid_only_mem
======================

.. c:function:: int suspend_valid_only_mem(suspend_state_t state)

    Generic memory-only valid callback.

    :param suspend_state_t state:
        *undescribed*

.. _`suspend_valid_only_mem.description`:

Description
-----------

Platform drivers that implement mem suspend only and only need to check for
that in their .\ :c:func:`valid`\  callback can use this instead of rolling their own
.\ :c:func:`valid`\  callback.

.. _`suspend_prepare`:

suspend_prepare
===============

.. c:function:: int suspend_prepare(suspend_state_t state)

    Prepare for entering system sleep state.

    :param suspend_state_t state:
        *undescribed*

.. _`suspend_prepare.description`:

Description
-----------

Common code run for every system sleep state that can be entered (except for
hibernation).  Run suspend notifiers, allocate the "suspend" console and
freeze processes.

.. _`suspend_enter`:

suspend_enter
=============

.. c:function:: int suspend_enter(suspend_state_t state, bool *wakeup)

    Make the system enter the given sleep state.

    :param suspend_state_t state:
        System sleep state to enter.

    :param bool \*wakeup:
        Returns information that the sleep state should not be re-entered.

.. _`suspend_enter.description`:

Description
-----------

This function should be called after devices have been suspended.

.. _`suspend_devices_and_enter`:

suspend_devices_and_enter
=========================

.. c:function:: int suspend_devices_and_enter(suspend_state_t state)

    Suspend devices and enter system sleep state.

    :param suspend_state_t state:
        System sleep state to enter.

.. _`suspend_finish`:

suspend_finish
==============

.. c:function:: void suspend_finish( void)

    Clean up before finishing the suspend sequence.

    :param  void:
        no arguments

.. _`suspend_finish.description`:

Description
-----------

Call platform code to clean up, restart processes, and free the console that
we've allocated. This routine is not called for hibernation.

.. _`enter_state`:

enter_state
===========

.. c:function:: int enter_state(suspend_state_t state)

    Do common work needed to enter system sleep state.

    :param suspend_state_t state:
        System sleep state to enter.

.. _`enter_state.description`:

Description
-----------

Make sure that no one else is trying to put the system into a sleep state.
Fail if that's not the case.  Otherwise, prepare for system suspend, make the
system enter the given sleep state and clean up after wakeup.

.. _`pm_suspend`:

pm_suspend
==========

.. c:function:: int pm_suspend(suspend_state_t state)

    Externally visible function for suspending the system.

    :param suspend_state_t state:
        System sleep state to enter.

.. _`pm_suspend.description`:

Description
-----------

Check if the value of \ ``state``\  represents one of the supported states,
execute \ :c:func:`enter_state`\  and update system suspend statistics.

.. This file was automatic generated / don't edit.


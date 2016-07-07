.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/tick-common.c

.. _`tick_is_oneshot_available`:

tick_is_oneshot_available
=========================

.. c:function:: int tick_is_oneshot_available( void)

    check for a oneshot capable event device

    :param  void:
        no arguments

.. _`tick_broadcast_oneshot_control`:

tick_broadcast_oneshot_control
==============================

.. c:function:: int tick_broadcast_oneshot_control(enum tick_broadcast_state state)

    Enter/exit broadcast oneshot mode

    :param enum tick_broadcast_state state:
        The target state (enter/exit)

.. _`tick_broadcast_oneshot_control.description`:

Description
-----------

The system enters/leaves a state, where affected devices might stop
Returns 0 on success, -EBUSY if the cpu is used to broadcast wakeups.

Called with interrupts disabled, so clockevents_lock is not
required here because the local clock event device cannot go away
under us.

.. _`tick_suspend_local`:

tick_suspend_local
==================

.. c:function:: void tick_suspend_local( void)

    Suspend the local tick device

    :param  void:
        no arguments

.. _`tick_suspend_local.description`:

Description
-----------

Called from the local cpu for freeze with interrupts disabled.

No locks required. Nothing can change the per cpu device.

.. _`tick_resume_local`:

tick_resume_local
=================

.. c:function:: void tick_resume_local( void)

    Resume the local tick device

    :param  void:
        no arguments

.. _`tick_resume_local.description`:

Description
-----------

Called from the local CPU for unfreeze or XEN resume magic.

No locks required. Nothing can change the per cpu device.

.. _`tick_suspend`:

tick_suspend
============

.. c:function:: void tick_suspend( void)

    Suspend the tick and the broadcast device

    :param  void:
        no arguments

.. _`tick_suspend.description`:

Description
-----------

Called from \ :c:func:`syscore_suspend`\  via timekeeping_suspend with only one
CPU online and interrupts disabled or from \ :c:func:`tick_unfreeze`\  under
tick_freeze_lock.

No locks required. Nothing can change the per cpu device.

.. _`tick_resume`:

tick_resume
===========

.. c:function:: void tick_resume( void)

    Resume the tick and the broadcast device

    :param  void:
        no arguments

.. _`tick_resume.description`:

Description
-----------

Called from \ :c:func:`syscore_resume`\  via timekeeping_resume with only one
CPU online and interrupts disabled.

No locks required. Nothing can change the per cpu device.

.. _`tick_freeze`:

tick_freeze
===========

.. c:function:: void tick_freeze( void)

    Suspend the local tick and (possibly) timekeeping.

    :param  void:
        no arguments

.. _`tick_freeze.description`:

Description
-----------

Check if this is the last online CPU executing the function and if so,
suspend timekeeping.  Otherwise suspend the local tick.

Call with interrupts disabled.  Must be balanced with %\ :c:func:`tick_unfreeze`\ .
Interrupts must not be enabled before the subsequent %\ :c:func:`tick_unfreeze`\ .

.. _`tick_unfreeze`:

tick_unfreeze
=============

.. c:function:: void tick_unfreeze( void)

    Resume the local tick and (possibly) timekeeping.

    :param  void:
        no arguments

.. _`tick_unfreeze.description`:

Description
-----------

Check if this is the first CPU executing the function and if so, resume
timekeeping.  Otherwise resume the local tick.

Call with interrupts disabled.  Must be balanced with %\ :c:func:`tick_freeze`\ .
Interrupts must not be enabled after the preceding %\ :c:func:`tick_freeze`\ .

.. _`tick_init`:

tick_init
=========

.. c:function:: void tick_init( void)

    initialize the tick control

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

================
tick-broadcast.c
================


.. _`tick_broadcast_control`:

tick_broadcast_control
======================

.. c:function:: void tick_broadcast_control (enum tick_broadcast_mode mode)

    Enable/disable or force broadcast mode

    :param enum tick_broadcast_mode mode:
        The selected broadcast mode



.. _`tick_broadcast_control.description`:

Description
-----------

Called when the system enters a state where affected tick devices
might stop. Note: TICK_BROADCAST_FORCE cannot be undone.

Called with interrupts disabled, so clockevents_lock is not
required here because the local clock event device cannot go away
under us.



.. _`tick_broadcast_setup_oneshot`:

tick_broadcast_setup_oneshot
============================

.. c:function:: void tick_broadcast_setup_oneshot (struct clock_event_device *bc)

    setup the broadcast device

    :param struct clock_event_device \*bc:

        *undescribed*


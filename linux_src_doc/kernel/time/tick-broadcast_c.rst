.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/tick-broadcast.c

.. _`tick_broadcast_control`:

tick_broadcast_control
======================

.. c:function:: void tick_broadcast_control(enum tick_broadcast_mode mode)

    Enable/disable or force broadcast mode

    :param mode:
        The selected broadcast mode
    :type mode: enum tick_broadcast_mode

.. _`tick_broadcast_control.description`:

Description
-----------

Called when the system enters a state where affected tick devices
might stop. Note: TICK_BROADCAST_FORCE cannot be undone.

.. _`tick_broadcast_setup_oneshot`:

tick_broadcast_setup_oneshot
============================

.. c:function:: void tick_broadcast_setup_oneshot(struct clock_event_device *bc)

    setup the broadcast device

    :param bc:
        *undescribed*
    :type bc: struct clock_event_device \*

.. This file was automatic generated / don't edit.


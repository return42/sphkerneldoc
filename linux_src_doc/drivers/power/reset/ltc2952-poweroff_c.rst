.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/reset/ltc2952-poweroff.c

.. _`ltc2952_poweroff_timer_wde`:

ltc2952_poweroff_timer_wde
==========================

.. c:function:: enum hrtimer_restart ltc2952_poweroff_timer_wde(struct hrtimer *timer)

    Timer callback Toggles the watchdog reset signal each wde_interval

    :param timer:
        corresponding timer
    :type timer: struct hrtimer \*

.. _`ltc2952_poweroff_timer_wde.description`:

Description
-----------

Returns HRTIMER_RESTART for an infinite loop which will only stop when the
machine actually shuts down

.. _`ltc2952_poweroff_handler`:

ltc2952_poweroff_handler
========================

.. c:function:: irqreturn_t ltc2952_poweroff_handler(int irq, void *dev_id)

    Interrupt handler Triggered each time the trigger signal changes state and (de)activates a time-out (timer_trigger). Once the time-out is actually reached the shut down is executed.

    :param irq:
        IRQ number
    :type irq: int

    :param dev_id:
        pointer to the main data structure
    :type dev_id: void \*

.. This file was automatic generated / don't edit.


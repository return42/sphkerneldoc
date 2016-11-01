.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/cadence_ttc_timer.c

.. _`ttc_timer`:

struct ttc_timer
================

.. c:type:: struct ttc_timer

    This definition defines local timer structure

.. _`ttc_timer.definition`:

Definition
----------

.. code-block:: c

    struct ttc_timer {
        void __iomem *base_addr;
        unsigned long freq;
        struct clk *clk;
        struct notifier_block clk_rate_change_nb;
    }

.. _`ttc_timer.members`:

Members
-------

base_addr
    Base address of timer

freq
    Timer input clock frequency

clk
    Associated clock source
    \ ``clk_rate_change_nb``\   Notifier block for clock rate changes

clk_rate_change_nb
    *undescribed*

.. _`ttc_set_interval`:

ttc_set_interval
================

.. c:function:: void ttc_set_interval(struct ttc_timer *timer, unsigned long cycles)

    Set the timer interval value

    :param struct ttc_timer \*timer:
        Pointer to the timer instance

    :param unsigned long cycles:
        Timer interval ticks

.. _`ttc_clock_event_interrupt`:

ttc_clock_event_interrupt
=========================

.. c:function:: irqreturn_t ttc_clock_event_interrupt(int irq, void *dev_id)

    Clock event timer interrupt handler

    :param int irq:
        IRQ number of the Timer

    :param void \*dev_id:
        void pointer to the ttc_timer instance

.. _`ttc_clock_event_interrupt.return`:

Return
------

Always IRQ_HANDLED - success

.. _`__ttc_clocksource_read`:

__ttc_clocksource_read
======================

.. c:function:: cycle_t __ttc_clocksource_read(struct clocksource *cs)

    Reads the timer counter register

    :param struct clocksource \*cs:
        *undescribed*

.. _`__ttc_clocksource_read.return`:

Return
------

Current timer counter register value

.. _`ttc_set_next_event`:

ttc_set_next_event
==================

.. c:function:: int ttc_set_next_event(unsigned long cycles, struct clock_event_device *evt)

    Sets the time interval for next event

    :param unsigned long cycles:
        Timer interval ticks

    :param struct clock_event_device \*evt:
        Address of clock event instance

.. _`ttc_set_next_event.return`:

Return
------

Always 0 - success

.. _`ttc_shutdown`:

ttc_shutdown
============

.. c:function:: int ttc_shutdown(struct clock_event_device *evt)

    Sets the state of timer

    :param struct clock_event_device \*evt:
        Address of clock event instance

.. _`ttc_timer_init`:

ttc_timer_init
==============

.. c:function:: int ttc_timer_init(struct device_node *timer)

    Initialize the timer

    :param struct device_node \*timer:
        *undescribed*

.. _`ttc_timer_init.description`:

Description
-----------

Initializes the timer hardware and register the clock source and clock event
timers with Linux kernal timer framework

.. This file was automatic generated / don't edit.


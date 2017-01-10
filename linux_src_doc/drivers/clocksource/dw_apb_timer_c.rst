.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/dw_apb_timer.c

.. _`dw_apb_clockevent_pause`:

dw_apb_clockevent_pause
=======================

.. c:function:: void dw_apb_clockevent_pause(struct dw_apb_clock_event_device *dw_ced)

    stop the clock_event_device from running

    :param struct dw_apb_clock_event_device \*dw_ced:
        The APB clock to stop generating events.

.. _`dw_apb_clockevent_init`:

dw_apb_clockevent_init
======================

.. c:function:: struct dw_apb_clock_event_device *dw_apb_clockevent_init(int cpu, const char *name, unsigned rating, void __iomem *base, int irq, unsigned long freq)

    use an APB timer as a clock_event_device

    :param int cpu:
        The CPU the events will be targeted at.

    :param const char \*name:
        The name used for the timer and the IRQ for it.

    :param unsigned rating:
        The rating to give the timer.

    :param void __iomem \*base:
        I/O base for the timer registers.

    :param int irq:
        The interrupt number to use for the timer.

    :param unsigned long freq:
        The frequency that the timer counts at.

.. _`dw_apb_clockevent_init.description`:

Description
-----------

This creates a clock_event_device for using with the generic clock layer
but does not start and register it.  This should be done with
\ :c:func:`dw_apb_clockevent_register`\  as the next step.  If this is the first time
it has been called for a timer then the IRQ will be requested, if not it
just be enabled to allow CPU hotplug to avoid repeatedly requesting and
releasing the IRQ.

.. _`dw_apb_clockevent_resume`:

dw_apb_clockevent_resume
========================

.. c:function:: void dw_apb_clockevent_resume(struct dw_apb_clock_event_device *dw_ced)

    resume a clock that has been paused.

    :param struct dw_apb_clock_event_device \*dw_ced:
        The APB clock to resume.

.. _`dw_apb_clockevent_stop`:

dw_apb_clockevent_stop
======================

.. c:function:: void dw_apb_clockevent_stop(struct dw_apb_clock_event_device *dw_ced)

    stop the clock_event_device and release the IRQ.

    :param struct dw_apb_clock_event_device \*dw_ced:
        The APB clock to stop generating the events.

.. _`dw_apb_clockevent_register`:

dw_apb_clockevent_register
==========================

.. c:function:: void dw_apb_clockevent_register(struct dw_apb_clock_event_device *dw_ced)

    register the clock with the generic layer

    :param struct dw_apb_clock_event_device \*dw_ced:
        The APB clock to register as a clock_event_device.

.. _`dw_apb_clocksource_start`:

dw_apb_clocksource_start
========================

.. c:function:: void dw_apb_clocksource_start(struct dw_apb_clocksource *dw_cs)

    start the clocksource counting.

    :param struct dw_apb_clocksource \*dw_cs:
        The clocksource to start.

.. _`dw_apb_clocksource_start.description`:

Description
-----------

This is used to start the clocksource before registration and can be used
to enable calibration of timers.

.. _`dw_apb_clocksource_init`:

dw_apb_clocksource_init
=======================

.. c:function:: struct dw_apb_clocksource *dw_apb_clocksource_init(unsigned rating, const char *name, void __iomem *base, unsigned long freq)

    use an APB timer as a clocksource.

    :param unsigned rating:
        The rating to give the clocksource.

    :param const char \*name:
        The name for the clocksource.

    :param void __iomem \*base:
        The I/O base for the timer registers.

    :param unsigned long freq:
        The frequency that the timer counts at.

.. _`dw_apb_clocksource_init.description`:

Description
-----------

This creates a clocksource using an APB timer but does not yet register it
with the clocksource system.  This should be done with
\ :c:func:`dw_apb_clocksource_register`\  as the next step.

.. _`dw_apb_clocksource_register`:

dw_apb_clocksource_register
===========================

.. c:function:: void dw_apb_clocksource_register(struct dw_apb_clocksource *dw_cs)

    register the APB clocksource.

    :param struct dw_apb_clocksource \*dw_cs:
        The clocksource to register.

.. _`dw_apb_clocksource_read`:

dw_apb_clocksource_read
=======================

.. c:function:: u64 dw_apb_clocksource_read(struct dw_apb_clocksource *dw_cs)

    read the current value of a clocksource.

    :param struct dw_apb_clocksource \*dw_cs:
        The clocksource to read.

.. This file was automatic generated / don't edit.


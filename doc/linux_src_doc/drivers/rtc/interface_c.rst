.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/interface.c

.. _`rtc_handle_legacy_irq`:

rtc_handle_legacy_irq
=====================

.. c:function:: void rtc_handle_legacy_irq(struct rtc_device *rtc, int num, int mode)

    AIE, UIE and PIE event hook

    :param struct rtc_device \*rtc:
        pointer to the rtc device

    :param int num:
        *undescribed*

    :param int mode:
        *undescribed*

.. _`rtc_handle_legacy_irq.description`:

Description
-----------

This function is called when an AIE, UIE or PIE mode interrupt
has occurred (or been emulated).

Triggers the registered irq_task function callback.

.. _`rtc_aie_update_irq`:

rtc_aie_update_irq
==================

.. c:function:: void rtc_aie_update_irq(void *private)

    AIE mode rtctimer hook

    :param void \*private:
        pointer to the rtc_device

.. _`rtc_aie_update_irq.description`:

Description
-----------

This functions is called when the aie_timer expires.

.. _`rtc_uie_update_irq`:

rtc_uie_update_irq
==================

.. c:function:: void rtc_uie_update_irq(void *private)

    UIE mode rtctimer hook

    :param void \*private:
        pointer to the rtc_device

.. _`rtc_uie_update_irq.description`:

Description
-----------

This functions is called when the uie_timer expires.

.. _`rtc_pie_update_irq`:

rtc_pie_update_irq
==================

.. c:function:: enum hrtimer_restart rtc_pie_update_irq(struct hrtimer *timer)

    PIE mode hrtimer hook

    :param struct hrtimer \*timer:
        pointer to the pie mode hrtimer

.. _`rtc_pie_update_irq.description`:

Description
-----------

This function is used to emulate PIE mode interrupts
using an hrtimer. This function is called when the periodic
hrtimer expires.

.. _`rtc_update_irq`:

rtc_update_irq
==============

.. c:function:: void rtc_update_irq(struct rtc_device *rtc, unsigned long num, unsigned long events)

    Triggered when a RTC interrupt occurs.

    :param struct rtc_device \*rtc:
        the rtc device

    :param unsigned long num:
        how many irqs are being reported (usually one)

    :param unsigned long events:
        mask of RTC_IRQF with one or more of RTC_PF, RTC_AF, RTC_UF

.. _`rtc_update_irq.context`:

Context
-------

any

.. _`rtc_irq_set_state`:

rtc_irq_set_state
=================

.. c:function:: int rtc_irq_set_state(struct rtc_device *rtc, struct rtc_task *task, int enabled)

    enable/disable 2^N Hz periodic IRQs

    :param struct rtc_device \*rtc:
        the rtc device

    :param struct rtc_task \*task:
        currently registered with \ :c:func:`rtc_irq_register`\ 

    :param int enabled:
        true to enable periodic IRQs

.. _`rtc_irq_set_state.context`:

Context
-------

any

.. _`rtc_irq_set_state.description`:

Description
-----------

Note that \ :c:func:`rtc_irq_set_freq`\  should previously have been used to
specify the desired frequency of periodic IRQ task->\ :c:func:`func`\  callbacks.

.. _`rtc_irq_set_freq`:

rtc_irq_set_freq
================

.. c:function:: int rtc_irq_set_freq(struct rtc_device *rtc, struct rtc_task *task, int freq)

    set 2^N Hz periodic IRQ frequency for IRQ

    :param struct rtc_device \*rtc:
        the rtc device

    :param struct rtc_task \*task:
        currently registered with \ :c:func:`rtc_irq_register`\ 

    :param int freq:
        positive frequency with which task->\ :c:func:`func`\  will be called

.. _`rtc_irq_set_freq.context`:

Context
-------

any

.. _`rtc_irq_set_freq.description`:

Description
-----------

Note that \ :c:func:`rtc_irq_set_state`\  is used to enable or disable the
periodic IRQs.

.. _`rtc_timer_enqueue`:

rtc_timer_enqueue
=================

.. c:function:: int rtc_timer_enqueue(struct rtc_device *rtc, struct rtc_timer *timer)

    Adds a rtc_timer to the rtc_device timerqueue \ ``rtc``\  rtc device \ ``timer``\  timer being added.

    :param struct rtc_device \*rtc:
        *undescribed*

    :param struct rtc_timer \*timer:
        *undescribed*

.. _`rtc_timer_enqueue.description`:

Description
-----------

Enqueues a timer onto the rtc devices timerqueue and sets
the next alarm event appropriately.

Sets the enabled bit on the added timer.

Must hold ops_lock for proper serialization of timerqueue

.. _`rtc_timer_remove`:

rtc_timer_remove
================

.. c:function:: void rtc_timer_remove(struct rtc_device *rtc, struct rtc_timer *timer)

    Removes a rtc_timer from the rtc_device timerqueue \ ``rtc``\  rtc device \ ``timer``\  timer being removed.

    :param struct rtc_device \*rtc:
        *undescribed*

    :param struct rtc_timer \*timer:
        *undescribed*

.. _`rtc_timer_remove.description`:

Description
-----------

Removes a timer onto the rtc devices timerqueue and sets
the next alarm event appropriately.

Clears the enabled bit on the removed timer.

Must hold ops_lock for proper serialization of timerqueue

.. _`rtc_timer_do_work`:

rtc_timer_do_work
=================

.. c:function:: void rtc_timer_do_work(struct work_struct *work)

    Expires rtc timers \ ``rtc``\  rtc device \ ``timer``\  timer being removed.

    :param struct work_struct \*work:
        *undescribed*

.. _`rtc_timer_do_work.description`:

Description
-----------

Expires rtc timers. Reprograms next alarm event if needed.
Called via worktask.

Serializes access to timerqueue via ops_lock mutex

.. _`rtc_read_offset`:

rtc_read_offset
===============

.. c:function:: int rtc_read_offset(struct rtc_device *rtc, long *offset)

    Read the amount of rtc offset in parts per billion @ rtc: rtc device to be used @ offset: the offset in parts per billion

    :param struct rtc_device \*rtc:
        *undescribed*

    :param long \*offset:
        *undescribed*

.. _`rtc_read_offset.description`:

Description
-----------

see below for details.

Kernel interface to read rtc clock offset
Returns 0 on success, or a negative number on error.
If \ :c:func:`read_offset`\  is not implemented for the rtc, return -EINVAL

.. _`rtc_set_offset`:

rtc_set_offset
==============

.. c:function:: int rtc_set_offset(struct rtc_device *rtc, long offset)

    Adjusts the duration of the average second @ rtc: rtc device to be used @ offset: the offset in parts per billion

    :param struct rtc_device \*rtc:
        *undescribed*

    :param long offset:
        *undescribed*

.. _`rtc_set_offset.description`:

Description
-----------

Some rtc's allow an adjustment to the average duration of a second
to compensate for differences in the actual clock rate due to temperature,
the crystal, capacitor, etc.

Kernel interface to adjust an rtc clock offset.
Return 0 on success, or a negative number on error.
If the rtc offset is not setable (or not implemented), return -EINVAL

.. This file was automatic generated / don't edit.


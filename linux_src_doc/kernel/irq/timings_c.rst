.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/timings.c

.. _`irqs_update`:

irqs_update
===========

.. c:function:: void irqs_update(struct irqt_stat *irqs, u64 ts)

    update the irq timing statistics with a new timestamp

    :param irqs:
        an irqt_stat struct pointer
    :type irqs: struct irqt_stat \*

    :param ts:
        the new timestamp
    :type ts: u64

.. _`irqs_update.description`:

Description
-----------

The statistics are computed online, in other words, the code is
designed to compute the statistics on a stream of values rather
than doing multiple passes on the values to compute the average,
then the variance. The integer division introduces a loss of
precision but with an acceptable error margin regarding the results

.. _`irqs_update.we-would-have-with-the-double-floating-precision`:

we would have with the double floating precision
------------------------------------------------

we are dealing
with nanosec, so big numbers, consequently the mantisse is
negligeable, especially when converting the time in usec
afterwards.

The computation happens at idle time. When the CPU is not idle, the
interrupts' timestamps are stored in the circular buffer, when the
CPU goes idle and this routine is called, all the buffer's values
are injected in the statistical model continuying to extend the
statistics from the previous busy-idle cycle.

The observations showed a device will trigger a burst of periodic
interrupts followed by one or two peaks of longer time, for
instance when a SD card device flushes its cache, then the periodic
intervals occur again. A one second inactivity period resets the
stats, that gives us the certitude the statistical values won't
exceed 1x10^9, thus the computation won't overflow.

Basically, the purpose of the algorithm is to watch the periodic
interrupts and eliminate the peaks.

An interrupt is considered periodically stable if the interval of
its occurences follow the normal distribution, thus the values

.. _`irqs_update.comply-with`:

comply with
-----------


avg - 3 x stddev < value < avg + 3 x stddev

.. _`irqs_update.which-can-be-simplified-to`:

Which can be simplified to
--------------------------


-3 x stddev < value - avg < 3 x stddev

abs(value - avg) < 3 x stddev

In order to save a costly square root computation, we use the
variance. For the record, stddev = sqrt(variance). The equation

.. _`irqs_update.above-becomes`:

above becomes
-------------


abs(value - avg) < 3 x sqrt(variance)

.. _`irqs_update.and-finally-we-square-it`:

And finally we square it
------------------------


(value - avg) ^ 2 < (3 x sqrt(variance)) ^ 2

(value - avg) x (value - avg) < 9 x variance

Statistically speaking, any values out of this interval is
considered as an anomaly and is discarded. However, a normal
distribution appears when the number of samples is 30 (it is the
rule of thumb in statistics, cf. "30 samples" on Internet). When
there are three consecutive anomalies, the statistics are resetted.

.. _`irq_timings_next_event`:

irq_timings_next_event
======================

.. c:function:: u64 irq_timings_next_event(u64 now)

    Return when the next event is supposed to arrive

    :param now:
        *undescribed*
    :type now: u64

.. _`irq_timings_next_event.description`:

Description
-----------

During the last busy cycle, the number of interrupts is incremented
and stored in the irq_timings structure. This information is

.. _`irq_timings_next_event.necessary-to`:

necessary to
------------


- know if the index in the table wrapped up:

If more than the array size interrupts happened during the
last busy/idle cycle, the index wrapped up and we have to
begin with the next element in the array which is the last one
in the sequence, otherwise it is a the index 0.

- have an indication of the interrupts activity on this CPU
(eg. irq/sec)

The values are 'consumed' after inserting in the statistical model,
thus the count is reinitialized.

The array of values \*\*must\*\* be browsed in the time direction, the
timestamp must increase between an element and the next one.

Returns a nanosec time based estimation of the earliest interrupt,
U64_MAX otherwise.

.. This file was automatic generated / don't edit.


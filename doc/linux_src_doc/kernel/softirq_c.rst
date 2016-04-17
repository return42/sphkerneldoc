.. -*- coding: utf-8; mode: rst -*-

=========
softirq.c
=========


.. _`tasklet_hrtimer_init`:

tasklet_hrtimer_init
====================

.. c:function:: void tasklet_hrtimer_init (struct tasklet_hrtimer *ttimer, enum hrtimer_restart (*function) (struct hrtimer *, clockid_t which_clock, enum hrtimer_mode mode)

    Init a tasklet/hrtimer combo for softirq callbacks

    :param struct tasklet_hrtimer \*ttimer:
        tasklet_hrtimer which is initialized

    :param enum hrtimer_restart (\*function) (struct hrtimer \*):
        hrtimer callback function which gets called from softirq context

    :param clockid_t which_clock:
        clock id (CLOCK_MONOTONIC/CLOCK_REALTIME)

    :param enum hrtimer_mode mode:
        hrtimer mode (HRTIMER_MODE_ABS/HRTIMER_MODE_REL)


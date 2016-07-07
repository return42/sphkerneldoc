.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/timekeeping.h

.. _`do_settimeofday`:

do_settimeofday
===============

.. c:function:: int do_settimeofday(const struct timespec *ts)

    :param const struct timespec \*ts:
        *undescribed*

.. _`do_settimeofday`:

do_settimeofday
===============

.. c:function:: int do_settimeofday(const struct timespec *ts)

    :param const struct timespec \*ts:
        *undescribed*

.. _`ktime_get_real`:

ktime_get_real
==============

.. c:function:: ktime_t ktime_get_real( void)

    get the real (wall-) time in ktime_t format

    :param  void:
        no arguments

.. _`ktime_get_boottime`:

ktime_get_boottime
==================

.. c:function:: ktime_t ktime_get_boottime( void)

    Returns monotonic time since boot in ktime_t format

    :param  void:
        no arguments

.. _`ktime_get_boottime.description`:

Description
-----------

This is similar to CLOCK_MONTONIC/ktime_get, but also includes the
time spent in suspend.

.. _`ktime_get_clocktai`:

ktime_get_clocktai
==================

.. c:function:: ktime_t ktime_get_clocktai( void)

    Returns the TAI time of day in ktime_t format

    :param  void:
        no arguments

.. _`ktime_mono_to_real`:

ktime_mono_to_real
==================

.. c:function:: ktime_t ktime_mono_to_real(ktime_t mono)

    Convert monotonic time to clock realtime

    :param ktime_t mono:
        *undescribed*

.. This file was automatic generated / don't edit.


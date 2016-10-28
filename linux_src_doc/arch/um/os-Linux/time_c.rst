.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/um/os-Linux/time.c

.. _`os_timer_create`:

os_timer_create
===============

.. c:function:: int os_timer_create(void*timer)

    create an new posix (interval) timer

    :param void\*timer:
        *undescribed*

.. _`os_timer_remain`:

os_timer_remain
===============

.. c:function:: long os_timer_remain(void*timer)

    returns the remaining nano seconds of the given interval timer Because this is the remaining time of an interval timer, which correspondends to HZ, this value can never be bigger than one second. Just the nanosecond part of the timer is returned. The returned time is relative to the start time of the interval timer. Return an negative value in an error case.

    :param void\*timer:
        *undescribed*

.. _`os_timer_disable`:

os_timer_disable
================

.. c:function:: long long os_timer_disable( void)

    disable the posix (interval) timer Returns the remaining interval timer time in nanoseconds

    :param  void:
        no arguments

.. _`os_idle_sleep`:

os_idle_sleep
=============

.. c:function:: void os_idle_sleep(unsigned long long nsecs)

    sleep for a given time of nsecs

    :param unsigned long long nsecs:
        nanoseconds to sleep

.. This file was automatic generated / don't edit.


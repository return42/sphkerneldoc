.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpufreq.h

.. _`cpufreq_scale`:

cpufreq_scale
=============

.. c:function:: unsigned long cpufreq_scale(unsigned long old, u_int div, u_int mult)

    "old \* mult / div" calculation for large values (32-bit-arch safe)

    :param old:
        old value
    :type old: unsigned long

    :param div:
        divisor
    :type div: u_int

    :param mult:
        multiplier
    :type mult: u_int

.. _`cpufreq_scale.description`:

Description
-----------


new = old \* mult / div

.. This file was automatic generated / don't edit.


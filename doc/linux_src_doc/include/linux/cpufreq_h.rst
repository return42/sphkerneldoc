.. -*- coding: utf-8; mode: rst -*-

=========
cpufreq.h
=========


.. _`cpufreq_scale`:

cpufreq_scale
=============

.. c:function:: unsigned long cpufreq_scale (unsigned long old, u_int div, u_int mult)

    "old * mult / div" calculation for large values (32-bit-arch safe)

    :param unsigned long old:
        old value

    :param u_int div:
        divisor

    :param u_int mult:
        multiplier



.. _`cpufreq_scale.description`:

Description
-----------


new = old * mult / div


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/cpufreq_userspace.c

.. _`cpufreq_set`:

cpufreq_set
===========

.. c:function:: int cpufreq_set(struct cpufreq_policy *policy, unsigned int freq)

    set the CPU frequency

    :param policy:
        pointer to policy struct where freq is being set
    :type policy: struct cpufreq_policy \*

    :param freq:
        target frequency in kHz
    :type freq: unsigned int

.. _`cpufreq_set.description`:

Description
-----------

Sets the CPU frequency to freq.

.. This file was automatic generated / don't edit.


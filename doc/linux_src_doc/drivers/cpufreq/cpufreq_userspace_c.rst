.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/cpufreq_userspace.c

.. _`cpufreq_set`:

cpufreq_set
===========

.. c:function:: int cpufreq_set(struct cpufreq_policy *policy, unsigned int freq)

    set the CPU frequency

    :param struct cpufreq_policy \*policy:
        pointer to policy struct where freq is being set

    :param unsigned int freq:
        target frequency in kHz

.. _`cpufreq_set.description`:

Description
-----------

Sets the CPU frequency to freq.

.. This file was automatic generated / don't edit.


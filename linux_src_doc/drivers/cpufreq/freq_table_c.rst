.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/freq_table.c

.. _`show_available_freqs`:

show_available_freqs
====================

.. c:function:: ssize_t show_available_freqs(struct cpufreq_policy *policy, char *buf, bool show_boost)

    show available frequencies for the specified CPU

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param show_boost:
        *undescribed*
    :type show_boost: bool

.. _`scaling_available_frequencies_show`:

scaling_available_frequencies_show
==================================

.. c:function:: ssize_t scaling_available_frequencies_show(struct cpufreq_policy *policy, char *buf)

    show available normal frequencies for the specified CPU

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`scaling_boost_frequencies_show`:

scaling_boost_frequencies_show
==============================

.. c:function:: ssize_t scaling_boost_frequencies_show(struct cpufreq_policy *policy, char *buf)

    show available boost frequencies for the specified CPU

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. This file was automatic generated / don't edit.


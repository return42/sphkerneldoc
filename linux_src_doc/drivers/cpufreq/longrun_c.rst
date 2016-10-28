.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/longrun.c

.. _`longrun_get_policy`:

longrun_get_policy
==================

.. c:function:: void longrun_get_policy(struct cpufreq_policy *policy)

    get the current LongRun policy

    :param struct cpufreq_policy \*policy:
        struct cpufreq_policy where current policy is written into

.. _`longrun_get_policy.description`:

Description
-----------

Reads the current LongRun policy by access to MSR_TMTA_LONGRUN_FLAGS
and MSR_TMTA_LONGRUN_CTRL

.. _`longrun_set_policy`:

longrun_set_policy
==================

.. c:function:: int longrun_set_policy(struct cpufreq_policy *policy)

    sets a new CPUFreq policy

    :param struct cpufreq_policy \*policy:
        new policy

.. _`longrun_set_policy.description`:

Description
-----------

Sets a new CPUFreq policy on LongRun-capable processors. This function
has to be called with cpufreq_driver locked.

.. _`longrun_verify_policy`:

longrun_verify_policy
=====================

.. c:function:: int longrun_verify_policy(struct cpufreq_policy *policy)

    verifies a new CPUFreq policy

    :param struct cpufreq_policy \*policy:
        the policy to verify

.. _`longrun_verify_policy.description`:

Description
-----------

Validates a new CPUFreq policy. This function has to be called with
cpufreq_driver locked.

.. _`longrun_determine_freqs`:

longrun_determine_freqs
=======================

.. c:function:: int longrun_determine_freqs(unsigned int *low_freq, unsigned int *high_freq)

    determines the lowest and highest possible core frequency

    :param unsigned int \*low_freq:
        an int to put the lowest frequency into

    :param unsigned int \*high_freq:
        an int to put the highest frequency into

.. _`longrun_determine_freqs.description`:

Description
-----------

Determines the lowest and highest possible core frequencies on this CPU.
This is necessary to calculate the performance percentage according to

.. _`longrun_determine_freqs.tmta-rules`:

TMTA rules
----------

performance_pctg = (target_freq - low_freq)/(high_freq - low_freq)

.. _`longrun_init`:

longrun_init
============

.. c:function:: int longrun_init( void)

    initializes the Transmeta Crusoe LongRun CPUFreq driver

    :param  void:
        no arguments

.. _`longrun_init.description`:

Description
-----------

Initializes the LongRun support.

.. _`longrun_exit`:

longrun_exit
============

.. c:function:: void __exit longrun_exit( void)

    unregisters LongRun support

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


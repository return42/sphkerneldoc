.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/powernow-k6.c

.. _`powernow_k6_get_cpu_multiplier`:

powernow_k6_get_cpu_multiplier
==============================

.. c:function:: int powernow_k6_get_cpu_multiplier( void)

    returns the current FSB multiplier

    :param void:
        no arguments
    :type void: 

.. _`powernow_k6_get_cpu_multiplier.description`:

Description
-----------

Returns the current setting of the frequency multiplier. Core clock
speed is frequency of the Front-Side Bus multiplied with this value.

.. _`powernow_k6_target`:

powernow_k6_target
==================

.. c:function:: int powernow_k6_target(struct cpufreq_policy *policy, unsigned int best_i)

    set the PowerNow! multiplier

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param best_i:
        clock_ratio[best_i] is the target multiplier
    :type best_i: unsigned int

.. _`powernow_k6_target.description`:

Description
-----------

Tries to change the PowerNow! multiplier

.. _`powernow_k6_init`:

powernow_k6_init
================

.. c:function:: int powernow_k6_init( void)

    initializes the k6 PowerNow! CPUFreq driver

    :param void:
        no arguments
    :type void: 

.. _`powernow_k6_init.description`:

Description
-----------

Initializes the K6 PowerNow! support. Returns -ENODEV on unsupported
devices, -EINVAL or -ENOMEM on problems during initiatization, and zero
on success.

.. _`powernow_k6_exit`:

powernow_k6_exit
================

.. c:function:: void __exit powernow_k6_exit( void)

    unregisters AMD K6-2+/3+ PowerNow! support

    :param void:
        no arguments
    :type void: 

.. _`powernow_k6_exit.description`:

Description
-----------

Unregisters AMD K6-2+ / K6-3+ PowerNow! support.

.. This file was automatic generated / don't edit.


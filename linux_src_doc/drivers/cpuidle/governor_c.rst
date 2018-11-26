.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/governor.c

.. _`__cpuidle_find_governor`:

\__cpuidle_find_governor
========================

.. c:function:: struct cpuidle_governor *__cpuidle_find_governor(const char *str)

    finds a governor of the specified name

    :param str:
        the name
    :type str: const char \*

.. _`__cpuidle_find_governor.description`:

Description
-----------

Must be called with cpuidle_lock acquired.

.. _`cpuidle_switch_governor`:

cpuidle_switch_governor
=======================

.. c:function:: int cpuidle_switch_governor(struct cpuidle_governor *gov)

    changes the governor

    :param gov:
        the new target governor
        Must be called with cpuidle_lock acquired.
    :type gov: struct cpuidle_governor \*

.. _`cpuidle_register_governor`:

cpuidle_register_governor
=========================

.. c:function:: int cpuidle_register_governor(struct cpuidle_governor *gov)

    registers a governor

    :param gov:
        the governor
    :type gov: struct cpuidle_governor \*

.. _`cpuidle_governor_latency_req`:

cpuidle_governor_latency_req
============================

.. c:function:: int cpuidle_governor_latency_req(unsigned int cpu)

    Compute a latency constraint for CPU

    :param cpu:
        Target CPU
    :type cpu: unsigned int

.. This file was automatic generated / don't edit.


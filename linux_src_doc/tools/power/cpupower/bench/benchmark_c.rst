.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/power/cpupower/bench/benchmark.c

.. _`calculate_timespace`:

calculate_timespace
===================

.. c:function:: unsigned int calculate_timespace(long load, struct config *config)

    to get the given load time

    :param load:
        *undescribed*
    :type load: long

    :param config:
        *undescribed*
    :type config: struct config \*

.. _`calculate_timespace.description`:

Description
-----------

\ ``param``\  load aimed load time in µs

\ ``retval``\  rounds of calculation

.. _`start_benchmark`:

start_benchmark
===============

.. c:function:: void start_benchmark(struct config *config)

    generates a specific sleep an load time with the performance governor and compares the used time for same calculations done with the configured powersave governor

    :param config:
        *undescribed*
    :type config: struct config \*

.. _`start_benchmark.description`:

Description
-----------

\ ``param``\  config config values for the benchmark

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/power/cpupower/bench/system.c

.. _`get_time`:

get_time
========

.. c:function:: long long int get_time( void)

    :param void:
        no arguments
    :type void: 

.. _`get_time.description`:

Description
-----------

\ ``retval``\  time

.. _`set_cpufreq_governor`:

set_cpufreq_governor
====================

.. c:function:: int set_cpufreq_governor(char *governor, unsigned int cpu)

    :param governor:
        *undescribed*
    :type governor: char \*

    :param cpu:
        *undescribed*
    :type cpu: unsigned int

.. _`set_cpufreq_governor.description`:

Description
-----------

\ ``param``\  governor cpufreq governor name
\ ``param``\  cpu cpu for which the governor should be set

\ ``retval``\  0 on success
\ ``retval``\  -1 when failed

.. _`set_cpu_affinity`:

set_cpu_affinity
================

.. c:function:: int set_cpu_affinity(unsigned int cpu)

    :param cpu:
        *undescribed*
    :type cpu: unsigned int

.. _`set_cpu_affinity.description`:

Description
-----------

\ ``param``\  cpu cpu# to which the affinity should be set

\ ``retval``\  0 on success
\ ``retval``\  -1 when setting the affinity failed

.. _`set_process_priority`:

set_process_priority
====================

.. c:function:: int set_process_priority(int priority)

    :param priority:
        *undescribed*
    :type priority: int

.. _`set_process_priority.description`:

Description
-----------

\ ``param``\  priority priority value

\ ``retval``\  0 on success
\ ``retval``\  -1 when setting the priority failed

.. _`prepare_user`:

prepare_user
============

.. c:function:: void prepare_user(const struct config *config)

    :param config:
        *undescribed*
    :type config: const struct config \*

.. _`prepare_user.description`:

Description
-----------

\ ``param``\  config benchmark config values

.. _`prepare_system`:

prepare_system
==============

.. c:function:: void prepare_system(const struct config *config)

    :param config:
        *undescribed*
    :type config: const struct config \*

.. _`prepare_system.description`:

Description
-----------

\ ``param``\  config benchmark config values

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-exynos/platsmp.c

.. _`exynos_cpu_power_down`:

exynos_cpu_power_down
=====================

.. c:function:: void exynos_cpu_power_down(int cpu)

    power down the specified cpu

    :param cpu:
        the cpu to power down
    :type cpu: int

.. _`exynos_cpu_power_down.description`:

Description
-----------

Power down the specified cpu. The sequence must be finished by a
call to \ :c:func:`cpu_do_idle`\ 

.. _`exynos_cpu_power_up`:

exynos_cpu_power_up
===================

.. c:function:: void exynos_cpu_power_up(int cpu)

    power up the specified cpu

    :param cpu:
        the cpu to power up
    :type cpu: int

.. _`exynos_cpu_power_up.description`:

Description
-----------

Power up the specified cpu

.. _`exynos_cpu_power_state`:

exynos_cpu_power_state
======================

.. c:function:: int exynos_cpu_power_state(int cpu)

    returns the power state of the cpu

    :param cpu:
        the cpu to retrieve the power state from
    :type cpu: int

.. _`exynos_cluster_power_down`:

exynos_cluster_power_down
=========================

.. c:function:: void exynos_cluster_power_down(int cluster)

    power down the specified cluster

    :param cluster:
        the cluster to power down
    :type cluster: int

.. _`exynos_cluster_power_up`:

exynos_cluster_power_up
=======================

.. c:function:: void exynos_cluster_power_up(int cluster)

    power up the specified cluster

    :param cluster:
        the cluster to power up
    :type cluster: int

.. _`exynos_cluster_power_state`:

exynos_cluster_power_state
==========================

.. c:function:: int exynos_cluster_power_state(int cluster)

    returns the power state of the cluster

    :param cluster:
        the cluster to retrieve the power state from
    :type cluster: int

.. _`exynos_scu_enable`:

exynos_scu_enable
=================

.. c:function:: void exynos_scu_enable( void)

    enables SCU for Cortex-A9 based system

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


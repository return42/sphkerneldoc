.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-exynos/platsmp.c

.. _`exynos_cpu_power_down`:

exynos_cpu_power_down
=====================

.. c:function:: void exynos_cpu_power_down(int cpu)

    power down the specified cpu

    :param int cpu:
        the cpu to power down

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

    :param int cpu:
        the cpu to power up

.. _`exynos_cpu_power_up.description`:

Description
-----------

Power up the specified cpu

.. _`exynos_cpu_power_state`:

exynos_cpu_power_state
======================

.. c:function:: int exynos_cpu_power_state(int cpu)

    returns the power state of the cpu

    :param int cpu:
        the cpu to retrieve the power state from

.. _`exynos_cluster_power_down`:

exynos_cluster_power_down
=========================

.. c:function:: void exynos_cluster_power_down(int cluster)

    power down the specified cluster

    :param int cluster:
        the cluster to power down

.. _`exynos_cluster_power_up`:

exynos_cluster_power_up
=======================

.. c:function:: void exynos_cluster_power_up(int cluster)

    power up the specified cluster

    :param int cluster:
        the cluster to power up

.. _`exynos_cluster_power_state`:

exynos_cluster_power_state
==========================

.. c:function:: int exynos_cluster_power_state(int cluster)

    returns the power state of the cluster

    :param int cluster:
        the cluster to retrieve the power state from

.. _`exynos_scu_enable`:

exynos_scu_enable
=================

.. c:function:: void exynos_scu_enable( void)

    enables SCU for Cortex-A9 based system

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


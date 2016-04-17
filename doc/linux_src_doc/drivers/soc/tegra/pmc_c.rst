.. -*- coding: utf-8; mode: rst -*-

=====
pmc.c
=====


.. _`tegra_pmc`:

struct tegra_pmc
================

.. c:type:: tegra_pmc

    NVIDIA Tegra PMC


.. _`tegra_pmc.definition`:

Definition
----------

.. code-block:: c

  struct tegra_pmc {
    void __iomem * base;
    struct clk * clk;
    unsigned long rate;
    enum tegra_suspend_mode suspend_mode;
    u32 cpu_good_time;
    u32 cpu_off_time;
    u32 core_osc_time;
    u32 core_pmu_time;
    u32 core_off_time;
    bool corereq_high;
    bool sysclkreq_high;
    bool combined_req;
    bool cpu_pwr_good_en;
    u32 lp0_vec_phys;
    u32 lp0_vec_size;
    struct mutex powergates_lock;
  };


.. _`tegra_pmc.members`:

Members
-------

:``base``:
    pointer to I/O remapped register region

:``clk``:
    pointer to pclk clock

:``rate``:
    currently configured rate of pclk

:``suspend_mode``:
    lowest suspend mode available

:``cpu_good_time``:
    CPU power good time (in microseconds)

:``cpu_off_time``:
    CPU power off time (in microsecends)

:``core_osc_time``:
    core power good OSC time (in microseconds)

:``core_pmu_time``:
    core power good PMU time (in microseconds)

:``core_off_time``:
    core power off time (in microseconds)

:``corereq_high``:
    core power request is active-high

:``sysclkreq_high``:
    system clock request is active-high

:``combined_req``:
    combined power request for CPU & core

:``cpu_pwr_good_en``:
    CPU power good signal is enabled

:``lp0_vec_phys``:
    physical base address of the LP0 warm boot code

:``lp0_vec_size``:
    size of the LP0 warm boot code

:``powergates_lock``:
    mutex for power gate register access




.. _`tegra_powergate_set`:

tegra_powergate_set
===================

.. c:function:: int tegra_powergate_set (int id, bool new_state)

    set the state of a partition

    :param int id:
        partition ID

    :param bool new_state:
        new state of the partition



.. _`tegra_powergate_power_on`:

tegra_powergate_power_on
========================

.. c:function:: int tegra_powergate_power_on (int id)

    power on partition

    :param int id:
        partition ID



.. _`tegra_powergate_power_off`:

tegra_powergate_power_off
=========================

.. c:function:: int tegra_powergate_power_off (int id)

    power off partition

    :param int id:
        partition ID



.. _`tegra_powergate_is_powered`:

tegra_powergate_is_powered
==========================

.. c:function:: int tegra_powergate_is_powered (int id)

    check if partition is powered

    :param int id:
        partition ID



.. _`tegra_powergate_remove_clamping`:

tegra_powergate_remove_clamping
===============================

.. c:function:: int tegra_powergate_remove_clamping (int id)

    remove power clamps for partition

    :param int id:
        partition ID



.. _`tegra_powergate_sequence_power_up`:

tegra_powergate_sequence_power_up
=================================

.. c:function:: int tegra_powergate_sequence_power_up (int id, struct clk *clk, struct reset_control *rst)

    power up partition

    :param int id:
        partition ID

    :param struct clk \*clk:
        clock for partition

    :param struct reset_control \*rst:
        reset for partition



.. _`tegra_powergate_sequence_power_up.description`:

Description
-----------

Must be called with clk disabled, and returns with clk enabled.



.. _`tegra_get_cpu_powergate_id`:

tegra_get_cpu_powergate_id
==========================

.. c:function:: int tegra_get_cpu_powergate_id (int cpuid)

    convert from CPU ID to partition ID

    :param int cpuid:
        CPU partition ID



.. _`tegra_get_cpu_powergate_id.description`:

Description
-----------

Returns the partition ID corresponding to the CPU partition ID or a
negative error code on failure.



.. _`tegra_pmc_cpu_is_powered`:

tegra_pmc_cpu_is_powered
========================

.. c:function:: bool tegra_pmc_cpu_is_powered (int cpuid)

    check if CPU partition is powered

    :param int cpuid:
        CPU partition ID



.. _`tegra_pmc_cpu_power_on`:

tegra_pmc_cpu_power_on
======================

.. c:function:: int tegra_pmc_cpu_power_on (int cpuid)

    power on CPU partition

    :param int cpuid:
        CPU partition ID



.. _`tegra_pmc_cpu_remove_clamping`:

tegra_pmc_cpu_remove_clamping
=============================

.. c:function:: int tegra_pmc_cpu_remove_clamping (int cpuid)

    remove power clamps for CPU partition

    :param int cpuid:
        CPU partition ID


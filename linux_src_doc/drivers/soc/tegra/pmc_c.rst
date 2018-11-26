.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/tegra/pmc.c

.. _`tegra_pmc`:

struct tegra_pmc
================

.. c:type:: struct tegra_pmc

    NVIDIA Tegra PMC

.. _`tegra_pmc.definition`:

Definition
----------

.. code-block:: c

    struct tegra_pmc {
        struct device *dev;
        void __iomem *base;
        void __iomem *wake;
        void __iomem *aotag;
        void __iomem *scratch;
        struct clk *clk;
        struct dentry *debugfs;
        const struct tegra_pmc_soc *soc;
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
        DECLARE_BITMAP(powergates_available, TEGRA_POWERGATE_MAX);
        struct mutex powergates_lock;
        struct pinctrl_dev *pctl_dev;
    }

.. _`tegra_pmc.members`:

Members
-------

dev
    pointer to PMC device structure

base
    pointer to I/O remapped register region

wake
    *undescribed*

aotag
    *undescribed*

scratch
    *undescribed*

clk
    pointer to pclk clock

debugfs
    pointer to debugfs entry

soc
    pointer to SoC data structure

rate
    currently configured rate of pclk

suspend_mode
    lowest suspend mode available

cpu_good_time
    CPU power good time (in microseconds)

cpu_off_time
    CPU power off time (in microsecends)

core_osc_time
    core power good OSC time (in microseconds)

core_pmu_time
    core power good PMU time (in microseconds)

core_off_time
    core power off time (in microseconds)

corereq_high
    core power request is active-high

sysclkreq_high
    system clock request is active-high

combined_req
    combined power request for CPU & core

cpu_pwr_good_en
    CPU power good signal is enabled

lp0_vec_phys
    physical base address of the LP0 warm boot code

lp0_vec_size
    size of the LP0 warm boot code

powergates_available
    Bitmap of available power gates

powergates_lock
    mutex for power gate register access

pctl_dev
    *undescribed*

.. _`tegra_powergate_set`:

tegra_powergate_set
===================

.. c:function:: int tegra_powergate_set(unsigned int id, bool new_state)

    set the state of a partition

    :param id:
        partition ID
    :type id: unsigned int

    :param new_state:
        new state of the partition
    :type new_state: bool

.. _`tegra_powergate_power_on`:

tegra_powergate_power_on
========================

.. c:function:: int tegra_powergate_power_on(unsigned int id)

    power on partition

    :param id:
        partition ID
    :type id: unsigned int

.. _`tegra_powergate_power_off`:

tegra_powergate_power_off
=========================

.. c:function:: int tegra_powergate_power_off(unsigned int id)

    power off partition

    :param id:
        partition ID
    :type id: unsigned int

.. _`tegra_powergate_is_powered`:

tegra_powergate_is_powered
==========================

.. c:function:: int tegra_powergate_is_powered(unsigned int id)

    check if partition is powered

    :param id:
        partition ID
    :type id: unsigned int

.. _`tegra_powergate_remove_clamping`:

tegra_powergate_remove_clamping
===============================

.. c:function:: int tegra_powergate_remove_clamping(unsigned int id)

    remove power clamps for partition

    :param id:
        partition ID
    :type id: unsigned int

.. _`tegra_powergate_sequence_power_up`:

tegra_powergate_sequence_power_up
=================================

.. c:function:: int tegra_powergate_sequence_power_up(unsigned int id, struct clk *clk, struct reset_control *rst)

    power up partition

    :param id:
        partition ID
    :type id: unsigned int

    :param clk:
        clock for partition
    :type clk: struct clk \*

    :param rst:
        reset for partition
    :type rst: struct reset_control \*

.. _`tegra_powergate_sequence_power_up.description`:

Description
-----------

Must be called with clk disabled, and returns with clk enabled.

.. _`tegra_get_cpu_powergate_id`:

tegra_get_cpu_powergate_id
==========================

.. c:function:: int tegra_get_cpu_powergate_id(unsigned int cpuid)

    convert from CPU ID to partition ID

    :param cpuid:
        CPU partition ID
    :type cpuid: unsigned int

.. _`tegra_get_cpu_powergate_id.description`:

Description
-----------

Returns the partition ID corresponding to the CPU partition ID or a
negative error code on failure.

.. _`tegra_pmc_cpu_is_powered`:

tegra_pmc_cpu_is_powered
========================

.. c:function:: bool tegra_pmc_cpu_is_powered(unsigned int cpuid)

    check if CPU partition is powered

    :param cpuid:
        CPU partition ID
    :type cpuid: unsigned int

.. _`tegra_pmc_cpu_power_on`:

tegra_pmc_cpu_power_on
======================

.. c:function:: int tegra_pmc_cpu_power_on(unsigned int cpuid)

    power on CPU partition

    :param cpuid:
        CPU partition ID
    :type cpuid: unsigned int

.. _`tegra_pmc_cpu_remove_clamping`:

tegra_pmc_cpu_remove_clamping
=============================

.. c:function:: int tegra_pmc_cpu_remove_clamping(unsigned int cpuid)

    remove power clamps for CPU partition

    :param cpuid:
        CPU partition ID
    :type cpuid: unsigned int

.. _`tegra_io_pad_power_enable`:

tegra_io_pad_power_enable
=========================

.. c:function:: int tegra_io_pad_power_enable(enum tegra_io_pad id)

    enable power to I/O pad

    :param id:
        Tegra I/O pad ID for which to enable power
    :type id: enum tegra_io_pad

.. _`tegra_io_pad_power_enable.return`:

Return
------

0 on success or a negative error code on failure.

.. _`tegra_io_pad_power_disable`:

tegra_io_pad_power_disable
==========================

.. c:function:: int tegra_io_pad_power_disable(enum tegra_io_pad id)

    disable power to I/O pad

    :param id:
        Tegra I/O pad ID for which to disable power
    :type id: enum tegra_io_pad

.. _`tegra_io_pad_power_disable.return`:

Return
------

0 on success or a negative error code on failure.

.. _`tegra_io_rail_power_on`:

tegra_io_rail_power_on
======================

.. c:function:: int tegra_io_rail_power_on(unsigned int id)

    enable power to I/O rail

    :param id:
        Tegra I/O pad ID for which to enable power
    :type id: unsigned int

.. _`tegra_io_rail_power_on.see-also`:

See also
--------

\ :c:func:`tegra_io_pad_power_enable`\ 

.. _`tegra_io_rail_power_off`:

tegra_io_rail_power_off
=======================

.. c:function:: int tegra_io_rail_power_off(unsigned int id)

    disable power to I/O rail

    :param id:
        Tegra I/O pad ID for which to disable power
    :type id: unsigned int

.. _`tegra_io_rail_power_off.see-also`:

See also
--------

\ :c:func:`tegra_io_pad_power_disable`\ 

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/samsung/clk-cpu.h

.. _`exynos_cpuclk_cfg_data`:

struct exynos_cpuclk_cfg_data
=============================

.. c:type:: struct exynos_cpuclk_cfg_data

    config data to setup cpu clocks.

.. _`exynos_cpuclk_cfg_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos_cpuclk_cfg_data {
        unsigned long prate;
        unsigned long div0;
        unsigned long div1;
    }

.. _`exynos_cpuclk_cfg_data.members`:

Members
-------

prate
    frequency of the primary parent clock (in KHz).

div0
    value to be programmed in the div_cpu0 register.

div1
    value to be programmed in the div_cpu1 register.

.. _`exynos_cpuclk_cfg_data.description`:

Description
-----------

This structure holds the divider configuration data for dividers in the CPU
clock domain. The parent frequency at which these divider values are valid is
specified in \ ``prate``\ . The \ ``prate``\  is the frequency of the primary parent clock.
For CPU clock domains that do not have a DIV1 register, the \ ``div1``\  member
value is not used.

.. _`exynos_cpuclk`:

struct exynos_cpuclk
====================

.. c:type:: struct exynos_cpuclk

    information about clock supplied to a CPU core.

.. _`exynos_cpuclk.definition`:

Definition
----------

.. code-block:: c

    struct exynos_cpuclk {
        struct clk_hw hw;
        struct clk *alt_parent;
        void __iomem *ctrl_base;
        spinlock_t *lock;
        const struct exynos_cpuclk_cfg_data *cfg;
        const unsigned long num_cfgs;
        struct notifier_block clk_nb;
        unsigned long flags;
    #define CLK_CPU_HAS_DIV1 (1 << 0)
    #define CLK_CPU_NEEDS_DEBUG_ALT_DIV (1 << 1)
    }

.. _`exynos_cpuclk.members`:

Members
-------

hw
    handle between CCF and CPU clock.

alt_parent
    alternate parent clock to use when switching the speed
    of the primary parent clock.

ctrl_base
    base address of the clock controller.

lock
    cpu clock domain register access lock.

cfg
    cpu clock rate configuration data.

num_cfgs
    number of array elements in \ ``cfg``\  array.

clk_nb
    clock notifier registered for changes in clock speed of the
    primary parent clock.

flags
    configuration flags for the CPU clock.

.. _`exynos_cpuclk.description`:

Description
-----------

This structure holds information required for programming the CPU clock for
various clock speeds.

.. This file was automatic generated / don't edit.


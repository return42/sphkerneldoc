.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/clk-dfll.h

.. _`tegra_dfll_soc_data`:

struct tegra_dfll_soc_data
==========================

.. c:type:: struct tegra_dfll_soc_data

    SoC-specific hooks/integration for the DFLL driver

.. _`tegra_dfll_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct tegra_dfll_soc_data {
        struct device *dev;
        unsigned long max_freq;
        const struct cvb_table *cvb;
        void (*init_clock_trimmers)(void);
        void (*set_clock_trimmers_high)(void);
        void (*set_clock_trimmers_low)(void);
    }

.. _`tegra_dfll_soc_data.members`:

Members
-------

dev
    struct device \* that holds the OPP table for the DFLL

max_freq
    maximum frequency supported on this SoC

cvb
    CPU frequency table for this SoC

init_clock_trimmers
    callback to initialize clock trimmers

set_clock_trimmers_high
    callback to tune clock trimmers for high voltage

set_clock_trimmers_low
    callback to tune clock trimmers for low voltage

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/x86/clk-pmc-atom.h

.. _`pmc_clk`:

struct pmc_clk
==============

.. c:type:: struct pmc_clk

    PMC platform clock configuration

.. _`pmc_clk.definition`:

Definition
----------

.. code-block:: c

    struct pmc_clk {
        const char *name;
        unsigned long freq;
        const char *parent_name;
    }

.. _`pmc_clk.members`:

Members
-------

name
    identified, typically pmc_plt_clk_<x>, x=[0..5]

freq
    in Hz, 19.2MHz  and 25MHz (Baytrail only) supported

parent_name
    one of 'xtal' or 'osc'

.. _`pmc_clk_data`:

struct pmc_clk_data
===================

.. c:type:: struct pmc_clk_data

    common PMC clock configuration

.. _`pmc_clk_data.definition`:

Definition
----------

.. code-block:: c

    struct pmc_clk_data {
        void __iomem *base;
        const struct pmc_clk *clks;
    }

.. _`pmc_clk_data.members`:

Members
-------

base
    PMC clock register base offset

clks
    pointer to set of registered clocks, typically 0..5

.. This file was automatic generated / don't edit.


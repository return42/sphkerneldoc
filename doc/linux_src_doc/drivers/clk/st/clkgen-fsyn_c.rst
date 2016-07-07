.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/st/clkgen-fsyn.c

.. _`st_clk_quadfs_pll`:

struct st_clk_quadfs_pll
========================

.. c:type:: struct st_clk_quadfs_pll

    A pll which outputs a fixed multiplier of its parent clock, found inside a type of ST quad channel frequency synthesizer block

.. _`st_clk_quadfs_pll.definition`:

Definition
----------

.. code-block:: c

    struct st_clk_quadfs_pll {
        struct clk_hw hw;
        void __iomem *regs_base;
        spinlock_t *lock;
        struct clkgen_quadfs_data *data;
        u32 ndiv;
    }

.. _`st_clk_quadfs_pll.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces.

regs_base
    base address of the configuration registers.

lock
    spinlock.

data
    *undescribed*

ndiv
    regmap field for the ndiv control.

.. _`st_clk_quadfs_fsynth`:

struct st_clk_quadfs_fsynth
===========================

.. c:type:: struct st_clk_quadfs_fsynth

    One clock output from a four channel digital frequency synthesizer (fsynth) block.

.. _`st_clk_quadfs_fsynth.definition`:

Definition
----------

.. code-block:: c

    struct st_clk_quadfs_fsynth {
        struct clk_hw hw;
        void __iomem *regs_base;
        spinlock_t *lock;
        struct clkgen_quadfs_data *data;
        u32 chan;
        u32 md;
        u32 pe;
        u32 sdiv;
        u32 nsdiv;
    }

.. _`st_clk_quadfs_fsynth.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

regs_base
    *undescribed*

lock
    *undescribed*

data
    *undescribed*

chan
    *undescribed*

md
    *undescribed*

pe
    *undescribed*

sdiv
    *undescribed*

nsdiv
    regmap field in the output control register for
    for the optional divide by 3 of this fsynth channel. This control
    is active low so the divide by 3 is active when the control bit is
    cleared and the divide is bypassed when the bit is set.

.. This file was automatic generated / don't edit.


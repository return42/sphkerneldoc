.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/opp2xxx.h

.. _`prcm_config`:

struct prcm_config
==================

.. c:type:: struct prcm_config

    define clock rates on a per-OPP basis (24xx)

.. _`prcm_config.definition`:

Definition
----------

.. code-block:: c

    struct prcm_config {
        unsigned long xtal_speed;
        unsigned long dpll_speed;
        unsigned long mpu_speed;
        unsigned long cm_clksel_mpu;
        unsigned long cm_clksel_dsp;
        unsigned long cm_clksel_gfx;
        unsigned long cm_clksel1_core;
        unsigned long cm_clksel1_pll;
        unsigned long cm_clksel2_pll;
        unsigned long cm_clksel_mdm;
        unsigned long base_sdrc_rfr;
        unsigned short flags;
    }

.. _`prcm_config.members`:

Members
-------

xtal_speed
    *undescribed*

dpll_speed
    *undescribed*

mpu_speed
    *undescribed*

cm_clksel_mpu
    *undescribed*

cm_clksel_dsp
    *undescribed*

cm_clksel_gfx
    *undescribed*

cm_clksel1_core
    *undescribed*

cm_clksel1_pll
    *undescribed*

cm_clksel2_pll
    *undescribed*

cm_clksel_mdm
    *undescribed*

base_sdrc_rfr
    *undescribed*

flags
    *undescribed*

.. _`prcm_config.description`:

Description
-----------

Key dividers which make up a PRCM set. Ratio's for a PRCM are mandated.
xtal_speed, dpll_speed, mpu_speed, CM_CLKSEL_MPU,CM_CLKSEL_DSP
CM_CLKSEL_GFX, CM_CLKSEL1_CORE, CM_CLKSEL1_PLL CM_CLKSEL2_PLL, CM_CLKSEL_MDM

This is deprecated.  As soon as we have a decent OPP API, we should
move all this stuff to it.

.. This file was automatic generated / don't edit.


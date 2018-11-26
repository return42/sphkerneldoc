.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clkt2xxx_virt_prcm_set.c

.. _`omap2_table_mpu_recalc`:

omap2_table_mpu_recalc
======================

.. c:function:: unsigned long omap2_table_mpu_recalc(struct clk_hw *clk, unsigned long parent_rate)

    just return the MPU speed

    :param clk:
        virt_prcm_set struct clk
    :type clk: struct clk_hw \*

    :param parent_rate:
        *undescribed*
    :type parent_rate: unsigned long

.. _`omap2_table_mpu_recalc.description`:

Description
-----------

Set virt_prcm_set's rate to the mpu_speed field of the current PRCM set.

.. _`omap2xxx_clkt_vps_check_bootloader_rates`:

omap2xxx_clkt_vps_check_bootloader_rates
========================================

.. c:function:: void omap2xxx_clkt_vps_check_bootloader_rates( void)

    determine which of the rate table sets matches the current CORE DPLL hardware rate

    :param void:
        no arguments
    :type void: 

.. _`omap2xxx_clkt_vps_check_bootloader_rates.description`:

Description
-----------

Check the MPU rate set by bootloader.  Sets the 'curr_prcm_set'
global to point to the active rate set when found; otherwise, sets
it to NULL.  No return value;

.. _`omap2xxx_clkt_vps_late_init`:

omap2xxx_clkt_vps_late_init
===========================

.. c:function:: void omap2xxx_clkt_vps_late_init( void)

    store a copy of the sys_ck rate

    :param void:
        no arguments
    :type void: 

.. _`omap2xxx_clkt_vps_late_init.description`:

Description
-----------

Store a copy of the sys_ck rate for later use by the OMAP2xxx DVFS
code.  (The sys_ck rate does not -- or rather, must not -- change
during kernel runtime.)  Must be called after we have a valid
sys_ck rate, but before the virt_prcm_set clock rate is
recalculated.  No return value.

.. _`omap2xxx_clkt_vps_init`:

omap2xxx_clkt_vps_init
======================

.. c:function:: void omap2xxx_clkt_vps_init( void)

    initialize virt_prcm_set clock

    :param void:
        no arguments
    :type void: 

.. _`omap2xxx_clkt_vps_init.description`:

Description
-----------

Does a manual init for the virtual prcm DVFS clock for OMAP2. This
function is called only from omap2 DT clock init, as the virtual
node is not modelled in the DT clock data.

.. This file was automatic generated / don't edit.


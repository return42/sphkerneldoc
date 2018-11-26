.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clock.c

.. _`omap2_clk_setup_ll_ops`:

omap2_clk_setup_ll_ops
======================

.. c:function:: int omap2_clk_setup_ll_ops( void)

    setup clock driver low-level ops

    :param void:
        no arguments
    :type void: 

.. _`omap2_clk_setup_ll_ops.description`:

Description
-----------

Sets up clock driver low-level platform ops. These are needed
for register accesses and various other misc platform operations.
Returns 0 on success, -EBUSY if low level ops have been registered
already.

.. _`ti_clk_init_features`:

ti_clk_init_features
====================

.. c:function:: void ti_clk_init_features( void)

    init clock features struct for the SoC

    :param void:
        no arguments
    :type void: 

.. _`ti_clk_init_features.description`:

Description
-----------

Initializes the clock features struct based on the SoC type.

.. This file was automatic generated / don't edit.


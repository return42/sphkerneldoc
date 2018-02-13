.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/autoidle.c

.. _`omap2_clk_deny_idle`:

omap2_clk_deny_idle
===================

.. c:function:: int omap2_clk_deny_idle(struct clk *clk)

    disable autoidle on an OMAP clock

    :param struct clk \*clk:
        struct clk \* to disable autoidle for

.. _`omap2_clk_deny_idle.description`:

Description
-----------

Disable autoidle on an OMAP clock.

.. _`omap2_clk_allow_idle`:

omap2_clk_allow_idle
====================

.. c:function:: int omap2_clk_allow_idle(struct clk *clk)

    enable autoidle on an OMAP clock

    :param struct clk \*clk:
        struct clk \* to enable autoidle for

.. _`omap2_clk_allow_idle.description`:

Description
-----------

Enable autoidle on an OMAP clock.

.. _`_clk_generic_allow_autoidle_all`:

\_clk_generic_allow_autoidle_all
================================

.. c:function:: void _clk_generic_allow_autoidle_all( void)

    enable autoidle for all clocks

    :param  void:
        no arguments

.. _`_clk_generic_allow_autoidle_all.description`:

Description
-----------

Enables hardware autoidle for all registered DT clocks, which have
the feature.

.. _`_clk_generic_deny_autoidle_all`:

\_clk_generic_deny_autoidle_all
===============================

.. c:function:: void _clk_generic_deny_autoidle_all( void)

    disable autoidle for all clocks

    :param  void:
        no arguments

.. _`_clk_generic_deny_autoidle_all.description`:

Description
-----------

Disables hardware autoidle for all registered DT clocks, which have
the feature.

.. _`of_ti_clk_autoidle_setup`:

of_ti_clk_autoidle_setup
========================

.. c:function:: int of_ti_clk_autoidle_setup(struct device_node *node)

    sets up hardware autoidle for a clock

    :param struct device_node \*node:
        pointer to the clock device node

.. _`of_ti_clk_autoidle_setup.description`:

Description
-----------

Checks if a clock has hardware autoidle support or not (check
for presence of 'ti,autoidle-shift' property in the device tree
node) and sets up the hardware autoidle feature for the clock
if available. If autoidle is available, the clock is also added
to the autoidle list for later processing. Returns 0 on success,
negative error value on failure.

.. _`omap2_init_clk_hw_omap_clocks`:

omap2_init_clk_hw_omap_clocks
=============================

.. c:function:: void omap2_init_clk_hw_omap_clocks(struct clk_hw *hw)

    initialize an OMAP clock

    :param struct clk_hw \*hw:
        struct clk_hw \* to initialize

.. _`omap2_init_clk_hw_omap_clocks.description`:

Description
-----------

Add an OMAP clock \ ``clk``\  to the internal list of OMAP clocks.  Used
temporarily for autoidle handling, until this support can be
integrated into the common clock framework code in some way.  No
return value.

.. _`omap2_clk_enable_autoidle_all`:

omap2_clk_enable_autoidle_all
=============================

.. c:function:: int omap2_clk_enable_autoidle_all( void)

    enable autoidle on all OMAP clocks that support it

    :param  void:
        no arguments

.. _`omap2_clk_enable_autoidle_all.description`:

Description
-----------

Enable clock autoidle on all OMAP clocks that have allow_idle
function pointers associated with them.  This function is intended
to be temporary until support for this is added to the common clock
code.  Returns 0.

.. _`omap2_clk_disable_autoidle_all`:

omap2_clk_disable_autoidle_all
==============================

.. c:function:: int omap2_clk_disable_autoidle_all( void)

    disable autoidle on all OMAP clocks that support it

    :param  void:
        no arguments

.. _`omap2_clk_disable_autoidle_all.description`:

Description
-----------

Disable clock autoidle on all OMAP clocks that have allow_idle
function pointers associated with them.  This function is intended
to be temporary until support for this is added to the common clock
code.  Returns 0.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clkt_dflt.c

.. _`_wait_idlest_generic`:

\_wait_idlest_generic
=====================

.. c:function:: int _wait_idlest_generic(struct clk_hw_omap *clk, struct clk_omap_reg *reg, u32 mask, u8 idlest, const char *name)

    wait for a module to leave the idle state

    :param clk:
        module clock to wait for (needed for register offsets)
    :type clk: struct clk_hw_omap \*

    :param reg:
        virtual address of module IDLEST register
    :type reg: struct clk_omap_reg \*

    :param mask:
        value to mask against to determine if the module is active
    :type mask: u32

    :param idlest:
        idle state indicator (0 or 1) for the clock
    :type idlest: u8

    :param name:
        name of the clock (for printk)
    :type name: const char \*

.. _`_wait_idlest_generic.description`:

Description
-----------

Wait for a module to leave idle, where its idle-status register is
not inside the CM module.  Returns 1 if the module left idle
promptly, or 0 if the module did not leave idle before the timeout
elapsed.  XXX Deprecated - should be moved into drivers for the
individual IP block that the IDLEST register exists in.

.. _`_omap2_module_wait_ready`:

\_omap2_module_wait_ready
=========================

.. c:function:: void _omap2_module_wait_ready(struct clk_hw_omap *clk)

    wait for an OMAP module to leave IDLE

    :param clk:
        struct clk \* belonging to the module
    :type clk: struct clk_hw_omap \*

.. _`_omap2_module_wait_ready.description`:

Description
-----------

If the necessary clocks for the OMAP hardware IP block that
corresponds to clock \ ``clk``\  are enabled, then wait for the module to
indicate readiness (i.e., to leave IDLE).  This code does not
belong in the clock code and will be moved in the medium term to
module-dependent code.  No return value.

.. _`omap2_clk_dflt_find_companion`:

omap2_clk_dflt_find_companion
=============================

.. c:function:: void omap2_clk_dflt_find_companion(struct clk_hw_omap *clk, struct clk_omap_reg *other_reg, u8 *other_bit)

    find companion clock to \ ``clk``\ 

    :param clk:
        struct clk \* to find the companion clock of
    :type clk: struct clk_hw_omap \*

    :param other_reg:
        void \__iomem \*\* to return the companion clock CM\_\*CLKEN va in
    :type other_reg: struct clk_omap_reg \*

    :param other_bit:
        u8 \*\* to return the companion clock bit shift in
    :type other_bit: u8 \*

.. _`omap2_clk_dflt_find_companion.note`:

Note
----

We don't need special code here for INVERT_ENABLE for the
time being since INVERT_ENABLE only applies to clocks enabled by
CM_CLKEN_PLL

Convert CM_ICLKEN\* <-> CM_FCLKEN\*.  This conversion assumes it's
just a matter of XORing the bits.

Some clocks don't have companion clocks.  For example, modules with
only an interface clock (such as MAILBOXES) don't have a companion
clock.  Right now, this code relies on the hardware exporting a bit
in the correct companion register that indicates that the
nonexistent 'companion clock' is active.  Future patches will
associate this type of code with per-module data structures to
avoid this issue, and remove the casts.  No return value.

.. _`omap2_clk_dflt_find_idlest`:

omap2_clk_dflt_find_idlest
==========================

.. c:function:: void omap2_clk_dflt_find_idlest(struct clk_hw_omap *clk, struct clk_omap_reg *idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    find CM_IDLEST reg va, bit shift for \ ``clk``\ 

    :param clk:
        struct clk \* to find IDLEST info for
    :type clk: struct clk_hw_omap \*

    :param idlest_reg:
        void \__iomem \*\* to return the CM_IDLEST va in
    :type idlest_reg: struct clk_omap_reg \*

    :param idlest_bit:
        u8 \* to return the CM_IDLEST bit shift in
    :type idlest_bit: u8 \*

    :param idlest_val:
        u8 \* to return the idle status indicator
    :type idlest_val: u8 \*

.. _`omap2_clk_dflt_find_idlest.description`:

Description
-----------

Return the CM_IDLEST register address and bit shift corresponding
to the module that "owns" this clock.  This default code assumes
that the CM_IDLEST bit shift is the CM\_\*CLKEN bit shift, and that
the IDLEST register address ID corresponds to the CM\_\*CLKEN
register address ID (e.g., that CM_FCLKEN2 corresponds to
CM_IDLEST2).  This is not true for all modules.  No return value.

.. _`omap2_dflt_clk_enable`:

omap2_dflt_clk_enable
=====================

.. c:function:: int omap2_dflt_clk_enable(struct clk_hw *hw)

    enable a clock in the hardware

    :param hw:
        struct clk_hw \* of the clock to enable
    :type hw: struct clk_hw \*

.. _`omap2_dflt_clk_enable.description`:

Description
-----------

Enable the clock \ ``hw``\  in the hardware.  We first call into the OMAP
clockdomain code to "enable" the corresponding clockdomain if this
is the first enabled user of the clockdomain.  Then program the
hardware to enable the clock.  Then wait for the IP block that uses
this clock to leave idle (if applicable).  Returns the error value
from \ :c:func:`clkdm_clk_enable`\  if it terminated with an error, or -EINVAL
if \ ``hw``\  has a null clock enable_reg, or zero upon success.

.. _`omap2_dflt_clk_disable`:

omap2_dflt_clk_disable
======================

.. c:function:: void omap2_dflt_clk_disable(struct clk_hw *hw)

    disable a clock in the hardware

    :param hw:
        struct clk_hw \* of the clock to disable
    :type hw: struct clk_hw \*

.. _`omap2_dflt_clk_disable.description`:

Description
-----------

Disable the clock \ ``hw``\  in the hardware, and call into the OMAP
clockdomain code to "disable" the corresponding clockdomain if all
clocks/hwmods in that clockdomain are now disabled.  No return
value.

.. _`omap2_dflt_clk_is_enabled`:

omap2_dflt_clk_is_enabled
=========================

.. c:function:: int omap2_dflt_clk_is_enabled(struct clk_hw *hw)

    is clock enabled in the hardware?

    :param hw:
        struct clk_hw \* to check
    :type hw: struct clk_hw \*

.. _`omap2_dflt_clk_is_enabled.description`:

Description
-----------

Return 1 if the clock represented by \ ``hw``\  is enabled in the
hardware, or 0 otherwise.  Intended for use in the struct
clk_ops.is_enabled function pointer.

.. This file was automatic generated / don't edit.


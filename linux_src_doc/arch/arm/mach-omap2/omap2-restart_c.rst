.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap2-restart.c

.. _`omap2xxx_restart`:

omap2xxx_restart
================

.. c:function:: void omap2xxx_restart(enum reboot_mode mode, const char *cmd)

    Set DPLL to bypass mode for reboot to work

    :param enum reboot_mode mode:
        *undescribed*

    :param const char \*cmd:
        *undescribed*

.. _`omap2xxx_restart.description`:

Description
-----------

Set the DPLL to bypass so that reboot completes successfully.  No
return value.

.. _`omap2xxx_common_look_up_clks_for_reset`:

omap2xxx_common_look_up_clks_for_reset
======================================

.. c:function:: int omap2xxx_common_look_up_clks_for_reset( void)

    look up clocks needed for restart

    :param  void:
        no arguments

.. _`omap2xxx_common_look_up_clks_for_reset.description`:

Description
-----------

Some clocks need to be looked up in advance for the SoC restart
operation to work - see \ :c:func:`omap2xxx_restart`\ .  Returns -EINVAL upon
error or 0 upon success.

.. This file was automatic generated / don't edit.


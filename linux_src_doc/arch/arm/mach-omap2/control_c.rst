.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/control.c

.. _`omap3_ctrl_write_boot_mode`:

omap3_ctrl_write_boot_mode
==========================

.. c:function:: void omap3_ctrl_write_boot_mode(u8 bootmode)

    set scratchpad boot mode for the next boot

    :param bootmode:
        8-bit value to pass to some boot code
    :type bootmode: u8

.. _`omap3_ctrl_write_boot_mode.description`:

Description
-----------

Set the bootmode in the scratchpad RAM.  This is used after the
system restarts.  Not sure what actually uses this - it may be the
bootloader, rather than the boot ROM - contrary to the preserved
comment below.  No return value.

.. _`omap_ctrl_write_dsp_boot_addr`:

omap_ctrl_write_dsp_boot_addr
=============================

.. c:function:: void omap_ctrl_write_dsp_boot_addr(u32 bootaddr)

    set boot address for a remote processor

    :param bootaddr:
        physical address of the boot loader
    :type bootaddr: u32

.. _`omap_ctrl_write_dsp_boot_addr.description`:

Description
-----------

Set boot address for the boot loader of a supported processor
when a power ON sequence occurs.

.. _`omap_ctrl_write_dsp_boot_mode`:

omap_ctrl_write_dsp_boot_mode
=============================

.. c:function:: void omap_ctrl_write_dsp_boot_mode(u8 bootmode)

    set boot mode for a remote processor

    :param bootmode:
        8-bit value to pass to some boot code
    :type bootmode: u8

.. _`omap_ctrl_write_dsp_boot_mode.description`:

Description
-----------

Sets boot mode for the boot loader of a supported processor
when a power ON sequence occurs.

.. _`omap3_ctrl_save_padconf`:

omap3_ctrl_save_padconf
=======================

.. c:function:: int omap3_ctrl_save_padconf( void)

    save padconf registers to scratchpad RAM

    :param void:
        no arguments
    :type void: 

.. _`omap3_ctrl_save_padconf.description`:

Description
-----------

Tell the SCM to start saving the padconf registers, then wait for
the process to complete.  Returns 0 unconditionally, although it
should also eventually be able to return -ETIMEDOUT, if the save
does not complete.

XXX This function is missing a timeout.  What should it be?

.. _`omap3_ctrl_set_iva_bootmode_idle`:

omap3_ctrl_set_iva_bootmode_idle
================================

.. c:function:: void omap3_ctrl_set_iva_bootmode_idle( void)

    sets the IVA2 bootmode to idle

    :param void:
        no arguments
    :type void: 

.. _`omap3_ctrl_set_iva_bootmode_idle.description`:

Description
-----------

Sets the bootmode for IVA2 to idle. This is needed by the PM code to
force disable IVA2 so that it does not prevent any low-power states.

.. _`omap3_ctrl_setup_d2d_padconf`:

omap3_ctrl_setup_d2d_padconf
============================

.. c:function:: void omap3_ctrl_setup_d2d_padconf( void)

    setup stacked modem pads for idle

    :param void:
        no arguments
    :type void: 

.. _`omap3_ctrl_setup_d2d_padconf.description`:

Description
-----------

Sets up the pads controlling the stacked modem in such way that the
device can enter idle.

.. _`omap3_ctrl_init`:

omap3_ctrl_init
===============

.. c:function:: void omap3_ctrl_init( void)

    does static initializations for control module

    :param void:
        no arguments
    :type void: 

.. _`omap3_ctrl_init.description`:

Description
-----------

Initializes system control module. This sets up the sysconfig autoidle,
and sets up modem and iva2 so that they can be idled properly.

.. _`am43xx_control_save_context`:

am43xx_control_save_context
===========================

.. c:function:: void am43xx_control_save_context( void)

    Save the wakeup domain registers

    :param void:
        no arguments
    :type void: 

.. _`am43xx_control_save_context.description`:

Description
-----------

Save the wkup domain registers

.. _`am43xx_control_restore_context`:

am43xx_control_restore_context
==============================

.. c:function:: void am43xx_control_restore_context( void)

    Restore the wakeup domain registers

    :param void:
        no arguments
    :type void: 

.. _`am43xx_control_restore_context.description`:

Description
-----------

Restore the wkup domain registers

.. _`omap2_control_base_init`:

omap2_control_base_init
=======================

.. c:function:: int omap2_control_base_init( void)

    initialize iomappings for the control driver

    :param void:
        no arguments
    :type void: 

.. _`omap2_control_base_init.description`:

Description
-----------

Detects and initializes the iomappings for the control driver, based
on the DT data. Returns 0 in success, negative error value
otherwise.

.. _`omap_control_init`:

omap_control_init
=================

.. c:function:: int omap_control_init( void)

    low level init for the control driver

    :param void:
        no arguments
    :type void: 

.. _`omap_control_init.description`:

Description
-----------

Initializes the low level clock infrastructure for control driver.
Returns 0 in success, negative error value in failure.

.. _`omap3_control_legacy_iomap_init`:

omap3_control_legacy_iomap_init
===============================

.. c:function:: void omap3_control_legacy_iomap_init( void)

    legacy iomap init for clock providers

    :param void:
        no arguments
    :type void: 

.. _`omap3_control_legacy_iomap_init.description`:

Description
-----------

Legacy iomap init for clock provider. Needed only by legacy boot mode,
where the base addresses are not parsed from DT, but still required
by the clock driver to be setup properly.

.. This file was automatic generated / don't edit.


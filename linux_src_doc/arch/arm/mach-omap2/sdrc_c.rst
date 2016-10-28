.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/sdrc.c

.. _`omap2_sms_save_context`:

omap2_sms_save_context
======================

.. c:function:: void omap2_sms_save_context( void)

    Save SMS registers

    :param  void:
        no arguments

.. _`omap2_sms_save_context.description`:

Description
-----------

Save SMS registers that need to be restored after off mode.

.. _`omap2_sms_restore_context`:

omap2_sms_restore_context
=========================

.. c:function:: void omap2_sms_restore_context( void)

    Restore SMS registers

    :param  void:
        no arguments

.. _`omap2_sms_restore_context.description`:

Description
-----------

Restore SMS registers that need to be Restored after off mode.

.. _`omap2_sdrc_get_params`:

omap2_sdrc_get_params
=====================

.. c:function:: int omap2_sdrc_get_params(unsigned long r, struct omap_sdrc_params **sdrc_cs0, struct omap_sdrc_params **sdrc_cs1)

    return SDRC register values for a given clock rate

    :param unsigned long r:
        SDRC clock rate (in Hz)

    :param struct omap_sdrc_params \*\*sdrc_cs0:
        chip select 0 ram timings \*\*

    :param struct omap_sdrc_params \*\*sdrc_cs1:
        chip select 1 ram timings \*\*

.. _`omap2_sdrc_get_params.description`:

Description
-----------

Return pre-calculated values for the SDRC_ACTIM_CTRLA,
SDRC_ACTIM_CTRLB, SDRC_RFR_CTRL and SDRC_MR registers in sdrc_cs[01]
structs,for a given SDRC clock rate 'r'.
These parameters control various timing delays in the SDRAM controller
that are expressed in terms of the number of SDRC clock cycles to
wait; hence the clock rate dependency.

Supports 2 different timing parameters for both chip selects.

.. _`omap2_sdrc_get_params.note-1`:

Note 1
------

the sdrc_init_params_cs[01] must be sorted rate descending.

.. _`omap2_sdrc_get_params.note-2`:

Note 2
------

If sdrc_init_params_cs_1 is not NULL it must be of same size
as sdrc_init_params_cs_0.

Fills in the struct omap_sdrc_params \* for each chip select.
Returns 0 upon success or -1 upon failure.

.. _`omap2_sdrc_init`:

omap2_sdrc_init
===============

.. c:function:: void omap2_sdrc_init(struct omap_sdrc_params *sdrc_cs0, struct omap_sdrc_params *sdrc_cs1)

    initialize SMS, SDRC devices on boot

    :param struct omap_sdrc_params \*sdrc_cs0:
        *undescribed*

    :param struct omap_sdrc_params \*sdrc_cs1:
        *undescribed*

.. _`omap2_sdrc_init.description`:

Description
-----------

Turn on smart idle modes for SDRAM scheduler and controller.
Program a known-good configuration for the SDRC to deal with buggy
bootloaders.

.. This file was automatic generated / don't edit.


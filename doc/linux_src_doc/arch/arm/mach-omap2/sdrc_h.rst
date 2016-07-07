.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/sdrc.h

.. _`omap_sdrc_params`:

struct omap_sdrc_params
=======================

.. c:type:: struct omap_sdrc_params

    SDRC parameters for a given SDRC clock rate

.. _`omap_sdrc_params.definition`:

Definition
----------

.. code-block:: c

    struct omap_sdrc_params {
        unsigned long rate;
        u32 actim_ctrla;
        u32 actim_ctrlb;
        u32 rfr_ctrl;
        u32 mr;
    }

.. _`omap_sdrc_params.members`:

Members
-------

rate
    SDRC clock rate (in Hz)

actim_ctrla
    Value to program to SDRC_ACTIM_CTRLA for this rate

actim_ctrlb
    Value to program to SDRC_ACTIM_CTRLB for this rate

rfr_ctrl
    Value to program to SDRC_RFR_CTRL for this rate

mr
    Value to program to SDRC_MR for this rate

.. _`omap_sdrc_params.description`:

Description
-----------

This structure holds a pre-computed set of register values for the
SDRC for a given SDRC clock rate and SDRAM chip.  These are
intended to be pre-computed and specified in an array in the board-\*.c
files.  The structure is keyed off the 'rate' field.

.. This file was automatic generated / don't edit.


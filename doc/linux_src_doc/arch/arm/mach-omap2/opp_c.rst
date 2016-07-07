.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/opp.c

.. _`omap_init_opp_table`:

omap_init_opp_table
===================

.. c:function:: int omap_init_opp_table(struct omap_opp_def *opp_def, u32 opp_def_size)

    Initialize opp table as per the CPU type

    :param struct omap_opp_def \*opp_def:
        opp default list for this silicon

    :param u32 opp_def_size:
        number of opp entries for this silicon

.. _`omap_init_opp_table.description`:

Description
-----------

Register the initial OPP table with the OPP library based on the CPU
type. This is meant to be used only by SoC specific registration.

.. This file was automatic generated / don't edit.


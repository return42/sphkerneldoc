.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm2xxx_3xxx.c

.. _`omap2_prm_is_hardreset_asserted`:

omap2_prm_is_hardreset_asserted
===============================

.. c:function:: int omap2_prm_is_hardreset_asserted(u8 shift, u8 part, s16 prm_mod, u16 offset)

    read the HW reset line state of submodules contained in the hwmod module

    :param shift:
        register bit shift corresponding to the reset line to check
    :type shift: u8

    :param part:
        PRM partition, ignored for OMAP2
    :type part: u8

    :param prm_mod:
        PRM submodule base (e.g. CORE_MOD)
    :type prm_mod: s16

    :param offset:
        register offset, ignored for OMAP2
    :type offset: u16

.. _`omap2_prm_is_hardreset_asserted.description`:

Description
-----------

Returns 1 if the (sub)module hardreset line is currently asserted,
0 if the (sub)module hardreset line is not currently asserted, or
-EINVAL if called while running on a non-OMAP2/3 chip.

.. _`omap2_prm_assert_hardreset`:

omap2_prm_assert_hardreset
==========================

.. c:function:: int omap2_prm_assert_hardreset(u8 shift, u8 part, s16 prm_mod, u16 offset)

    assert the HW reset line of a submodule

    :param shift:
        register bit shift corresponding to the reset line to assert
    :type shift: u8

    :param part:
        PRM partition, ignored for OMAP2
    :type part: u8

    :param prm_mod:
        PRM submodule base (e.g. CORE_MOD)
    :type prm_mod: s16

    :param offset:
        register offset, ignored for OMAP2
    :type offset: u16

.. _`omap2_prm_assert_hardreset.description`:

Description
-----------

Some IPs like dsp or iva contain processors that require an HW
reset line to be asserted / deasserted in order to fully enable the
IP.  These modules may have multiple hard-reset lines that reset
different 'submodules' inside the IP block.  This function will
place the submodule into reset.  Returns 0 upon success or -EINVAL
upon an argument error.

.. _`omap2_prm_deassert_hardreset`:

omap2_prm_deassert_hardreset
============================

.. c:function:: int omap2_prm_deassert_hardreset(u8 rst_shift, u8 st_shift, u8 part, s16 prm_mod, u16 rst_offset, u16 st_offset)

    deassert a submodule hardreset line and wait

    :param rst_shift:
        register bit shift corresponding to the reset line to deassert
    :type rst_shift: u8

    :param st_shift:
        register bit shift for the status of the deasserted submodule
    :type st_shift: u8

    :param part:
        PRM partition, not used for OMAP2
    :type part: u8

    :param prm_mod:
        PRM submodule base (e.g. CORE_MOD)
    :type prm_mod: s16

    :param rst_offset:
        reset register offset, not used for OMAP2
    :type rst_offset: u16

    :param st_offset:
        reset status register offset, not used for OMAP2
    :type st_offset: u16

.. _`omap2_prm_deassert_hardreset.description`:

Description
-----------

Some IPs like dsp or iva contain processors that require an HW
reset line to be asserted / deasserted in order to fully enable the
IP.  These modules may have multiple hard-reset lines that reset
different 'submodules' inside the IP block.  This function will
take the submodule out of reset and wait until the PRCM indicates
that the reset has completed before returning.  Returns 0 upon success or
-EINVAL upon an argument error, -EEXIST if the submodule was already out
of reset, or -EBUSY if the submodule did not exit reset promptly.

.. This file was automatic generated / don't edit.


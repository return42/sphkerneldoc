.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prminst44xx.c

.. _`omap_prm_base_init`:

omap_prm_base_init
==================

.. c:function:: void omap_prm_base_init( void)

    Populates the prm partitions

    :param  void:
        no arguments

.. _`omap_prm_base_init.description`:

Description
-----------

Populates the base addresses of the \_prm_bases
array used for read/write of prm module registers.

.. _`omap4_prminst_is_hardreset_asserted`:

omap4_prminst_is_hardreset_asserted
===================================

.. c:function:: int omap4_prminst_is_hardreset_asserted(u8 shift, u8 part, s16 inst, u16 rstctrl_offs)

    read the HW reset line state of submodules contained in the hwmod module

    :param u8 shift:
        register bit shift corresponding to the reset line to check

    :param u8 part:
        *undescribed*

    :param s16 inst:
        *undescribed*

    :param u16 rstctrl_offs:
        *undescribed*

.. _`omap4_prminst_is_hardreset_asserted.description`:

Description
-----------

Returns 1 if the (sub)module hardreset line is currently asserted,
0 if the (sub)module hardreset line is not currently asserted, or
-EINVAL upon parameter error.

.. _`omap4_prminst_assert_hardreset`:

omap4_prminst_assert_hardreset
==============================

.. c:function:: int omap4_prminst_assert_hardreset(u8 shift, u8 part, s16 inst, u16 rstctrl_offs)

    assert the HW reset line of a submodule

    :param u8 shift:
        register bit shift corresponding to the reset line to assert

    :param u8 part:
        *undescribed*

    :param s16 inst:
        *undescribed*

    :param u16 rstctrl_offs:
        *undescribed*

.. _`omap4_prminst_assert_hardreset.description`:

Description
-----------

Some IPs like dsp, ipu or iva contain processors that require an HW
reset line to be asserted / deasserted in order to fully enable the
IP.  These modules may have multiple hard-reset lines that reset
different 'submodules' inside the IP block.  This function will
place the submodule into reset.  Returns 0 upon success or -EINVAL
upon an argument error.

.. _`omap4_prminst_deassert_hardreset`:

omap4_prminst_deassert_hardreset
================================

.. c:function:: int omap4_prminst_deassert_hardreset(u8 shift, u8 st_shift, u8 part, s16 inst, u16 rstctrl_offs, u16 rstst_offs)

    deassert a submodule hardreset line and wait

    :param u8 shift:
        register bit shift corresponding to the reset line to deassert

    :param u8 st_shift:
        status bit offset corresponding to the reset line

    :param u8 part:
        PRM partition

    :param s16 inst:
        PRM instance offset

    :param u16 rstctrl_offs:
        reset register offset

    :param u16 rstst_offs:
        reset status register offset

.. _`omap4_prminst_deassert_hardreset.description`:

Description
-----------

Some IPs like dsp, ipu or iva contain processors that require an HW
reset line to be asserted / deasserted in order to fully enable the
IP.  These modules may have multiple hard-reset lines that reset
different 'submodules' inside the IP block.  This function will
take the submodule out of reset and wait until the PRCM indicates
that the reset has completed before returning.  Returns 0 upon success or
-EINVAL upon an argument error, -EEXIST if the submodule was already out
of reset, or -EBUSY if the submodule did not exit reset promptly.

.. This file was automatic generated / don't edit.


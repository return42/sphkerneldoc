.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm33xx.c

.. _`am33xx_prm_is_hardreset_asserted`:

am33xx_prm_is_hardreset_asserted
================================

.. c:function:: int am33xx_prm_is_hardreset_asserted(u8 shift, u8 part, s16 inst, u16 rstctrl_offs)

    read the HW reset line state of submodules contained in the hwmod module

    :param u8 shift:
        register bit shift corresponding to the reset line to check

    :param u8 part:
        PRM partition, ignored for AM33xx

    :param s16 inst:
        CM instance register offset (\*\_INST macro)

    :param u16 rstctrl_offs:
        RM_RSTCTRL register address offset for this module

.. _`am33xx_prm_is_hardreset_asserted.description`:

Description
-----------

Returns 1 if the (sub)module hardreset line is currently asserted,
0 if the (sub)module hardreset line is not currently asserted, or
-EINVAL upon parameter error.

.. _`am33xx_prm_assert_hardreset`:

am33xx_prm_assert_hardreset
===========================

.. c:function:: int am33xx_prm_assert_hardreset(u8 shift, u8 part, s16 inst, u16 rstctrl_offs)

    assert the HW reset line of a submodule

    :param u8 shift:
        register bit shift corresponding to the reset line to assert

    :param u8 part:
        CM partition, ignored for AM33xx

    :param s16 inst:
        CM instance register offset (\*\_INST macro)

    :param u16 rstctrl_offs:
        *undescribed*

.. _`am33xx_prm_assert_hardreset.description`:

Description
-----------

Some IPs like dsp, ipu or iva contain processors that require an HW
reset line to be asserted / deasserted in order to fully enable the
IP.  These modules may have multiple hard-reset lines that reset
different 'submodules' inside the IP block.  This function will
place the submodule into reset.  Returns 0 upon success or -EINVAL
upon an argument error.

.. _`am33xx_prm_deassert_hardreset`:

am33xx_prm_deassert_hardreset
=============================

.. c:function:: int am33xx_prm_deassert_hardreset(u8 shift, u8 st_shift, u8 part, s16 inst, u16 rstctrl_offs, u16 rstst_offs)

    deassert a submodule hardreset line and wait

    :param u8 shift:
        register bit shift corresponding to the reset line to deassert

    :param u8 st_shift:
        reset status register bit shift corresponding to the reset line

    :param u8 part:
        PRM partition, not used for AM33xx

    :param s16 inst:
        CM instance register offset (\*\_INST macro)

    :param u16 rstctrl_offs:
        *undescribed*

    :param u16 rstst_offs:
        *undescribed*

.. _`am33xx_prm_deassert_hardreset.description`:

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

.. _`am33xx_prm_global_warm_sw_reset`:

am33xx_prm_global_warm_sw_reset
===============================

.. c:function:: void am33xx_prm_global_warm_sw_reset( void)

    reboot the device via warm reset

    :param  void:
        no arguments

.. _`am33xx_prm_global_warm_sw_reset.description`:

Description
-----------

Immediately reboots the device through warm reset.

.. This file was automatic generated / don't edit.


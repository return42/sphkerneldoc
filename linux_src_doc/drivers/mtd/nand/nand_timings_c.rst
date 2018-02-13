.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/nand_timings.c

.. _`onfi_async_timing_mode_to_sdr_timings`:

onfi_async_timing_mode_to_sdr_timings
=====================================

.. c:function:: const struct nand_sdr_timings *onfi_async_timing_mode_to_sdr_timings(int mode)

    [NAND Interface] Retrieve NAND timings according to the given ONFI timing mode

    :param int mode:
        ONFI timing mode

.. _`onfi_fill_data_interface`:

onfi_fill_data_interface
========================

.. c:function:: int onfi_fill_data_interface(struct nand_chip *chip, enum nand_data_interface_type type, int timing_mode)

    [NAND Interface] Initialize a data interface from given ONFI mode

    :param struct nand_chip \*chip:
        *undescribed*

    :param enum nand_data_interface_type type:
        *undescribed*

    :param int timing_mode:
        *undescribed*

.. This file was automatic generated / don't edit.


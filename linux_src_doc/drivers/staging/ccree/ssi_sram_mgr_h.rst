.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ccree/ssi_sram_mgr.h

.. _`ssi_sram_mgr_const2sram_desc`:

ssi_sram_mgr_const2sram_desc
============================

.. c:function:: void ssi_sram_mgr_const2sram_desc(const uint32_t *src, ssi_sram_addr_t dst, unsigned int nelement, HwDesc_s *seq, unsigned int *seq_len)

    Create const descriptors sequence to set values in given array into SRAM.

    :param const uint32_t \*src:
        A pointer to array of words to set as consts.

    :param ssi_sram_addr_t dst:
        The target SRAM buffer to set into

    :param unsigned int nelement:
        *undescribed*

    :param HwDesc_s \*seq:
        A pointer to the given IN/OUT descriptor sequence

    :param unsigned int \*seq_len:
        A pointer to the given IN/OUT sequence length

.. _`ssi_sram_mgr_const2sram_desc.note`:

Note
----

each const value can't exceed word size.

.. This file was automatic generated / don't edit.


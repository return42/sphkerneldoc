.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ccree/ssi_sram_mgr.c

.. _`ssi_sram_mgr_ctx`:

struct ssi_sram_mgr_ctx
=======================

.. c:type:: struct ssi_sram_mgr_ctx

    Internal RAM context manager

.. _`ssi_sram_mgr_ctx.definition`:

Definition
----------

.. code-block:: c

    struct ssi_sram_mgr_ctx {
        ssi_sram_addr_t sram_free_offset;
    }

.. _`ssi_sram_mgr_ctx.members`:

Members
-------

sram_free_offset
    the offset to the non-allocated area

.. _`ssi_sram_mgr_fini`:

ssi_sram_mgr_fini
=================

.. c:function:: void ssi_sram_mgr_fini(struct ssi_drvdata *drvdata)

    Cleanup SRAM pool.

    :param struct ssi_drvdata \*drvdata:
        Associated device driver context

.. _`ssi_sram_mgr_init`:

ssi_sram_mgr_init
=================

.. c:function:: int ssi_sram_mgr_init(struct ssi_drvdata *drvdata)

    Initializes SRAM pool. The pool starts right at the beginning of SRAM. Returns zero for success, negative value otherwise.

    :param struct ssi_drvdata \*drvdata:
        Associated device driver context

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


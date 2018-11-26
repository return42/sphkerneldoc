.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ccree/cc_sram_mgr.c

.. _`cc_sram_ctx`:

struct cc_sram_ctx
==================

.. c:type:: struct cc_sram_ctx

    Internal RAM context manager

.. _`cc_sram_ctx.definition`:

Definition
----------

.. code-block:: c

    struct cc_sram_ctx {
        cc_sram_addr_t sram_free_offset;
    }

.. _`cc_sram_ctx.members`:

Members
-------

sram_free_offset
    the offset to the non-allocated area

.. _`cc_sram_mgr_fini`:

cc_sram_mgr_fini
================

.. c:function:: void cc_sram_mgr_fini(struct cc_drvdata *drvdata)

    Cleanup SRAM pool.

    :param drvdata:
        Associated device driver context
    :type drvdata: struct cc_drvdata \*

.. _`cc_sram_mgr_init`:

cc_sram_mgr_init
================

.. c:function:: int cc_sram_mgr_init(struct cc_drvdata *drvdata)

    Initializes SRAM pool. The pool starts right at the beginning of SRAM. Returns zero for success, negative value otherwise.

    :param drvdata:
        Associated device driver context
    :type drvdata: struct cc_drvdata \*

.. _`cc_set_sram_desc`:

cc_set_sram_desc
================

.. c:function:: void cc_set_sram_desc(const u32 *src, cc_sram_addr_t dst, unsigned int nelement, struct cc_hw_desc *seq, unsigned int *seq_len)

    Create const descriptors sequence to set values in given array into SRAM.

    :param src:
        A pointer to array of words to set as consts.
    :type src: const u32 \*

    :param dst:
        The target SRAM buffer to set into
    :type dst: cc_sram_addr_t

    :param nelement:
        *undescribed*
    :type nelement: unsigned int

    :param seq:
        A pointer to the given IN/OUT descriptor sequence
    :type seq: struct cc_hw_desc \*

    :param seq_len:
        A pointer to the given IN/OUT sequence length
    :type seq_len: unsigned int \*

.. _`cc_set_sram_desc.note`:

Note
----

each const value can't exceed word size.

.. This file was automatic generated / don't edit.


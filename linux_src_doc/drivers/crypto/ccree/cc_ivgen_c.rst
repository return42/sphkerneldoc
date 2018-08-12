.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ccree/cc_ivgen.c

.. _`cc_ivgen_ctx`:

struct cc_ivgen_ctx
===================

.. c:type:: struct cc_ivgen_ctx

    IV pool generation context

.. _`cc_ivgen_ctx.definition`:

Definition
----------

.. code-block:: c

    struct cc_ivgen_ctx {
        cc_sram_addr_t pool;
        cc_sram_addr_t ctr_key;
        cc_sram_addr_t ctr_iv;
        u32 next_iv_ofs;
        u8 *pool_meta;
        dma_addr_t pool_meta_dma;
    }

.. _`cc_ivgen_ctx.members`:

Members
-------

pool
    the start address of the iv-pool resides in internal RAM

ctr_key
    *undescribed*

ctr_iv
    *undescribed*

next_iv_ofs
    the offset to the next available IV in pool

pool_meta
    virt. address of the initial enc. key/IV

pool_meta_dma
    phys. address of the initial enc. key/IV

.. This file was automatic generated / don't edit.


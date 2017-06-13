.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ccree/ssi_ivgen.c

.. _`ssi_ivgen_ctx`:

struct ssi_ivgen_ctx
====================

.. c:type:: struct ssi_ivgen_ctx

    IV pool generation context

.. _`ssi_ivgen_ctx.definition`:

Definition
----------

.. code-block:: c

    struct ssi_ivgen_ctx {
        ssi_sram_addr_t pool;
        ssi_sram_addr_t ctr_key;
        ssi_sram_addr_t ctr_iv;
        uint32_t next_iv_ofs;
        uint8_t *pool_meta;
        dma_addr_t pool_meta_dma;
    }

.. _`ssi_ivgen_ctx.members`:

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


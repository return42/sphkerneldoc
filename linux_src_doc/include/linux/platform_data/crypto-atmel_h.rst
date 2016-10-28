.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/crypto-atmel.h

.. _`crypto_dma_data`:

struct crypto_dma_data
======================

.. c:type:: struct crypto_dma_data

    DMA data for AES/TDES/SHA

.. _`crypto_dma_data.definition`:

Definition
----------

.. code-block:: c

    struct crypto_dma_data {
        struct at_dma_slave txdata;
        struct at_dma_slave rxdata;
    }

.. _`crypto_dma_data.members`:

Members
-------

txdata
    *undescribed*

rxdata
    *undescribed*

.. _`crypto_platform_data`:

struct crypto_platform_data
===========================

.. c:type:: struct crypto_platform_data

    board-specific AES/TDES/SHA configuration

.. _`crypto_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct crypto_platform_data {
        struct crypto_dma_data *dma_slave;
    }

.. _`crypto_platform_data.members`:

Members
-------

dma_slave
    DMA slave interface to use in data transfers.

.. This file was automatic generated / don't edit.


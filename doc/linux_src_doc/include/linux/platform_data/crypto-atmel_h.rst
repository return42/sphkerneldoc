.. -*- coding: utf-8; mode: rst -*-

==============
crypto-atmel.h
==============


.. _`crypto_dma_data`:

struct crypto_dma_data
======================

.. c:type:: crypto_dma_data

    DMA data for AES/TDES/SHA


.. _`crypto_dma_data.definition`:

Definition
----------

.. code-block:: c

  struct crypto_dma_data {
  };


.. _`crypto_dma_data.members`:

Members
-------




.. _`crypto_platform_data`:

struct crypto_platform_data
===========================

.. c:type:: crypto_platform_data

    board-specific AES/TDES/SHA configuration


.. _`crypto_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct crypto_platform_data {
    struct crypto_dma_data * dma_slave;
  };


.. _`crypto_platform_data.members`:

Members
-------

:``dma_slave``:
    DMA slave interface to use in data transfers.



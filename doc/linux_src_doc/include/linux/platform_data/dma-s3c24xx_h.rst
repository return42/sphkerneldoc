.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/dma-s3c24xx.h

.. _`s3c24xx_dma_platdata`:

struct s3c24xx_dma_platdata
===========================

.. c:type:: struct s3c24xx_dma_platdata

    platform specific settings

.. _`s3c24xx_dma_platdata.definition`:

Definition
----------

.. code-block:: c

    struct s3c24xx_dma_platdata {
        int num_phy_channels;
        struct s3c24xx_dma_channel *channels;
        int num_channels;
    }

.. _`s3c24xx_dma_platdata.members`:

Members
-------

num_phy_channels
    number of physical channels

channels
    array of virtual channel descriptions

num_channels
    number of virtual channels

.. This file was automatic generated / don't edit.


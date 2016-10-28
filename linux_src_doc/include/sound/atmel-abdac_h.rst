.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/atmel-abdac.h

.. _`atmel_abdac_pdata`:

struct atmel_abdac_pdata
========================

.. c:type:: struct atmel_abdac_pdata

    board specific ABDAC configuration

.. _`atmel_abdac_pdata.definition`:

Definition
----------

.. code-block:: c

    struct atmel_abdac_pdata {
        struct dw_dma_slave dws;
    }

.. _`atmel_abdac_pdata.members`:

Members
-------

dws
    DMA slave interface to use for sound playback.

.. This file was automatic generated / don't edit.


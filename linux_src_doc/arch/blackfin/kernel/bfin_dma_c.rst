.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/blackfin/kernel/bfin_dma.c

.. _`request_dma`:

request_dma
===========

.. c:function:: int request_dma(unsigned int channel, const char *device_id)

    request a DMA channel

    :param unsigned int channel:
        *undescribed*

    :param const char \*device_id:
        *undescribed*

.. _`request_dma.description`:

Description
-----------

Request the specific DMA channel from the system if it's available.

.. _`clear_dma_buffer`:

clear_dma_buffer
================

.. c:function:: void clear_dma_buffer(unsigned int channel)

    clear DMA fifos for specified channel

    :param unsigned int channel:
        *undescribed*

.. _`clear_dma_buffer.description`:

Description
-----------

Set the Buffer Clear bit in the Configuration register of specific DMA
channel. This will stop the descriptor based DMA operation.

.. _`blackfin_dma_early_init`:

blackfin_dma_early_init
=======================

.. c:function:: void blackfin_dma_early_init( void)

    minimal DMA init

    :param  void:
        no arguments

.. _`blackfin_dma_early_init.description`:

Description
-----------

Setup a few DMA registers so we can safely do DMA transfers early on in
the kernel booting process.  Really this just means using \ :c:func:`dma_memcpy`\ .

.. _`__dma_memcpy`:

\__dma_memcpy
=============

.. c:function:: void __dma_memcpy(u32 daddr, s16 dmod, u32 saddr, s16 smod, size_t cnt, u32 conf)

    program the MDMA registers

    :param u32 daddr:
        *undescribed*

    :param s16 dmod:
        *undescribed*

    :param u32 saddr:
        *undescribed*

    :param s16 smod:
        *undescribed*

    :param size_t cnt:
        *undescribed*

    :param u32 conf:
        *undescribed*

.. _`__dma_memcpy.description`:

Description
-----------

Actually program MDMA0 and wait for the transfer to finish.  Disable IRQs
while programming registers so that everything is fully configured.  Wait
for DMA to finish with IRQs enabled.  If interrupted, the initial DMA_DONE
check will make sure we don't clobber any existing transfer.

.. _`_dma_memcpy`:

\_dma_memcpy
============

.. c:function:: void *_dma_memcpy(void *pdst, const void *psrc, size_t size)

    translate C memcpy settings into MDMA settings

    :param void \*pdst:
        *undescribed*

    :param const void \*psrc:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`_dma_memcpy.description`:

Description
-----------

Handle all the high level steps before we touch the MDMA registers.  So
handle direction, tweaking of sizes, and formatting of addresses.

.. _`dma_memcpy`:

dma_memcpy
==========

.. c:function:: void *dma_memcpy(void *pdst, const void *psrc, size_t size)

    DMA memcpy under mutex lock

    :param void \*pdst:
        *undescribed*

    :param const void \*psrc:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`dma_memcpy.description`:

Description
-----------

Do not check arguments before starting the DMA memcpy.  Break the transfer
up into two pieces.  The first transfer is in multiples of 64k and the
second transfer is the piece smaller than 64k.

.. _`dma_memcpy_nocache`:

dma_memcpy_nocache
==================

.. c:function:: void *dma_memcpy_nocache(void *pdst, const void *psrc, size_t size)

    DMA memcpy under mutex lock - No cache flush/invalidate

    :param void \*pdst:
        *undescribed*

    :param const void \*psrc:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`dma_memcpy_nocache.description`:

Description
-----------

Do not check arguments before starting the DMA memcpy.  Break the transfer
up into two pieces.  The first transfer is in multiples of 64k and the
second transfer is the piece smaller than 64k.

.. _`safe_dma_memcpy`:

safe_dma_memcpy
===============

.. c:function:: void *safe_dma_memcpy(void *dst, const void *src, size_t size)

    DMA memcpy w/argument checking

    :param void \*dst:
        *undescribed*

    :param const void \*src:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`safe_dma_memcpy.description`:

Description
-----------

Verify arguments are safe before heading to \ :c:func:`dma_memcpy`\ .

.. This file was automatic generated / don't edit.


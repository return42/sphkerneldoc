.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/dmaengine.h

.. _`dma_cookie_init`:

dma_cookie_init
===============

.. c:function:: void dma_cookie_init(struct dma_chan *chan)

    initialize the cookies for a DMA channel

    :param struct dma_chan \*chan:
        dma channel to initialize

.. _`dma_cookie_assign`:

dma_cookie_assign
=================

.. c:function:: dma_cookie_t dma_cookie_assign(struct dma_async_tx_descriptor *tx)

    assign a DMA engine cookie to the descriptor

    :param struct dma_async_tx_descriptor \*tx:
        descriptor needing cookie

.. _`dma_cookie_assign.description`:

Description
-----------

Assign a unique non-zero per-channel cookie to the descriptor.

.. _`dma_cookie_assign.note`:

Note
----

caller is expected to hold a lock to prevent concurrency.

.. _`dma_cookie_complete`:

dma_cookie_complete
===================

.. c:function:: void dma_cookie_complete(struct dma_async_tx_descriptor *tx)

    complete a descriptor

    :param struct dma_async_tx_descriptor \*tx:
        descriptor to complete

.. _`dma_cookie_complete.description`:

Description
-----------

Mark this descriptor complete by updating the channels completed
cookie marker.  Zero the descriptors cookie to prevent accidental
repeated completions.

.. _`dma_cookie_complete.note`:

Note
----

caller is expected to hold a lock to prevent concurrency.

.. _`dma_cookie_status`:

dma_cookie_status
=================

.. c:function:: enum dma_status dma_cookie_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *state)

    report cookie status

    :param struct dma_chan \*chan:
        dma channel

    :param dma_cookie_t cookie:
        cookie we are interested in

    :param struct dma_tx_state \*state:
        dma_tx_state structure to return last/used cookies

.. _`dma_cookie_status.description`:

Description
-----------

Report the status of the cookie, filling in the state structure if
non-NULL.  No locking is required.

.. This file was automatic generated / don't edit.


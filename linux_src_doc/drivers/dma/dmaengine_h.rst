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

.. _`dmaengine_desc_get_callback`:

dmaengine_desc_get_callback
===========================

.. c:function:: void dmaengine_desc_get_callback(struct dma_async_tx_descriptor *tx, struct dmaengine_desc_callback *cb)

    get the passed in callback function

    :param struct dma_async_tx_descriptor \*tx:
        tx descriptor

    :param struct dmaengine_desc_callback \*cb:
        temp struct to hold the callback info

.. _`dmaengine_desc_get_callback.description`:

Description
-----------

Fill the passed in cb struct with what's available in the passed in
tx descriptor struct
No locking is required.

.. _`dmaengine_desc_callback_invoke`:

dmaengine_desc_callback_invoke
==============================

.. c:function:: void dmaengine_desc_callback_invoke(struct dmaengine_desc_callback *cb, const struct dmaengine_result *result)

    call the callback function in cb struct

    :param struct dmaengine_desc_callback \*cb:
        temp struct that is holding the callback info

    :param const struct dmaengine_result \*result:
        transaction result

.. _`dmaengine_desc_callback_invoke.description`:

Description
-----------

Call the callback function provided in the cb struct with the parameter
in the cb struct.
Locking is dependent on the driver.

.. _`dmaengine_desc_get_callback_invoke`:

dmaengine_desc_get_callback_invoke
==================================

.. c:function:: void dmaengine_desc_get_callback_invoke(struct dma_async_tx_descriptor *tx, const struct dmaengine_result *result)

    get the callback in tx descriptor and then immediately call the callback.

    :param struct dma_async_tx_descriptor \*tx:
        dma async tx descriptor

    :param const struct dmaengine_result \*result:
        transaction result

.. _`dmaengine_desc_get_callback_invoke.description`:

Description
-----------

Call \ :c:func:`dmaengine_desc_get_callback`\  and \ :c:func:`dmaengine_desc_callback_invoke`\ 
in a single function since no work is necessary in between for the driver.
Locking is dependent on the driver.

.. _`dmaengine_desc_callback_valid`:

dmaengine_desc_callback_valid
=============================

.. c:function:: bool dmaengine_desc_callback_valid(struct dmaengine_desc_callback *cb)

    verify the callback is valid in cb

    :param struct dmaengine_desc_callback \*cb:
        callback info struct

.. _`dmaengine_desc_callback_valid.description`:

Description
-----------

Return a bool that verifies whether callback in cb is valid or not.
No locking is required.

.. This file was automatic generated / don't edit.


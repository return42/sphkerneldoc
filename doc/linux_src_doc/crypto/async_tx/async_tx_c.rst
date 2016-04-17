.. -*- coding: utf-8; mode: rst -*-

==========
async_tx.c
==========


.. _`__async_tx_find_channel`:

__async_tx_find_channel
=======================

.. c:function:: struct dma_chan *__async_tx_find_channel (struct async_submit_ctl *submit, enum dma_transaction_type tx_type)

    find a channel to carry out the operation or let the transaction execute synchronously

    :param struct async_submit_ctl \*submit:
        transaction dependency and submission modifiers

    :param enum dma_transaction_type tx_type:
        transaction type



.. _`async_tx_channel_switch`:

async_tx_channel_switch
=======================

.. c:function:: void async_tx_channel_switch (struct dma_async_tx_descriptor *depend_tx, struct dma_async_tx_descriptor *tx)

    queue an interrupt descriptor with a dependency pre-attached.

    :param struct dma_async_tx_descriptor \*depend_tx:
        the operation that must finish before the new operation runs

    :param struct dma_async_tx_descriptor \*tx:
        the new operation



.. _`async_trigger_callback`:

async_trigger_callback
======================

.. c:function:: struct dma_async_tx_descriptor *async_trigger_callback (struct async_submit_ctl *submit)

    schedules the callback function to be run

    :param struct async_submit_ctl \*submit:
        submission and completion parameters



.. _`async_trigger_callback.honored-flags`:

honored flags
-------------

ASYNC_TX_ACK

The callback is run after any dependent operations have completed.



.. _`async_tx_quiesce`:

async_tx_quiesce
================

.. c:function:: void async_tx_quiesce (struct dma_async_tx_descriptor **tx)

    ensure tx is complete and freeable upon return @tx - transaction to quiesce

    :param struct dma_async_tx_descriptor \*\*tx:

        *undescribed*


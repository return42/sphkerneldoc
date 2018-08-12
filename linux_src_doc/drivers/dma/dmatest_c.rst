.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/dmatest.c

.. _`dmatest_params`:

struct dmatest_params
=====================

.. c:type:: struct dmatest_params

    test parameters.

.. _`dmatest_params.definition`:

Definition
----------

.. code-block:: c

    struct dmatest_params {
        unsigned int buf_size;
        char channel[20];
        char device[32];
        unsigned int threads_per_chan;
        unsigned int max_channels;
        unsigned int iterations;
        unsigned int xor_sources;
        unsigned int pq_sources;
        int timeout;
        bool noverify;
        bool norandom;
    }

.. _`dmatest_params.members`:

Members
-------

buf_size
    size of the memcpy test buffer

channel
    bus ID of the channel to test

device
    bus ID of the DMA Engine to test

threads_per_chan
    number of threads to start per channel

max_channels
    maximum number of channels to use

iterations
    iterations before stopping test

xor_sources
    number of xor source buffers

pq_sources
    number of p+q source buffers

timeout
    transfer timeout in msec, -1 for infinite timeout

noverify
    *undescribed*

norandom
    *undescribed*

.. This file was automatic generated / don't edit.


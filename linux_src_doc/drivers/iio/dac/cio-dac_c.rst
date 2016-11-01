.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dac/cio-dac.c

.. _`cio_dac_iio`:

struct cio_dac_iio
==================

.. c:type:: struct cio_dac_iio

    IIO device private data structure

.. _`cio_dac_iio.definition`:

Definition
----------

.. code-block:: c

    struct cio_dac_iio {
        int chan_out_states[CIO_DAC_NUM_CHAN];
        unsigned int base;
    }

.. _`cio_dac_iio.members`:

Members
-------

chan_out_states
    channels' output states

base
    base port address of the IIO device

.. This file was automatic generated / don't edit.


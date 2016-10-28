.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dac/stx104.c

.. _`stx104_iio`:

struct stx104_iio
=================

.. c:type:: struct stx104_iio

    IIO device private data structure

.. _`stx104_iio.definition`:

Definition
----------

.. code-block:: c

    struct stx104_iio {
        unsigned chan_out_states[STX104_NUM_CHAN];
        unsigned base;
    }

.. _`stx104_iio.members`:

Members
-------

chan_out_states
    channels' output states

base
    base port address of the IIO device

.. This file was automatic generated / don't edit.


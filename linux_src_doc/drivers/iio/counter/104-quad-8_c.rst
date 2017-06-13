.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/counter/104-quad-8.c

.. _`quad8_iio`:

struct quad8_iio
================

.. c:type:: struct quad8_iio

    IIO device private data structure

.. _`quad8_iio.definition`:

Definition
----------

.. code-block:: c

    struct quad8_iio {
        unsigned int preset;
        unsigned int count_mode;
        unsigned int quadrature_mode;
        unsigned int quadrature_scale;
        unsigned int ab_enable;
        unsigned int preset_enable;
        unsigned int synchronous_mode;
        unsigned int index_polarity;
        unsigned int base;
    }

.. _`quad8_iio.members`:

Members
-------

preset
    array of preset values

count_mode
    array of count mode configurations

quadrature_mode
    array of quadrature mode configurations

quadrature_scale
    array of quadrature mode scale configurations

ab_enable
    array of A and B inputs enable configurations

preset_enable
    array of set_to_preset_on_index attribute configurations

synchronous_mode
    array of index function synchronous mode configurations

index_polarity
    array of index function polarity configurations

base
    base port address of the IIO device

.. This file was automatic generated / don't edit.


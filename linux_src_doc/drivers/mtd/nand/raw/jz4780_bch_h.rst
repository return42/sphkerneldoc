.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/jz4780_bch.h

.. _`jz4780_bch_params`:

struct jz4780_bch_params
========================

.. c:type:: struct jz4780_bch_params

    BCH parameters

.. _`jz4780_bch_params.definition`:

Definition
----------

.. code-block:: c

    struct jz4780_bch_params {
        int size;
        int bytes;
        int strength;
    }

.. _`jz4780_bch_params.members`:

Members
-------

size
    data bytes per ECC step.

bytes
    ECC bytes per step.

strength
    number of correctable bits per ECC step.

.. This file was automatic generated / don't edit.


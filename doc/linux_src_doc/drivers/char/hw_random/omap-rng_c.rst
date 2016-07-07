.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/hw_random/omap-rng.c

.. _`omap_rng_pdata`:

struct omap_rng_pdata
=====================

.. c:type:: struct omap_rng_pdata

    RNG IP block-specific data

.. _`omap_rng_pdata.definition`:

Definition
----------

.. code-block:: c

    struct omap_rng_pdata {
        u16 *regs;
        u32 data_size;
        u32 (* data_present) (struct omap_rng_dev *priv);
        int (* init) (struct omap_rng_dev *priv);
        void (* cleanup) (struct omap_rng_dev *priv);
    }

.. _`omap_rng_pdata.members`:

Members
-------

regs
    Pointer to the register offsets structure.

data_size
    No. of bytes in RNG output.

data_present
    Callback to determine if data is available.

init
    Callback for IP specific initialization sequence.

cleanup
    Callback for IP specific cleanup sequence.

.. This file was automatic generated / don't edit.


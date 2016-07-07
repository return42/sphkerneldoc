.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/versatile/clk-icst.h

.. _`clk_icst_desc`:

struct clk_icst_desc
====================

.. c:type:: struct clk_icst_desc

    descriptor for the ICST VCO

.. _`clk_icst_desc.definition`:

Definition
----------

.. code-block:: c

    struct clk_icst_desc {
        const struct icst_params *params;
        u32 vco_offset;
        u32 lock_offset;
    }

.. _`clk_icst_desc.members`:

Members
-------

params
    ICST parameters

vco_offset
    offset to the ICST VCO from the provided memory base

lock_offset
    offset to the ICST VCO locking register from the provided
    memory base

.. This file was automatic generated / don't edit.


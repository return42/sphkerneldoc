.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-xgene.c

.. _`xgene_clk_pmd`:

struct xgene_clk_pmd
====================

.. c:type:: struct xgene_clk_pmd

    PMD clock

.. _`xgene_clk_pmd.definition`:

Definition
----------

.. code-block:: c

    struct xgene_clk_pmd {
        struct clk_hw hw;
        void __iomem *reg;
        u8 shift;
        u32 mask;
        u64 denom;
        u32 flags;
        spinlock_t *lock;
    }

.. _`xgene_clk_pmd.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing the fractional scale multiplier (scaler)

shift
    shift to the unit bit field

mask
    *undescribed*

denom
    1/denominator unit

flags
    *undescribed*

lock
    register lock

.. _`xgene_clk_pmd.flags`:

Flags
-----

XGENE_CLK_PMD_SCALE_INVERTED - By default the scaler is the value read
from the register plus one. For example,
0 for (0 + 1) / denom,
1 for (1 + 1) / denom and etc.
If this flag is set, it is
0 for (denom - 0) / denom,
1 for (denom - 1) / denom and etc.

.. This file was automatic generated / don't edit.


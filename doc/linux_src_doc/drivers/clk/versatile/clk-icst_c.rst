.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/versatile/clk-icst.c

.. _`clk_icst`:

struct clk_icst
===============

.. c:type:: struct clk_icst

    ICST VCO clock wrapper

.. _`clk_icst.definition`:

Definition
----------

.. code-block:: c

    struct clk_icst {
        struct clk_hw hw;
        struct regmap *map;
        u32 vcoreg_off;
        u32 lockreg_off;
        struct icst_params *params;
        unsigned long rate;
    }

.. _`clk_icst.members`:

Members
-------

hw
    corresponding clock hardware entry

map
    *undescribed*

vcoreg_off
    *undescribed*

lockreg_off
    *undescribed*

params
    parameters for this ICST instance

rate
    current rate

.. _`vco_get`:

vco_get
=======

.. c:function:: int vco_get(struct clk_icst *icst, struct icst_vco *vco)

    get ICST VCO settings from a certain ICST

    :param struct clk_icst \*icst:
        the ICST clock to get

    :param struct icst_vco \*vco:
        the VCO struct to return the value in

.. _`vco_set`:

vco_set
=======

.. c:function:: int vco_set(struct clk_icst *icst, struct icst_vco vco)

    commit changes to an ICST VCO

    :param struct clk_icst \*icst:
        the ICST clock to set

    :param struct icst_vco vco:
        the VCO struct to set the changes from

.. This file was automatic generated / don't edit.


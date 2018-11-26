.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/versatile/clk-icst.c

.. _`icst_control_type`:

enum icst_control_type
======================

.. c:type:: enum icst_control_type

    the type of ICST control register

.. _`icst_control_type.definition`:

Definition
----------

.. code-block:: c

    enum icst_control_type {
        ICST_VERSATILE,
        ICST_INTEGRATOR_AP_CM,
        ICST_INTEGRATOR_AP_SYS,
        ICST_INTEGRATOR_AP_PCI,
        ICST_INTEGRATOR_CP_CM_CORE,
        ICST_INTEGRATOR_CP_CM_MEM
    };

.. _`icst_control_type.constants`:

Constants
---------

ICST_VERSATILE
    *undescribed*

ICST_INTEGRATOR_AP_CM
    *undescribed*

ICST_INTEGRATOR_AP_SYS
    *undescribed*

ICST_INTEGRATOR_AP_PCI
    *undescribed*

ICST_INTEGRATOR_CP_CM_CORE
    *undescribed*

ICST_INTEGRATOR_CP_CM_MEM
    *undescribed*

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
        enum icst_control_type ctype;
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

ctype
    the type of control register for the ICST

.. _`vco_get`:

vco_get
=======

.. c:function:: int vco_get(struct clk_icst *icst, struct icst_vco *vco)

    get ICST VCO settings from a certain ICST

    :param icst:
        the ICST clock to get
    :type icst: struct clk_icst \*

    :param vco:
        the VCO struct to return the value in
    :type vco: struct icst_vco \*

.. _`vco_set`:

vco_set
=======

.. c:function:: int vco_set(struct clk_icst *icst, struct icst_vco vco)

    commit changes to an ICST VCO

    :param icst:
        the ICST clock to set
    :type icst: struct clk_icst \*

    :param vco:
        the VCO struct to set the changes from
    :type vco: struct icst_vco

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clock.h

.. _`ti_dt_clk`:

struct ti_dt_clk
================

.. c:type:: struct ti_dt_clk

    OMAP DT clock alias declarations

.. _`ti_dt_clk.definition`:

Definition
----------

.. code-block:: c

    struct ti_dt_clk {
        struct clk_lookup lk;
        char *node_name;
    }

.. _`ti_dt_clk.members`:

Members
-------

lk
    clock lookup definition

node_name
    clock DT node to map to

.. This file was automatic generated / don't edit.


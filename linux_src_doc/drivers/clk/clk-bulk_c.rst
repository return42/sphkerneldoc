.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-bulk.c

.. _`clk_bulk_unprepare`:

clk_bulk_unprepare
==================

.. c:function:: void clk_bulk_unprepare(int num_clks, const struct clk_bulk_data *clks)

    undo preparation of a set of clock sources

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table being unprepared
    :type clks: const struct clk_bulk_data \*

.. _`clk_bulk_unprepare.description`:

Description
-----------

clk_bulk_unprepare may sleep, which differentiates it from clk_bulk_disable.
Returns 0 on success, -EERROR otherwise.

.. _`clk_bulk_prepare`:

clk_bulk_prepare
================

.. c:function:: int clk_bulk_prepare(int num_clks, const struct clk_bulk_data *clks)

    prepare a set of clocks

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table being prepared
    :type clks: const struct clk_bulk_data \*

.. _`clk_bulk_prepare.description`:

Description
-----------

clk_bulk_prepare may sleep, which differentiates it from clk_bulk_enable.
Returns 0 on success, -EERROR otherwise.

.. _`clk_bulk_disable`:

clk_bulk_disable
================

.. c:function:: void clk_bulk_disable(int num_clks, const struct clk_bulk_data *clks)

    gate a set of clocks

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table being gated
    :type clks: const struct clk_bulk_data \*

.. _`clk_bulk_disable.description`:

Description
-----------

clk_bulk_disable must not sleep, which differentiates it from
clk_bulk_unprepare. clk_bulk_disable must be called before
clk_bulk_unprepare.

.. _`clk_bulk_enable`:

clk_bulk_enable
===============

.. c:function:: int clk_bulk_enable(int num_clks, const struct clk_bulk_data *clks)

    ungate a set of clocks

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table being ungated
    :type clks: const struct clk_bulk_data \*

.. _`clk_bulk_enable.description`:

Description
-----------

clk_bulk_enable must not sleep
Returns 0 on success, -EERROR otherwise.

.. This file was automatic generated / don't edit.


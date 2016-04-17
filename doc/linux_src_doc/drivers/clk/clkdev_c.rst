.. -*- coding: utf-8; mode: rst -*-

========
clkdev.c
========


.. _`of_clk_get_by_name`:

of_clk_get_by_name
==================

.. c:function:: struct clk *of_clk_get_by_name (struct device_node *np, const char *name)

    Parse and lookup a clock referenced by a device node

    :param struct device_node \*np:
        pointer to clock consumer node

    :param const char \*name:
        name of consumer's clock input, or NULL for the first clock reference



.. _`of_clk_get_by_name.description`:

Description
-----------

This function parses the clocks and clock-names properties,
and uses them to look up the struct clk from the registered list of clock
providers.



.. _`clkdev_create`:

clkdev_create
=============

.. c:function:: struct clk_lookup *clkdev_create (struct clk *clk, const char *con_id, const char *dev_fmt,  ...)

    allocate and add a clkdev lookup structure

    :param struct clk \*clk:
        struct clk to associate with all clk_lookups

    :param const char \*con_id:
        connection ID string on device

    :param const char \*dev_fmt:
        format string describing device name

    :param ...:
        variable arguments



.. _`clkdev_create.description`:

Description
-----------

Returns a clk_lookup structure, which can be later unregistered and
freed.



.. _`clk_register_clkdev`:

clk_register_clkdev
===================

.. c:function:: int clk_register_clkdev (struct clk *clk, const char *con_id, const char *dev_id)

    register one clock lookup for a struct clk

    :param struct clk \*clk:
        struct clk to associate with all clk_lookups

    :param const char \*con_id:
        connection ID string on device

    :param const char \*dev_id:
        string describing device name



.. _`clk_register_clkdev.description`:

Description
-----------

con_id or dev_id may be NULL as a wildcard, just as in the rest of
clkdev.

To make things easier for mass registration, we detect error clks
from a previous :c:func:`clk_register` call, and return the error code for
those.  This is to permit this function to be called immediately
after :c:func:`clk_register`.



.. _`clk_register_clkdevs`:

clk_register_clkdevs
====================

.. c:function:: int clk_register_clkdevs (struct clk *clk, struct clk_lookup *cl, size_t num)

    register a set of clk_lookup for a struct clk

    :param struct clk \*clk:
        struct clk to associate with all clk_lookups

    :param struct clk_lookup \*cl:
        array of clk_lookup structures with con_id and dev_id pre-initialized

    :param size_t num:
        number of clk_lookup structures to register



.. _`clk_register_clkdevs.description`:

Description
-----------

To make things easier for mass registration, we detect error clks
from a previous :c:func:`clk_register` call, and return the error code for
those.  This is to permit this function to be called immediately
after :c:func:`clk_register`.


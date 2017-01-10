.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clkdev.c

.. _`of_clk_get_by_name`:

of_clk_get_by_name
==================

.. c:function:: struct clk *of_clk_get_by_name(struct device_node *np, const char *name)

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

.. c:function:: struct clk_lookup *clkdev_create(struct clk *clk, const char *con_id, const char *dev_fmt,  ...)

    allocate and add a clkdev lookup structure

    :param struct clk \*clk:
        struct clk to associate with all clk_lookups

    :param const char \*con_id:
        connection ID string on device

    :param const char \*dev_fmt:
        format string describing device name

    :param ... :
        variable arguments

.. _`clkdev_create.description`:

Description
-----------

Returns a clk_lookup structure, which can be later unregistered and
freed.

.. _`clkdev_hw_create`:

clkdev_hw_create
================

.. c:function:: struct clk_lookup *clkdev_hw_create(struct clk_hw *hw, const char *con_id, const char *dev_fmt,  ...)

    allocate and add a clkdev lookup structure

    :param struct clk_hw \*hw:
        struct clk_hw to associate with all clk_lookups

    :param const char \*con_id:
        connection ID string on device

    :param const char \*dev_fmt:
        format string describing device name

    :param ... :
        variable arguments

.. _`clkdev_hw_create.description`:

Description
-----------

Returns a clk_lookup structure, which can be later unregistered and
freed.

.. _`clk_register_clkdev`:

clk_register_clkdev
===================

.. c:function:: int clk_register_clkdev(struct clk *clk, const char *con_id, const char *dev_id)

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
from a previous \ :c:func:`clk_register`\  call, and return the error code for
those.  This is to permit this function to be called immediately
after \ :c:func:`clk_register`\ .

.. _`clk_hw_register_clkdev`:

clk_hw_register_clkdev
======================

.. c:function:: int clk_hw_register_clkdev(struct clk_hw *hw, const char *con_id, const char *dev_id)

    register one clock lookup for a struct clk_hw

    :param struct clk_hw \*hw:
        struct clk_hw to associate with all clk_lookups

    :param const char \*con_id:
        connection ID string on device

    :param const char \*dev_id:
        format string describing device name

.. _`clk_hw_register_clkdev.description`:

Description
-----------

con_id or dev_id may be NULL as a wildcard, just as in the rest of
clkdev.

To make things easier for mass registration, we detect error clk_hws
from a previous clk_hw_register\_\*() call, and return the error code for
those.  This is to permit this function to be called immediately
after clk_hw_register\_\*().

.. This file was automatic generated / don't edit.


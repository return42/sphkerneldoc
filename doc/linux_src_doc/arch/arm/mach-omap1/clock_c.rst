.. -*- coding: utf-8; mode: rst -*-

=======
clock.c
=======


.. _`recalculate_root_clocks`:

recalculate_root_clocks
=======================

.. c:function:: void recalculate_root_clocks ( void)

    recalculate and propagate all root clocks

    :param void:
        no arguments



.. _`recalculate_root_clocks.description`:

Description
-----------


Recalculates all root clocks (clocks with no parent), which if the
clock's .recalc is set correctly, should also propagate their rates.
Called at init.



.. _`clk_preinit`:

clk_preinit
===========

.. c:function:: void clk_preinit (struct clk *clk)

    initialize any fields in the struct clk before clk init

    :param struct clk \*clk:
        struct clk * to initialize



.. _`clk_preinit.description`:

Description
-----------

Initialize any struct clk fields needed before normal clk initialization
can run.  No return value.



.. _`omap_clk_get_by_name`:

omap_clk_get_by_name
====================

.. c:function:: struct clk *omap_clk_get_by_name (const char *name)

    locate OMAP struct clk by its name

    :param const char \*name:
        name of the struct clk to locate



.. _`omap_clk_get_by_name.description`:

Description
-----------

Locate an OMAP struct clk by its name.  Assumes that struct clk
names are unique.  Returns NULL if not found or a pointer to the
struct clk if found.


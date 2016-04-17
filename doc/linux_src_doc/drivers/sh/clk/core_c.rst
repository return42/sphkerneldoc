.. -*- coding: utf-8; mode: rst -*-

======
core.c
======


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


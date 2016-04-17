.. -*- coding: utf-8; mode: rst -*-

======
init.c
======


.. _`show_mem`:

show_mem
========

.. c:function:: void show_mem (unsigned int filter)

    give short summary of memory stats

    :param unsigned int filter:

        *undescribed*



.. _`show_mem.description`:

Description
-----------


Shows a simple page count of reserved and used pages in the system.
For discontig machines, it does this on a per-pgdat basis.


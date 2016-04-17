.. -*- coding: utf-8; mode: rst -*-

=============
csrc-octeon.c
=============


.. _`octeon_io_clk_delay`:

octeon_io_clk_delay
===================

.. c:function:: void octeon_io_clk_delay (unsigned long count)

    wait for a given number of io clock cycles to pass.

    :param unsigned long count:
        The number of clocks to wait.



.. _`octeon_io_clk_delay.description`:

Description
-----------


We scale the wait by the clock ratio, and then wait for the
corresponding number of core clocks.


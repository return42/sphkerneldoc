.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/loadavg.c

.. _`get_avenrun`:

get_avenrun
===========

.. c:function:: void get_avenrun(unsigned long *loads, unsigned long offset, int shift)

    get the load average array

    :param unsigned long \*loads:
        pointer to dest load array

    :param unsigned long offset:
        offset to add

    :param int shift:
        shift count to shift the result left

.. _`get_avenrun.description`:

Description
-----------

These values are estimates at best, so no need for locking.

.. _`fixed_power_int`:

fixed_power_int
===============

.. c:function:: unsigned long fixed_power_int(unsigned long x, unsigned int frac_bits, unsigned int n)

    compute: x^n, in O(log n) time

    :param unsigned long x:
        base of the power

    :param unsigned int frac_bits:
        fractional bits of \ ``x``\ 

    :param unsigned int n:
        power to raise \ ``x``\  to.

.. _`fixed_power_int.description`:

Description
-----------

By exploiting the relation between the definition of the natural power
function: x^n := x\*x\*...\*x (x multiplied by itself for n times), and
the binary encoding of numbers used by computers: n := \Sum n_i \* 2^i,
(where: n_i \elem {0, 1}, the binary vector representing n),
we find: x^n := x^(\Sum n_i \* 2^i) := \Prod x^(n_i \* 2^i), which is
of course trivially computable in O(log_2 n), the length of our binary
vector.

.. This file was automatic generated / don't edit.


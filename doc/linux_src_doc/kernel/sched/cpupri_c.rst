.. -*- coding: utf-8; mode: rst -*-

========
cpupri.c
========

.. _`cpupri_find`:

cpupri_find
===========

.. c:function:: int cpupri_find (struct cpupri *cp, struct task_struct *p, struct cpumask *lowest_mask)

    find the best (lowest-pri) CPU in the system

    :param struct cpupri \*cp:
        The cpupri context

    :param struct task_struct \*p:
        The task

    :param struct cpumask \*lowest_mask:
        A mask to fill in with selected CPUs (or NULL)


.. _`cpupri_find.description`:

Description
-----------

Note: This function returns the recommended CPUs as calculated during the
current invocation.  By the time the call returns, the CPUs may have in
fact changed priorities any number of times.  While not ideal, it is not
an issue of correctness since the normal rebalancer logic will correct
any discrepancies created by racing against the uncertainty of the current
priority configuration.

Return: (int)bool - CPUs were found


.. _`cpupri_set`:

cpupri_set
==========

.. c:function:: void cpupri_set (struct cpupri *cp, int cpu, int newpri)

    update the cpu priority setting

    :param struct cpupri \*cp:
        The cpupri context

    :param int cpu:
        The target cpu

    :param int newpri:
        The priority (INVALID-RT99) to assign to this CPU


.. _`cpupri_set.description`:

Description
-----------

Note: Assumes cpu_rq(cpu)->lock is locked

Returns: (void)


.. _`cpupri_init`:

cpupri_init
===========

.. c:function:: int cpupri_init (struct cpupri *cp)

    initialize the cpupri structure

    :param struct cpupri \*cp:
        The cpupri context


.. _`cpupri_init.description`:

Description
-----------

Return: -ENOMEM on memory allocation failure.


.. _`cpupri_cleanup`:

cpupri_cleanup
==============

.. c:function:: void cpupri_cleanup (struct cpupri *cp)

    clean up the cpupri structure

    :param struct cpupri \*cp:
        The cpupri context


.. -*- coding: utf-8; mode: rst -*-

=======
icswx.c
=======


.. _`use_cop`:

use_cop
=======

.. c:function:: int use_cop (unsigned long acop, struct mm_struct *mm)

    :param unsigned long acop:
        mask of coprocessor to be used.

    :param struct mm_struct \*mm:
        The mm the coprocessor to associate with. Most likely current mm.



.. _`use_cop.description`:

Description
-----------

Return a positive PID if successful. Negative errno otherwise.
The returned PID will be fed to the coprocessor to determine if an
icswx transaction is authenticated.



.. _`drop_cop`:

drop_cop
========

.. c:function:: void drop_cop (unsigned long acop, struct mm_struct *mm)

    :param unsigned long acop:
        mask of coprocessor to be stopped.

    :param struct mm_struct \*mm:
        The mm the coprocessor associated with.


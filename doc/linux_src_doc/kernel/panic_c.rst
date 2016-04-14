.. -*- coding: utf-8; mode: rst -*-

=======
panic.c
=======

.. _`panic`:

panic
=====

.. c:function:: void panic (const char *fmt,  ...)

    halt the system

    :param const char \*fmt:
        The text string to print

    :param ...:
        variable arguments


.. _`panic.description`:

Description
-----------

Display a message, then perform cleanups.

This function never returns.


.. _`print_tainted`:

print_tainted
=============

.. c:function:: const char *print_tainted ( void)

    return a string to represent the kernel taint state.

    :param void:
        no arguments


.. _`print_tainted.description`:

Description
-----------


'P' - Proprietary module has been loaded.
'F' - Module has been forcibly loaded.
'S' - SMP with CPUs not designed for SMP.
'R' - User forced a module unload.
'M' - System experienced a machine check exception.
'B' - System has hit bad_page.
'U' - Userspace-defined naughtiness.
'D' - Kernel has oopsed before
'A' - ACPI table overridden.
'W' - Taint on warning.
'C' - modules from drivers/staging are loaded.
'I' - Working around severe firmware bug.
'O' - Out-of-tree module has been loaded.
'E' - Unsigned module has been loaded.
'L' - A soft lockup has previously occurred.
'K' - Kernel has been live patched.::

       The string is overwritten by the next call to :c:func:`print_tainted`.


.. _`add_taint`:

add_taint
=========

.. c:function:: void add_taint (unsigned flag, enum lockdep_ok lockdep_ok)

    :param unsigned flag:
        one of the TAINT_\* constants.

    :param enum lockdep_ok lockdep_ok:
        whether lock debugging is still OK.


.. _`add_taint.description`:

Description
-----------

If something bad has gone wrong, you'll want ``lockdebug_ok`` = false, but for
some notewortht-but-not-corrupting cases, it can be set to true.


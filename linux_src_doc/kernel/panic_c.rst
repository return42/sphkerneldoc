.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/panic.c

.. _`panic`:

panic
=====

.. c:function:: void panic(const char *fmt,  ...)

    halt the system

    :param fmt:
        The text string to print
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`panic.description`:

Description
-----------

     Display a message, then perform cleanups.

     This function never returns.

.. _`print_tainted`:

print_tainted
=============

.. c:function:: const char *print_tainted( void)

    return a string to represent the kernel taint state.

    :param void:
        no arguments
    :type void: 

.. _`print_tainted.description`:

Description
-----------

For individual taint flag meanings, see Documentation/sysctl/kernel.txt

The string is overwritten by the next call to \ :c:func:`print_tainted`\ ,
but is always NULL terminated.

.. _`add_taint`:

add_taint
=========

.. c:function:: void add_taint(unsigned flag, enum lockdep_ok lockdep_ok)

    add a taint flag if not already set.

    :param flag:
        one of the TAINT_* constants.
    :type flag: unsigned

    :param lockdep_ok:
        whether lock debugging is still OK.
    :type lockdep_ok: enum lockdep_ok

.. _`add_taint.description`:

Description
-----------

If something bad has gone wrong, you'll want \ ``lockdebug_ok``\  = false, but for
some notewortht-but-not-corrupting cases, it can be set to true.

.. This file was automatic generated / don't edit.


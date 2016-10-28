.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bug.h

.. _`build_bug_on_msg`:

BUILD_BUG_ON_MSG
================

.. c:function::  BUILD_BUG_ON_MSG( cond,  msg)

    break compile if a condition is true & emit supplied error message.

    :param  cond:
        *undescribed*

    :param  msg:
        *undescribed*

.. _`build_bug_on_msg.description`:

Description
-----------

See BUILD_BUG_ON for description.

.. _`build_bug_on`:

BUILD_BUG_ON
============

.. c:function::  BUILD_BUG_ON( condition)

    break compile if a condition is true.

    :param  condition:
        the condition which the compiler should know is false.

.. _`build_bug_on.description`:

Description
-----------

If you have some code which relies on certain constants being equal, or
some other compile-time-evaluated condition, you should use BUILD_BUG_ON to
detect if someone changes it.

The implementation uses gcc's reluctance to create a negative array, but gcc
(as of 4.4) only emits that error for obvious cases (e.g. not arguments to
inline functions).  Luckily, in 4.3 they added the "error" function
attribute just for this type of case.  Thus, we use a negative sized array
(should always create an error on gcc versions older than 4.4) and then call
an undefined function with the error attribute (should always create an
error on gcc 4.3 and later).  If for some reason, neither creates a
compile-time error, we'll still have a link-time error, which is harder to
track down.

.. _`build_bug`:

BUILD_BUG
=========

.. c:function::  BUILD_BUG( void)

    break compile if used.

    :param  void:
        no arguments

.. _`build_bug.description`:

Description
-----------

If you have some code that you expect the compiler to eliminate at
build time, you should use BUILD_BUG to detect if it is
unexpectedly used.

.. This file was automatic generated / don't edit.


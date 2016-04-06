
.. _API-add-taint:

=========
add_taint
=========

*man add_taint(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: void add_taint( unsigned flag, enum lockdep_ok lockdep_ok )

Arguments
=========

``flag``
    one of the TAINT_⋆ constants.

``lockdep_ok``
    whether lock debugging is still OK.


Description
===========

If something bad has gone wrong, you'll want ``lockdebug_ok`` = false, but for some notewortht-but-not-corrupting cases, it can be set to true.

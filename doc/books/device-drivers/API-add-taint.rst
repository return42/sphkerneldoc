.. -*- coding: utf-8; mode: rst -*-

.. _API-add-taint:

=========
add_taint
=========

*man add_taint(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: void add_taint( unsigned flag, enum lockdep_ok lockdep_ok )

Arguments
=========

``flag``
    one of the TAINT_* constants.

``lockdep_ok``
    whether lock debugging is still OK.


Description
===========

If something bad has gone wrong, you'll want ``lockdebug_ok`` = false,
but for some notewortht-but-not-corrupting cases, it can be set to true.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

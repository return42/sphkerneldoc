.. -*- coding: utf-8; mode: rst -*-

.. _API-abs:

===
abs
===

*man abs(9)*

*4.6.0-rc5*

return absolute value of an argument


Synopsis
========

.. c:function:: abs( x )

Arguments
=========

``x``
    the value. If it is unsigned type, it is converted to signed type
    first. char is treated as if it was signed (regardless of whether it
    really is) but the macro's return type is preserved as char.


Return
======

an absolute value of x.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-clamp-t:

=======
clamp_t
=======

*man clamp_t(9)*

*4.6.0-rc5*

return a value clamped to a given range using a given type


Synopsis
========

.. c:function:: clamp_t( type, val, lo, hi )

Arguments
=========

``type``
    the type of variable to use

``val``
    current value

``lo``
    minimum allowable value

``hi``
    maximum allowable value


Description
===========

This macro does no typechecking and uses temporary variables of type
'type' to make all the comparisons.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-kstrtobool:

==========
kstrtobool
==========

*man kstrtobool(9)*

*4.6.0-rc5*

convert common user inputs into boolean values


Synopsis
========

.. c:function:: int kstrtobool( const char * s, bool * res )

Arguments
=========

``s``
    input string

``res``
    result


Description
===========

This routine returns 0 iff the first character is one of 'Yy1Nn0', or
[oO][NnFf] for “on” and “off”. Otherwise it will return -EINVAL. Value
pointed to by res is updated upon finding a match.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

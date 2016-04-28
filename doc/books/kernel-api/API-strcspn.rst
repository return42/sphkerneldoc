.. -*- coding: utf-8; mode: rst -*-

.. _API-strcspn:

=======
strcspn
=======

*man strcspn(9)*

*4.6.0-rc5*

Calculate the length of the initial substring of ``s`` which does not
contain letters in ``reject``


Synopsis
========

.. c:function:: size_t strcspn( const char * s, const char * reject )

Arguments
=========

``s``
    The string to be searched

``reject``
    The string to avoid


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

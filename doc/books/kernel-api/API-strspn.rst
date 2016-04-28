.. -*- coding: utf-8; mode: rst -*-

.. _API-strspn:

======
strspn
======

*man strspn(9)*

*4.6.0-rc5*

Calculate the length of the initial substring of ``s`` which only
contain letters in ``accept``


Synopsis
========

.. c:function:: size_t strspn( const char * s, const char * accept )

Arguments
=========

``s``
    The string to be searched

``accept``
    The string to search for


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-has-allocations:

==================
sk_has_allocations
==================

*man sk_has_allocations(9)*

*4.6.0-rc5*

check if allocations are outstanding


Synopsis
========

.. c:function:: bool sk_has_allocations( const struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

Returns true if socket has write or read allocations


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

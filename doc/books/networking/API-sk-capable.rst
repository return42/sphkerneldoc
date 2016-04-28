.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-capable:

==========
sk_capable
==========

*man sk_capable(9)*

*4.6.0-rc5*

Socket global capability test


Synopsis
========

.. c:function:: bool sk_capable( const struct sock * sk, int cap )

Arguments
=========

``sk``
    Socket to use a capability on or through

``cap``
    The global capability to use


Description
===========

Test to see if the opener of the socket had when the socket was created
and the current process has the capability ``cap`` in all user
namespaces.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

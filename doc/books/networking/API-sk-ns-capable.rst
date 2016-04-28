.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-ns-capable:

=============
sk_ns_capable
=============

*man sk_ns_capable(9)*

*4.6.0-rc5*

General socket capability test


Synopsis
========

.. c:function:: bool sk_ns_capable( const struct sock * sk, struct user_namespace * user_ns, int cap )

Arguments
=========

``sk``
    Socket to use a capability on or through

``user_ns``
    The user namespace of the capability to use

``cap``
    The capability to use


Description
===========

Test to see if the opener of the socket had when the socket was created
and the current process has the capability ``cap`` in the user namespace
``user_ns``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-net-capable:

==============
sk_net_capable
==============

*man sk_net_capable(9)*

*4.6.0-rc5*

Network namespace socket capability test


Synopsis
========

.. c:function:: bool sk_net_capable( const struct sock * sk, int cap )

Arguments
=========

``sk``
    Socket to use a capability on or through

``cap``
    The capability to use


Description
===========

Test to see if the opener of the socket had when the socket was created
and the current process has the capability ``cap`` over the network
namespace the socket is a member of.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

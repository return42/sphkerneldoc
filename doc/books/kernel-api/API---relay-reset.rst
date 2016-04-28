.. -*- coding: utf-8; mode: rst -*-

.. _API---relay-reset:

=============
__relay_reset
=============

*man __relay_reset(9)*

*4.6.0-rc5*

reset a channel buffer


Synopsis
========

.. c:function:: void __relay_reset( struct rchan_buf * buf, unsigned int init )

Arguments
=========

``buf``
    the channel buffer

``init``
    1 if this is a first-time initialization


Description
===========

See ``relay_reset`` for description of effect.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

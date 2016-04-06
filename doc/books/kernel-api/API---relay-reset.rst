
.. _API---relay-reset:

=============
__relay_reset
=============

*man __relay_reset(9)*

*4.6.0-rc1*

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

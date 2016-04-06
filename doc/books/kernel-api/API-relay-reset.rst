
.. _API-relay-reset:

===========
relay_reset
===========

*man relay_reset(9)*

*4.6.0-rc1*

reset the channel


Synopsis
========

.. c:function:: void relay_reset( struct rchan * chan )

Arguments
=========

``chan``
    the channel


Description
===========

This has the effect of erasing all data from all channel buffers and restarting the channel in its initial state. The buffers are not freed, so any mappings are still in effect.

NOTE. Care should be taken that the channel isn't actually being used by anything when this call is made.

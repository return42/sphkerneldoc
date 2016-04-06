
.. _API-relay-flush:

===========
relay_flush
===========

*man relay_flush(9)*

*4.6.0-rc1*

close the channel


Synopsis
========

.. c:function:: void relay_flush( struct rchan * chan )

Arguments
=========

``chan``
    the channel


Description
===========

Flushes all channel buffers, i.e. forces buffer switch.

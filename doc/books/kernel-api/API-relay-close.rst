
.. _API-relay-close:

===========
relay_close
===========

*man relay_close(9)*

*4.6.0-rc1*

close the channel


Synopsis
========

.. c:function:: void relay_close( struct rchan * chan )

Arguments
=========

``chan``
    the channel


Description
===========

Closes all channel buffers and frees the channel.

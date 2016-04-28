.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-close:

===========
relay_close
===========

*man relay_close(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

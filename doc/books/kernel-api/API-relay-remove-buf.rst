.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-remove-buf:

================
relay_remove_buf
================

*man relay_remove_buf(9)*

*4.6.0-rc5*

remove a channel buffer


Synopsis
========

.. c:function:: void relay_remove_buf( struct kref * kref )

Arguments
=========

``kref``
    target kernel reference that contains the relay buffer


Description
===========

Removes the file from the filesystem, which also frees the
rchan_buf_struct and the channel buffer. Should only be called from
``kref_put``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

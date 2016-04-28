.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-destroy-channel:

=====================
relay_destroy_channel
=====================

*man relay_destroy_channel(9)*

*4.6.0-rc5*

free the channel struct


Synopsis
========

.. c:function:: void relay_destroy_channel( struct kref * kref )

Arguments
=========

``kref``
    target kernel reference that contains the relay channel


Description
===========

Should only be called from ``kref_put``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


.. _API-relay-destroy-channel:

=====================
relay_destroy_channel
=====================

*man relay_destroy_channel(9)*

*4.6.0-rc1*

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

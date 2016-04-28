.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-use-client:

==============
i2c_use_client
==============

*man i2c_use_client(9)*

*4.6.0-rc5*

increments the reference count of the i2c client structure


Synopsis
========

.. c:function:: struct i2c_client * i2c_use_client( struct i2c_client * client )

Arguments
=========

``client``
    the client being referenced


Description
===========

Each live reference to a client should be refcounted. The driver model
does that automatically as part of driver binding, so that most drivers
don't


need to do this explicitly
==========================

they hold a reference until they're unbound from the device.

A pointer to the client with the incremented reference counter is
returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

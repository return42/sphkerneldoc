.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-release-client:

==================
i2c_release_client
==================

*man i2c_release_client(9)*

*4.6.0-rc5*

release a use of the i2c client structure


Synopsis
========

.. c:function:: void i2c_release_client( struct i2c_client * client )

Arguments
=========

``client``
    the client being no longer referenced


Description
===========

Must be called when a user of a client is finished with it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

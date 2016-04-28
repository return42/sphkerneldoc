.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-unregister-device:

=====================
i2c_unregister_device
=====================

*man i2c_unregister_device(9)*

*4.6.0-rc5*

reverse effect of ``i2c_new_device``


Synopsis
========

.. c:function:: void i2c_unregister_device( struct i2c_client * client )

Arguments
=========

``client``
    value returned from ``i2c_new_device``


Context
=======

can sleep


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

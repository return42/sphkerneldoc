.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-check-quirks:

================
i2c_check_quirks
================

*man i2c_check_quirks(9)*

*4.6.0-rc5*

Function for checking the quirk flags in an i2c adapter


Synopsis
========

.. c:function:: bool i2c_check_quirks( struct i2c_adapter * adap, u64 quirks )

Arguments
=========

``adap``
    i2c adapter

``quirks``
    quirk flags


Return
======

true if the adapter has all the specified quirk flags, false if not


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

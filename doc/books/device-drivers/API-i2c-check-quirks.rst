
.. _API-i2c-check-quirks:

================
i2c_check_quirks
================

*man i2c_check_quirks(9)*

*4.6.0-rc1*

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

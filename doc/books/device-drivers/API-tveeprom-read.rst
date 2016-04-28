.. -*- coding: utf-8; mode: rst -*-

.. _API-tveeprom-read:

=============
tveeprom_read
=============

*man tveeprom_read(9)*

*4.6.0-rc5*

Reads the contents of the eeprom found at the Hauppauge devices.


Synopsis
========

.. c:function:: int tveeprom_read( struct i2c_client * c, unsigned char * eedata, int len )

Arguments
=========

``c``
    I2C client struct

``eedata``
    Array where the eeprom content will be stored.

``len``
    Size of ``eedata`` array. If the eeprom content will be latter be
    parsed by ``tveeprom_hauppauge_analog``, len should be, at least,
    256.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

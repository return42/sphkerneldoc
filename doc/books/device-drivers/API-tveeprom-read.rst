
.. _API-tveeprom-read:

=============
tveeprom_read
=============

*man tveeprom_read(9)*

*4.6.0-rc1*

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
    Size of ``eedata`` array. If the eeprom content will be latter be parsed by ``tveeprom_hauppauge_analog``, len should be, at least, 256.

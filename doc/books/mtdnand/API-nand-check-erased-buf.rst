
.. _API-nand-check-erased-buf:

=====================
nand_check_erased_buf
=====================

*man nand_check_erased_buf(9)*

*4.6.0-rc1*

check if a buffer contains (almost) only 0xff data


Synopsis
========

.. c:function:: int nand_check_erased_buf( void * buf, int len, int bitflips_threshold )

Arguments
=========

``buf``
    buffer to test

``len``
    buffer length

``bitflips_threshold``
    maximum number of bitflips


Description
===========

Check if a buffer contains only 0xff, which means the underlying region has been erased and is ready to be programmed. The bitflips_threshold specify the maximum number of
bitflips before considering the region is not erased.


Note
====

The logic of this function has been extracted from the memweight implementation, except that nand_check_erased_buf function exit before testing the whole buffer if the number of
bitflips exceed the bitflips_threshold value.

Returns a positive number of bitflips less than or equal to bitflips_threshold, or -ERROR_CODE for bitflips in excess of the threshold.

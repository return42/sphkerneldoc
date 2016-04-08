
.. _API-z8530-describe:

==============
z8530_describe
==============

*man z8530_describe(9)*

*4.6.0-rc1*

Uniformly describe a Z8530 port


Synopsis
========

.. c:function:: void z8530_describe( struct z8530_dev * dev, char * mapping, unsigned long io )

Arguments
=========

``dev``
    Z8530 device to describe

``mapping``
    string holding mapping type (eg “I/O” or “Mem”)

``io``
    the port value in question


Description
===========

Describe a Z8530 in a standard format. We must pass the I/O as the port offset isn't predictable. The main reason for this function is to try and get a common format of report.

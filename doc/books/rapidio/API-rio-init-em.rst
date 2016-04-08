
.. _API-rio-init-em:

===========
rio_init_em
===========

*man rio_init_em(9)*

*4.6.0-rc1*

Initializes RIO Error Management (for switches)


Synopsis
========

.. c:function:: void rio_init_em( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

For each enumerated switch, call device-specific error management initialization routine (if supplied by the switch driver).

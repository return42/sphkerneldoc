
.. _API-ata-id-xfermask:

===============
ata_id_xfermask
===============

*man ata_id_xfermask(9)*

*4.6.0-rc1*

Compute xfermask from the given IDENTIFY data


Synopsis
========

.. c:function:: unsigned long ata_id_xfermask( const u16 * id )

Arguments
=========

``id``
    IDENTIFY data to compute xfer mask from


Description
===========

Compute the xfermask for this device. This is not as trivial as it seems if we must consider early devices correctly.


FIXME
=====

pre IDE drive timing (do we care ?).


LOCKING
=======

None.


RETURNS
=======

Computed xfermask

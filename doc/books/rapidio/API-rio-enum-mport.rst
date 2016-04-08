
.. _API-rio-enum-mport:

==============
rio_enum_mport
==============

*man rio_enum_mport(9)*

*4.6.0-rc1*

Start enumeration through a master port


Synopsis
========

.. c:function:: int rio_enum_mport( struct rio_mport * mport, u32 flags )

Arguments
=========

``mport``
    Master port to send transactions

``flags``
    Enumeration control flags


Description
===========

Starts the enumeration process. If somebody has enumerated our master port device, then give up. If not and we have an active link, then start recursive peer enumeration. Returns
``0`` if enumeration succeeds or ``-EBUSY`` if enumeration fails.

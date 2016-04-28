.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-enum-mport:

==============
rio_enum_mport
==============

*man rio_enum_mport(9)*

*4.6.0-rc5*

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

Starts the enumeration process. If somebody has enumerated our master
port device, then give up. If not and we have an active link, then start
recursive peer enumeration. Returns ``0`` if enumeration succeeds or
``-EBUSY`` if enumeration fails.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

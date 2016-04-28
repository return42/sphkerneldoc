.. -*- coding: utf-8; mode: rst -*-

.. _API-fsl-rio-config-write:

====================
fsl_rio_config_write
====================

*man fsl_rio_config_write(9)*

*4.6.0-rc5*

Generate a MPC85xx write maintenance transaction


Synopsis
========

.. c:function:: int fsl_rio_config_write( struct rio_mport * mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 val )

Arguments
=========

``mport``
    RapidIO master port info

``index``
    ID of RapdiIO interface

``destid``
    Destination ID of transaction

``hopcount``
    Number of hops to target device

``offset``
    Offset into configuration space

``len``
    Length (in bytes) of the maintenance transaction

``val``
    Value to be written


Description
===========

Generates an MPC85xx write maintenance transaction. Returns ``0`` on
success or ``-EINVAL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

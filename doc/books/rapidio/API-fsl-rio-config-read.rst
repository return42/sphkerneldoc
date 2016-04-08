
.. _API-fsl-rio-config-read:

===================
fsl_rio_config_read
===================

*man fsl_rio_config_read(9)*

*4.6.0-rc1*

Generate a MPC85xx read maintenance transaction


Synopsis
========

.. c:function:: int fsl_rio_config_read( struct rio_mport * mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 * val )

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
    Location to be read into


Description
===========

Generates a MPC85xx read maintenance transaction. Returns ``0`` on success or ``-EINVAL`` on failure.

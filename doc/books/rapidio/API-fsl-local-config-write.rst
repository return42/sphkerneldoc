
.. _API-fsl-local-config-write:

======================
fsl_local_config_write
======================

*man fsl_local_config_write(9)*

*4.6.0-rc1*

Generate a MPC85xx local config space write


Synopsis
========

.. c:function:: int fsl_local_config_write( struct rio_mport * mport, int index, u32 offset, int len, u32 data )

Arguments
=========

``mport``
    RapidIO master port info

``index``
    ID of RapdiIO interface

``offset``
    Offset into configuration space

``len``
    Length (in bytes) of the maintenance transaction

``data``
    Value to be written


Description
===========

Generates a MPC85xx local configuration space write. Returns ``0`` on success or ``-EINVAL`` on failure.

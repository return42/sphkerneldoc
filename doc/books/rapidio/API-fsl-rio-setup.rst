
.. _API-fsl-rio-setup:

=============
fsl_rio_setup
=============

*man fsl_rio_setup(9)*

*4.6.0-rc1*

Setup Freescale PowerPC RapidIO interface


Synopsis
========

.. c:function:: int fsl_rio_setup( struct platform_device * dev )

Arguments
=========

``dev``
    platform_device pointer


Description
===========

Initializes MPC85xx RapidIO hardware interface, configures master port with system-specific info, and registers the master port with the RapidIO subsystem.

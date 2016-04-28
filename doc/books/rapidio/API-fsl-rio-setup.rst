.. -*- coding: utf-8; mode: rst -*-

.. _API-fsl-rio-setup:

=============
fsl_rio_setup
=============

*man fsl_rio_setup(9)*

*4.6.0-rc5*

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

Initializes MPC85xx RapidIO hardware interface, configures master port
with system-specific info, and registers the master port with the
RapidIO subsystem.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-display-xfer-agreement:

==========================
spi_display_xfer_agreement
==========================

*man spi_display_xfer_agreement(9)*

*4.6.0-rc5*

Print the current target transfer agreement


Synopsis
========

.. c:function:: void spi_display_xfer_agreement( struct scsi_target * starget )

Arguments
=========

``starget``
    The target for which to display the agreement


Description
===========

Each SPI port is required to maintain a transfer agreement for each
other port on the bus. This function prints a one-line summary of the
current agreement; more detailed information is available in sysfs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

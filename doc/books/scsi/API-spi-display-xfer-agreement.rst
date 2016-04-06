
.. _API-spi-display-xfer-agreement:

==========================
spi_display_xfer_agreement
==========================

*man spi_display_xfer_agreement(9)*

*4.6.0-rc1*

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

Each SPI port is required to maintain a transfer agreement for each other port on the bus. This function prints a one-line summary of the current agreement; more detailed
information is available in sysfs.

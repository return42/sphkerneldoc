.. -*- coding: utf-8; mode: rst -*-

====================
scsi_transport_spi.c
====================

.. _`spi_schedule_dv_device`:

spi_schedule_dv_device
======================

.. c:function:: void spi_schedule_dv_device (struct scsi_device *sdev)

    schedule domain validation to occur on the device

    :param struct scsi_device \*sdev:
        The device to validate


.. _`spi_schedule_dv_device.description`:

Description
-----------

Identical to :c:func:`spi_dv_device` above, except that the DV will be
scheduled to occur in a workqueue later.  All memory allocations
are atomic, so may be called from any context including those holding
SCSI locks.


.. _`spi_display_xfer_agreement`:

spi_display_xfer_agreement
==========================

.. c:function:: void spi_display_xfer_agreement (struct scsi_target *starget)

    Print the current target transfer agreement

    :param struct scsi_target \*starget:
        The target for which to display the agreement


.. _`spi_display_xfer_agreement.description`:

Description
-----------

Each SPI port is required to maintain a transfer agreement for each
other port on the bus.  This function prints a one-line summary of
the current agreement; more detailed information is available in sysfs.


.. _`spi_populate_tag_msg`:

spi_populate_tag_msg
====================

.. c:function:: int spi_populate_tag_msg (unsigned char *msg, struct scsi_cmnd *cmd)

    place a tag message in a buffer

    :param unsigned char \*msg:
        pointer to the area to place the tag

    :param struct scsi_cmnd \*cmd:
        pointer to the scsi command for the tag


.. _`spi_populate_tag_msg.description`:

Description
-----------

Notes::

        designed to create the correct type of tag message for the 
        particular request.  Returns the size of the tag message.
        May return 0 if TCQ is disabled for this device.


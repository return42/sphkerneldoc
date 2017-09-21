.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/g_NCR5380.c

.. _`g_ncr5380_probe_irq`:

g_NCR5380_probe_irq
===================

.. c:function:: int g_NCR5380_probe_irq(struct Scsi_Host *instance)

    find the IRQ of a NCR5380 or equivalent

    :param struct Scsi_Host \*instance:
        SCSI host instance

.. _`g_ncr5380_probe_irq.description`:

Description
-----------

Autoprobe for the IRQ line used by the card by triggering an IRQ
and then looking to see what interrupt actually turned up.

.. _`generic_ncr5380_precv`:

generic_NCR5380_precv
=====================

.. c:function:: int generic_NCR5380_precv(struct NCR5380_hostdata *hostdata, unsigned char *dst, int len)

    pseudo DMA receive

    :param struct NCR5380_hostdata \*hostdata:
        scsi host private data

    :param unsigned char \*dst:
        buffer to write into

    :param int len:
        transfer size

.. _`generic_ncr5380_precv.description`:

Description
-----------

Perform a pseudo DMA mode receive from a 53C400 or equivalent device.

.. _`generic_ncr5380_psend`:

generic_NCR5380_psend
=====================

.. c:function:: int generic_NCR5380_psend(struct NCR5380_hostdata *hostdata, unsigned char *src, int len)

    pseudo DMA send

    :param struct NCR5380_hostdata \*hostdata:
        scsi host private data

    :param unsigned char \*src:
        buffer to read from

    :param int len:
        transfer size

.. _`generic_ncr5380_psend.description`:

Description
-----------

Perform a pseudo DMA mode send to a 53C400 or equivalent device.

.. This file was automatic generated / don't edit.


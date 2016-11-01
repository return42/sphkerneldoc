.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/g_NCR5380.c

.. _`generic_ncr5380_pread`:

generic_NCR5380_pread
=====================

.. c:function:: int generic_NCR5380_pread(struct Scsi_Host *instance, unsigned char *dst, int len)

    pseudo DMA read

    :param struct Scsi_Host \*instance:
        adapter to read from

    :param unsigned char \*dst:
        buffer to read into

    :param int len:
        buffer length

.. _`generic_ncr5380_pread.description`:

Description
-----------

Perform a pseudo DMA mode read from an NCR53C400 or equivalent
controller

.. _`generic_ncr5380_pwrite`:

generic_NCR5380_pwrite
======================

.. c:function:: int generic_NCR5380_pwrite(struct Scsi_Host *instance, unsigned char *src, int len)

    pseudo DMA write

    :param struct Scsi_Host \*instance:
        adapter to read from

    :param unsigned char \*src:
        *undescribed*

    :param int len:
        buffer length

.. _`generic_ncr5380_pwrite.description`:

Description
-----------

Perform a pseudo DMA mode read from an NCR53C400 or equivalent
controller

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/g_NCR5380.c

.. _`internal_setup`:

internal_setup
==============

.. c:function:: void internal_setup(int board, char *str, int *ints)

    handle lilo command string override

    :param int board:
        BOARD\_\* identifier for the board

    :param char \*str:
        unused

    :param int \*ints:
        numeric parameters

.. _`internal_setup.description`:

Description
-----------

Do LILO command line initialization of the overrides array. Display
errors when needed

.. _`internal_setup.locks`:

Locks
-----

none

.. _`do_ncr5380_setup`:

do_NCR5380_setup
================

.. c:function:: int do_NCR5380_setup(char *str)

    set up entry point

    :param char \*str:
        unused

.. _`do_ncr5380_setup.description`:

Description
-----------

Setup function invoked at boot to parse the ncr5380= command
line.

.. _`do_ncr53c400_setup`:

do_NCR53C400_setup
==================

.. c:function:: int do_NCR53C400_setup(char *str)

    set up entry point

    :param char \*str:
        unused

.. _`do_ncr53c400_setup.description`:

Description
-----------

Setup function invoked at boot to parse the ncr53c400= command
line.

.. _`do_ncr53c400a_setup`:

do_NCR53C400A_setup
===================

.. c:function:: int do_NCR53C400A_setup(char *str)

    set up entry point

    :param char \*str:
        unused

.. _`do_ncr53c400a_setup.description`:

Description
-----------

Setup function invoked at boot to parse the ncr53c400a= command
line.

.. _`do_dtc3181e_setup`:

do_DTC3181E_setup
=================

.. c:function:: int do_DTC3181E_setup(char *str)

    set up entry point

    :param char \*str:
        unused

.. _`do_dtc3181e_setup.description`:

Description
-----------

Setup function invoked at boot to parse the dtc3181e= command
line.

.. _`generic_ncr5380_detect`:

generic_NCR5380_detect
======================

.. c:function:: int generic_NCR5380_detect(struct scsi_host_template *tpnt)

    look for NCR5380 controllers

    :param struct scsi_host_template \*tpnt:
        the scsi template

.. _`generic_ncr5380_detect.description`:

Description
-----------

Scan for the present of NCR5380, NCR53C400, NCR53C400A, DTC3181E
and DTC436(ISAPnP) controllers. If overrides have been set we use
them.

.. _`generic_ncr5380_detect.locks`:

Locks
-----

none

.. _`generic_ncr5380_release_resources`:

generic_NCR5380_release_resources
=================================

.. c:function:: int generic_NCR5380_release_resources(struct Scsi_Host *instance)

    free resources

    :param struct Scsi_Host \*instance:
        host adapter to clean up

.. _`generic_ncr5380_release_resources.description`:

Description
-----------

Free the generic interface resources from this adapter.

.. _`generic_ncr5380_release_resources.locks`:

Locks
-----

none

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


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fnic/fnic_scsi.c

.. _`__fnic_set_state_flags`:

\__fnic_set_state_flags
=======================

.. c:function:: void __fnic_set_state_flags(struct fnic *fnic, unsigned long st_flags, unsigned long clearbits)

    Sets/Clears bits in fnic's state_flags

    :param fnic:
        *undescribed*
    :type fnic: struct fnic \*

    :param st_flags:
        *undescribed*
    :type st_flags: unsigned long

    :param clearbits:
        *undescribed*
    :type clearbits: unsigned long

.. _`fnic_scsi_host_start_tag`:

fnic_scsi_host_start_tag
========================

.. c:function:: int fnic_scsi_host_start_tag(struct fnic *fnic, struct scsi_cmnd *sc)

    Allocates tagid from host's tag list

    :param fnic:
        *undescribed*
    :type fnic: struct fnic \*

    :param sc:
        *undescribed*
    :type sc: struct scsi_cmnd \*

.. _`fnic_scsi_host_end_tag`:

fnic_scsi_host_end_tag
======================

.. c:function:: void fnic_scsi_host_end_tag(struct fnic *fnic, struct scsi_cmnd *sc)

    frees tag allocated by fnic_scsi_host_start_tag.

    :param fnic:
        *undescribed*
    :type fnic: struct fnic \*

    :param sc:
        *undescribed*
    :type sc: struct scsi_cmnd \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fnic/fnic_scsi.c

.. _`__fnic_set_state_flags`:

\__fnic_set_state_flags
=======================

.. c:function:: void __fnic_set_state_flags(struct fnic *fnic, unsigned long st_flags, unsigned long clearbits)

    Sets/Clears bits in fnic's state_flags

    :param struct fnic \*fnic:
        *undescribed*

    :param unsigned long st_flags:
        *undescribed*

    :param unsigned long clearbits:
        *undescribed*

.. _`fnic_scsi_host_start_tag`:

fnic_scsi_host_start_tag
========================

.. c:function:: int fnic_scsi_host_start_tag(struct fnic *fnic, struct scsi_cmnd *sc)

    Allocates tagid from host's tag list

    :param struct fnic \*fnic:
        *undescribed*

    :param struct scsi_cmnd \*sc:
        *undescribed*

.. _`fnic_scsi_host_end_tag`:

fnic_scsi_host_end_tag
======================

.. c:function:: void fnic_scsi_host_end_tag(struct fnic *fnic, struct scsi_cmnd *sc)

    frees tag allocated by fnic_scsi_host_start_tag.

    :param struct fnic \*fnic:
        *undescribed*

    :param struct scsi_cmnd \*sc:
        *undescribed*

.. This file was automatic generated / don't edit.


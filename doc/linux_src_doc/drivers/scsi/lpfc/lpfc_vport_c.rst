.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_vport.c

.. _`lpfc_discovery_wait`:

lpfc_discovery_wait
===================

.. c:function:: void lpfc_discovery_wait(struct lpfc_vport *vport)

    Wait for driver discovery to quiesce

    :param struct lpfc_vport \*vport:
        The virtual port for which this call is being executed.

.. _`lpfc_discovery_wait.description`:

Description
-----------

This driver calls this routine specifically from lpfc_vport_delete
to enforce a synchronous execution of vport
delete relative to discovery activities.  The
lpfc_vport_delete routine should not return until it
can reasonably guarantee that discovery has quiesced.
Post FDISC LOGO, the driver must wait until its SAN teardown is
complete and all resources recovered before allowing
cleanup.

This routine does not require any locks held.

.. _`lpfc_vport_reset_stat_data`:

lpfc_vport_reset_stat_data
==========================

.. c:function:: void lpfc_vport_reset_stat_data(struct lpfc_vport *vport)

    Reset the statistical data for the vport

    :param struct lpfc_vport \*vport:
        Pointer to vport object.

.. _`lpfc_vport_reset_stat_data.description`:

Description
-----------

This function resets the statistical data for the vport. This function
is called with the host_lock held

.. _`lpfc_alloc_bucket`:

lpfc_alloc_bucket
=================

.. c:function:: void lpfc_alloc_bucket(struct lpfc_vport *vport)

    Allocate data buffer required for statistical data

    :param struct lpfc_vport \*vport:
        Pointer to vport object.

.. _`lpfc_alloc_bucket.description`:

Description
-----------

This function allocates data buffer required for all the FC
nodes of the vport to collect statistical data.

.. _`lpfc_free_bucket`:

lpfc_free_bucket
================

.. c:function:: void lpfc_free_bucket(struct lpfc_vport *vport)

    Free data buffer required for statistical data

    :param struct lpfc_vport \*vport:
        Pointer to vport object.

.. _`lpfc_free_bucket.description`:

Description
-----------

Th function frees statistical data buffer of all the FC
nodes of the vport.

.. This file was automatic generated / don't edit.


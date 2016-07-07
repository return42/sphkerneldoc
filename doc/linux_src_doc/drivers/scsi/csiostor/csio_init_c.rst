.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_init.c

.. _`csio_shost_init`:

csio_shost_init
===============

.. c:function:: struct csio_lnode *csio_shost_init(struct csio_hw *hw, struct device *dev, bool probe, struct csio_lnode *pln)

    Create and initialize the lnode module.

    :param struct csio_hw \*hw:
        The HW module.

    :param struct device \*dev:
        The device associated with this invocation.

    :param bool probe:
        Called from probe context or not?

    :param struct csio_lnode \*pln:
        *undescribed*

.. _`csio_shost_init.description`:

Description
-----------

Allocates lnode structure via scsi_host_alloc, initializes
shost, initializes lnode module and registers with SCSI ML
via scsi_host_add. This function is shared between physical and
virtual node ports.

.. _`csio_shost_exit`:

csio_shost_exit
===============

.. c:function:: void csio_shost_exit(struct csio_lnode *ln)

    De-instantiate the shost.

    :param struct csio_lnode \*ln:
        The lnode module corresponding to the shost.

.. This file was automatic generated / don't edit.


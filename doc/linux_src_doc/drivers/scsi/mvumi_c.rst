.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mvumi.c

.. _`mvumi_make_sgl`:

mvumi_make_sgl
==============

.. c:function:: int mvumi_make_sgl(struct mvumi_hba *mhba, struct scsi_cmnd *scmd, void *sgl_p, unsigned char *sg_count)

    Prepares  SGL

    :param struct mvumi_hba \*mhba:
        Adapter soft state

    :param struct scsi_cmnd \*scmd:
        SCSI command from the mid-layer

    :param void \*sgl_p:
        SGL to be filled in
        \ ``sg_count``\             return the number of SG elements

    :param unsigned char \*sg_count:
        *undescribed*

.. _`mvumi_make_sgl.description`:

Description
-----------

If successful, this function returns 0. otherwise, it returns -1.

.. _`mvumi_get_cmd`:

mvumi_get_cmd
=============

.. c:function:: struct mvumi_cmd *mvumi_get_cmd(struct mvumi_hba *mhba)

    Get a command from the free pool

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_get_cmd.description`:

Description
-----------

Returns a free command from the pool

.. _`mvumi_return_cmd`:

mvumi_return_cmd
================

.. c:function:: void mvumi_return_cmd(struct mvumi_hba *mhba, struct mvumi_cmd *cmd)

    Return a cmd to free command pool

    :param struct mvumi_hba \*mhba:
        Adapter soft state

    :param struct mvumi_cmd \*cmd:
        Command packet to be returned to free command pool

.. _`mvumi_free_cmds`:

mvumi_free_cmds
===============

.. c:function:: void mvumi_free_cmds(struct mvumi_hba *mhba)

    Free all the cmds in the free cmd pool

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_alloc_cmds`:

mvumi_alloc_cmds
================

.. c:function:: int mvumi_alloc_cmds(struct mvumi_hba *mhba)

    Allocates the command packets

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_init_data`:

mvumi_init_data
===============

.. c:function:: int mvumi_init_data(struct mvumi_hba *mhba)

    Initialize requested date for FW

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_handshake`:

mvumi_handshake
===============

.. c:function:: int mvumi_handshake(struct mvumi_hba *mhba)

    Move the FW to READY state

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_handshake.description`:

Description
-----------

During the initialization, FW passes can potentially be in any one of
several possible states. If the FW in operational, waiting-for-handshake
states, driver must take steps to bring it to ready state. Otherwise, it
has to wait for the ready state.

.. _`mvumi_complete_cmd`:

mvumi_complete_cmd
==================

.. c:function:: void mvumi_complete_cmd(struct mvumi_hba *mhba, struct mvumi_cmd *cmd, struct mvumi_rsp_frame *ob_frame)

    Completes a command

    :param struct mvumi_hba \*mhba:
        Adapter soft state

    :param struct mvumi_cmd \*cmd:
        Command to be completed

    :param struct mvumi_rsp_frame \*ob_frame:
        *undescribed*

.. _`mvumi_enable_intr`:

mvumi_enable_intr
=================

.. c:function:: void mvumi_enable_intr(struct mvumi_hba *mhba)

    Enables interrupts

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_disable_intr`:

mvumi_disable_intr
==================

.. c:function:: void mvumi_disable_intr(struct mvumi_hba *mhba)

    Disables interrupt

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_read_fw_status_reg`:

mvumi_read_fw_status_reg
========================

.. c:function:: unsigned int mvumi_read_fw_status_reg(struct mvumi_hba *mhba)

    returns the current FW status value

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_build_frame`:

mvumi_build_frame
=================

.. c:function:: unsigned char mvumi_build_frame(struct mvumi_hba *mhba, struct scsi_cmnd *scmd, struct mvumi_cmd *cmd)

    Prepares a direct cdb (DCDB) command

    :param struct mvumi_hba \*mhba:
        Adapter soft state

    :param struct scsi_cmnd \*scmd:
        SCSI command

    :param struct mvumi_cmd \*cmd:
        Command to be prepared in

.. _`mvumi_build_frame.description`:

Description
-----------

This function prepares CDB commands. These are typcially pass-through
commands to the devices.

.. _`mvumi_queue_command`:

mvumi_queue_command
===================

.. c:function:: int mvumi_queue_command(struct Scsi_Host *shost, struct scsi_cmnd *scmd)

    Queue entry point

    :param struct Scsi_Host \*shost:
        *undescribed*

    :param struct scsi_cmnd \*scmd:
        SCSI command to be queued

.. _`mvumi_init_fw`:

mvumi_init_fw
=============

.. c:function:: int mvumi_init_fw(struct mvumi_hba *mhba)

    Initializes the FW

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_init_fw.description`:

Description
-----------

This is the main function for initializing firmware.

.. _`mvumi_io_attach`:

mvumi_io_attach
===============

.. c:function:: int mvumi_io_attach(struct mvumi_hba *mhba)

    Attaches this driver to SCSI mid-layer

    :param struct mvumi_hba \*mhba:
        Adapter soft state

.. _`mvumi_probe_one`:

mvumi_probe_one
===============

.. c:function:: int mvumi_probe_one(struct pci_dev *pdev, const struct pci_device_id *id)

    PCI hotplug entry point

    :param struct pci_dev \*pdev:
        PCI device structure

    :param const struct pci_device_id \*id:
        PCI ids of supported hotplugged adapter

.. _`mvumi_shutdown`:

mvumi_shutdown
==============

.. c:function:: void mvumi_shutdown(struct pci_dev *pdev)

    Shutdown entry point

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`mvumi_init`:

mvumi_init
==========

.. c:function:: int mvumi_init( void)

    Driver load entry point

    :param  void:
        no arguments

.. _`mvumi_exit`:

mvumi_exit
==========

.. c:function:: void __exit mvumi_exit( void)

    Driver unload entry point

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


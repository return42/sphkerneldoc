.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/myrb.c

.. _`myrb_create_mempools`:

myrb_create_mempools
====================

.. c:function:: bool myrb_create_mempools(struct pci_dev *pdev, struct myrb_hba *cb)

    allocates auxiliary data structures

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_create_mempools.return`:

Return
------

true on success, false otherwise.

.. _`myrb_destroy_mempools`:

myrb_destroy_mempools
=====================

.. c:function:: void myrb_destroy_mempools(struct myrb_hba *cb)

    tears down the memory pools for the controller

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_reset_cmd`:

myrb_reset_cmd
==============

.. c:function:: void myrb_reset_cmd(struct myrb_cmdblk *cmd_blk)

    reset command block

    :param cmd_blk:
        *undescribed*
    :type cmd_blk: struct myrb_cmdblk \*

.. _`myrb_qcmd`:

myrb_qcmd
=========

.. c:function:: void myrb_qcmd(struct myrb_hba *cb, struct myrb_cmdblk *cmd_blk)

    queues command block for execution

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param cmd_blk:
        *undescribed*
    :type cmd_blk: struct myrb_cmdblk \*

.. _`myrb_exec_cmd`:

myrb_exec_cmd
=============

.. c:function:: unsigned short myrb_exec_cmd(struct myrb_hba *cb, struct myrb_cmdblk *cmd_blk)

    executes command block and waits for completion.

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param cmd_blk:
        *undescribed*
    :type cmd_blk: struct myrb_cmdblk \*

.. _`myrb_exec_cmd.return`:

Return
------

command status

.. _`myrb_exec_type3`:

myrb_exec_type3
===============

.. c:function:: unsigned short myrb_exec_type3(struct myrb_hba *cb, enum myrb_cmd_opcode op, dma_addr_t addr)

    executes a type 3 command and waits for completion.

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param op:
        *undescribed*
    :type op: enum myrb_cmd_opcode

    :param addr:
        *undescribed*
    :type addr: dma_addr_t

.. _`myrb_exec_type3.return`:

Return
------

command status

.. _`myrb_exec_type3d`:

myrb_exec_type3D
================

.. c:function:: unsigned short myrb_exec_type3D(struct myrb_hba *cb, enum myrb_cmd_opcode op, struct scsi_device *sdev, struct myrb_pdev_state *pdev_info)

    executes a type 3D command and waits for completion.

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param op:
        *undescribed*
    :type op: enum myrb_cmd_opcode

    :param sdev:
        *undescribed*
    :type sdev: struct scsi_device \*

    :param pdev_info:
        *undescribed*
    :type pdev_info: struct myrb_pdev_state \*

.. _`myrb_exec_type3d.return`:

Return
------

command status

.. _`myrb_get_event`:

myrb_get_event
==============

.. c:function:: void myrb_get_event(struct myrb_hba *cb, unsigned int event)

    get event log from HBA

    :param cb:
        pointer to the hba structure
    :type cb: struct myrb_hba \*

    :param event:
        number of the event
    :type event: unsigned int

.. _`myrb_get_event.description`:

Description
-----------

Execute a type 3E command and logs the event message

.. _`myrb_get_errtable`:

myrb_get_errtable
=================

.. c:function:: void myrb_get_errtable(struct myrb_hba *cb)

    retrieves the error table from the controller

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_get_errtable.description`:

Description
-----------

Executes a type 3 command and logs the error table from the controller.

.. _`myrb_get_ldev_info`:

myrb_get_ldev_info
==================

.. c:function:: unsigned short myrb_get_ldev_info(struct myrb_hba *cb)

    retrieves the logical device table from the controller

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_get_ldev_info.description`:

Description
-----------

Executes a type 3 command and updates the logical device table.

.. _`myrb_get_ldev_info.return`:

Return
------

command status

.. _`myrb_get_rbld_progress`:

myrb_get_rbld_progress
======================

.. c:function:: unsigned short myrb_get_rbld_progress(struct myrb_hba *cb, struct myrb_rbld_progress *rbld)

    get rebuild progress information

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param rbld:
        *undescribed*
    :type rbld: struct myrb_rbld_progress \*

.. _`myrb_get_rbld_progress.description`:

Description
-----------

Executes a type 3 command and returns the rebuild progress
information.

.. _`myrb_get_rbld_progress.return`:

Return
------

command status

.. _`myrb_update_rbld_progress`:

myrb_update_rbld_progress
=========================

.. c:function:: void myrb_update_rbld_progress(struct myrb_hba *cb)

    updates the rebuild status

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_update_rbld_progress.description`:

Description
-----------

Updates the rebuild status for the attached logical devices.

.. _`myrb_get_cc_progress`:

myrb_get_cc_progress
====================

.. c:function:: void myrb_get_cc_progress(struct myrb_hba *cb)

    retrieve the rebuild status

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_get_cc_progress.description`:

Description
-----------

Execute a type 3 Command and fetch the rebuild / consistency check
status.

.. _`myrb_bgi_control`:

myrb_bgi_control
================

.. c:function:: void myrb_bgi_control(struct myrb_hba *cb)

    updates background initialisation status

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_bgi_control.description`:

Description
-----------

Executes a type 3B command and updates the background initialisation status

.. _`myrb_hba_enquiry`:

myrb_hba_enquiry
================

.. c:function:: unsigned short myrb_hba_enquiry(struct myrb_hba *cb)

    updates the controller status

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_hba_enquiry.description`:

Description
-----------

Executes a DAC_V1_Enquiry command and updates the controller status.

.. _`myrb_hba_enquiry.return`:

Return
------

command status

.. _`myrb_set_pdev_state`:

myrb_set_pdev_state
===================

.. c:function:: unsigned short myrb_set_pdev_state(struct myrb_hba *cb, struct scsi_device *sdev, enum myrb_devstate state)

    sets the device state for a physical device

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param sdev:
        *undescribed*
    :type sdev: struct scsi_device \*

    :param state:
        *undescribed*
    :type state: enum myrb_devstate

.. _`myrb_set_pdev_state.return`:

Return
------

command status

.. _`myrb_enable_mmio`:

myrb_enable_mmio
================

.. c:function:: bool myrb_enable_mmio(struct myrb_hba *cb, mbox_mmio_init_t mmio_init_fn)

    enables the Memory Mailbox Interface

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param mmio_init_fn:
        *undescribed*
    :type mmio_init_fn: mbox_mmio_init_t

.. _`myrb_enable_mmio.description`:

Description
-----------

PD and P controller types have no memory mailbox, but still need the
other dma mapped memory.

.. _`myrb_enable_mmio.return`:

Return
------

true on success, false otherwise.

.. _`myrb_get_hba_config`:

myrb_get_hba_config
===================

.. c:function:: int myrb_get_hba_config(struct myrb_hba *cb)

    reads the configuration information

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_get_hba_config.description`:

Description
-----------

Reads the configuration information from the controller and
initializes the controller structure.

.. _`myrb_get_hba_config.return`:

Return
------

0 on success, errno otherwise

.. _`myrb_unmap`:

myrb_unmap
==========

.. c:function:: void myrb_unmap(struct myrb_hba *cb)

    unmaps controller structures

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_cleanup`:

myrb_cleanup
============

.. c:function:: void myrb_cleanup(struct myrb_hba *cb)

    cleanup controller structures

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

.. _`myrb_is_raid`:

myrb_is_raid
============

.. c:function:: int myrb_is_raid(struct device *dev)

    return boolean indicating device is raid volume \ ``dev``\  the device struct object

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`myrb_get_resync`:

myrb_get_resync
===============

.. c:function:: void myrb_get_resync(struct device *dev)

    get raid volume resync percent complete \ ``dev``\  the device struct object

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`myrb_get_state`:

myrb_get_state
==============

.. c:function:: void myrb_get_state(struct device *dev)

    get raid volume status \ ``dev``\  the device struct object

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`myrb_err_status`:

myrb_err_status
===============

.. c:function:: bool myrb_err_status(struct myrb_hba *cb, unsigned char error, unsigned char parm0, unsigned char parm1)

    reports controller BIOS messages

    :param cb:
        *undescribed*
    :type cb: struct myrb_hba \*

    :param error:
        *undescribed*
    :type error: unsigned char

    :param parm0:
        *undescribed*
    :type parm0: unsigned char

    :param parm1:
        *undescribed*
    :type parm1: unsigned char

.. _`myrb_err_status.description`:

Description
-----------

Controller BIOS messages are passed through the Error Status Register
when the driver performs the BIOS handshaking.

.. _`myrb_err_status.return`:

Return
------

true for fatal errors and false otherwise.

.. This file was automatic generated / don't edit.


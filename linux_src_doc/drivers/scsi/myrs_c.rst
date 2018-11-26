.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/myrs.c

.. _`myrs_reset_cmd`:

myrs_reset_cmd
==============

.. c:function:: void myrs_reset_cmd(struct myrs_cmdblk *cmd_blk)

    clears critical fields in struct myrs_cmdblk

    :param cmd_blk:
        *undescribed*
    :type cmd_blk: struct myrs_cmdblk \*

.. _`myrs_qcmd`:

myrs_qcmd
=========

.. c:function:: void myrs_qcmd(struct myrs_hba *cs, struct myrs_cmdblk *cmd_blk)

    queues Command for DAC960 V2 Series Controllers.

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param cmd_blk:
        *undescribed*
    :type cmd_blk: struct myrs_cmdblk \*

.. _`myrs_exec_cmd`:

myrs_exec_cmd
=============

.. c:function:: void myrs_exec_cmd(struct myrs_hba *cs, struct myrs_cmdblk *cmd_blk)

    executes V2 Command and waits for completion.

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param cmd_blk:
        *undescribed*
    :type cmd_blk: struct myrs_cmdblk \*

.. _`myrs_report_progress`:

myrs_report_progress
====================

.. c:function:: void myrs_report_progress(struct myrs_hba *cs, unsigned short ldev_num, unsigned char *msg, unsigned long blocks, unsigned long size)

    prints progress message

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param ldev_num:
        *undescribed*
    :type ldev_num: unsigned short

    :param msg:
        *undescribed*
    :type msg: unsigned char \*

    :param blocks:
        *undescribed*
    :type blocks: unsigned long

    :param size:
        *undescribed*
    :type size: unsigned long

.. _`myrs_get_ctlr_info`:

myrs_get_ctlr_info
==================

.. c:function:: unsigned char myrs_get_ctlr_info(struct myrs_hba *cs)

    executes a Controller Information IOCTL Command

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

.. _`myrs_get_ldev_info`:

myrs_get_ldev_info
==================

.. c:function:: unsigned char myrs_get_ldev_info(struct myrs_hba *cs, unsigned short ldev_num, struct myrs_ldev_info *ldev_info)

    executes a Logical Device Information IOCTL Command

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param ldev_num:
        *undescribed*
    :type ldev_num: unsigned short

    :param ldev_info:
        *undescribed*
    :type ldev_info: struct myrs_ldev_info \*

.. _`myrs_get_pdev_info`:

myrs_get_pdev_info
==================

.. c:function:: unsigned char myrs_get_pdev_info(struct myrs_hba *cs, unsigned char channel, unsigned char target, unsigned char lun, struct myrs_pdev_info *pdev_info)

    executes a "Read Physical Device Information" Command

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param channel:
        *undescribed*
    :type channel: unsigned char

    :param target:
        *undescribed*
    :type target: unsigned char

    :param lun:
        *undescribed*
    :type lun: unsigned char

    :param pdev_info:
        *undescribed*
    :type pdev_info: struct myrs_pdev_info \*

.. _`myrs_dev_op`:

myrs_dev_op
===========

.. c:function:: unsigned char myrs_dev_op(struct myrs_hba *cs, enum myrs_ioctl_opcode opcode, enum myrs_opdev opdev)

    executes a "Device Operation" Command

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param opcode:
        *undescribed*
    :type opcode: enum myrs_ioctl_opcode

    :param opdev:
        *undescribed*
    :type opdev: enum myrs_opdev

.. _`myrs_translate_pdev`:

myrs_translate_pdev
===================

.. c:function:: unsigned char myrs_translate_pdev(struct myrs_hba *cs, unsigned char channel, unsigned char target, unsigned char lun, struct myrs_devmap *devmap)

    translates a Physical Device Channel and TargetID into a Logical Device.

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param channel:
        *undescribed*
    :type channel: unsigned char

    :param target:
        *undescribed*
    :type target: unsigned char

    :param lun:
        *undescribed*
    :type lun: unsigned char

    :param devmap:
        *undescribed*
    :type devmap: struct myrs_devmap \*

.. _`myrs_get_event`:

myrs_get_event
==============

.. c:function:: unsigned char myrs_get_event(struct myrs_hba *cs, unsigned int event_num, struct myrs_event *event_buf)

    executes a Get Event Command

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param event_num:
        *undescribed*
    :type event_num: unsigned int

    :param event_buf:
        *undescribed*
    :type event_buf: struct myrs_event \*

.. _`myrs_enable_mmio_mbox`:

myrs_enable_mmio_mbox
=====================

.. c:function:: bool myrs_enable_mmio_mbox(struct myrs_hba *cs, enable_mbox_t enable_mbox_fn)

    enables the Memory Mailbox Interface

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param enable_mbox_fn:
        *undescribed*
    :type enable_mbox_fn: enable_mbox_t

.. _`myrs_get_config`:

myrs_get_config
===============

.. c:function:: int myrs_get_config(struct myrs_hba *cs)

    reads the Configuration Information

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

.. _`myrs_is_raid`:

myrs_is_raid
============

.. c:function:: int myrs_is_raid(struct device *dev)

    return boolean indicating device is raid volume \ ``dev``\  the device struct object

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`myrs_get_resync`:

myrs_get_resync
===============

.. c:function:: void myrs_get_resync(struct device *dev)

    get raid volume resync percent complete \ ``dev``\  the device struct object

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`myrs_get_state`:

myrs_get_state
==============

.. c:function:: void myrs_get_state(struct device *dev)

    get raid volume status \ ``dev``\  the device struct object

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`myrs_err_status`:

myrs_err_status
===============

.. c:function:: bool myrs_err_status(struct myrs_hba *cs, unsigned char status, unsigned char parm0, unsigned char parm1)

    :param cs:
        *undescribed*
    :type cs: struct myrs_hba \*

    :param status:
        *undescribed*
    :type status: unsigned char

    :param parm0:
        *undescribed*
    :type parm0: unsigned char

    :param parm1:
        *undescribed*
    :type parm1: unsigned char

.. This file was automatic generated / don't edit.


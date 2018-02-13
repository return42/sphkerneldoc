.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/block.c

.. _`mmc_rpmb_data`:

struct mmc_rpmb_data
====================

.. c:type:: struct mmc_rpmb_data

    special RPMB device type for these areas

.. _`mmc_rpmb_data.definition`:

Definition
----------

.. code-block:: c

    struct mmc_rpmb_data {
        struct device dev;
        struct cdev chrdev;
        int id;
        unsigned int part_index;
        struct mmc_blk_data *md;
        struct list_head node;
    }

.. _`mmc_rpmb_data.members`:

Members
-------

dev
    the device for the RPMB area

chrdev
    character device for the RPMB area

id
    unique device ID number

part_index
    partition index (0 on first)

md
    parent MMC block device

node
    list item, so we can put this device on a list

.. _`mmc_rpmb_ioctl`:

mmc_rpmb_ioctl
==============

.. c:function:: long mmc_rpmb_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    ioctl handler for the RPMB chardev

    :param struct file \*filp:
        the character device file

    :param unsigned int cmd:
        the \ :c:func:`ioctl`\  command

    :param unsigned long arg:
        the argument from userspace

.. _`mmc_rpmb_ioctl.description`:

Description
-----------

This will essentially just redirect the \ :c:func:`ioctl`\ s coming in over to
the main block device spawning the RPMB character device.

.. This file was automatic generated / don't edit.


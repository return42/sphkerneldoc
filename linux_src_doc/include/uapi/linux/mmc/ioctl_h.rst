.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/mmc/ioctl.h

.. _`mmc_ioc_multi_cmd`:

struct mmc_ioc_multi_cmd
========================

.. c:type:: struct mmc_ioc_multi_cmd

    multi command information

.. _`mmc_ioc_multi_cmd.definition`:

Definition
----------

.. code-block:: c

    struct mmc_ioc_multi_cmd {
        __u64 num_of_cmds;
        struct mmc_ioc_cmd cmds[0];
    }

.. _`mmc_ioc_multi_cmd.members`:

Members
-------

num_of_cmds
    Number of commands to send. Must be equal to or less than
    MMC_IOC_MAX_CMDS.

cmds
    Array of commands with length equal to 'num_of_cmds'

.. This file was automatic generated / don't edit.


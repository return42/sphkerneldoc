.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_dl.h

.. _`vsp1_dl_ext_cmd`:

struct vsp1_dl_ext_cmd
======================

.. c:type:: struct vsp1_dl_ext_cmd

    Extended Display command

.. _`vsp1_dl_ext_cmd.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_ext_cmd {
        struct vsp1_dl_cmd_pool *pool;
        struct list_head free;
        u8 opcode;
        u32 flags;
        struct vsp1_pre_ext_dl_body *cmds;
        unsigned int num_cmds;
        dma_addr_t cmd_dma;
        void *data;
        dma_addr_t data_dma;
    }

.. _`vsp1_dl_ext_cmd.members`:

Members
-------

pool
    pool to which this command belongs

free
    entry in the pool of free commands list

opcode
    command type opcode

flags
    flags used by the command

cmds
    array of command bodies for this extended cmd

num_cmds
    quantity of commands in \ ``cmds``\  array

cmd_dma
    DMA address of the command body

data
    memory allocation for command-specific data

data_dma
    DMA address for command-specific data

.. This file was automatic generated / don't edit.


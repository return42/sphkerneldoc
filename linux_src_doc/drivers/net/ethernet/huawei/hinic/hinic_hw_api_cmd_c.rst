.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_api_cmd.c

.. _`chain_busy`:

chain_busy
==========

.. c:function:: int chain_busy(struct hinic_api_cmd_chain *chain)

    check if the chain is still processing last requests

    :param chain:
        chain to check
    :type chain: struct hinic_api_cmd_chain \*

.. _`chain_busy.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_cell_data_size`:

get_cell_data_size
==================

.. c:function:: u8 get_cell_data_size(enum hinic_api_cmd_chain_type type)

    get the data size of a specific cell type

    :param type:
        chain type
    :type type: enum hinic_api_cmd_chain_type

.. _`get_cell_data_size.description`:

Description
-----------

Return the data(Desc + Address) size in the cell

.. _`prepare_cell_ctrl`:

prepare_cell_ctrl
=================

.. c:function:: void prepare_cell_ctrl(u64 *cell_ctrl, u16 data_size)

    prepare the ctrl of the cell for the command

    :param cell_ctrl:
        the control of the cell to set the control value into it
    :type cell_ctrl: u64 \*

    :param data_size:
        the size of the data in the cell
    :type data_size: u16

.. _`prepare_api_cmd`:

prepare_api_cmd
===============

.. c:function:: void prepare_api_cmd(struct hinic_api_cmd_chain *chain, enum hinic_node_id dest, void *cmd, u16 cmd_size)

    prepare API CMD command

    :param chain:
        chain for the command
    :type chain: struct hinic_api_cmd_chain \*

    :param dest:
        destination node on the card that will receive the command
    :type dest: enum hinic_node_id

    :param cmd:
        command data
    :type cmd: void \*

    :param cmd_size:
        the command size
    :type cmd_size: u16

.. _`prepare_cell`:

prepare_cell
============

.. c:function:: void prepare_cell(struct hinic_api_cmd_chain *chain, enum hinic_node_id dest, void *cmd, u16 cmd_size)

    prepare cell ctrl and cmd in the current cell

    :param chain:
        chain for the command
    :type chain: struct hinic_api_cmd_chain \*

    :param dest:
        destination node on the card that will receive the command
    :type dest: enum hinic_node_id

    :param cmd:
        command data
    :type cmd: void \*

    :param cmd_size:
        the command size
    :type cmd_size: u16

.. _`prepare_cell.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_cmd_status_update`:

api_cmd_status_update
=====================

.. c:function:: void api_cmd_status_update(struct hinic_api_cmd_chain *chain)

    update the status in the chain struct

    :param chain:
        chain to update
    :type chain: struct hinic_api_cmd_chain \*

.. _`wait_for_status_poll`:

wait_for_status_poll
====================

.. c:function:: int wait_for_status_poll(struct hinic_api_cmd_chain *chain)

    wait for write to api cmd command to complete

    :param chain:
        the chain of the command
    :type chain: struct hinic_api_cmd_chain \*

.. _`wait_for_status_poll.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`wait_for_api_cmd_completion`:

wait_for_api_cmd_completion
===========================

.. c:function:: int wait_for_api_cmd_completion(struct hinic_api_cmd_chain *chain)

    wait for command to complete

    :param chain:
        chain for the command
    :type chain: struct hinic_api_cmd_chain \*

.. _`wait_for_api_cmd_completion.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_cmd`:

api_cmd
=======

.. c:function:: int api_cmd(struct hinic_api_cmd_chain *chain, enum hinic_node_id dest, u8 *cmd, u16 cmd_size)

    API CMD command

    :param chain:
        chain for the command
    :type chain: struct hinic_api_cmd_chain \*

    :param dest:
        destination node on the card that will receive the command
    :type dest: enum hinic_node_id

    :param cmd:
        command data
    :type cmd: u8 \*

    :param cmd_size:
        *undescribed*
    :type cmd_size: u16

.. _`api_cmd.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_api_cmd_write`:

hinic_api_cmd_write
===================

.. c:function:: int hinic_api_cmd_write(struct hinic_api_cmd_chain *chain, enum hinic_node_id dest, u8 *cmd, u16 size)

    Write API CMD command

    :param chain:
        chain for write command
    :type chain: struct hinic_api_cmd_chain \*

    :param dest:
        destination node on the card that will receive the command
    :type dest: enum hinic_node_id

    :param cmd:
        command data
    :type cmd: u8 \*

    :param size:
        the command size
    :type size: u16

.. _`hinic_api_cmd_write.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_cmd_hw_restart`:

api_cmd_hw_restart
==================

.. c:function:: int api_cmd_hw_restart(struct hinic_api_cmd_chain *chain)

    restart the chain in the HW

    :param chain:
        the API CMD specific chain to restart
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_hw_restart.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_cmd_ctrl_init`:

api_cmd_ctrl_init
=================

.. c:function:: void api_cmd_ctrl_init(struct hinic_api_cmd_chain *chain)

    set the control register of a chain

    :param chain:
        the API CMD specific chain to set control register for
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_set_status_addr`:

api_cmd_set_status_addr
=======================

.. c:function:: void api_cmd_set_status_addr(struct hinic_api_cmd_chain *chain)

    set the status address of a chain in the HW

    :param chain:
        the API CMD specific chain to set in HW status address for
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_set_num_cells`:

api_cmd_set_num_cells
=====================

.. c:function:: void api_cmd_set_num_cells(struct hinic_api_cmd_chain *chain)

    set the number cells of a chain in the HW

    :param chain:
        the API CMD specific chain to set in HW the number of cells for
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_head_init`:

api_cmd_head_init
=================

.. c:function:: void api_cmd_head_init(struct hinic_api_cmd_chain *chain)

    set the head of a chain in the HW

    :param chain:
        the API CMD specific chain to set in HW the head for
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_chain_hw_clean`:

api_cmd_chain_hw_clean
======================

.. c:function:: void api_cmd_chain_hw_clean(struct hinic_api_cmd_chain *chain)

    clean the HW

    :param chain:
        the API CMD specific chain
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_chain_hw_init`:

api_cmd_chain_hw_init
=====================

.. c:function:: int api_cmd_chain_hw_init(struct hinic_api_cmd_chain *chain)

    initialize the chain in the HW

    :param chain:
        the API CMD specific chain to initialize in HW
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_chain_hw_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_cmd_buf`:

free_cmd_buf
============

.. c:function:: void free_cmd_buf(struct hinic_api_cmd_chain *chain, int cell_idx)

    free the dma buffer of API CMD command

    :param chain:
        the API CMD specific chain of the cmd
    :type chain: struct hinic_api_cmd_chain \*

    :param cell_idx:
        the cell index of the cmd
    :type cell_idx: int

.. _`alloc_cmd_buf`:

alloc_cmd_buf
=============

.. c:function:: int alloc_cmd_buf(struct hinic_api_cmd_chain *chain, struct hinic_api_cmd_cell *cell, int cell_idx)

    allocate a dma buffer for API CMD command

    :param chain:
        the API CMD specific chain for the cmd
    :type chain: struct hinic_api_cmd_chain \*

    :param cell:
        the cell in the HW for the cmd
    :type cell: struct hinic_api_cmd_cell \*

    :param cell_idx:
        the index of the cell
    :type cell_idx: int

.. _`alloc_cmd_buf.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_cmd_create_cell`:

api_cmd_create_cell
===================

.. c:function:: int api_cmd_create_cell(struct hinic_api_cmd_chain *chain, int cell_idx, struct hinic_api_cmd_cell *pre_node, struct hinic_api_cmd_cell **node_vaddr)

    create API CMD cell for specific chain

    :param chain:
        the API CMD specific chain to create its cell
    :type chain: struct hinic_api_cmd_chain \*

    :param cell_idx:
        the index of the cell to create
    :type cell_idx: int

    :param pre_node:
        previous cell
    :type pre_node: struct hinic_api_cmd_cell \*

    :param node_vaddr:
        the returned virt addr of the cell
    :type node_vaddr: struct hinic_api_cmd_cell \*\*

.. _`api_cmd_create_cell.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_cmd_destroy_cell`:

api_cmd_destroy_cell
====================

.. c:function:: void api_cmd_destroy_cell(struct hinic_api_cmd_chain *chain, int cell_idx)

    destroy API CMD cell of specific chain

    :param chain:
        the API CMD specific chain to destroy its cell
    :type chain: struct hinic_api_cmd_chain \*

    :param cell_idx:
        the cell to destroy
    :type cell_idx: int

.. _`api_cmd_destroy_cells`:

api_cmd_destroy_cells
=====================

.. c:function:: void api_cmd_destroy_cells(struct hinic_api_cmd_chain *chain, int num_cells)

    destroy API CMD cells of specific chain

    :param chain:
        the API CMD specific chain to destroy its cells
    :type chain: struct hinic_api_cmd_chain \*

    :param num_cells:
        number of cells to destroy
    :type num_cells: int

.. _`api_cmd_create_cells`:

api_cmd_create_cells
====================

.. c:function:: int api_cmd_create_cells(struct hinic_api_cmd_chain *chain)

    create API CMD cells for specific chain

    :param chain:
        the API CMD specific chain
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_create_cells.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_chain_init`:

api_chain_init
==============

.. c:function:: int api_chain_init(struct hinic_api_cmd_chain *chain, struct hinic_api_cmd_chain_attr *attr)

    initialize API CMD specific chain

    :param chain:
        the API CMD specific chain to initialize
    :type chain: struct hinic_api_cmd_chain \*

    :param attr:
        attributes to set in the chain
    :type attr: struct hinic_api_cmd_chain_attr \*

.. _`api_chain_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`api_chain_free`:

api_chain_free
==============

.. c:function:: void api_chain_free(struct hinic_api_cmd_chain *chain)

    free API CMD specific chain

    :param chain:
        the API CMD specific chain to free
    :type chain: struct hinic_api_cmd_chain \*

.. _`api_cmd_create_chain`:

api_cmd_create_chain
====================

.. c:function:: struct hinic_api_cmd_chain *api_cmd_create_chain(struct hinic_api_cmd_chain_attr *attr)

    create API CMD specific chain

    :param attr:
        attributes to set the chain
    :type attr: struct hinic_api_cmd_chain_attr \*

.. _`api_cmd_create_chain.description`:

Description
-----------

Return the created chain

.. _`api_cmd_destroy_chain`:

api_cmd_destroy_chain
=====================

.. c:function:: void api_cmd_destroy_chain(struct hinic_api_cmd_chain *chain)

    destroy API CMD specific chain

    :param chain:
        the API CMD specific chain to destroy
    :type chain: struct hinic_api_cmd_chain \*

.. _`hinic_api_cmd_init`:

hinic_api_cmd_init
==================

.. c:function:: int hinic_api_cmd_init(struct hinic_api_cmd_chain **chain, struct hinic_hwif *hwif)

    Initialize all the API CMD chains

    :param chain:
        the API CMD chains that are initialized
    :type chain: struct hinic_api_cmd_chain \*\*

    :param hwif:
        the hardware interface of a pci function device
    :type hwif: struct hinic_hwif \*

.. _`hinic_api_cmd_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_api_cmd_free`:

hinic_api_cmd_free
==================

.. c:function:: void hinic_api_cmd_free(struct hinic_api_cmd_chain **chain)

    free the API CMD chains

    :param chain:
        the API CMD chains that are freed
    :type chain: struct hinic_api_cmd_chain \*\*

.. This file was automatic generated / don't edit.


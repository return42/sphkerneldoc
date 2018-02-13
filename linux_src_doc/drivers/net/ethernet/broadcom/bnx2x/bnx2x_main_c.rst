.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_main.c

.. _`bnx2x_get_leader_lock_resource`:

bnx2x_get_leader_lock_resource
==============================

.. c:function:: int bnx2x_get_leader_lock_resource(struct bnx2x *bp)

    get the recovery leader resource id

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_get_leader_lock_resource.description`:

Description
-----------

Returns the recovery leader resource id according to the engine this function
belongs to. Currently only only 2 engines is supported.

.. _`bnx2x_trylock_leader_lock`:

bnx2x_trylock_leader_lock
=========================

.. c:function:: bool bnx2x_trylock_leader_lock(struct bnx2x *bp)

    try to acquire a leader lock.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_trylock_leader_lock.description`:

Description
-----------

Tries to acquire a leader lock for current engine.

.. _`bnx2x_get_common_flags`:

bnx2x_get_common_flags
======================

.. c:function:: unsigned long bnx2x_get_common_flags(struct bnx2x *bp, struct bnx2x_fastpath *fp, bool zero_stats)

    Return common flags

    :param struct bnx2x \*bp:
        *undescribed*

    :param struct bnx2x_fastpath \*fp:
        *undescribed*

    :param bool zero_stats:
        *undescribed*

.. _`bnx2x_get_common_flags.description`:

Description
-----------

\ ``bp``\           device handle
\ ``fp``\           queue handle
\ ``zero_stats``\   TRUE if statistics zeroing is needed

Return the flags that are common for the Tx-only and not normal connections.

.. _`bnx2x_is_contextless_ramrod`:

bnx2x_is_contextless_ramrod
===========================

.. c:function:: bool bnx2x_is_contextless_ramrod(int cmd, int cmd_type)

    check if the current command ends on EQ

    :param int cmd:
        command to check

    :param int cmd_type:
        command type

.. _`bnx2x_sp_post`:

bnx2x_sp_post
=============

.. c:function:: int bnx2x_sp_post(struct bnx2x *bp, int command, int cid, u32 data_hi, u32 data_lo, int cmd_type)

    place a single command on an SP ring

    :param struct bnx2x \*bp:
        driver handle

    :param int command:
        command to place (e.g. SETUP, FILTER_RULES, etc.)

    :param int cid:
        SW CID the command is related to

    :param u32 data_hi:
        command private data address (high 32 bits)

    :param u32 data_lo:
        command private data address (low 32 bits)

    :param int cmd_type:
        command type (e.g. NONE, ETH)

.. _`bnx2x_sp_post.description`:

Description
-----------

SP data is handled as if it's always an address pair, thus data fields are
not swapped to little endian in upper functions. Instead this function swaps
data as if it's two u32 fields.

.. _`bnx2x_clear_pf_load`:

bnx2x_clear_pf_load
===================

.. c:function:: bool bnx2x_clear_pf_load(struct bnx2x *bp)

    clear pf load mark

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_clear_pf_load.description`:

Description
-----------

Should be run under rtnl lock.
Decrements the load counter for the current engine. Returns
whether other functions are still loaded

.. _`bnx2x_chk_parity_attn`:

bnx2x_chk_parity_attn
=====================

.. c:function:: bool bnx2x_chk_parity_attn(struct bnx2x *bp, bool *global, bool print)

    checks for parity attentions.

    :param struct bnx2x \*bp:
        driver handle

    :param bool \*global:
        true if there was a global attention

    :param bool print:
        show parity attention in syslog

.. _`bnx2x_init_hw_common`:

bnx2x_init_hw_common
====================

.. c:function:: int bnx2x_init_hw_common(struct bnx2x *bp)

    initialize the HW at the COMMON phase.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_init_hw_common_chip`:

bnx2x_init_hw_common_chip
=========================

.. c:function:: int bnx2x_init_hw_common_chip(struct bnx2x *bp)

    init HW at the COMMON_CHIP phase.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_set_int_mode`:

bnx2x_set_int_mode
==================

.. c:function:: int bnx2x_set_int_mode(struct bnx2x *bp)

    configure interrupt mode

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_set_int_mode.description`:

Description
-----------

In case of MSI-X it will also try to enable MSI-X.

.. _`bnx2x_pf_q_prep_init`:

bnx2x_pf_q_prep_init
====================

.. c:function:: void bnx2x_pf_q_prep_init(struct bnx2x *bp, struct bnx2x_fastpath *fp, struct bnx2x_queue_init_params *init_params)

    prepare INIT transition parameters

    :param struct bnx2x \*bp:
        driver handle

    :param struct bnx2x_fastpath \*fp:
        pointer to fastpath

    :param struct bnx2x_queue_init_params \*init_params:
        pointer to parameters structure

.. _`bnx2x_pf_q_prep_init.parameters-configured`:

parameters configured
---------------------

- HC configuration
- Queue's CDU context

.. _`bnx2x_setup_queue`:

bnx2x_setup_queue
=================

.. c:function:: int bnx2x_setup_queue(struct bnx2x *bp, struct bnx2x_fastpath *fp, bool leading)

    setup queue

    :param struct bnx2x \*bp:
        driver handle

    :param struct bnx2x_fastpath \*fp:
        pointer to fastpath

    :param bool leading:
        is leading

.. _`bnx2x_setup_queue.description`:

Description
-----------

This function performs 2 steps in a Queue state machine

.. _`bnx2x_setup_queue.actually`:

actually
--------

1) RESET->INIT 2) INIT->SETUP

.. _`bnx2x_send_unload_req`:

bnx2x_send_unload_req
=====================

.. c:function:: u32 bnx2x_send_unload_req(struct bnx2x *bp, int unload_mode)

    request unload mode from the MCP.

    :param struct bnx2x \*bp:
        driver handle

    :param int unload_mode:
        requested function's unload mode

.. _`bnx2x_send_unload_req.return-unload-mode-returned-by-the-mcp`:

Return unload mode returned by the MCP
--------------------------------------

COMMON, PORT or FUNC.

.. _`bnx2x_send_unload_done`:

bnx2x_send_unload_done
======================

.. c:function:: void bnx2x_send_unload_done(struct bnx2x *bp, bool keep_link)

    send UNLOAD_DONE command to the MCP.

    :param struct bnx2x \*bp:
        driver handle

    :param bool keep_link:
        true iff link should be kept up

.. _`bnx2x_clp_reset_done`:

bnx2x_clp_reset_done
====================

.. c:function:: void bnx2x_clp_reset_done(struct bnx2x *bp, u32 magic_val)

    restore the value of the \`magic' bit.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 magic_val:
        old value of the \`magic' bit.

.. _`bnx2x_reset_mcp_prep`:

bnx2x_reset_mcp_prep
====================

.. c:function:: void bnx2x_reset_mcp_prep(struct bnx2x *bp, u32 *magic_val)

    prepare for MCP reset.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 \*magic_val:
        old value of 'magic' bit.

.. _`bnx2x_reset_mcp_prep.description`:

Description
-----------

Takes care of CLP configurations.

.. _`bnx2x_mcp_wait_one`:

bnx2x_mcp_wait_one
==================

.. c:function:: void bnx2x_mcp_wait_one(struct bnx2x *bp)

    wait for MCP_ONE_TIMEOUT

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_er_poll_igu_vq`:

bnx2x_er_poll_igu_vq
====================

.. c:function:: int bnx2x_er_poll_igu_vq(struct bnx2x *bp)

    poll for pending writes bit. It should get cleared in no more than 1s.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_er_poll_igu_vq.description`:

Description
-----------

It should get cleared in no more than 1s. Returns 0 if
pending writes bit gets cleared.

.. _`bnx2x_set_uc_list`:

bnx2x_set_uc_list
=================

.. c:function:: int bnx2x_set_uc_list(struct bnx2x *bp)

    configure a new unicast MACs list.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_set_uc_list.description`:

Description
-----------

We will use zero (0) as a MAC type for these MACs.

.. _`bnx2x_get_num_non_def_sbs`:

bnx2x_get_num_non_def_sbs
=========================

.. c:function:: int bnx2x_get_num_non_def_sbs(struct pci_dev *pdev, int cnic_cnt)

    return the number of none default SBs

    :param struct pci_dev \*pdev:
        *undescribed*

    :param int cnic_cnt:
        *undescribed*

.. _`bnx2x_io_error_detected`:

bnx2x_io_error_detected
=======================

.. c:function:: pci_ers_result_t bnx2x_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`bnx2x_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`bnx2x_io_slot_reset`:

bnx2x_io_slot_reset
===================

.. c:function:: pci_ers_result_t bnx2x_io_slot_reset(struct pci_dev *pdev)

    called after the PCI bus has been reset

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`bnx2x_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.

.. _`bnx2x_io_resume`:

bnx2x_io_resume
===============

.. c:function:: void bnx2x_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`bnx2x_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation.

.. _`bnx2x_set_iscsi_eth_mac_addr`:

bnx2x_set_iscsi_eth_mac_addr
============================

.. c:function:: int bnx2x_set_iscsi_eth_mac_addr(struct bnx2x *bp)

    set iSCSI MAC(s).

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_set_iscsi_eth_mac_addr.description`:

Description
-----------

This function will wait until the ramrod completion returns.
Return 0 if success, -ENODEV if ramrod doesn't return.

.. This file was automatic generated / don't edit.


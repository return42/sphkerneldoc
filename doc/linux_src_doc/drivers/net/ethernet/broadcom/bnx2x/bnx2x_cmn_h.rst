.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_cmn.h

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

.. _`bnx2x_rss`:

bnx2x_rss
=========

.. c:function:: int bnx2x_rss(struct bnx2x *bp, struct bnx2x_rss_config_obj *rss_obj, bool config_hash, bool enable)

    configure RSS parameters in a PF.

    :param struct bnx2x \*bp:
        driver handle

    :param struct bnx2x_rss_config_obj \*rss_obj:
        RSS object to use

    :param bool config_hash:
        re-configure RSS hash keys configuration

    :param bool enable:
        enabled or disabled configuration

.. _`bnx2x__init_func_obj`:

bnx2x__init_func_obj
====================

.. c:function:: void bnx2x__init_func_obj(struct bnx2x *bp)

    init function object

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x__init_func_obj.description`:

Description
-----------

Initializes the Function Object with the appropriate
parameters which include a function slow path driver
interface.

.. _`bnx2x_setup_queue`:

bnx2x_setup_queue
=================

.. c:function:: int bnx2x_setup_queue(struct bnx2x *bp, struct bnx2x_fastpath *fp, bool leading)

    setup eth queue.

    :param struct bnx2x \*bp:
        driver handle

    :param struct bnx2x_fastpath \*fp:
        pointer to the fastpath structure

    :param bool leading:
        boolean

.. _`bnx2x_setup_leading`:

bnx2x_setup_leading
===================

.. c:function:: int bnx2x_setup_leading(struct bnx2x *bp)

    bring up a leading eth queue.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_fw_command`:

bnx2x_fw_command
================

.. c:function:: u32 bnx2x_fw_command(struct bnx2x *bp, u32 command, u32 param)

    send the MCP a request

    :param struct bnx2x \*bp:
        driver handle

    :param u32 command:
        request

    :param u32 param:
        request's parameter

.. _`bnx2x_fw_command.description`:

Description
-----------

block until there is a reply

.. _`bnx2x_initial_phy_init`:

bnx2x_initial_phy_init
======================

.. c:function:: int bnx2x_initial_phy_init(struct bnx2x *bp, int load_mode)

    initialize link parameters structure variables.

    :param struct bnx2x \*bp:
        driver handle

    :param int load_mode:
        current mode

.. _`bnx2x_link_set`:

bnx2x_link_set
==============

.. c:function:: void bnx2x_link_set(struct bnx2x *bp)

    configure hw according to link parameters structure.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_force_link_reset`:

bnx2x_force_link_reset
======================

.. c:function:: void bnx2x_force_link_reset(struct bnx2x *bp)

    Forces link reset, and put the PHY in reset as well.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_link_test`:

bnx2x_link_test
===============

.. c:function:: u8 bnx2x_link_test(struct bnx2x *bp, u8 is_serdes)

    query link status.

    :param struct bnx2x \*bp:
        driver handle

    :param u8 is_serdes:
        bool

.. _`bnx2x_link_test.description`:

Description
-----------

Returns 0 if link is UP.

.. _`bnx2x_drv_pulse`:

bnx2x_drv_pulse
===============

.. c:function:: void bnx2x_drv_pulse(struct bnx2x *bp)

    write driver pulse to shmem

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_drv_pulse.description`:

Description
-----------

writes the value in bp->fw_drv_pulse_wr_seq to drv_pulse mbox
in the shmem.

.. _`bnx2x_igu_ack_sb`:

bnx2x_igu_ack_sb
================

.. c:function:: void bnx2x_igu_ack_sb(struct bnx2x *bp, u8 igu_sb_id, u8 segment, u16 index, u8 op, u8 update)

    update IGU with current SB value

    :param struct bnx2x \*bp:
        driver handle

    :param u8 igu_sb_id:
        SB id

    :param u8 segment:
        SB segment

    :param u16 index:
        SB index

    :param u8 op:
        SB operation

    :param u8 update:
        is HW update required

.. _`bnx2x__link_status_update`:

bnx2x__link_status_update
=========================

.. c:function:: void bnx2x__link_status_update(struct bnx2x *bp)

    handles link status change.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_link_report`:

bnx2x_link_report
=================

.. c:function:: void bnx2x_link_report(struct bnx2x *bp)

    report link status to upper layer.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_get_mf_speed`:

bnx2x_get_mf_speed
==================

.. c:function:: u16 bnx2x_get_mf_speed(struct bnx2x *bp)

    calculate MF speed.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_get_mf_speed.description`:

Description
-----------

Takes into account current linespeed and MF configuration.

.. _`bnx2x_msix_sp_int`:

bnx2x_msix_sp_int
=================

.. c:function:: irqreturn_t bnx2x_msix_sp_int(int irq, void *dev_instance)

    MSI-X slowpath interrupt handler

    :param int irq:
        irq number

    :param void \*dev_instance:
        private instance

.. _`bnx2x_interrupt`:

bnx2x_interrupt
===============

.. c:function:: irqreturn_t bnx2x_interrupt(int irq, void *dev_instance)

    non MSI-X interrupt handler

    :param int irq:
        irq number

    :param void \*dev_instance:
        private instance

.. _`bnx2x_cnic_notify`:

bnx2x_cnic_notify
=================

.. c:function:: int bnx2x_cnic_notify(struct bnx2x *bp, int cmd)

    send command to cnic driver

    :param struct bnx2x \*bp:
        driver handle

    :param int cmd:
        command

.. _`bnx2x_setup_cnic_irq_info`:

bnx2x_setup_cnic_irq_info
=========================

.. c:function:: void bnx2x_setup_cnic_irq_info(struct bnx2x *bp)

    provides cnic with IRQ information

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_setup_cnic_info`:

bnx2x_setup_cnic_info
=====================

.. c:function:: void bnx2x_setup_cnic_info(struct bnx2x *bp)

    provides cnic with updated info

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_int_enable`:

bnx2x_int_enable
================

.. c:function:: void bnx2x_int_enable(struct bnx2x *bp)

    enable HW interrupts.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_int_disable_sync`:

bnx2x_int_disable_sync
======================

.. c:function:: void bnx2x_int_disable_sync(struct bnx2x *bp, int disable_hw)

    disable interrupts.

    :param struct bnx2x \*bp:
        driver handle

    :param int disable_hw:
        true, disable HW interrupts.

.. _`bnx2x_int_disable_sync.description`:

Description
-----------

This function ensures that there are no
ISRs or SP DPCs (sp_task) are running after it returns.

.. _`bnx2x_nic_init_cnic`:

bnx2x_nic_init_cnic
===================

.. c:function:: void bnx2x_nic_init_cnic(struct bnx2x *bp)

    init driver internals for cnic.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_nic_init_cnic.initializes`:

Initializes
-----------

- rings
- status blocks
- etc.

.. _`bnx2x_pre_irq_nic_init`:

bnx2x_pre_irq_nic_init
======================

.. c:function:: void bnx2x_pre_irq_nic_init(struct bnx2x *bp)

    init driver internals.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_pre_irq_nic_init.initializes`:

Initializes
-----------

- fastpath object
- fastpath rings
etc.

.. _`bnx2x_post_irq_nic_init`:

bnx2x_post_irq_nic_init
=======================

.. c:function:: void bnx2x_post_irq_nic_init(struct bnx2x *bp, u32 load_code)

    init driver internals.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 load_code:
        COMMON, PORT or FUNCTION

.. _`bnx2x_post_irq_nic_init.initializes`:

Initializes
-----------

- status blocks
- slowpath rings
- etc.

.. _`bnx2x_alloc_mem_cnic`:

bnx2x_alloc_mem_cnic
====================

.. c:function:: int bnx2x_alloc_mem_cnic(struct bnx2x *bp)

    allocate driver's memory for cnic.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_alloc_mem`:

bnx2x_alloc_mem
===============

.. c:function:: int bnx2x_alloc_mem(struct bnx2x *bp)

    allocate driver's memory.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_free_mem_cnic`:

bnx2x_free_mem_cnic
===================

.. c:function:: void bnx2x_free_mem_cnic(struct bnx2x *bp)

    release driver's memory for cnic.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_free_mem`:

bnx2x_free_mem
==============

.. c:function:: void bnx2x_free_mem(struct bnx2x *bp)

    release driver's memory.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_set_num_queues`:

bnx2x_set_num_queues
====================

.. c:function:: void bnx2x_set_num_queues(struct bnx2x *bp)

    set number of queues according to mode.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_chip_cleanup`:

bnx2x_chip_cleanup
==================

.. c:function:: void bnx2x_chip_cleanup(struct bnx2x *bp, int unload_mode, bool keep_link)

    cleanup chip internals.

    :param struct bnx2x \*bp:
        driver handle

    :param int unload_mode:
        COMMON, PORT, FUNCTION

    :param bool keep_link:
        true iff link should be kept up.

.. _`bnx2x_chip_cleanup.description`:

Description
-----------

- Cleanup MAC configuration.
- Closes clients.
- etc.

.. _`bnx2x_acquire_hw_lock`:

bnx2x_acquire_hw_lock
=====================

.. c:function:: int bnx2x_acquire_hw_lock(struct bnx2x *bp, u32 resource)

    acquire HW lock.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 resource:
        resource bit which was locked

.. _`bnx2x_release_hw_lock`:

bnx2x_release_hw_lock
=====================

.. c:function:: int bnx2x_release_hw_lock(struct bnx2x *bp, u32 resource)

    release HW lock.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 resource:
        resource bit which was locked

.. _`bnx2x_release_leader_lock`:

bnx2x_release_leader_lock
=========================

.. c:function:: int bnx2x_release_leader_lock(struct bnx2x *bp)

    release recovery leader lock

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_set_eth_mac`:

bnx2x_set_eth_mac
=================

.. c:function:: int bnx2x_set_eth_mac(struct bnx2x *bp, bool set)

    configure eth MAC address in the HW

    :param struct bnx2x \*bp:
        driver handle

    :param bool set:
        set or clear

.. _`bnx2x_set_eth_mac.description`:

Description
-----------

Configures according to the value in netdev->dev_addr.

.. _`bnx2x_set_rx_mode_inner`:

bnx2x_set_rx_mode_inner
=======================

.. c:function:: void bnx2x_set_rx_mode_inner(struct bnx2x *bp)

    set MAC filtering configurations.

    :param struct bnx2x \*bp:
        *undescribed*

.. _`bnx2x_set_rx_mode_inner.description`:

Description
-----------

called with netif_tx_lock from dev_mcast.c
If bp->state is OPEN, should be called with
\ :c:func:`netif_addr_lock_bh`\ 

.. _`bnx2x_sp_event`:

bnx2x_sp_event
==============

.. c:function:: void bnx2x_sp_event(struct bnx2x_fastpath *fp, union eth_rx_cqe *rr_cqe)

    handle ramrods completion.

    :param struct bnx2x_fastpath \*fp:
        fastpath handle for the event

    :param union eth_rx_cqe \*rr_cqe:
        eth_rx_cqe

.. _`bnx2x_ilt_set_info`:

bnx2x_ilt_set_info
==================

.. c:function:: void bnx2x_ilt_set_info(struct bnx2x *bp)

    prepare ILT configurations.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_ilt_set_info_cnic`:

bnx2x_ilt_set_info_cnic
=======================

.. c:function:: void bnx2x_ilt_set_info_cnic(struct bnx2x *bp)

    prepare ILT configurations for SRC and TM.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_dcbx_init`:

bnx2x_dcbx_init
===============

.. c:function:: void bnx2x_dcbx_init(struct bnx2x *bp, bool update_shmem)

    initialize dcbx protocol.

    :param struct bnx2x \*bp:
        driver handle

    :param bool update_shmem:
        *undescribed*

.. _`bnx2x_set_power_state`:

bnx2x_set_power_state
=====================

.. c:function:: int bnx2x_set_power_state(struct bnx2x *bp, pci_power_t state)

    set power state to the requested value.

    :param struct bnx2x \*bp:
        driver handle

    :param pci_power_t state:
        required state D0 or D3hot

.. _`bnx2x_set_power_state.description`:

Description
-----------

Currently only D0 and D3hot are supported.

.. _`bnx2x_update_max_mf_config`:

bnx2x_update_max_mf_config
==========================

.. c:function:: void bnx2x_update_max_mf_config(struct bnx2x *bp, u32 value)

    update MAX part of MF configuration in HW.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 value:
        new value

.. _`bnx2x_enable_msix`:

bnx2x_enable_msix
=================

.. c:function:: int bnx2x_enable_msix(struct bnx2x *bp)

    set msix configuration.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_enable_msix.description`:

Description
-----------

fills msix_table, requests vectors, updates num_queues
according to number of available vectors.

.. _`bnx2x_enable_msi`:

bnx2x_enable_msi
================

.. c:function:: int bnx2x_enable_msi(struct bnx2x *bp)

    request msi mode from OS, updated internals accordingly

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_alloc_mem_bp`:

bnx2x_alloc_mem_bp
==================

.. c:function:: int bnx2x_alloc_mem_bp(struct bnx2x *bp)

    allocate memories outsize main driver structure

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_free_mem_bp`:

bnx2x_free_mem_bp
=================

.. c:function:: void bnx2x_free_mem_bp(struct bnx2x *bp)

    release memories outsize main driver structure

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_change_mtu`:

bnx2x_change_mtu
================

.. c:function:: int bnx2x_change_mtu(struct net_device *dev, int new_mtu)

    change mtu netdev callback

    :param struct net_device \*dev:
        net device

    :param int new_mtu:
        requested mtu

.. _`bnx2x_fcoe_get_wwn`:

bnx2x_fcoe_get_wwn
==================

.. c:function:: int bnx2x_fcoe_get_wwn(struct net_device *dev, u64 *wwn, int type)

    return the requested WWN value for this port

    :param struct net_device \*dev:
        net_device

    :param u64 \*wwn:
        output buffer

    :param int type:
        WWN type: NETDEV_FCOE_WWNN (node) or NETDEV_FCOE_WWPN (port)

.. _`bnx2x_tx_timeout`:

bnx2x_tx_timeout
================

.. c:function:: void bnx2x_tx_timeout(struct net_device *dev)

    tx timeout netdev callback

    :param struct net_device \*dev:
        net device

.. _`bnx2x_tx_disable`:

bnx2x_tx_disable
================

.. c:function:: void bnx2x_tx_disable(struct bnx2x *bp)

    disables tx from stack point of view

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_func_start`:

bnx2x_func_start
================

.. c:function:: int bnx2x_func_start(struct bnx2x *bp)

    init function

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_func_start.description`:

Description
-----------

Must be called before sending CLIENT_SETUP for the first client.

.. _`bnx2x_set_fw_mac_addr`:

bnx2x_set_fw_mac_addr
=====================

.. c:function:: void bnx2x_set_fw_mac_addr(__le16 *fw_hi, __le16 *fw_mid, __le16 *fw_lo, u8 *mac)

    fill in a MAC address in FW format

    :param __le16 \*fw_hi:
        pointer to upper part

    :param __le16 \*fw_mid:
        pointer to middle part

    :param __le16 \*fw_lo:
        pointer to lower part

    :param u8 \*mac:
        pointer to MAC address

.. _`bnx2x_get_path_func_num`:

bnx2x_get_path_func_num
=======================

.. c:function:: u8 bnx2x_get_path_func_num(struct bnx2x *bp)

    get number of active functions

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_get_path_func_num.description`:

Description
-----------

Calculates the number of active (not hidden) functions on the
current path.

.. _`bnx2x_wait_sp_comp`:

bnx2x_wait_sp_comp
==================

.. c:function:: bool bnx2x_wait_sp_comp(struct bnx2x *bp, unsigned long mask)

    wait for the outstanding SP commands.

    :param struct bnx2x \*bp:
        driver handle

    :param unsigned long mask:
        bits that need to be cleared

.. _`bnx2x_set_ctx_validation`:

bnx2x_set_ctx_validation
========================

.. c:function:: void bnx2x_set_ctx_validation(struct bnx2x *bp, struct eth_context *cxt, u32 cid)

    set CDU context validation values

    :param struct bnx2x \*bp:
        driver handle

    :param struct eth_context \*cxt:
        context of the connection on the host memory

    :param u32 cid:
        SW CID of the connection to be configured

.. _`bnx2x_extract_max_cfg`:

bnx2x_extract_max_cfg
=====================

.. c:function:: u16 bnx2x_extract_max_cfg(struct bnx2x *bp, u32 mf_cfg)

    extract MAX BW part from MF configuration.

    :param struct bnx2x \*bp:
        driver handle

    :param u32 mf_cfg:
        MF configuration

.. _`bnx2x_get_iscsi_info`:

bnx2x_get_iscsi_info
====================

.. c:function:: void bnx2x_get_iscsi_info(struct bnx2x *bp)

    update iSCSI params according to licensing info.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_link_sync_notify`:

bnx2x_link_sync_notify
======================

.. c:function:: void bnx2x_link_sync_notify(struct bnx2x *bp)

    send notification to other functions.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_update_drv_flags`:

bnx2x_update_drv_flags
======================

.. c:function:: void bnx2x_update_drv_flags(struct bnx2x *bp, u32 flags, u32 set)

    update flags in shmem

    :param struct bnx2x \*bp:
        driver handle

    :param u32 flags:
        flags to update

    :param u32 set:
        set or clear

.. _`bnx2x_fill_fw_str`:

bnx2x_fill_fw_str
=================

.. c:function:: void bnx2x_fill_fw_str(struct bnx2x *bp, char *buf, size_t buf_len)

    Fill buffer with FW version string

    :param struct bnx2x \*bp:
        driver handle

    :param char \*buf:
        character buffer to fill with the fw name

    :param size_t buf_len:
        length of the above buffer

.. _`bnx2x_set_os_driver_state`:

bnx2x_set_os_driver_state
=========================

.. c:function:: void bnx2x_set_os_driver_state(struct bnx2x *bp, u32 state)

    write driver state for management FW usage

    :param struct bnx2x \*bp:
        driver handle

    :param u32 state:
        OS_DRIVER_STATE\_\* value reflecting current driver state

.. _`bnx2x_nvram_read`:

bnx2x_nvram_read
================

.. c:function:: int bnx2x_nvram_read(struct bnx2x *bp, u32 offset, u8 *ret_buf, int buf_size)

    reads data from nvram [might sleep]

    :param struct bnx2x \*bp:
        driver handle

    :param u32 offset:
        byte offset in nvram

    :param u8 \*ret_buf:
        pointer to buffer where data is to be stored

    :param int buf_size:
        Length of 'ret_buf' in bytes

.. This file was automatic generated / don't edit.


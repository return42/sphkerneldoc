.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_main.c

.. _`i40iw_find_i40e_handler`:

i40iw_find_i40e_handler
=======================

.. c:function:: struct i40iw_handler *i40iw_find_i40e_handler(struct i40e_info *ldev)

    find a handler given a client info

    :param ldev:
        pointer to a client info
    :type ldev: struct i40e_info \*

.. _`i40iw_find_netdev`:

i40iw_find_netdev
=================

.. c:function:: struct i40iw_handler *i40iw_find_netdev(struct net_device *netdev)

    find a handler given a netdev

    :param netdev:
        pointer to net_device
    :type netdev: struct net_device \*

.. _`i40iw_add_handler`:

i40iw_add_handler
=================

.. c:function:: void i40iw_add_handler(struct i40iw_handler *hdl)

    add a handler to the list

    :param hdl:
        handler to be added to the handler list
    :type hdl: struct i40iw_handler \*

.. _`i40iw_del_handler`:

i40iw_del_handler
=================

.. c:function:: int i40iw_del_handler(struct i40iw_handler *hdl)

    delete a handler from the list

    :param hdl:
        handler to be deleted from the handler list
    :type hdl: struct i40iw_handler \*

.. _`i40iw_enable_intr`:

i40iw_enable_intr
=================

.. c:function:: void i40iw_enable_intr(struct i40iw_sc_dev *dev, u32 msix_id)

    set up device interrupts

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param msix_id:
        id of the interrupt to be enabled
    :type msix_id: u32

.. _`i40iw_dpc`:

i40iw_dpc
=========

.. c:function:: void i40iw_dpc(unsigned long data)

    tasklet for aeq and ceq 0

    :param data:
        iwarp device
    :type data: unsigned long

.. _`i40iw_ceq_dpc`:

i40iw_ceq_dpc
=============

.. c:function:: void i40iw_ceq_dpc(unsigned long data)

    dpc handler for CEQ

    :param data:
        data points to CEQ
    :type data: unsigned long

.. _`i40iw_irq_handler`:

i40iw_irq_handler
=================

.. c:function:: irqreturn_t i40iw_irq_handler(int irq, void *data)

    interrupt handler for aeq and ceq0

    :param irq:
        Interrupt request number
    :type irq: int

    :param data:
        iwarp device
    :type data: void \*

.. _`i40iw_destroy_cqp`:

i40iw_destroy_cqp
=================

.. c:function:: void i40iw_destroy_cqp(struct i40iw_device *iwdev, bool free_hwcqp)

    destroy control qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param free_hwcqp:
        *undescribed*
    :type free_hwcqp: bool

.. _`i40iw_destroy_cqp.description`:

Description
-----------

Issue destroy cqp request and
free the resources associated with the cqp

.. _`i40iw_disable_irq`:

i40iw_disable_irq
=================

.. c:function:: void i40iw_disable_irq(struct i40iw_sc_dev *dev, struct i40iw_msix_vector *msix_vec, void *dev_id)

    disable device interrupts

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param msix_vec:
        *undescribed*
    :type msix_vec: struct i40iw_msix_vector \*

    :param dev_id:
        parameter to pass to free_irq (used during irq setup)
    :type dev_id: void \*

.. _`i40iw_disable_irq.description`:

Description
-----------

The function is called when destroying aeq/ceq

.. _`i40iw_destroy_aeq`:

i40iw_destroy_aeq
=================

.. c:function:: void i40iw_destroy_aeq(struct i40iw_device *iwdev)

    destroy aeq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_destroy_aeq.description`:

Description
-----------

Issue a destroy aeq request and
free the resources associated with the aeq
The function is called during driver unload

.. _`i40iw_destroy_ceq`:

i40iw_destroy_ceq
=================

.. c:function:: void i40iw_destroy_ceq(struct i40iw_device *iwdev, struct i40iw_ceq *iwceq)

    destroy ceq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwceq:
        ceq to be destroyed
    :type iwceq: struct i40iw_ceq \*

.. _`i40iw_destroy_ceq.description`:

Description
-----------

Issue a destroy ceq request and
free the resources associated with the ceq

.. _`i40iw_dele_ceqs`:

i40iw_dele_ceqs
===============

.. c:function:: void i40iw_dele_ceqs(struct i40iw_device *iwdev)

    destroy all ceq's

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_dele_ceqs.description`:

Description
-----------

Go through all of the device ceq's and for each ceq
disable the ceq interrupt and destroy the ceq

.. _`i40iw_destroy_ccq`:

i40iw_destroy_ccq
=================

.. c:function:: void i40iw_destroy_ccq(struct i40iw_device *iwdev)

    destroy control cq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_destroy_ccq.description`:

Description
-----------

Issue destroy ccq request and
free the resources associated with the ccq

.. _`i40iw_close_hmc_objects_type`:

i40iw_close_hmc_objects_type
============================

.. c:function:: void i40iw_close_hmc_objects_type(struct i40iw_sc_dev *dev, enum i40iw_hmc_rsrc_type obj_type, struct i40iw_hmc_info *hmc_info, bool is_pf, bool reset)

    delete hmc objects of a given type

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param obj_type:
        the hmc object type to be deleted
    :type obj_type: enum i40iw_hmc_rsrc_type

    :param hmc_info:
        *undescribed*
    :type hmc_info: struct i40iw_hmc_info \*

    :param is_pf:
        true if the function is PF otherwise false
    :type is_pf: bool

    :param reset:
        true if called before reset
    :type reset: bool

.. _`i40iw_del_hmc_objects`:

i40iw_del_hmc_objects
=====================

.. c:function:: void i40iw_del_hmc_objects(struct i40iw_sc_dev *dev, struct i40iw_hmc_info *hmc_info, bool is_pf, bool reset)

    remove all device hmc objects

    :param dev:
        iwarp device
    :type dev: struct i40iw_sc_dev \*

    :param hmc_info:
        hmc_info to free
    :type hmc_info: struct i40iw_hmc_info \*

    :param is_pf:
        true if hmc_info belongs to PF, not vf nor allocated
        by PF on behalf of VF
    :type is_pf: bool

    :param reset:
        true if called before reset
    :type reset: bool

.. _`i40iw_ceq_handler`:

i40iw_ceq_handler
=================

.. c:function:: irqreturn_t i40iw_ceq_handler(int irq, void *data)

    interrupt handler for ceq

    :param irq:
        *undescribed*
    :type irq: int

    :param data:
        ceq pointer
    :type data: void \*

.. _`i40iw_create_hmc_obj_type`:

i40iw_create_hmc_obj_type
=========================

.. c:function:: enum i40iw_status_code i40iw_create_hmc_obj_type(struct i40iw_sc_dev *dev, struct i40iw_hmc_create_obj_info *info)

    create hmc object of a given type

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param info:
        information for the hmc object to create
    :type info: struct i40iw_hmc_create_obj_info \*

.. _`i40iw_create_hmc_objs`:

i40iw_create_hmc_objs
=====================

.. c:function:: enum i40iw_status_code i40iw_create_hmc_objs(struct i40iw_device *iwdev, bool is_pf)

    create all hmc objects for the device

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param is_pf:
        true if the function is PF otherwise false
    :type is_pf: bool

.. _`i40iw_create_hmc_objs.description`:

Description
-----------

Create the device hmc objects and allocate hmc pages
Return 0 if successful, otherwise clean up and return error

.. _`i40iw_obj_aligned_mem`:

i40iw_obj_aligned_mem
=====================

.. c:function:: enum i40iw_status_code i40iw_obj_aligned_mem(struct i40iw_device *iwdev, struct i40iw_dma_mem *memptr, u32 size, u32 mask)

    get aligned memory from device allocated memory

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param memptr:
        points to the memory addresses
    :type memptr: struct i40iw_dma_mem \*

    :param size:
        size of memory needed
    :type size: u32

    :param mask:
        mask for the aligned memory
    :type mask: u32

.. _`i40iw_obj_aligned_mem.description`:

Description
-----------

Get aligned memory of the requested size and
update the memptr to point to the new aligned memory
Return 0 if successful, otherwise return no memory error

.. _`i40iw_create_cqp`:

i40iw_create_cqp
================

.. c:function:: enum i40iw_status_code i40iw_create_cqp(struct i40iw_device *iwdev)

    create control qp

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_create_cqp.description`:

Description
-----------

Return 0, if the cqp and all the resources associated with it
are successfully created, otherwise return error

.. _`i40iw_create_ccq`:

i40iw_create_ccq
================

.. c:function:: enum i40iw_status_code i40iw_create_ccq(struct i40iw_device *iwdev)

    create control cq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_create_ccq.description`:

Description
-----------

Return 0, if the ccq and the resources associated with it
are successfully created, otherwise return error

.. _`i40iw_configure_ceq_vector`:

i40iw_configure_ceq_vector
==========================

.. c:function:: enum i40iw_status_code i40iw_configure_ceq_vector(struct i40iw_device *iwdev, struct i40iw_ceq *iwceq, u32 ceq_id, struct i40iw_msix_vector *msix_vec)

    set up the msix interrupt vector for ceq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwceq:
        ceq associated with the vector
    :type iwceq: struct i40iw_ceq \*

    :param ceq_id:
        the id number of the iwceq
    :type ceq_id: u32

    :param msix_vec:
        interrupt vector information
    :type msix_vec: struct i40iw_msix_vector \*

.. _`i40iw_configure_ceq_vector.description`:

Description
-----------

Allocate interrupt resources and enable irq handling
Return 0 if successful, otherwise return error

.. _`i40iw_create_ceq`:

i40iw_create_ceq
================

.. c:function:: enum i40iw_status_code i40iw_create_ceq(struct i40iw_device *iwdev, struct i40iw_ceq *iwceq, u32 ceq_id)

    create completion event queue

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param iwceq:
        pointer to the ceq resources to be created
    :type iwceq: struct i40iw_ceq \*

    :param ceq_id:
        the id number of the iwceq
    :type ceq_id: u32

.. _`i40iw_create_ceq.description`:

Description
-----------

Return 0, if the ceq and the resources associated with it
are successfully created, otherwise return error

.. _`i40iw_setup_ceqs`:

i40iw_setup_ceqs
================

.. c:function:: enum i40iw_status_code i40iw_setup_ceqs(struct i40iw_device *iwdev, struct i40e_info *ldev)

    manage the device ceq's and their interrupt resources

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param ldev:
        i40e lan device
    :type ldev: struct i40e_info \*

.. _`i40iw_setup_ceqs.description`:

Description
-----------

Allocate a list for all device completion event queues
Create the ceq's and configure their msix interrupt vectors
Return 0, if at least one ceq is successfully set up, otherwise return error

.. _`i40iw_configure_aeq_vector`:

i40iw_configure_aeq_vector
==========================

.. c:function:: enum i40iw_status_code i40iw_configure_aeq_vector(struct i40iw_device *iwdev)

    set up the msix vector for aeq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_configure_aeq_vector.description`:

Description
-----------

Allocate interrupt resources and enable irq handling
Return 0 if successful, otherwise return error

.. _`i40iw_create_aeq`:

i40iw_create_aeq
================

.. c:function:: enum i40iw_status_code i40iw_create_aeq(struct i40iw_device *iwdev)

    create async event queue

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_create_aeq.description`:

Description
-----------

Return 0, if the aeq and the resources associated with it
are successfully created, otherwise return error

.. _`i40iw_setup_aeq`:

i40iw_setup_aeq
===============

.. c:function:: enum i40iw_status_code i40iw_setup_aeq(struct i40iw_device *iwdev)

    set up the device aeq

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_setup_aeq.description`:

Description
-----------

Create the aeq and configure its msix interrupt vector
Return 0 if successful, otherwise return error

.. _`i40iw_initialize_ilq`:

i40iw_initialize_ilq
====================

.. c:function:: enum i40iw_status_code i40iw_initialize_ilq(struct i40iw_device *iwdev)

    create iwarp local queue for cm

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_initialize_ilq.description`:

Description
-----------

Return 0 if successful, otherwise return error

.. _`i40iw_initialize_ieq`:

i40iw_initialize_ieq
====================

.. c:function:: enum i40iw_status_code i40iw_initialize_ieq(struct i40iw_device *iwdev)

    create iwarp exception queue

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_initialize_ieq.description`:

Description
-----------

Return 0 if successful, otherwise return error

.. _`i40iw_reinitialize_ieq`:

i40iw_reinitialize_ieq
======================

.. c:function:: void i40iw_reinitialize_ieq(struct i40iw_sc_dev *dev)

    destroy and re-create ieq

    :param dev:
        iwarp device
    :type dev: struct i40iw_sc_dev \*

.. _`i40iw_hmc_setup`:

i40iw_hmc_setup
===============

.. c:function:: enum i40iw_status_code i40iw_hmc_setup(struct i40iw_device *iwdev)

    create hmc objects for the device

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_hmc_setup.description`:

Description
-----------

Set up the device private memory space for the number and size of
the hmc objects and create the objects
Return 0 if successful, otherwise return error

.. _`i40iw_del_init_mem`:

i40iw_del_init_mem
==================

.. c:function:: void i40iw_del_init_mem(struct i40iw_device *iwdev)

    deallocate memory resources

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_del_macip_entry`:

i40iw_del_macip_entry
=====================

.. c:function:: void i40iw_del_macip_entry(struct i40iw_device *iwdev, u8 idx)

    remove a mac ip address entry from the hw table

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param idx:
        the index of the mac ip address to delete
    :type idx: u8

.. _`i40iw_add_mac_ipaddr_entry`:

i40iw_add_mac_ipaddr_entry
==========================

.. c:function:: enum i40iw_status_code i40iw_add_mac_ipaddr_entry(struct i40iw_device *iwdev, u8 *mac_addr, u8 idx)

    add a mac ip address entry to the hw table

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param mac_addr:
        pointer to mac address
    :type mac_addr: u8 \*

    :param idx:
        the index of the mac ip address to add
    :type idx: u8

.. _`i40iw_alloc_local_mac_ipaddr_entry`:

i40iw_alloc_local_mac_ipaddr_entry
==================================

.. c:function:: enum i40iw_status_code i40iw_alloc_local_mac_ipaddr_entry(struct i40iw_device *iwdev, u16 *mac_ip_tbl_idx)

    allocate a mac ip address entry

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param mac_ip_tbl_idx:
        the index of the new mac ip address
    :type mac_ip_tbl_idx: u16 \*

.. _`i40iw_alloc_local_mac_ipaddr_entry.description`:

Description
-----------

Allocate a mac ip address entry and update the mac_ip_tbl_idx
to hold the index of the newly created mac ip address
Return 0 if successful, otherwise return error

.. _`i40iw_alloc_set_mac_ipaddr`:

i40iw_alloc_set_mac_ipaddr
==========================

.. c:function:: enum i40iw_status_code i40iw_alloc_set_mac_ipaddr(struct i40iw_device *iwdev, u8 *macaddr)

    set up a mac ip address table entry

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param macaddr:
        pointer to mac address
    :type macaddr: u8 \*

.. _`i40iw_alloc_set_mac_ipaddr.description`:

Description
-----------

Allocate a mac ip address entry and add it to the hw table
Return 0 if successful, otherwise return error

.. _`i40iw_add_ipv6_addr`:

i40iw_add_ipv6_addr
===================

.. c:function:: void i40iw_add_ipv6_addr(struct i40iw_device *iwdev)

    add ipv6 address to the hw arp table

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_add_ipv4_addr`:

i40iw_add_ipv4_addr
===================

.. c:function:: void i40iw_add_ipv4_addr(struct i40iw_device *iwdev)

    add ipv4 address to the hw arp table

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_add_mac_ip`:

i40iw_add_mac_ip
================

.. c:function:: enum i40iw_status_code i40iw_add_mac_ip(struct i40iw_device *iwdev)

    add mac and ip addresses

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_add_mac_ip.description`:

Description
-----------

Create and add a mac ip address entry to the hw table and
ipv4/ipv6 addresses to the arp cache
Return 0 if successful, otherwise return error

.. _`i40iw_wait_pe_ready`:

i40iw_wait_pe_ready
===================

.. c:function:: void i40iw_wait_pe_ready(struct i40iw_hw *hw)

    Check if firmware is ready

    :param hw:
        provides access to registers
    :type hw: struct i40iw_hw \*

.. _`i40iw_initialize_dev`:

i40iw_initialize_dev
====================

.. c:function:: enum i40iw_status_code i40iw_initialize_dev(struct i40iw_device *iwdev, struct i40e_info *ldev)

    initialize device

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

.. _`i40iw_initialize_dev.description`:

Description
-----------

Allocate memory for the hmc objects and initialize iwdev
Return 0 if successful, otherwise clean up the resources
and return error

.. _`i40iw_register_notifiers`:

i40iw_register_notifiers
========================

.. c:function:: void i40iw_register_notifiers( void)

    register tcp ip notifiers

    :param void:
        no arguments
    :type void: 

.. _`i40iw_unregister_notifiers`:

i40iw_unregister_notifiers
==========================

.. c:function:: void i40iw_unregister_notifiers( void)

    unregister tcp ip notifiers

    :param void:
        no arguments
    :type void: 

.. _`i40iw_save_msix_info`:

i40iw_save_msix_info
====================

.. c:function:: enum i40iw_status_code i40iw_save_msix_info(struct i40iw_device *iwdev, struct i40e_info *ldev)

    copy msix vector information to iwarp device

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

.. _`i40iw_save_msix_info.description`:

Description
-----------

Allocate iwdev msix table and copy the ldev msix info to the table
Return 0 if successful, otherwise return error

.. _`i40iw_deinit_device`:

i40iw_deinit_device
===================

.. c:function:: void i40iw_deinit_device(struct i40iw_device *iwdev)

    clean up the device resources

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_deinit_device.description`:

Description
-----------

Destroy the ib device interface, remove the mac ip entry and ipv4/ipv6 addresses,
destroy the device queues and free the pble and the hmc objects

.. _`i40iw_setup_init_state`:

i40iw_setup_init_state
======================

.. c:function:: enum i40iw_status_code i40iw_setup_init_state(struct i40iw_handler *hdl, struct i40e_info *ldev, struct i40e_client *client)

    set up the initial device struct

    :param hdl:
        handler for iwarp device - one per instance
    :type hdl: struct i40iw_handler \*

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        iwarp client information, provided during registration
    :type client: struct i40e_client \*

.. _`i40iw_setup_init_state.description`:

Description
-----------

Initialize the iwarp device and its hdl information
using the ldev and client information
Return 0 if successful, otherwise return error

.. _`i40iw_get_used_rsrc`:

i40iw_get_used_rsrc
===================

.. c:function:: void i40iw_get_used_rsrc(struct i40iw_device *iwdev)

    determine resources used internally

    :param iwdev:
        iwarp device
    :type iwdev: struct i40iw_device \*

.. _`i40iw_get_used_rsrc.description`:

Description
-----------

Called after internal allocations

.. _`i40iw_open`:

i40iw_open
==========

.. c:function:: int i40iw_open(struct i40e_info *ldev, struct i40e_client *client)

    client interface operation open for iwarp/uda device

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        iwarp client information, provided during registration
    :type client: struct i40e_client \*

.. _`i40iw_open.description`:

Description
-----------

Called by the lan driver during the processing of client register
Create device resources, set up queues, pble and hmc objects and
register the device with the ib verbs interface
Return 0 if successful, otherwise return error

.. _`i40iw_l2params_worker`:

i40iw_l2params_worker
=====================

.. c:function:: void i40iw_l2params_worker(struct work_struct *work)

    worker for l2 params change

    :param work:
        work pointer for l2 params
    :type work: struct work_struct \*

.. _`i40iw_l2param_change`:

i40iw_l2param_change
====================

.. c:function:: void i40iw_l2param_change(struct i40e_info *ldev, struct i40e_client *client, struct i40e_params *params)

    handle qs handles for qos and mss change

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        client for paramater change
    :type client: struct i40e_client \*

    :param params:
        new parameters from L2
    :type params: struct i40e_params \*

.. _`i40iw_close`:

i40iw_close
===========

.. c:function:: void i40iw_close(struct i40e_info *ldev, struct i40e_client *client, bool reset)

    client interface operation close for iwarp/uda device

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        client to close
    :type client: struct i40e_client \*

    :param reset:
        *undescribed*
    :type reset: bool

.. _`i40iw_close.description`:

Description
-----------

Called by the lan driver during the processing of client unregister
Destroy and clean up the driver resources

.. _`i40iw_vf_reset`:

i40iw_vf_reset
==============

.. c:function:: void i40iw_vf_reset(struct i40e_info *ldev, struct i40e_client *client, u32 vf_id)

    process VF reset

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        client interface instance
    :type client: struct i40e_client \*

    :param vf_id:
        virtual function id
    :type vf_id: u32

.. _`i40iw_vf_reset.description`:

Description
-----------

Called when a VF is reset by the PF
Destroy and clean up the VF resources

.. _`i40iw_vf_enable`:

i40iw_vf_enable
===============

.. c:function:: void i40iw_vf_enable(struct i40e_info *ldev, struct i40e_client *client, u32 num_vfs)

    enable a number of VFs

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        client interface instance
    :type client: struct i40e_client \*

    :param num_vfs:
        number of VFs for the PF
    :type num_vfs: u32

.. _`i40iw_vf_enable.description`:

Description
-----------

Called when the number of VFs changes

.. _`i40iw_vf_capable`:

i40iw_vf_capable
================

.. c:function:: int i40iw_vf_capable(struct i40e_info *ldev, struct i40e_client *client, u32 vf_id)

    check if VF capable

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        client interface instance
    :type client: struct i40e_client \*

    :param vf_id:
        virtual function id
    :type vf_id: u32

.. _`i40iw_vf_capable.description`:

Description
-----------

Return 1 if a VF slot is available or if VF is already RDMA enabled
Return 0 otherwise

.. _`i40iw_virtchnl_receive`:

i40iw_virtchnl_receive
======================

.. c:function:: int i40iw_virtchnl_receive(struct i40e_info *ldev, struct i40e_client *client, u32 vf_id, u8 *msg, u16 len)

    receive a message through the virtual channel

    :param ldev:
        lan device information
    :type ldev: struct i40e_info \*

    :param client:
        client interface instance
    :type client: struct i40e_client \*

    :param vf_id:
        virtual function id associated with the message
    :type vf_id: u32

    :param msg:
        message buffer pointer
    :type msg: u8 \*

    :param len:
        length of the message
    :type len: u16

.. _`i40iw_virtchnl_receive.description`:

Description
-----------

Invoke virtual channel receive operation for the given msg
Return 0 if successful, otherwise return error

.. _`i40iw_vf_clear_to_send`:

i40iw_vf_clear_to_send
======================

.. c:function:: bool i40iw_vf_clear_to_send(struct i40iw_sc_dev *dev)

    wait to send virtual channel message

    :param dev:
        iwarp device \*
        Wait for until virtual channel is clear
        before sending the next message
    :type dev: struct i40iw_sc_dev \*

.. _`i40iw_vf_clear_to_send.description`:

Description
-----------

Returns false if error
Returns true if clear to send

.. _`i40iw_virtchnl_send`:

i40iw_virtchnl_send
===================

.. c:function:: enum i40iw_status_code i40iw_virtchnl_send(struct i40iw_sc_dev *dev, u32 vf_id, u8 *msg, u16 len)

    send a message through the virtual channel

    :param dev:
        iwarp device
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        virtual function id associated with the message
    :type vf_id: u32

    :param msg:
        virtual channel message buffer pointer
    :type msg: u8 \*

    :param len:
        length of the message
    :type len: u16

.. _`i40iw_virtchnl_send.description`:

Description
-----------

Invoke virtual channel send operation for the given msg
Return 0 if successful, otherwise return error

.. _`i40iw_init_module`:

i40iw_init_module
=================

.. c:function:: int i40iw_init_module( void)

    driver initialization function

    :param void:
        no arguments
    :type void: 

.. _`i40iw_init_module.description`:

Description
-----------

First function to call when the driver is loaded
Register the driver as i40e client and port mapper client

.. _`i40iw_exit_module`:

i40iw_exit_module
=================

.. c:function:: void __exit i40iw_exit_module( void)

    driver exit clean up function

    :param void:
        no arguments
    :type void: 

.. _`i40iw_exit_module.description`:

Description
-----------

The function is called just before the driver is unloaded
Unregister the driver as i40e client and port mapper client

.. This file was automatic generated / don't edit.


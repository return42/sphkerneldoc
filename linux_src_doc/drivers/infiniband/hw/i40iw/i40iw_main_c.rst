.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_main.c

.. _`i40iw_find_i40e_handler`:

i40iw_find_i40e_handler
=======================

.. c:function:: struct i40iw_handler *i40iw_find_i40e_handler(struct i40e_info *ldev)

    find a handler given a client info

    :param struct i40e_info \*ldev:
        pointer to a client info

.. _`i40iw_find_netdev`:

i40iw_find_netdev
=================

.. c:function:: struct i40iw_handler *i40iw_find_netdev(struct net_device *netdev)

    find a handler given a netdev

    :param struct net_device \*netdev:
        pointer to net_device

.. _`i40iw_add_handler`:

i40iw_add_handler
=================

.. c:function:: void i40iw_add_handler(struct i40iw_handler *hdl)

    add a handler to the list

    :param struct i40iw_handler \*hdl:
        handler to be added to the handler list

.. _`i40iw_del_handler`:

i40iw_del_handler
=================

.. c:function:: int i40iw_del_handler(struct i40iw_handler *hdl)

    delete a handler from the list

    :param struct i40iw_handler \*hdl:
        handler to be deleted from the handler list

.. _`i40iw_enable_intr`:

i40iw_enable_intr
=================

.. c:function:: void i40iw_enable_intr(struct i40iw_sc_dev *dev, u32 msix_id)

    set up device interrupts

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param u32 msix_id:
        id of the interrupt to be enabled

.. _`i40iw_dpc`:

i40iw_dpc
=========

.. c:function:: void i40iw_dpc(unsigned long data)

    tasklet for aeq and ceq 0

    :param unsigned long data:
        iwarp device

.. _`i40iw_ceq_dpc`:

i40iw_ceq_dpc
=============

.. c:function:: void i40iw_ceq_dpc(unsigned long data)

    dpc handler for CEQ

    :param unsigned long data:
        data points to CEQ

.. _`i40iw_irq_handler`:

i40iw_irq_handler
=================

.. c:function:: irqreturn_t i40iw_irq_handler(int irq, void *data)

    interrupt handler for aeq and ceq0

    :param int irq:
        Interrupt request number

    :param void \*data:
        iwarp device

.. _`i40iw_destroy_cqp`:

i40iw_destroy_cqp
=================

.. c:function:: void i40iw_destroy_cqp(struct i40iw_device *iwdev, bool free_hwcqp)

    destroy control qp

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param bool free_hwcqp:
        *undescribed*

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

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_msix_vector \*msix_vec:
        *undescribed*

    :param void \*dev_id:
        parameter to pass to free_irq (used during irq setup)

.. _`i40iw_disable_irq.description`:

Description
-----------

The function is called when destroying aeq/ceq

.. _`i40iw_destroy_aeq`:

i40iw_destroy_aeq
=================

.. c:function:: void i40iw_destroy_aeq(struct i40iw_device *iwdev)

    destroy aeq

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_ceq \*iwceq:
        ceq to be destroyed

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param enum i40iw_hmc_rsrc_type obj_type:
        the hmc object type to be deleted

    :param struct i40iw_hmc_info \*hmc_info:
        *undescribed*

    :param bool is_pf:
        true if the function is PF otherwise false

    :param bool reset:
        true if called before reset

.. _`i40iw_del_hmc_objects`:

i40iw_del_hmc_objects
=====================

.. c:function:: void i40iw_del_hmc_objects(struct i40iw_sc_dev *dev, struct i40iw_hmc_info *hmc_info, bool is_pf, bool reset)

    remove all device hmc objects

    :param struct i40iw_sc_dev \*dev:
        iwarp device

    :param struct i40iw_hmc_info \*hmc_info:
        hmc_info to free

    :param bool is_pf:
        true if hmc_info belongs to PF, not vf nor allocated
        by PF on behalf of VF

    :param bool reset:
        true if called before reset

.. _`i40iw_ceq_handler`:

i40iw_ceq_handler
=================

.. c:function:: irqreturn_t i40iw_ceq_handler(int irq, void *data)

    interrupt handler for ceq

    :param int irq:
        *undescribed*

    :param void \*data:
        ceq pointer

.. _`i40iw_create_hmc_obj_type`:

i40iw_create_hmc_obj_type
=========================

.. c:function:: enum i40iw_status_code i40iw_create_hmc_obj_type(struct i40iw_sc_dev *dev, struct i40iw_hmc_create_obj_info *info)

    create hmc object of a given type

    :param struct i40iw_sc_dev \*dev:
        hardware control device structure

    :param struct i40iw_hmc_create_obj_info \*info:
        information for the hmc object to create

.. _`i40iw_create_hmc_objs`:

i40iw_create_hmc_objs
=====================

.. c:function:: enum i40iw_status_code i40iw_create_hmc_objs(struct i40iw_device *iwdev, bool is_pf)

    create all hmc objects for the device

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param bool is_pf:
        true if the function is PF otherwise false

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

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_dma_mem \*memptr:
        points to the memory addresses

    :param u32 size:
        size of memory needed

    :param u32 mask:
        mask for the aligned memory

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_ceq \*iwceq:
        ceq associated with the vector

    :param u32 ceq_id:
        the id number of the iwceq

    :param struct i40iw_msix_vector \*msix_vec:
        interrupt vector information

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

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40iw_ceq \*iwceq:
        pointer to the ceq resources to be created

    :param u32 ceq_id:
        the id number of the iwceq

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

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40e_info \*ldev:
        i40e lan device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_initialize_ilq.description`:

Description
-----------

Return 0 if successful, otherwise return error

.. _`i40iw_initialize_ieq`:

i40iw_initialize_ieq
====================

.. c:function:: enum i40iw_status_code i40iw_initialize_ieq(struct i40iw_device *iwdev)

    create iwarp exception queue

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_initialize_ieq.description`:

Description
-----------

Return 0 if successful, otherwise return error

.. _`i40iw_hmc_setup`:

i40iw_hmc_setup
===============

.. c:function:: enum i40iw_status_code i40iw_hmc_setup(struct i40iw_device *iwdev)

    create hmc objects for the device

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_del_macip_entry`:

i40iw_del_macip_entry
=====================

.. c:function:: void i40iw_del_macip_entry(struct i40iw_device *iwdev, u8 idx)

    remove a mac ip address entry from the hw table

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u8 idx:
        the index of the mac ip address to delete

.. _`i40iw_add_mac_ipaddr_entry`:

i40iw_add_mac_ipaddr_entry
==========================

.. c:function:: enum i40iw_status_code i40iw_add_mac_ipaddr_entry(struct i40iw_device *iwdev, u8 *mac_addr, u8 idx)

    add a mac ip address entry to the hw table

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u8 \*mac_addr:
        pointer to mac address

    :param u8 idx:
        the index of the mac ip address to add

.. _`i40iw_alloc_local_mac_ipaddr_entry`:

i40iw_alloc_local_mac_ipaddr_entry
==================================

.. c:function:: enum i40iw_status_code i40iw_alloc_local_mac_ipaddr_entry(struct i40iw_device *iwdev, u16 *mac_ip_tbl_idx)

    allocate a mac ip address entry

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u16 \*mac_ip_tbl_idx:
        the index of the new mac ip address

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

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param u8 \*macaddr:
        pointer to mac address

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

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_add_ipv4_addr`:

i40iw_add_ipv4_addr
===================

.. c:function:: void i40iw_add_ipv4_addr(struct i40iw_device *iwdev)

    add ipv4 address to the hw arp table

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_add_mac_ip`:

i40iw_add_mac_ip
================

.. c:function:: enum i40iw_status_code i40iw_add_mac_ip(struct i40iw_device *iwdev)

    add mac and ip addresses

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_hw \*hw:
        provides access to registers

.. _`i40iw_initialize_dev`:

i40iw_initialize_dev
====================

.. c:function:: enum i40iw_status_code i40iw_initialize_dev(struct i40iw_device *iwdev, struct i40e_info *ldev)

    initialize device

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40e_info \*ldev:
        lan device information

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

    :param  void:
        no arguments

.. _`i40iw_save_msix_info`:

i40iw_save_msix_info
====================

.. c:function:: enum i40iw_status_code i40iw_save_msix_info(struct i40iw_device *iwdev, struct i40e_info *ldev)

    copy msix vector information to iwarp device

    :param struct i40iw_device \*iwdev:
        iwarp device

    :param struct i40e_info \*ldev:
        lan device information

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

    :param struct i40iw_device \*iwdev:
        iwarp device

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

    :param struct i40iw_handler \*hdl:
        handler for iwarp device - one per instance

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        iwarp client information, provided during registration

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

    :param struct i40iw_device \*iwdev:
        iwarp device

.. _`i40iw_get_used_rsrc.description`:

Description
-----------

Called after internal allocations

.. _`i40iw_open`:

i40iw_open
==========

.. c:function:: int i40iw_open(struct i40e_info *ldev, struct i40e_client *client)

    client interface operation open for iwarp/uda device

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        iwarp client information, provided during registration

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

    :param struct work_struct \*work:
        work pointer for l2 params

.. _`i40iw_l2param_change`:

i40iw_l2param_change
====================

.. c:function:: void i40iw_l2param_change(struct i40e_info *ldev, struct i40e_client *client, struct i40e_params *params)

    handle qs handles for qos and mss change

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        client for paramater change

    :param struct i40e_params \*params:
        new parameters from L2

.. _`i40iw_close`:

i40iw_close
===========

.. c:function:: void i40iw_close(struct i40e_info *ldev, struct i40e_client *client, bool reset)

    client interface operation close for iwarp/uda device

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        client to close

    :param bool reset:
        *undescribed*

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

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        client interface instance

    :param u32 vf_id:
        virtual function id

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

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        client interface instance

    :param u32 num_vfs:
        number of VFs for the PF

.. _`i40iw_vf_enable.description`:

Description
-----------

Called when the number of VFs changes

.. _`i40iw_vf_capable`:

i40iw_vf_capable
================

.. c:function:: int i40iw_vf_capable(struct i40e_info *ldev, struct i40e_client *client, u32 vf_id)

    check if VF capable

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        client interface instance

    :param u32 vf_id:
        virtual function id

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

    :param struct i40e_info \*ldev:
        lan device information

    :param struct i40e_client \*client:
        client interface instance

    :param u32 vf_id:
        virtual function id associated with the message

    :param u8 \*msg:
        message buffer pointer

    :param u16 len:
        length of the message

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

    :param struct i40iw_sc_dev \*dev:
        iwarp device \*
        Wait for until virtual channel is clear
        before sending the next message

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

    :param struct i40iw_sc_dev \*dev:
        iwarp device

    :param u32 vf_id:
        virtual function id associated with the message

    :param u8 \*msg:
        virtual channel message buffer pointer

    :param u16 len:
        length of the message

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

.. _`i40iw_exit_module.description`:

Description
-----------

The function is called just before the driver is unloaded
Unregister the driver as i40e client and port mapper client

.. This file was automatic generated / don't edit.


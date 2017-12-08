.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ibmvscsi/ibmvscsi.c

.. _`ibmvscsi_handle_event`:

ibmvscsi_handle_event
=====================

.. c:function:: irqreturn_t ibmvscsi_handle_event(int irq, void *dev_instance)

    - Interrupt handler for crq events

    :param int irq:
        number of irq to handle, not used

    :param void \*dev_instance:
        ibmvscsi_host_data of host that received interrupt

.. _`ibmvscsi_handle_event.description`:

Description
-----------

Disables interrupts and schedules srp_task
Always returns IRQ_HANDLED

.. _`ibmvscsi_release_crq_queue`:

ibmvscsi_release_crq_queue
==========================

.. c:function:: void ibmvscsi_release_crq_queue(struct crq_queue *queue, struct ibmvscsi_host_data *hostdata, int max_requests)

    - Deallocates data and unregisters CRQ

    :param struct crq_queue \*queue:
        crq_queue to initialize and register

    :param struct ibmvscsi_host_data \*hostdata:
        *undescribed*

    :param int max_requests:
        *undescribed*

.. _`ibmvscsi_release_crq_queue.description`:

Description
-----------

Frees irq, deallocates a page for messages, unmaps dma, and unregisters
the crq with the hypervisor.

.. _`crq_queue_next_crq`:

crq_queue_next_crq
==================

.. c:function:: struct viosrp_crq *crq_queue_next_crq(struct crq_queue *queue)

    - Returns the next entry in message queue

    :param struct crq_queue \*queue:
        crq_queue to use

.. _`crq_queue_next_crq.description`:

Description
-----------

Returns pointer to next entry in queue, or NULL if there are no new
entried in the CRQ.

.. _`ibmvscsi_send_crq`:

ibmvscsi_send_crq
=================

.. c:function:: int ibmvscsi_send_crq(struct ibmvscsi_host_data *hostdata, u64 word1, u64 word2)

    - Send a CRQ

    :param struct ibmvscsi_host_data \*hostdata:
        the adapter

    :param u64 word1:
        the first 64 bits of the data

    :param u64 word2:
        the second 64 bits of the data

.. _`ibmvscsi_task`:

ibmvscsi_task
=============

.. c:function:: void ibmvscsi_task(void *data)

    - Process srps asynchronously

    :param void \*data:
        ibmvscsi_host_data of host

.. _`ibmvscsi_reset_crq_queue`:

ibmvscsi_reset_crq_queue
========================

.. c:function:: int ibmvscsi_reset_crq_queue(struct crq_queue *queue, struct ibmvscsi_host_data *hostdata)

    - resets a crq after a failure

    :param struct crq_queue \*queue:
        crq_queue to initialize and register

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`ibmvscsi_init_crq_queue`:

ibmvscsi_init_crq_queue
=======================

.. c:function:: int ibmvscsi_init_crq_queue(struct crq_queue *queue, struct ibmvscsi_host_data *hostdata, int max_requests)

    - Initializes and registers CRQ with hypervisor

    :param struct crq_queue \*queue:
        crq_queue to initialize and register

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

    :param int max_requests:
        *undescribed*

.. _`ibmvscsi_init_crq_queue.description`:

Description
-----------

Allocates a page for messages, maps it for dma, and registers
the crq with the hypervisor.
Returns zero on success.

.. _`ibmvscsi_reenable_crq_queue`:

ibmvscsi_reenable_crq_queue
===========================

.. c:function:: int ibmvscsi_reenable_crq_queue(struct crq_queue *queue, struct ibmvscsi_host_data *hostdata)

    - reenables a crq after

    :param struct crq_queue \*queue:
        crq_queue to initialize and register

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`initialize_event_pool`:

initialize_event_pool
=====================

.. c:function:: int initialize_event_pool(struct event_pool *pool, int size, struct ibmvscsi_host_data *hostdata)

    - Allocates and initializes the event pool for a host

    :param struct event_pool \*pool:
        event_pool to be initialized

    :param int size:
        Number of events in pool

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data who owns the event pool

.. _`initialize_event_pool.description`:

Description
-----------

Returns zero on success.

.. _`release_event_pool`:

release_event_pool
==================

.. c:function:: void release_event_pool(struct event_pool *pool, struct ibmvscsi_host_data *hostdata)

    - Frees memory of an event pool of a host

    :param struct event_pool \*pool:
        event_pool to be released

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data who owns the even pool

.. _`release_event_pool.description`:

Description
-----------

Returns zero on success.

.. _`valid_event_struct`:

valid_event_struct
==================

.. c:function:: int valid_event_struct(struct event_pool *pool, struct srp_event_struct *evt)

    - Determines if event is valid.

    :param struct event_pool \*pool:
        event_pool that contains the event

    :param struct srp_event_struct \*evt:
        srp_event_struct to be checked for validity

.. _`valid_event_struct.description`:

Description
-----------

Returns zero if event is invalid, one otherwise.

.. _`free_event_struct`:

free_event_struct
=================

.. c:function:: void free_event_struct(struct event_pool *pool, struct srp_event_struct *evt)

    event_struct: - Changes status of event to "free"

    :param struct event_pool \*pool:
        event_pool that contains the event

    :param struct srp_event_struct \*evt:
        srp_event_struct to be modified

.. _`get_event_struct`:

get_event_struct
================

.. c:function:: struct srp_event_struct *get_event_struct(struct event_pool *pool)

    - Gets the next free event in pool

    :param struct event_pool \*pool:
        event_pool that contains the events to be searched

.. _`get_event_struct.description`:

Description
-----------

Returns the next event in "free" state, and NULL if none are free.
Note that no synchronization is done here, we assume the host_lock
will syncrhonze things.

.. _`init_event_struct`:

init_event_struct
=================

.. c:function:: void init_event_struct(struct srp_event_struct *evt_struct, void (*done)(struct srp_event_struct *), u8 format, int timeout)

    Initialize fields in an event struct that are always required.

    :param struct srp_event_struct \*evt_struct:
        *undescribed*

    :param void (\*done)(struct srp_event_struct \*):
        Routine to call when the event is responded to

    :param u8 format:
        SRP or MAD format

    :param int timeout:
        timeout value set in the CRQ

.. _`set_srp_direction`:

set_srp_direction
=================

.. c:function:: void set_srp_direction(struct scsi_cmnd *cmd, struct srp_cmd *srp_cmd, int numbuf)

    Set the fields in the srp related to data direction and number of buffers based on the direction in the scsi_cmnd and the number of buffers

    :param struct scsi_cmnd \*cmd:
        *undescribed*

    :param struct srp_cmd \*srp_cmd:
        *undescribed*

    :param int numbuf:
        *undescribed*

.. _`unmap_cmd_data`:

unmap_cmd_data
==============

.. c:function:: void unmap_cmd_data(struct srp_cmd *cmd, struct srp_event_struct *evt_struct, struct device *dev)

    - Unmap data pointed in srp_cmd based on the format

    :param struct srp_cmd \*cmd:
        srp_cmd whose additional_data member will be unmapped

    :param struct srp_event_struct \*evt_struct:
        *undescribed*

    :param struct device \*dev:
        device for which the memory is mapped

.. _`map_sg_data`:

map_sg_data
===========

.. c:function:: int map_sg_data(struct scsi_cmnd *cmd, struct srp_event_struct *evt_struct, struct srp_cmd *srp_cmd, struct device *dev)

    - Maps dma for a scatterlist and initializes decriptor fields

    :param struct scsi_cmnd \*cmd:
        Scsi_Cmnd with the scatterlist

    :param struct srp_event_struct \*evt_struct:
        *undescribed*

    :param struct srp_cmd \*srp_cmd:
        srp_cmd that contains the memory descriptor

    :param struct device \*dev:
        device for which to map dma memory

.. _`map_sg_data.description`:

Description
-----------

Called by \ :c:func:`map_data_for_srp_cmd`\  when building srp cmd from scsi cmd.
Returns 1 on success.

.. _`map_data_for_srp_cmd`:

map_data_for_srp_cmd
====================

.. c:function:: int map_data_for_srp_cmd(struct scsi_cmnd *cmd, struct srp_event_struct *evt_struct, struct srp_cmd *srp_cmd, struct device *dev)

    - Calls functions to map data for srp cmds

    :param struct scsi_cmnd \*cmd:
        struct scsi_cmnd with the memory to be mapped

    :param struct srp_event_struct \*evt_struct:
        *undescribed*

    :param struct srp_cmd \*srp_cmd:
        srp_cmd that contains the memory descriptor

    :param struct device \*dev:
        dma device for which to map dma memory

.. _`map_data_for_srp_cmd.description`:

Description
-----------

Called by \ :c:func:`scsi_cmd_to_srp_cmd`\  when converting scsi cmds to srp cmds
Returns 1 on success.

.. _`purge_requests`:

purge_requests
==============

.. c:function:: void purge_requests(struct ibmvscsi_host_data *hostdata, int error_code)

    Our virtual adapter just shut down.  purge any sent requests

    :param struct ibmvscsi_host_data \*hostdata:
        the adapter

    :param int error_code:
        *undescribed*

.. _`ibmvscsi_reset_host`:

ibmvscsi_reset_host
===================

.. c:function:: void ibmvscsi_reset_host(struct ibmvscsi_host_data *hostdata)

    Reset the connection to the server

    :param struct ibmvscsi_host_data \*hostdata:
        struct ibmvscsi_host_data to reset

.. _`ibmvscsi_timeout`:

ibmvscsi_timeout
================

.. c:function:: void ibmvscsi_timeout(struct timer_list *t)

    Internal command timeout handler

    :param struct timer_list \*t:
        *undescribed*

.. _`ibmvscsi_timeout.description`:

Description
-----------

Called when an internally generated command times out

.. _`ibmvscsi_send_srp_event`:

ibmvscsi_send_srp_event
=======================

.. c:function:: int ibmvscsi_send_srp_event(struct srp_event_struct *evt_struct, struct ibmvscsi_host_data *hostdata, unsigned long timeout)

    - Transforms event to u64 array and calls \ :c:func:`send_crq`\ 

    :param struct srp_event_struct \*evt_struct:
        evt_struct to be sent

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

    :param unsigned long timeout:
        timeout in seconds - 0 means do not time command

.. _`ibmvscsi_send_srp_event.description`:

Description
-----------

Returns the value returned from \ :c:func:`ibmvscsi_send_crq`\ . (Zero for success)
Note that this routine assumes that host_lock is held for synchronization

.. _`handle_cmd_rsp`:

handle_cmd_rsp
==============

.. c:function:: void handle_cmd_rsp(struct srp_event_struct *evt_struct)

    -  Handle responses from commands

    :param struct srp_event_struct \*evt_struct:
        srp_event_struct to be handled

.. _`handle_cmd_rsp.description`:

Description
-----------

Used as a callback by when sending scsi cmds.
Gets called by \ :c:func:`ibmvscsi_handle_crq`\ 

.. _`lun_from_dev`:

lun_from_dev
============

.. c:function:: u16 lun_from_dev(struct scsi_device *dev)

    - Returns the lun of the scsi device

    :param struct scsi_device \*dev:
        struct scsi_device

.. _`ibmvscsi_queuecommand_lck`:

ibmvscsi_queuecommand_lck
=========================

.. c:function:: int ibmvscsi_queuecommand_lck(struct scsi_cmnd *cmnd, void (*done)(struct scsi_cmnd *))

    - The queuecommand function of the scsi template

    :param struct scsi_cmnd \*cmnd:
        *undescribed*

    :param void (\*done)(struct scsi_cmnd \*):
        Callback function to be called when cmd is completed

.. _`map_persist_bufs`:

map_persist_bufs
================

.. c:function:: int map_persist_bufs(struct ibmvscsi_host_data *hostdata)

    - Pre-map persistent data for adapter logins

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`map_persist_bufs.description`:

Description
-----------

Map the capabilities and adapter info DMA buffers to avoid runtime failures.
Return 1 on error, 0 on success.

.. _`unmap_persist_bufs`:

unmap_persist_bufs
==================

.. c:function:: void unmap_persist_bufs(struct ibmvscsi_host_data *hostdata)

    - Unmap persistent data needed for adapter logins

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`unmap_persist_bufs.description`:

Description
-----------

Unmap the capabilities and adapter info DMA buffers

.. _`login_rsp`:

login_rsp
=========

.. c:function:: void login_rsp(struct srp_event_struct *evt_struct)

    - Handle response to SRP login request

    :param struct srp_event_struct \*evt_struct:
        srp_event_struct with the response

.. _`login_rsp.description`:

Description
-----------

Used as a "done" callback by when sending srp_login. Gets called
by \ :c:func:`ibmvscsi_handle_crq`\ 

.. _`send_srp_login`:

send_srp_login
==============

.. c:function:: int send_srp_login(struct ibmvscsi_host_data *hostdata)

    - Sends the srp login

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`send_srp_login.description`:

Description
-----------

Returns zero if successful.

.. _`capabilities_rsp`:

capabilities_rsp
================

.. c:function:: void capabilities_rsp(struct srp_event_struct *evt_struct)

    - Handle response to MAD adapter capabilities request

    :param struct srp_event_struct \*evt_struct:
        srp_event_struct with the response

.. _`capabilities_rsp.description`:

Description
-----------

Used as a "done" callback by when sending adapter_info.

.. _`send_mad_capabilities`:

send_mad_capabilities
=====================

.. c:function:: void send_mad_capabilities(struct ibmvscsi_host_data *hostdata)

    - Sends the mad capabilities request and stores the result so it can be retrieved with

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`fast_fail_rsp`:

fast_fail_rsp
=============

.. c:function:: void fast_fail_rsp(struct srp_event_struct *evt_struct)

    - Handle response to MAD enable fast fail

    :param struct srp_event_struct \*evt_struct:
        srp_event_struct with the response

.. _`fast_fail_rsp.description`:

Description
-----------

Used as a "done" callback by when sending enable fast fail. Gets called
by \ :c:func:`ibmvscsi_handle_crq`\ 

.. _`enable_fast_fail`:

enable_fast_fail
================

.. c:function:: int enable_fast_fail(struct ibmvscsi_host_data *hostdata)

    Start host initialization

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`enable_fast_fail.description`:

Description
-----------

Returns zero if successful.

.. _`adapter_info_rsp`:

adapter_info_rsp
================

.. c:function:: void adapter_info_rsp(struct srp_event_struct *evt_struct)

    - Handle response to MAD adapter info request

    :param struct srp_event_struct \*evt_struct:
        srp_event_struct with the response

.. _`adapter_info_rsp.description`:

Description
-----------

Used as a "done" callback by when sending adapter_info. Gets called
by \ :c:func:`ibmvscsi_handle_crq`\ 

.. _`send_mad_adapter_info`:

send_mad_adapter_info
=====================

.. c:function:: void send_mad_adapter_info(struct ibmvscsi_host_data *hostdata)

    - Sends the mad adapter info request and stores the result so it can be retrieved with sysfs.  We COULD consider causing a failure if the returned SRP version doesn't match ours.

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`send_mad_adapter_info.description`:

Description
-----------

Returns zero if successful.

.. _`init_adapter`:

init_adapter
============

.. c:function:: void init_adapter(struct ibmvscsi_host_data *hostdata)

    Start virtual adapter initialization sequence

    :param struct ibmvscsi_host_data \*hostdata:
        *undescribed*

.. _`sync_completion`:

sync_completion
===============

.. c:function:: void sync_completion(struct srp_event_struct *evt_struct)

    Signal that a synchronous command has completed Note that after returning from this call, the evt_struct is freed. the caller waiting on this completion shouldn't touch the evt_struct again.

    :param struct srp_event_struct \*evt_struct:
        *undescribed*

.. _`ibmvscsi_eh_abort_handler`:

ibmvscsi_eh_abort_handler
=========================

.. c:function:: int ibmvscsi_eh_abort_handler(struct scsi_cmnd *cmd)

    Abort a command...from scsi host template send this over to the server and wait synchronously for the response

    :param struct scsi_cmnd \*cmd:
        *undescribed*

.. _`ibmvscsi_eh_device_reset_handler`:

ibmvscsi_eh_device_reset_handler
================================

.. c:function:: int ibmvscsi_eh_device_reset_handler(struct scsi_cmnd *cmd)

    Reset a single LUN...from scsi host template send this over to the server and wait synchronously for the response

    :param struct scsi_cmnd \*cmd:
        *undescribed*

.. _`ibmvscsi_eh_host_reset_handler`:

ibmvscsi_eh_host_reset_handler
==============================

.. c:function:: int ibmvscsi_eh_host_reset_handler(struct scsi_cmnd *cmd)

    Reset the connection to the server

    :param struct scsi_cmnd \*cmd:
        struct scsi_cmnd having problems

.. _`ibmvscsi_handle_crq`:

ibmvscsi_handle_crq
===================

.. c:function:: void ibmvscsi_handle_crq(struct viosrp_crq *crq, struct ibmvscsi_host_data *hostdata)

    - Handles and frees received events in the CRQ

    :param struct viosrp_crq \*crq:
        Command/Response queue

    :param struct ibmvscsi_host_data \*hostdata:
        ibmvscsi_host_data of host

.. _`ibmvscsi_slave_configure`:

ibmvscsi_slave_configure
========================

.. c:function:: int ibmvscsi_slave_configure(struct scsi_device *sdev)

    Set the "allow_restart" flag for each disk.

    :param struct scsi_device \*sdev:
        struct scsi_device device to configure

.. _`ibmvscsi_slave_configure.description`:

Description
-----------

Enable allow_restart for a device if it is a disk.  Adjust the
queue_depth here also as is required by the documentation for
struct scsi_host_template.

.. _`ibmvscsi_change_queue_depth`:

ibmvscsi_change_queue_depth
===========================

.. c:function:: int ibmvscsi_change_queue_depth(struct scsi_device *sdev, int qdepth)

    Change the device's queue depth

    :param struct scsi_device \*sdev:
        scsi device struct

    :param int qdepth:
        depth to set

.. _`ibmvscsi_change_queue_depth.return-value`:

Return value
------------

actual depth set

.. _`ibmvscsi_get_desired_dma`:

ibmvscsi_get_desired_dma
========================

.. c:function:: unsigned long ibmvscsi_get_desired_dma(struct vio_dev *vdev)

    Calculate IO memory desired by the driver

    :param struct vio_dev \*vdev:
        struct vio_dev for the device whose desired IO mem is to be returned

.. _`ibmvscsi_get_desired_dma.return-value`:

Return value
------------

Number of bytes of IO data the driver will need to perform well.

.. _`ibmvscsi_probe`:

ibmvscsi_probe
==============

.. c:function:: int ibmvscsi_probe(struct vio_dev *vdev, const struct vio_device_id *id)

    :param struct vio_dev \*vdev:
        *undescribed*

    :param const struct vio_device_id \*id:
        *undescribed*

.. _`ibmvscsi_resume`:

ibmvscsi_resume
===============

.. c:function:: int ibmvscsi_resume(struct device *dev)

    Resume from suspend

    :param struct device \*dev:
        device struct

.. _`ibmvscsi_resume.description`:

Description
-----------

We may have lost an interrupt across suspend/resume, so kick the
interrupt handler

.. This file was automatic generated / don't edit.


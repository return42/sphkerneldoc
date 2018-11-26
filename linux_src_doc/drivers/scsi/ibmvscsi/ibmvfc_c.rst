.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ibmvscsi/ibmvfc.c

.. _`ibmvfc_trc_start`:

ibmvfc_trc_start
================

.. c:function:: void ibmvfc_trc_start(struct ibmvfc_event *evt)

    Log a start trace entry

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_trc_end`:

ibmvfc_trc_end
==============

.. c:function:: void ibmvfc_trc_end(struct ibmvfc_event *evt)

    Log an end trace entry

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_get_err_index`:

ibmvfc_get_err_index
====================

.. c:function:: int ibmvfc_get_err_index(u16 status, u16 error)

    Find the index into cmd_status for the fcp response

    :param status:
        status / error class
    :type status: u16

    :param error:
        error
    :type error: u16

.. _`ibmvfc_get_err_index.return-value`:

Return value
------------

index into cmd_status / -EINVAL on failure

.. _`ibmvfc_get_cmd_error`:

ibmvfc_get_cmd_error
====================

.. c:function:: const char *ibmvfc_get_cmd_error(u16 status, u16 error)

    Find the error description for the fcp response

    :param status:
        status / error class
    :type status: u16

    :param error:
        error
    :type error: u16

.. _`ibmvfc_get_cmd_error.return-value`:

Return value
------------

error description string

.. _`ibmvfc_get_err_result`:

ibmvfc_get_err_result
=====================

.. c:function:: int ibmvfc_get_err_result(struct ibmvfc_cmd *vfc_cmd)

    Find the scsi status to return for the fcp response

    :param vfc_cmd:
        ibmvfc command struct
    :type vfc_cmd: struct ibmvfc_cmd \*

.. _`ibmvfc_get_err_result.return-value`:

Return value
------------

SCSI result value to return for completed command

.. _`ibmvfc_retry_cmd`:

ibmvfc_retry_cmd
================

.. c:function:: int ibmvfc_retry_cmd(u16 status, u16 error)

    Determine if error status is retryable

    :param status:
        status / error class
    :type status: u16

    :param error:
        error
    :type error: u16

.. _`ibmvfc_retry_cmd.return-value`:

Return value
------------

1 if error should be retried / 0 if it should not

.. _`ibmvfc_get_ls_explain`:

ibmvfc_get_ls_explain
=====================

.. c:function:: const char *ibmvfc_get_ls_explain(u16 status)

    Return the FC Explain description text

    :param status:
        FC Explain status
    :type status: u16

.. _`ibmvfc_get_ls_explain.return`:

Return
------

error string

.. _`ibmvfc_get_gs_explain`:

ibmvfc_get_gs_explain
=====================

.. c:function:: const char *ibmvfc_get_gs_explain(u16 status)

    Return the FC Explain description text

    :param status:
        FC Explain status
    :type status: u16

.. _`ibmvfc_get_gs_explain.return`:

Return
------

error string

.. _`ibmvfc_get_fc_type`:

ibmvfc_get_fc_type
==================

.. c:function:: const char *ibmvfc_get_fc_type(u16 status)

    Return the FC Type description text

    :param status:
        FC Type error status
    :type status: u16

.. _`ibmvfc_get_fc_type.return`:

Return
------

error string

.. _`ibmvfc_set_tgt_action`:

ibmvfc_set_tgt_action
=====================

.. c:function:: void ibmvfc_set_tgt_action(struct ibmvfc_target *tgt, enum ibmvfc_target_action action)

    Set the next init action for the target

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

    :param action:
        action to perform
    :type action: enum ibmvfc_target_action

.. _`ibmvfc_set_host_state`:

ibmvfc_set_host_state
=====================

.. c:function:: int ibmvfc_set_host_state(struct ibmvfc_host *vhost, enum ibmvfc_host_state state)

    Set the state for the host

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param state:
        state to set host to
    :type state: enum ibmvfc_host_state

.. _`ibmvfc_set_host_state.return`:

Return
------

0 if state changed / non-zero if not changed

.. _`ibmvfc_set_host_action`:

ibmvfc_set_host_action
======================

.. c:function:: void ibmvfc_set_host_action(struct ibmvfc_host *vhost, enum ibmvfc_host_action action)

    Set the next init action for the host

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param action:
        action to perform
    :type action: enum ibmvfc_host_action

.. _`ibmvfc_reinit_host`:

ibmvfc_reinit_host
==================

.. c:function:: void ibmvfc_reinit_host(struct ibmvfc_host *vhost)

    Re-start host initialization (no NPIV Login)

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_reinit_host.return-value`:

Return value
------------

nothing

.. _`ibmvfc_link_down`:

ibmvfc_link_down
================

.. c:function:: void ibmvfc_link_down(struct ibmvfc_host *vhost, enum ibmvfc_host_state state)

    Handle a link down event from the adapter

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param state:
        ibmvfc host state to enter
    :type state: enum ibmvfc_host_state

.. _`ibmvfc_init_host`:

ibmvfc_init_host
================

.. c:function:: void ibmvfc_init_host(struct ibmvfc_host *vhost)

    Start host initialization

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_init_host.return-value`:

Return value
------------

nothing

.. _`ibmvfc_send_crq`:

ibmvfc_send_crq
===============

.. c:function:: int ibmvfc_send_crq(struct ibmvfc_host *vhost, u64 word1, u64 word2)

    Send a CRQ

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param word1:
        the first 64 bits of the data
    :type word1: u64

    :param word2:
        the second 64 bits of the data
    :type word2: u64

.. _`ibmvfc_send_crq.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_send_crq_init`:

ibmvfc_send_crq_init
====================

.. c:function:: int ibmvfc_send_crq_init(struct ibmvfc_host *vhost)

    Send a CRQ init message

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_send_crq_init.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_send_crq_init_complete`:

ibmvfc_send_crq_init_complete
=============================

.. c:function:: int ibmvfc_send_crq_init_complete(struct ibmvfc_host *vhost)

    Send a CRQ init complete message

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_send_crq_init_complete.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_release_crq_queue`:

ibmvfc_release_crq_queue
========================

.. c:function:: void ibmvfc_release_crq_queue(struct ibmvfc_host *vhost)

    Deallocates data and unregisters CRQ

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_release_crq_queue.description`:

Description
-----------

Frees irq, deallocates a page for messages, unmaps dma, and unregisters
the crq with the hypervisor.

.. _`ibmvfc_reenable_crq_queue`:

ibmvfc_reenable_crq_queue
=========================

.. c:function:: int ibmvfc_reenable_crq_queue(struct ibmvfc_host *vhost)

    reenables the CRQ

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_reenable_crq_queue.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_reset_crq`:

ibmvfc_reset_crq
================

.. c:function:: int ibmvfc_reset_crq(struct ibmvfc_host *vhost)

    resets a crq after a failure

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_reset_crq.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_valid_event`:

ibmvfc_valid_event
==================

.. c:function:: int ibmvfc_valid_event(struct ibmvfc_event_pool *pool, struct ibmvfc_event *evt)

    Determines if event is valid.

    :param pool:
        event_pool that contains the event
    :type pool: struct ibmvfc_event_pool \*

    :param evt:
        ibmvfc event to be checked for validity
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_valid_event.return-value`:

Return value
------------

1 if event is valid / 0 if event is not valid

.. _`ibmvfc_free_event`:

ibmvfc_free_event
=================

.. c:function:: void ibmvfc_free_event(struct ibmvfc_event *evt)

    Free the specified event

    :param evt:
        ibmvfc_event to be freed
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_scsi_eh_done`:

ibmvfc_scsi_eh_done
===================

.. c:function:: void ibmvfc_scsi_eh_done(struct ibmvfc_event *evt)

    EH done function for queuecommand commands

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_scsi_eh_done.description`:

Description
-----------

This function does not setup any error status, that must be done
before this function gets called.

.. _`ibmvfc_fail_request`:

ibmvfc_fail_request
===================

.. c:function:: void ibmvfc_fail_request(struct ibmvfc_event *evt, int error_code)

    Fail request with specified error code

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param error_code:
        error code to fail request with
    :type error_code: int

.. _`ibmvfc_fail_request.return-value`:

Return value
------------

none

.. _`ibmvfc_purge_requests`:

ibmvfc_purge_requests
=====================

.. c:function:: void ibmvfc_purge_requests(struct ibmvfc_host *vhost, int error_code)

    Our virtual adapter just shut down. Purge any sent requests

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param error_code:
        error code to fail requests with
    :type error_code: int

.. _`ibmvfc_purge_requests.return-value`:

Return value
------------

none

.. _`ibmvfc_hard_reset_host`:

ibmvfc_hard_reset_host
======================

.. c:function:: void ibmvfc_hard_reset_host(struct ibmvfc_host *vhost)

    Reset the connection to the server by breaking the CRQ

    :param vhost:
        struct ibmvfc host to reset
    :type vhost: struct ibmvfc_host \*

.. _`__ibmvfc_reset_host`:

\__ibmvfc_reset_host
====================

.. c:function:: void __ibmvfc_reset_host(struct ibmvfc_host *vhost)

    Reset the connection to the server (no locking)

    :param vhost:
        struct ibmvfc host to reset
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_reset_host`:

ibmvfc_reset_host
=================

.. c:function:: void ibmvfc_reset_host(struct ibmvfc_host *vhost)

    Reset the connection to the server

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_retry_host_init`:

ibmvfc_retry_host_init
======================

.. c:function:: int ibmvfc_retry_host_init(struct ibmvfc_host *vhost)

    Retry host initialization if allowed

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_retry_host_init.return`:

Return
------

1 if init will be retried / 0 if not

.. _`__ibmvfc_get_target`:

\__ibmvfc_get_target
====================

.. c:function:: struct ibmvfc_target *__ibmvfc_get_target(struct scsi_target *starget)

    Find the specified scsi_target (no locking)

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`__ibmvfc_get_target.return-value`:

Return value
------------

ibmvfc_target struct / NULL if not found

.. _`ibmvfc_get_target`:

ibmvfc_get_target
=================

.. c:function:: struct ibmvfc_target *ibmvfc_get_target(struct scsi_target *starget)

    Find the specified scsi_target

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ibmvfc_get_target.return-value`:

Return value
------------

ibmvfc_target struct / NULL if not found

.. _`ibmvfc_get_host_speed`:

ibmvfc_get_host_speed
=====================

.. c:function:: void ibmvfc_get_host_speed(struct Scsi_Host *shost)

    Get host port speed

    :param shost:
        scsi host struct
    :type shost: struct Scsi_Host \*

.. _`ibmvfc_get_host_speed.return-value`:

Return value
------------

none

.. _`ibmvfc_get_host_port_state`:

ibmvfc_get_host_port_state
==========================

.. c:function:: void ibmvfc_get_host_port_state(struct Scsi_Host *shost)

    Get host port state

    :param shost:
        scsi host struct
    :type shost: struct Scsi_Host \*

.. _`ibmvfc_get_host_port_state.return-value`:

Return value
------------

none

.. _`ibmvfc_set_rport_dev_loss_tmo`:

ibmvfc_set_rport_dev_loss_tmo
=============================

.. c:function:: void ibmvfc_set_rport_dev_loss_tmo(struct fc_rport *rport, u32 timeout)

    Set rport's device loss timeout

    :param rport:
        rport struct
    :type rport: struct fc_rport \*

    :param timeout:
        timeout value
    :type timeout: u32

.. _`ibmvfc_set_rport_dev_loss_tmo.return-value`:

Return value
------------

none

.. _`ibmvfc_release_tgt`:

ibmvfc_release_tgt
==================

.. c:function:: void ibmvfc_release_tgt(struct kref *kref)

    Free memory allocated for a target

    :param kref:
        kref struct
    :type kref: struct kref \*

.. _`ibmvfc_get_starget_node_name`:

ibmvfc_get_starget_node_name
============================

.. c:function:: void ibmvfc_get_starget_node_name(struct scsi_target *starget)

    Get SCSI target's node name

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ibmvfc_get_starget_node_name.return-value`:

Return value
------------

none

.. _`ibmvfc_get_starget_port_name`:

ibmvfc_get_starget_port_name
============================

.. c:function:: void ibmvfc_get_starget_port_name(struct scsi_target *starget)

    Get SCSI target's port name

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ibmvfc_get_starget_port_name.return-value`:

Return value
------------

none

.. _`ibmvfc_get_starget_port_id`:

ibmvfc_get_starget_port_id
==========================

.. c:function:: void ibmvfc_get_starget_port_id(struct scsi_target *starget)

    Get SCSI target's port ID

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ibmvfc_get_starget_port_id.return-value`:

Return value
------------

none

.. _`ibmvfc_wait_while_resetting`:

ibmvfc_wait_while_resetting
===========================

.. c:function:: int ibmvfc_wait_while_resetting(struct ibmvfc_host *vhost)

    Wait while the host resets

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_wait_while_resetting.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_issue_fc_host_lip`:

ibmvfc_issue_fc_host_lip
========================

.. c:function:: int ibmvfc_issue_fc_host_lip(struct Scsi_Host *shost)

    Re-initiate link initialization

    :param shost:
        scsi host struct
    :type shost: struct Scsi_Host \*

.. _`ibmvfc_issue_fc_host_lip.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_gather_partition_info`:

ibmvfc_gather_partition_info
============================

.. c:function:: void ibmvfc_gather_partition_info(struct ibmvfc_host *vhost)

    Gather info about the LPAR

    :param vhost:
        *undescribed*
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_gather_partition_info.return-value`:

Return value
------------

none

.. _`ibmvfc_set_login_info`:

ibmvfc_set_login_info
=====================

.. c:function:: void ibmvfc_set_login_info(struct ibmvfc_host *vhost)

    Setup info for NPIV login

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_set_login_info.return-value`:

Return value
------------

none

.. _`ibmvfc_init_event_pool`:

ibmvfc_init_event_pool
======================

.. c:function:: int ibmvfc_init_event_pool(struct ibmvfc_host *vhost)

    Allocates and initializes the event pool for a host

    :param vhost:
        ibmvfc host who owns the event pool
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_init_event_pool.description`:

Description
-----------

Returns zero on success.

.. _`ibmvfc_free_event_pool`:

ibmvfc_free_event_pool
======================

.. c:function:: void ibmvfc_free_event_pool(struct ibmvfc_host *vhost)

    Frees memory of the event pool of a host

    :param vhost:
        ibmvfc host who owns the event pool
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_get_event`:

ibmvfc_get_event
================

.. c:function:: struct ibmvfc_event *ibmvfc_get_event(struct ibmvfc_host *vhost)

    Gets the next free event in pool

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_get_event.description`:

Description
-----------

Returns a free event from the pool.

.. _`ibmvfc_init_event`:

ibmvfc_init_event
=================

.. c:function:: void ibmvfc_init_event(struct ibmvfc_event *evt, void (*done)(struct ibmvfc_event *), u8 format)

    Initialize fields in an event struct that are always required.

    :param evt:
        The event
    :type evt: struct ibmvfc_event \*

    :param void (\*done)(struct ibmvfc_event \*):
        Routine to call when the event is responded to

    :param format:
        SRP or MAD format
    :type format: u8

.. _`ibmvfc_map_sg_list`:

ibmvfc_map_sg_list
==================

.. c:function:: void ibmvfc_map_sg_list(struct scsi_cmnd *scmd, int nseg, struct srp_direct_buf *md)

    Initialize scatterlist

    :param scmd:
        scsi command struct
    :type scmd: struct scsi_cmnd \*

    :param nseg:
        number of scatterlist segments
    :type nseg: int

    :param md:
        memory descriptor list to initialize
    :type md: struct srp_direct_buf \*

.. _`ibmvfc_map_sg_data`:

ibmvfc_map_sg_data
==================

.. c:function:: int ibmvfc_map_sg_data(struct scsi_cmnd *scmd, struct ibmvfc_event *evt, struct ibmvfc_cmd *vfc_cmd, struct device *dev)

    Maps dma for a scatterlist and initializes decriptor fields

    :param scmd:
        struct scsi_cmnd with the scatterlist
    :type scmd: struct scsi_cmnd \*

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param vfc_cmd:
        vfc_cmd that contains the memory descriptor
    :type vfc_cmd: struct ibmvfc_cmd \*

    :param dev:
        device for which to map dma memory
    :type dev: struct device \*

.. _`ibmvfc_map_sg_data.return`:

Return
------

0 on success / non-zero on failure

.. _`ibmvfc_timeout`:

ibmvfc_timeout
==============

.. c:function:: void ibmvfc_timeout(struct timer_list *t)

    Internal command timeout handler

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ibmvfc_timeout.description`:

Description
-----------

Called when an internally generated command times out

.. _`ibmvfc_send_event`:

ibmvfc_send_event
=================

.. c:function:: int ibmvfc_send_event(struct ibmvfc_event *evt, struct ibmvfc_host *vhost, unsigned long timeout)

    Transforms event to u64 array and calls \ :c:func:`send_crq`\ 

    :param evt:
        event to be sent
    :type evt: struct ibmvfc_event \*

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param timeout:
        timeout in seconds - 0 means do not time command
    :type timeout: unsigned long

.. _`ibmvfc_send_event.description`:

Description
-----------

Returns the value returned from \ :c:func:`ibmvfc_send_crq`\ . (Zero for success)

.. _`ibmvfc_log_error`:

ibmvfc_log_error
================

.. c:function:: void ibmvfc_log_error(struct ibmvfc_event *evt)

    Log an error for the failed command if appropriate

    :param evt:
        ibmvfc event to log
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_relogin`:

ibmvfc_relogin
==============

.. c:function:: void ibmvfc_relogin(struct scsi_device *sdev)

    Log back into the specified device

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`ibmvfc_scsi_done`:

ibmvfc_scsi_done
================

.. c:function:: void ibmvfc_scsi_done(struct ibmvfc_event *evt)

    Handle responses from commands

    :param evt:
        ibmvfc event to be handled
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_scsi_done.description`:

Description
-----------

Used as a callback when sending scsi cmds.

.. _`ibmvfc_host_chkready`:

ibmvfc_host_chkready
====================

.. c:function:: int ibmvfc_host_chkready(struct ibmvfc_host *vhost)

    Check if the host can accept commands

    :param vhost:
        struct ibmvfc host
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_host_chkready.return`:

Return
------

1 if host can accept command / 0 if not

.. _`ibmvfc_queuecommand_lck`:

ibmvfc_queuecommand_lck
=======================

.. c:function:: int ibmvfc_queuecommand_lck(struct scsi_cmnd *cmnd, void (*done)(struct scsi_cmnd *))

    The queuecommand function of the scsi template

    :param cmnd:
        struct scsi_cmnd to be executed
    :type cmnd: struct scsi_cmnd \*

    :param void (\*done)(struct scsi_cmnd \*):
        Callback function to be called when cmnd is completed

.. _`ibmvfc_queuecommand_lck.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_sync_completion`:

ibmvfc_sync_completion
======================

.. c:function:: void ibmvfc_sync_completion(struct ibmvfc_event *evt)

    Signal that a synchronous command has completed

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_bsg_timeout_done`:

ibmvfc_bsg_timeout_done
=======================

.. c:function:: void ibmvfc_bsg_timeout_done(struct ibmvfc_event *evt)

    Completion handler for cancelling BSG commands

    :param evt:
        struct ibmvfc_event
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_bsg_timeout`:

ibmvfc_bsg_timeout
==================

.. c:function:: int ibmvfc_bsg_timeout(struct bsg_job *job)

    Handle a BSG timeout

    :param job:
        struct bsg_job that timed out
    :type job: struct bsg_job \*

.. _`ibmvfc_bsg_timeout.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_bsg_plogi`:

ibmvfc_bsg_plogi
================

.. c:function:: int ibmvfc_bsg_plogi(struct ibmvfc_host *vhost, unsigned int port_id)

    PLOGI into a target to handle a BSG command

    :param vhost:
        struct ibmvfc_host to send command
    :type vhost: struct ibmvfc_host \*

    :param port_id:
        port ID to send command
    :type port_id: unsigned int

.. _`ibmvfc_bsg_plogi.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_bsg_request`:

ibmvfc_bsg_request
==================

.. c:function:: int ibmvfc_bsg_request(struct bsg_job *job)

    Handle a BSG request

    :param job:
        struct bsg_job to be executed
    :type job: struct bsg_job \*

.. _`ibmvfc_bsg_request.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_reset_device`:

ibmvfc_reset_device
===================

.. c:function:: int ibmvfc_reset_device(struct scsi_device *sdev, int type, char *desc)

    Reset the device with the specified reset type

    :param sdev:
        scsi device to reset
    :type sdev: struct scsi_device \*

    :param type:
        reset type
    :type type: int

    :param desc:
        reset type description for log messages
    :type desc: char \*

.. _`ibmvfc_reset_device.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_match_rport`:

ibmvfc_match_rport
==================

.. c:function:: int ibmvfc_match_rport(struct ibmvfc_event *evt, void *rport)

    Match function for specified remote port

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param rport:
        *undescribed*
    :type rport: void \*

.. _`ibmvfc_match_rport.return`:

Return
------

1 if event matches rport / 0 if event does not match rport

.. _`ibmvfc_match_target`:

ibmvfc_match_target
===================

.. c:function:: int ibmvfc_match_target(struct ibmvfc_event *evt, void *device)

    Match function for specified target

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param device:
        device to match (starget)
    :type device: void \*

.. _`ibmvfc_match_target.return`:

Return
------

1 if event matches starget / 0 if event does not match starget

.. _`ibmvfc_match_lun`:

ibmvfc_match_lun
================

.. c:function:: int ibmvfc_match_lun(struct ibmvfc_event *evt, void *device)

    Match function for specified LUN

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param device:
        device to match (sdev)
    :type device: void \*

.. _`ibmvfc_match_lun.return`:

Return
------

1 if event matches sdev / 0 if event does not match sdev

.. _`ibmvfc_wait_for_ops`:

ibmvfc_wait_for_ops
===================

.. c:function:: int ibmvfc_wait_for_ops(struct ibmvfc_host *vhost, void *device, int (*match)(struct ibmvfc_event *, void *))

    Wait for ops to complete

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param device:
        device to match (starget or sdev)
    :type device: void \*

    :param int (\*match)(struct ibmvfc_event \*, void \*):
        match function

.. _`ibmvfc_wait_for_ops.return`:

Return
------

SUCCESS / FAILED

.. _`ibmvfc_cancel_all`:

ibmvfc_cancel_all
=================

.. c:function:: int ibmvfc_cancel_all(struct scsi_device *sdev, int type)

    Cancel all outstanding commands to the device

    :param sdev:
        scsi device to cancel commands
    :type sdev: struct scsi_device \*

    :param type:
        type of error recovery being performed
    :type type: int

.. _`ibmvfc_cancel_all.description`:

Description
-----------

This sends a cancel to the VIOS for the specified device. This does
NOT send any abort to the actual device. That must be done separately.

.. _`ibmvfc_cancel_all.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_match_key`:

ibmvfc_match_key
================

.. c:function:: int ibmvfc_match_key(struct ibmvfc_event *evt, void *key)

    Match function for specified cancel key

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param key:
        cancel key to match
    :type key: void \*

.. _`ibmvfc_match_key.return`:

Return
------

1 if event matches key / 0 if event does not match key

.. _`ibmvfc_match_evt`:

ibmvfc_match_evt
================

.. c:function:: int ibmvfc_match_evt(struct ibmvfc_event *evt, void *match)

    Match function for specified event

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

    :param match:
        event to match
    :type match: void \*

.. _`ibmvfc_match_evt.return`:

Return
------

1 if event matches key / 0 if event does not match key

.. _`ibmvfc_abort_task_set`:

ibmvfc_abort_task_set
=====================

.. c:function:: int ibmvfc_abort_task_set(struct scsi_device *sdev)

    Abort outstanding commands to the device

    :param sdev:
        scsi device to abort commands
    :type sdev: struct scsi_device \*

.. _`ibmvfc_abort_task_set.description`:

Description
-----------

This sends an Abort Task Set to the VIOS for the specified device. This does
NOT send any cancel to the VIOS. That must be done separately.

.. _`ibmvfc_abort_task_set.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_eh_abort_handler`:

ibmvfc_eh_abort_handler
=======================

.. c:function:: int ibmvfc_eh_abort_handler(struct scsi_cmnd *cmd)

    Abort a command

    :param cmd:
        scsi command to abort
    :type cmd: struct scsi_cmnd \*

.. _`ibmvfc_eh_abort_handler.return`:

Return
------

SUCCESS / FAST_IO_FAIL / FAILED

.. _`ibmvfc_eh_device_reset_handler`:

ibmvfc_eh_device_reset_handler
==============================

.. c:function:: int ibmvfc_eh_device_reset_handler(struct scsi_cmnd *cmd)

    Reset a single LUN

    :param cmd:
        scsi command struct
    :type cmd: struct scsi_cmnd \*

.. _`ibmvfc_eh_device_reset_handler.return`:

Return
------

SUCCESS / FAST_IO_FAIL / FAILED

.. _`ibmvfc_dev_cancel_all_noreset`:

ibmvfc_dev_cancel_all_noreset
=============================

.. c:function:: void ibmvfc_dev_cancel_all_noreset(struct scsi_device *sdev, void *data)

    Device iterated cancel all function

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

    :param data:
        return code
    :type data: void \*

.. _`ibmvfc_dev_cancel_all_reset`:

ibmvfc_dev_cancel_all_reset
===========================

.. c:function:: void ibmvfc_dev_cancel_all_reset(struct scsi_device *sdev, void *data)

    Device iterated cancel all function

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

    :param data:
        return code
    :type data: void \*

.. _`ibmvfc_eh_target_reset_handler`:

ibmvfc_eh_target_reset_handler
==============================

.. c:function:: int ibmvfc_eh_target_reset_handler(struct scsi_cmnd *cmd)

    Reset the target

    :param cmd:
        scsi command struct
    :type cmd: struct scsi_cmnd \*

.. _`ibmvfc_eh_target_reset_handler.return`:

Return
------

SUCCESS / FAST_IO_FAIL / FAILED

.. _`ibmvfc_eh_host_reset_handler`:

ibmvfc_eh_host_reset_handler
============================

.. c:function:: int ibmvfc_eh_host_reset_handler(struct scsi_cmnd *cmd)

    Reset the connection to the server

    :param cmd:
        struct scsi_cmnd having problems
    :type cmd: struct scsi_cmnd \*

.. _`ibmvfc_terminate_rport_io`:

ibmvfc_terminate_rport_io
=========================

.. c:function:: void ibmvfc_terminate_rport_io(struct fc_rport *rport)

    Terminate all pending I/O to the rport.

    :param rport:
        rport struct
    :type rport: struct fc_rport \*

.. _`ibmvfc_terminate_rport_io.return-value`:

Return value
------------

none

.. _`ibmvfc_get_ae_desc`:

ibmvfc_get_ae_desc
==================

.. c:function:: const struct ibmvfc_async_desc *ibmvfc_get_ae_desc(u64 ae)

    Get text description for async event

    :param ae:
        async event
    :type ae: u64

.. _`ibmvfc_get_link_state`:

ibmvfc_get_link_state
=====================

.. c:function:: const char *ibmvfc_get_link_state(enum ibmvfc_ae_link_state state)

    Get text description for link state

    :param state:
        link state
    :type state: enum ibmvfc_ae_link_state

.. _`ibmvfc_handle_async`:

ibmvfc_handle_async
===================

.. c:function:: void ibmvfc_handle_async(struct ibmvfc_async_crq *crq, struct ibmvfc_host *vhost)

    Handle an async event from the adapter

    :param crq:
        crq to process
    :type crq: struct ibmvfc_async_crq \*

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_handle_crq`:

ibmvfc_handle_crq
=================

.. c:function:: void ibmvfc_handle_crq(struct ibmvfc_crq *crq, struct ibmvfc_host *vhost)

    Handles and frees received events in the CRQ

    :param crq:
        Command/Response queue
    :type crq: struct ibmvfc_crq \*

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_scan_finished`:

ibmvfc_scan_finished
====================

.. c:function:: int ibmvfc_scan_finished(struct Scsi_Host *shost, unsigned long time)

    Check if the device scan is done.

    :param shost:
        scsi host struct
    :type shost: struct Scsi_Host \*

    :param time:
        current elapsed time
    :type time: unsigned long

.. _`ibmvfc_scan_finished.return`:

Return
------

0 if scan is not done / 1 if scan is done

.. _`ibmvfc_slave_alloc`:

ibmvfc_slave_alloc
==================

.. c:function:: int ibmvfc_slave_alloc(struct scsi_device *sdev)

    Setup the device's task set value

    :param sdev:
        struct scsi_device device to configure
    :type sdev: struct scsi_device \*

.. _`ibmvfc_slave_alloc.description`:

Description
-----------

Set the device's task set value so that error handling works as
expected.

.. _`ibmvfc_slave_alloc.return`:

Return
------

0 on success / -ENXIO if device does not exist

.. _`ibmvfc_target_alloc`:

ibmvfc_target_alloc
===================

.. c:function:: int ibmvfc_target_alloc(struct scsi_target *starget)

    Setup the target's task set value

    :param starget:
        struct scsi_target
    :type starget: struct scsi_target \*

.. _`ibmvfc_target_alloc.description`:

Description
-----------

Set the target's task set value so that error handling works as
expected.

.. _`ibmvfc_target_alloc.return`:

Return
------

0 on success / -ENXIO if device does not exist

.. _`ibmvfc_slave_configure`:

ibmvfc_slave_configure
======================

.. c:function:: int ibmvfc_slave_configure(struct scsi_device *sdev)

    Configure the device

    :param sdev:
        struct scsi_device device to configure
    :type sdev: struct scsi_device \*

.. _`ibmvfc_slave_configure.description`:

Description
-----------

Enable allow_restart for a device if it is a disk. Adjust the
queue_depth here also.

.. _`ibmvfc_slave_configure.return`:

Return
------

0

.. _`ibmvfc_change_queue_depth`:

ibmvfc_change_queue_depth
=========================

.. c:function:: int ibmvfc_change_queue_depth(struct scsi_device *sdev, int qdepth)

    Change the device's queue depth

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

    :param qdepth:
        depth to set
    :type qdepth: int

.. _`ibmvfc_change_queue_depth.return-value`:

Return value
------------

actual depth set

.. _`ibmvfc_show_log_level`:

ibmvfc_show_log_level
=====================

.. c:function:: ssize_t ibmvfc_show_log_level(struct device *dev, struct device_attribute *attr, char *buf)

    Show the adapter's error logging level

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ibmvfc_show_log_level.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ibmvfc_store_log_level`:

ibmvfc_store_log_level
======================

.. c:function:: ssize_t ibmvfc_store_log_level(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change the adapter's error logging level

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`ibmvfc_store_log_level.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ibmvfc_read_trace`:

ibmvfc_read_trace
=================

.. c:function:: ssize_t ibmvfc_read_trace(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Dump the adapter trace

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject struct
    :type kobj: struct kobject \*

    :param bin_attr:
        bin_attribute struct
    :type bin_attr: struct bin_attribute \*

    :param buf:
        buffer
    :type buf: char \*

    :param off:
        offset
    :type off: loff_t

    :param count:
        buffer size
    :type count: size_t

.. _`ibmvfc_read_trace.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ibmvfc_next_async_crq`:

ibmvfc_next_async_crq
=====================

.. c:function:: struct ibmvfc_async_crq *ibmvfc_next_async_crq(struct ibmvfc_host *vhost)

    Returns the next entry in async queue

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_next_async_crq.return`:

Return
------

Pointer to next entry in queue / NULL if empty

.. _`ibmvfc_next_crq`:

ibmvfc_next_crq
===============

.. c:function:: struct ibmvfc_crq *ibmvfc_next_crq(struct ibmvfc_host *vhost)

    Returns the next entry in message queue

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_next_crq.return`:

Return
------

Pointer to next entry in queue / NULL if empty

.. _`ibmvfc_interrupt`:

ibmvfc_interrupt
================

.. c:function:: irqreturn_t ibmvfc_interrupt(int irq, void *dev_instance)

    Interrupt handler

    :param irq:
        number of irq to handle, not used
    :type irq: int

    :param dev_instance:
        ibmvfc_host that received interrupt
    :type dev_instance: void \*

.. _`ibmvfc_interrupt.return`:

Return
------

IRQ_HANDLED

.. _`ibmvfc_tasklet`:

ibmvfc_tasklet
==============

.. c:function:: void ibmvfc_tasklet(void *data)

    Interrupt handler tasklet

    :param data:
        ibmvfc host struct
    :type data: void \*

.. _`ibmvfc_tasklet.return`:

Return
------

Nothing

.. _`ibmvfc_init_tgt`:

ibmvfc_init_tgt
===============

.. c:function:: void ibmvfc_init_tgt(struct ibmvfc_target *tgt, void (*job_step)(struct ibmvfc_target *))

    Set the next init job step for the target

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

    :param void (\*job_step)(struct ibmvfc_target \*):
        job step to perform

.. _`ibmvfc_retry_tgt_init`:

ibmvfc_retry_tgt_init
=====================

.. c:function:: int ibmvfc_retry_tgt_init(struct ibmvfc_target *tgt, void (*job_step)(struct ibmvfc_target *))

    Attempt to retry a step in target initialization

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

    :param void (\*job_step)(struct ibmvfc_target \*):
        initialization job step

.. _`ibmvfc_retry_tgt_init.return`:

Return
------

1 if step will be retried / 0 if not

.. _`ibmvfc_get_prli_rsp`:

ibmvfc_get_prli_rsp
===================

.. c:function:: int ibmvfc_get_prli_rsp(u16 flags)

    Find PRLI response index

    :param flags:
        PRLI response flags
    :type flags: u16

.. _`ibmvfc_tgt_prli_done`:

ibmvfc_tgt_prli_done
====================

.. c:function:: void ibmvfc_tgt_prli_done(struct ibmvfc_event *evt)

    Completion handler for Process Login

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_tgt_send_prli`:

ibmvfc_tgt_send_prli
====================

.. c:function:: void ibmvfc_tgt_send_prli(struct ibmvfc_target *tgt)

    Send a process login

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_tgt_plogi_done`:

ibmvfc_tgt_plogi_done
=====================

.. c:function:: void ibmvfc_tgt_plogi_done(struct ibmvfc_event *evt)

    Completion handler for Port Login

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_tgt_send_plogi`:

ibmvfc_tgt_send_plogi
=====================

.. c:function:: void ibmvfc_tgt_send_plogi(struct ibmvfc_target *tgt)

    Send PLOGI to the specified target

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_tgt_implicit_logout_done`:

ibmvfc_tgt_implicit_logout_done
===============================

.. c:function:: void ibmvfc_tgt_implicit_logout_done(struct ibmvfc_event *evt)

    Completion handler for Implicit Logout MAD

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_tgt_implicit_logout`:

ibmvfc_tgt_implicit_logout
==========================

.. c:function:: void ibmvfc_tgt_implicit_logout(struct ibmvfc_target *tgt)

    Initiate an Implicit Logout for specified target

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_adisc_needs_plogi`:

ibmvfc_adisc_needs_plogi
========================

.. c:function:: int ibmvfc_adisc_needs_plogi(struct ibmvfc_passthru_mad *mad, struct ibmvfc_target *tgt)

    Does device need PLOGI?

    :param mad:
        ibmvfc passthru mad struct
    :type mad: struct ibmvfc_passthru_mad \*

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_adisc_needs_plogi.return`:

Return
------

1 if PLOGI needed / 0 if PLOGI not needed

.. _`ibmvfc_tgt_adisc_done`:

ibmvfc_tgt_adisc_done
=====================

.. c:function:: void ibmvfc_tgt_adisc_done(struct ibmvfc_event *evt)

    Completion handler for ADISC

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_init_passthru`:

ibmvfc_init_passthru
====================

.. c:function:: void ibmvfc_init_passthru(struct ibmvfc_event *evt)

    Initialize an event struct for FC passthru

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_tgt_adisc_cancel_done`:

ibmvfc_tgt_adisc_cancel_done
============================

.. c:function:: void ibmvfc_tgt_adisc_cancel_done(struct ibmvfc_event *evt)

    Completion handler when cancelling an ADISC

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_tgt_adisc_cancel_done.description`:

Description
-----------

Just cleanup this event struct. Everything else is handled by
the ADISC completion handler. If the ADISC never actually comes
back, we still have the timer running on the ADISC event struct
which will fire and cause the CRQ to get reset.

.. _`ibmvfc_adisc_timeout`:

ibmvfc_adisc_timeout
====================

.. c:function:: void ibmvfc_adisc_timeout(struct timer_list *t)

    Handle an ADISC timeout

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ibmvfc_adisc_timeout.description`:

Description
-----------

If an ADISC times out, send a cancel. If the cancel times
out, reset the CRQ. When the ADISC comes back as cancelled,
log back into the target.

.. _`ibmvfc_tgt_adisc`:

ibmvfc_tgt_adisc
================

.. c:function:: void ibmvfc_tgt_adisc(struct ibmvfc_target *tgt)

    Initiate an ADISC for specified target

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_tgt_adisc.description`:

Description
-----------

When sending an ADISC we end up with two timers running. The
first timer is the timer in the ibmvfc target struct. If this
fires, we send a cancel to the target. The second timer is the
timer on the ibmvfc event for the ADISC, which is longer. If that
fires, it means the ADISC timed out and our attempt to cancel it
also failed, so we need to reset the CRQ.

.. _`ibmvfc_tgt_query_target_done`:

ibmvfc_tgt_query_target_done
============================

.. c:function:: void ibmvfc_tgt_query_target_done(struct ibmvfc_event *evt)

    Completion handler for Query Target MAD

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_tgt_query_target`:

ibmvfc_tgt_query_target
=======================

.. c:function:: void ibmvfc_tgt_query_target(struct ibmvfc_target *tgt)

    Initiate a Query Target for specified target

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_alloc_target`:

ibmvfc_alloc_target
===================

.. c:function:: int ibmvfc_alloc_target(struct ibmvfc_host *vhost, u64 scsi_id)

    Allocate and initialize an ibmvfc target

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param scsi_id:
        SCSI ID to allocate target for
    :type scsi_id: u64

.. _`ibmvfc_alloc_target.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_alloc_targets`:

ibmvfc_alloc_targets
====================

.. c:function:: int ibmvfc_alloc_targets(struct ibmvfc_host *vhost)

    Allocate and initialize ibmvfc targets

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_alloc_targets.return`:

Return
------

0 on success / other on failure

.. _`ibmvfc_discover_targets_done`:

ibmvfc_discover_targets_done
============================

.. c:function:: void ibmvfc_discover_targets_done(struct ibmvfc_event *evt)

    Completion handler for discover targets MAD

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_discover_targets`:

ibmvfc_discover_targets
=======================

.. c:function:: void ibmvfc_discover_targets(struct ibmvfc_host *vhost)

    Send Discover Targets MAD

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_npiv_login_done`:

ibmvfc_npiv_login_done
======================

.. c:function:: void ibmvfc_npiv_login_done(struct ibmvfc_event *evt)

    Completion handler for NPIV Login

    :param evt:
        ibmvfc event struct
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_npiv_login`:

ibmvfc_npiv_login
=================

.. c:function:: void ibmvfc_npiv_login(struct ibmvfc_host *vhost)

    Sends NPIV login

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_npiv_logout_done`:

ibmvfc_npiv_logout_done
=======================

.. c:function:: void ibmvfc_npiv_logout_done(struct ibmvfc_event *evt)

    Completion handler for NPIV Logout

    :param evt:
        *undescribed*
    :type evt: struct ibmvfc_event \*

.. _`ibmvfc_npiv_logout`:

ibmvfc_npiv_logout
==================

.. c:function:: void ibmvfc_npiv_logout(struct ibmvfc_host *vhost)

    Issue an NPIV Logout

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_dev_init_to_do`:

ibmvfc_dev_init_to_do
=====================

.. c:function:: int ibmvfc_dev_init_to_do(struct ibmvfc_host *vhost)

    Is there target initialization work to do?

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_dev_init_to_do.return`:

Return
------

1 if work to do / 0 if not

.. _`__ibmvfc_work_to_do`:

\__ibmvfc_work_to_do
====================

.. c:function:: int __ibmvfc_work_to_do(struct ibmvfc_host *vhost)

    Is there task level work to do? (no locking)

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`__ibmvfc_work_to_do.return`:

Return
------

1 if work to do / 0 if not

.. _`ibmvfc_work_to_do`:

ibmvfc_work_to_do
=================

.. c:function:: int ibmvfc_work_to_do(struct ibmvfc_host *vhost)

    Is there task level work to do?

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_work_to_do.return`:

Return
------

1 if work to do / 0 if not

.. _`ibmvfc_log_ae`:

ibmvfc_log_ae
=============

.. c:function:: void ibmvfc_log_ae(struct ibmvfc_host *vhost, int events)

    Log async events if necessary

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

    :param events:
        events to log
    :type events: int

.. _`ibmvfc_tgt_add_rport`:

ibmvfc_tgt_add_rport
====================

.. c:function:: void ibmvfc_tgt_add_rport(struct ibmvfc_target *tgt)

    Tell the FC transport about a new remote port

    :param tgt:
        ibmvfc target struct
    :type tgt: struct ibmvfc_target \*

.. _`ibmvfc_do_work`:

ibmvfc_do_work
==============

.. c:function:: void ibmvfc_do_work(struct ibmvfc_host *vhost)

    Do task level work

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_work`:

ibmvfc_work
===========

.. c:function:: int ibmvfc_work(void *data)

    Do task level work

    :param data:
        ibmvfc host struct
    :type data: void \*

.. _`ibmvfc_work.return`:

Return
------

zero

.. _`ibmvfc_init_crq`:

ibmvfc_init_crq
===============

.. c:function:: int ibmvfc_init_crq(struct ibmvfc_host *vhost)

    Initializes and registers CRQ with hypervisor

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_init_crq.description`:

Description
-----------

Allocates a page for messages, maps it for dma, and registers
the crq with the hypervisor.

.. _`ibmvfc_init_crq.return-value`:

Return value
------------

zero on success / other on failure

.. _`ibmvfc_free_mem`:

ibmvfc_free_mem
===============

.. c:function:: void ibmvfc_free_mem(struct ibmvfc_host *vhost)

    Free memory for vhost

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_free_mem.return-value`:

Return value
------------

none

.. _`ibmvfc_alloc_mem`:

ibmvfc_alloc_mem
================

.. c:function:: int ibmvfc_alloc_mem(struct ibmvfc_host *vhost)

    Allocate memory for vhost

    :param vhost:
        ibmvfc host struct
    :type vhost: struct ibmvfc_host \*

.. _`ibmvfc_alloc_mem.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`ibmvfc_rport_add_thread`:

ibmvfc_rport_add_thread
=======================

.. c:function:: void ibmvfc_rport_add_thread(struct work_struct *work)

    Worker thread for rport adds

    :param work:
        work struct
    :type work: struct work_struct \*

.. _`ibmvfc_probe`:

ibmvfc_probe
============

.. c:function:: int ibmvfc_probe(struct vio_dev *vdev, const struct vio_device_id *id)

    Adapter hot plug add entry point

    :param vdev:
        vio device struct
    :type vdev: struct vio_dev \*

    :param id:
        vio device id struct
    :type id: const struct vio_device_id \*

.. _`ibmvfc_probe.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`ibmvfc_remove`:

ibmvfc_remove
=============

.. c:function:: int ibmvfc_remove(struct vio_dev *vdev)

    Adapter hot plug remove entry point

    :param vdev:
        vio device struct
    :type vdev: struct vio_dev \*

.. _`ibmvfc_remove.return-value`:

Return value
------------

0

.. _`ibmvfc_resume`:

ibmvfc_resume
=============

.. c:function:: int ibmvfc_resume(struct device *dev)

    Resume from suspend

    :param dev:
        device struct
    :type dev: struct device \*

.. _`ibmvfc_resume.description`:

Description
-----------

We may have lost an interrupt across suspend/resume, so kick the
interrupt handler

.. _`ibmvfc_get_desired_dma`:

ibmvfc_get_desired_dma
======================

.. c:function:: unsigned long ibmvfc_get_desired_dma(struct vio_dev *vdev)

    Calculate DMA resources needed by the driver

    :param vdev:
        vio device struct
    :type vdev: struct vio_dev \*

.. _`ibmvfc_get_desired_dma.return-value`:

Return value
------------

Number of bytes the driver will need to DMA map at the same time in
order to perform well.

.. _`ibmvfc_module_init`:

ibmvfc_module_init
==================

.. c:function:: int ibmvfc_module_init( void)

    Initialize the ibmvfc module

    :param void:
        no arguments
    :type void: 

.. _`ibmvfc_module_init.return-value`:

Return value
------------

0 on success / other on failure

.. _`ibmvfc_module_exit`:

ibmvfc_module_exit
==================

.. c:function:: void __exit ibmvfc_module_exit( void)

    Teardown the ibmvfc module

    :param void:
        no arguments
    :type void: 

.. _`ibmvfc_module_exit.return-value`:

Return value
------------

nothing

.. This file was automatic generated / don't edit.


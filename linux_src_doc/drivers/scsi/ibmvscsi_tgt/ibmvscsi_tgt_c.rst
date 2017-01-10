.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ibmvscsi_tgt/ibmvscsi_tgt.c

.. _`connection_broken`:

connection_broken
=================

.. c:function:: bool connection_broken(struct scsi_info *vscsi)

    Determine if the connection to the client is good

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`connection_broken.description`:

Description
-----------

This function attempts to send a ping MAD to the client. If the call to
queue the request returns H_CLOSED then the connection has been broken
and the function returns TRUE.

.. _`connection_broken.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt or Process environment

.. _`ibmvscsis_unregister_command_q`:

ibmvscsis_unregister_command_q
==============================

.. c:function:: long ibmvscsis_unregister_command_q(struct scsi_info *vscsi)

    Helper Function-Unregister Command Queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_unregister_command_q.description`:

Description
-----------

This function calls h_free_q then frees the interrupt bit etc.
It must release the lock before doing so because of the time it can take
for h_free_crq in PHYP

.. _`ibmvscsis_unregister_command_q.note`:

NOTE
----

the caller must make sure that state and or flags will prevent
interrupt handler from scheduling work.

anyone calling this function may need to set the CRQ_CLOSED flag
we can't do it here, because we don't have the lock

.. _`ibmvscsis_unregister_command_q.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process level

.. _`ibmvscsis_delete_client_info`:

ibmvscsis_delete_client_info
============================

.. c:function:: void ibmvscsis_delete_client_info(struct scsi_info *vscsi, bool client_closed)

    Helper function to Delete Client Info

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param bool client_closed:
        True if client closed its queue

.. _`ibmvscsis_delete_client_info.description`:

Description
-----------

Deletes information specific to the client when the client goes away

.. _`ibmvscsis_delete_client_info.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt or Process

.. _`ibmvscsis_free_command_q`:

ibmvscsis_free_command_q
========================

.. c:function:: long ibmvscsis_free_command_q(struct scsi_info *vscsi)

    Free Command Queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_free_command_q.description`:

Description
-----------

This function calls unregister_command_q, then clears interrupts and
any pending interrupt acknowledgments associated with the command q.
It also clears memory if there is no error.

PHYP did not meet the PAPR architecture so that we must give up the
lock. This causes a timing hole regarding state change.  To close the
hole this routine does accounting on any change that occurred during
the time the lock is not held.

.. _`ibmvscsis_free_command_q.note`:

NOTE
----

must give up and then acquire the interrupt lock, the caller must
make sure that state and or flags will prevent interrupt handler from
scheduling work.

.. _`ibmvscsis_free_command_q.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process level, interrupt lock is held

.. _`ibmvscsis_cmd_q_dequeue`:

ibmvscsis_cmd_q_dequeue
=======================

.. c:function:: struct viosrp_crq *ibmvscsis_cmd_q_dequeue(uint mask, uint *current_index, struct viosrp_crq *base_addr)

    Get valid Command element

    :param uint mask:
        Mask to use in case index wraps

    :param uint \*current_index:
        Current index into command queue

    :param struct viosrp_crq \*base_addr:
        Pointer to start of command queue

.. _`ibmvscsis_cmd_q_dequeue.description`:

Description
-----------

Returns a pointer to a valid command element or NULL, if the command
queue is empty

.. _`ibmvscsis_cmd_q_dequeue.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt environment, interrupt lock held

.. _`ibmvscsis_send_init_message`:

ibmvscsis_send_init_message
===========================

.. c:function:: long ibmvscsis_send_init_message(struct scsi_info *vscsi, u8 format)

    send initialize message to the client

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param u8 format:
        Which Init Message format to send

.. _`ibmvscsis_send_init_message.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt environment interrupt lock held

.. _`ibmvscsis_check_init_msg`:

ibmvscsis_check_init_msg
========================

.. c:function:: long ibmvscsis_check_init_msg(struct scsi_info *vscsi, uint *format)

    Check init message valid

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param uint \*format:
        Pointer to return format of Init Message, if any.
        Set to UNUSED_FORMAT if no Init Message in queue.

.. _`ibmvscsis_check_init_msg.description`:

Description
-----------

Checks if an initialize message was queued by the initiatior
after the queue was created and before the interrupt was enabled.

.. _`ibmvscsis_check_init_msg.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process level only, interrupt lock held

.. _`ibmvscsis_disconnect`:

ibmvscsis_disconnect
====================

.. c:function:: void ibmvscsis_disconnect(struct work_struct *work)

    Helper function to disconnect

    :param struct work_struct \*work:
        Pointer to work_struct, gives access to our adapter structure

.. _`ibmvscsis_disconnect.description`:

Description
-----------

An error has occurred or the driver received a Transport event,
and the driver is requesting that the command queue be de-registered
in a safe manner. If there is no outstanding I/O then we can stop the
queue. If we are restarting the queue it will be reflected in the
the state of the adapter.

.. _`ibmvscsis_disconnect.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process environment

.. _`ibmvscsis_post_disconnect`:

ibmvscsis_post_disconnect
=========================

.. c:function:: void ibmvscsis_post_disconnect(struct scsi_info *vscsi, uint new_state, uint flag_bits)

    Schedule the disconnect

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param uint new_state:
        State to move to after disconnecting

    :param uint flag_bits:
        Flags to turn on in adapter structure

.. _`ibmvscsis_post_disconnect.description`:

Description
-----------

If it's already been scheduled, then see if we need to "upgrade"
the new state (if the one passed in is more "severe" than the
previous one).

.. _`ibmvscsis_post_disconnect.precondition`:

PRECONDITION
------------

interrupt lock is held

.. _`ibmvscsis_handle_init_compl_msg`:

ibmvscsis_handle_init_compl_msg
===============================

.. c:function:: long ibmvscsis_handle_init_compl_msg(struct scsi_info *vscsi)

    Respond to an Init Complete Message

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_handle_init_compl_msg.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`ibmvscsis_handle_init_msg`:

ibmvscsis_handle_init_msg
=========================

.. c:function:: long ibmvscsis_handle_init_msg(struct scsi_info *vscsi)

    Respond to an Init Message

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_handle_init_msg.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`ibmvscsis_init_msg`:

ibmvscsis_init_msg
==================

.. c:function:: long ibmvscsis_init_msg(struct scsi_info *vscsi, struct viosrp_crq *crq)

    Respond to an init message

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct viosrp_crq \*crq:
        Pointer to CRQ element containing the Init Message

.. _`ibmvscsis_init_msg.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_establish_new_q`:

ibmvscsis_establish_new_q
=========================

.. c:function:: long ibmvscsis_establish_new_q(struct scsi_info *vscsi)

    Establish new CRQ queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_establish_new_q.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`ibmvscsis_reset_queue`:

ibmvscsis_reset_queue
=====================

.. c:function:: void ibmvscsis_reset_queue(struct scsi_info *vscsi)

    Reset CRQ Queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_reset_queue.description`:

Description
-----------

This function calls h_free_q and then calls h_reg_q and does all
of the bookkeeping to get us back to where we can communicate.

Actually, we don't always call h_free_crq.  A problem was discovered
where one partition would close and reopen his queue, which would
cause his partner to get a transport event, which would cause him to
close and reopen his queue, which would cause the original partition
to get a transport event, etc., etc.  To prevent this, we don't
actually close our queue if the client initiated the reset, (i.e.
either we got a transport event or we have detected that the client's
queue is gone)

.. _`ibmvscsis_reset_queue.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process environment, called with interrupt lock held

.. _`ibmvscsis_free_cmd_resources`:

ibmvscsis_free_cmd_resources
============================

.. c:function:: void ibmvscsis_free_cmd_resources(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd)

    Free command resources

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Command which is not longer in use

.. _`ibmvscsis_free_cmd_resources.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`ibmvscsis_trans_event`:

ibmvscsis_trans_event
=====================

.. c:function:: long ibmvscsis_trans_event(struct scsi_info *vscsi, struct viosrp_crq *crq)

    Handle a Transport Event

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct viosrp_crq \*crq:
        Pointer to CRQ entry containing the Transport Event

.. _`ibmvscsis_trans_event.description`:

Description
-----------

Do the logic to close the I_T nexus.  This function may not
behave to specification.

.. _`ibmvscsis_trans_event.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_poll_cmd_q`:

ibmvscsis_poll_cmd_q
====================

.. c:function:: void ibmvscsis_poll_cmd_q(struct scsi_info *vscsi)

    Poll Command Queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_poll_cmd_q.description`:

Description
-----------

Called to handle command elements that may have arrived while
interrupts were disabled.

.. _`ibmvscsis_poll_cmd_q.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

intr_lock must be held

.. _`ibmvscsis_free_cmd_qs`:

ibmvscsis_free_cmd_qs
=====================

.. c:function:: void ibmvscsis_free_cmd_qs(struct scsi_info *vscsi)

    Free elements in queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_free_cmd_qs.description`:

Description
-----------

Free all of the elements on all queues that are waiting for
whatever reason.

.. _`ibmvscsis_free_cmd_qs.precondition`:

PRECONDITION
------------

Called with interrupt lock held

.. _`ibmvscsis_get_free_cmd`:

ibmvscsis_get_free_cmd
======================

.. c:function:: struct ibmvscsis_cmd *ibmvscsis_get_free_cmd(struct scsi_info *vscsi)

    Get free command from list

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_get_free_cmd.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`ibmvscsis_adapter_idle`:

ibmvscsis_adapter_idle
======================

.. c:function:: void ibmvscsis_adapter_idle(struct scsi_info *vscsi)

    Helper function to handle idle adapter

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_adapter_idle.description`:

Description
-----------

This function is called when the adapter is idle when the driver
is attempting to clear an error condition.
The adapter is considered busy if any of its cmd queues
are non-empty. This function can be invoked
from the off level disconnect function.

.. _`ibmvscsis_adapter_idle.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process environment called with interrupt lock held

.. _`ibmvscsis_copy_crq_packet`:

ibmvscsis_copy_crq_packet
=========================

.. c:function:: long ibmvscsis_copy_crq_packet(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd, struct viosrp_crq *crq)

    Copy CRQ Packet

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Pointer to command element to use to process the request

    :param struct viosrp_crq \*crq:
        Pointer to CRQ entry containing the request

.. _`ibmvscsis_copy_crq_packet.description`:

Description
-----------

Copy the srp information unit from the hosted
partition using remote dma

.. _`ibmvscsis_copy_crq_packet.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_adapter_info`:

ibmvscsis_adapter_info
======================

.. c:function:: long ibmvscsis_adapter_info(struct scsi_info *vscsi, struct iu_entry *iue)

    Service an Adapter Info MAnagement Data gram

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct iu_entry \*iue:
        Information Unit containing the Adapter Info MAD request

.. _`ibmvscsis_adapter_info.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt adapter lock is held

.. _`ibmvscsis_cap_mad`:

ibmvscsis_cap_mad
=================

.. c:function:: int ibmvscsis_cap_mad(struct scsi_info *vscsi, struct iu_entry *iue)

    Service a Capabilities MAnagement Data gram

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct iu_entry \*iue:
        Information Unit containing the Capabilities MAD request

.. _`ibmvscsis_cap_mad.note`:

NOTE
----

if you return an error from this routine you must be
disconnecting or you will cause a hang

.. _`ibmvscsis_cap_mad.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt called with adapter lock held

.. _`ibmvscsis_process_mad`:

ibmvscsis_process_mad
=====================

.. c:function:: long ibmvscsis_process_mad(struct scsi_info *vscsi, struct iu_entry *iue)

    Service a MAnagement Data gram

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct iu_entry \*iue:
        Information Unit containing the MAD request

.. _`ibmvscsis_process_mad.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`srp_snd_msg_failed`:

srp_snd_msg_failed
==================

.. c:function:: void srp_snd_msg_failed(struct scsi_info *vscsi, long rc)

    Handle an error when sending a response

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param long rc:
        The return code from the h_send_crq command

.. _`srp_snd_msg_failed.description`:

Description
-----------

Must be called with interrupt lock held.

.. _`ibmvscsis_send_messages`:

ibmvscsis_send_messages
=======================

.. c:function:: void ibmvscsis_send_messages(struct scsi_info *vscsi)

    Send a Response

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_send_messages.description`:

Description
-----------

Send a response, first checking the waiting queue. Responses are
sent in order they are received. If the response cannot be sent,
because the client queue is full, it stays on the waiting queue.

.. _`ibmvscsis_send_messages.precondition`:

PRECONDITION
------------

Called with interrupt lock held

.. _`ibmvscsis_mad`:

ibmvscsis_mad
=============

.. c:function:: long ibmvscsis_mad(struct scsi_info *vscsi, struct viosrp_crq *crq)

    Service a MAnagement Data gram.

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct viosrp_crq \*crq:
        Pointer to the CRQ entry containing the MAD request

.. _`ibmvscsis_mad.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, called with adapter lock held

.. _`ibmvscsis_login_rsp`:

ibmvscsis_login_rsp
===================

.. c:function:: long ibmvscsis_login_rsp(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd)

    Create/copy a login response notice to the client

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Pointer to the command for the SRP Login request

.. _`ibmvscsis_login_rsp.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_srp_login_rej`:

ibmvscsis_srp_login_rej
=======================

.. c:function:: long ibmvscsis_srp_login_rej(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd, u32 reason)

    Create/copy a login rejection notice to client

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Pointer to the command for the SRP Login request

    :param u32 reason:
        The reason the SRP Login is being rejected, per SRP protocol

.. _`ibmvscsis_srp_login_rej.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_srp_login`:

ibmvscsis_srp_login
===================

.. c:function:: long ibmvscsis_srp_login(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd, struct viosrp_crq *crq)

    Process an SRP Login Request

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Command element to use to process the SRP Login request

    :param struct viosrp_crq \*crq:
        Pointer to CRQ entry containing the SRP Login request

.. _`ibmvscsis_srp_login.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, called with interrupt lock held

.. _`ibmvscsis_srp_i_logout`:

ibmvscsis_srp_i_logout
======================

.. c:function:: long ibmvscsis_srp_i_logout(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd, struct viosrp_crq *crq)

    Helper Function to close I_T Nexus

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Command element to use to process the Implicit Logout request

    :param struct viosrp_crq \*crq:
        Pointer to CRQ entry containing the Implicit Logout request

.. _`ibmvscsis_srp_i_logout.description`:

Description
-----------

Do the logic to close the I_T nexus.  This function may not
behave to specification.

.. _`ibmvscsis_srp_i_logout.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_ping_response`:

ibmvscsis_ping_response
=======================

.. c:function:: long ibmvscsis_ping_response(struct scsi_info *vscsi)

    Respond to a ping request

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_ping_response.description`:

Description
-----------

Let the client know that the server is alive and waiting on
its native I/O stack.
If any type of error occurs from the call to queue a ping
response then the client is either not accepting or receiving
interrupts.  Disconnect with an error.

.. _`ibmvscsis_ping_response.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, interrupt lock held

.. _`ibmvscsis_parse_command`:

ibmvscsis_parse_command
=======================

.. c:function:: long ibmvscsis_parse_command(struct scsi_info *vscsi, struct viosrp_crq *crq)

    Parse an element taken from the cmd rsp queue.

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct viosrp_crq \*crq:
        Pointer to CRQ element containing the SRP request

.. _`ibmvscsis_parse_command.description`:

Description
-----------

This function will return success if the command queue element is valid
and the srp iu or MAD request it pointed to was also valid.  That does
not mean that an error was not returned to the client.

.. _`ibmvscsis_parse_command.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Interrupt, intr lock held

.. _`ibmvscsis_parse_cmd`:

ibmvscsis_parse_cmd
===================

.. c:function:: void ibmvscsis_parse_cmd(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd)

    Parse SRP Command

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Pointer to command element with SRP command

.. _`ibmvscsis_parse_cmd.description`:

Description
-----------

Parse the srp command; if it is valid then submit it to tcm.

.. _`ibmvscsis_parse_cmd.note`:

Note
----

The return code does not reflect the status of the SCSI CDB.

.. _`ibmvscsis_parse_cmd.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process level

.. _`ibmvscsis_parse_task`:

ibmvscsis_parse_task
====================

.. c:function:: void ibmvscsis_parse_task(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd)

    Parse SRP Task Management Request

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Pointer to command element with SRP task management request

.. _`ibmvscsis_parse_task.description`:

Description
-----------

Parse the srp task management request; if it is valid then submit it to tcm.

.. _`ibmvscsis_parse_task.note`:

Note
----

The return code does not reflect the status of the task management
request.

.. _`ibmvscsis_parse_task.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Processor level

.. _`ibmvscsis_service_wait_q`:

ibmvscsis_service_wait_q
========================

.. c:function:: enum hrtimer_restart ibmvscsis_service_wait_q(struct hrtimer *timer)

    Service Waiting Queue

    :param struct hrtimer \*timer:
        Pointer to timer which has expired

.. _`ibmvscsis_service_wait_q.description`:

Description
-----------

This routine is called when the timer pops to service the waiting
queue. Elements on the queue have completed, their responses have been
copied to the client, but the client's response queue was full so
the queue message could not be sent. The routine grabs the proper locks
and calls send messages.

.. _`ibmvscsis_service_wait_q.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

called at interrupt level

.. _`ibmvscsis_enable_change_state`:

ibmvscsis_enable_change_state
=============================

.. c:function:: long ibmvscsis_enable_change_state(struct scsi_info *vscsi)

    Set new state based on enabled status

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_enable_change_state.description`:

Description
-----------

This function determines our new state now that we are enabled.  This
may involve sending an Init Complete message to the client.

Must be called with interrupt lock held.

.. _`ibmvscsis_create_command_q`:

ibmvscsis_create_command_q
==========================

.. c:function:: long ibmvscsis_create_command_q(struct scsi_info *vscsi, int num_cmds)

    Create Command Queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param int num_cmds:
        Currently unused.  In the future, may be used to determine
        the size of the CRQ.

.. _`ibmvscsis_create_command_q.description`:

Description
-----------

Allocates memory for command queue maps remote memory into an ioba
initializes the command response queue

.. _`ibmvscsis_create_command_q.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process level only

.. _`ibmvscsis_destroy_command_q`:

ibmvscsis_destroy_command_q
===========================

.. c:function:: void ibmvscsis_destroy_command_q(struct scsi_info *vscsi)

    Destroy Command Queue

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

.. _`ibmvscsis_destroy_command_q.description`:

Description
-----------

Releases memory for command queue and unmaps mapped remote memory.

.. _`ibmvscsis_destroy_command_q.execution-environment`:

EXECUTION ENVIRONMENT
---------------------

Process level only

.. _`srp_build_response`:

srp_build_response
==================

.. c:function:: long srp_build_response(struct scsi_info *vscsi, struct ibmvscsis_cmd *cmd, uint *len_p)

    Build an SRP response buffer

    :param struct scsi_info \*vscsi:
        Pointer to our adapter structure

    :param struct ibmvscsis_cmd \*cmd:
        Pointer to command for which to send the response

    :param uint \*len_p:
        Where to return the length of the IU response sent.  This
        is needed to construct the CRQ response.

.. _`srp_build_response.description`:

Description
-----------

Build the SRP response buffer and copy it to the client's memory space.

.. _`ibmvscsis_handle_crq`:

ibmvscsis_handle_crq
====================

.. c:function:: void ibmvscsis_handle_crq(unsigned long data)

    Handle CRQ

    :param unsigned long data:
        Pointer to our adapter structure

.. _`ibmvscsis_handle_crq.description`:

Description
-----------

Read the command elements from the command queue and copy the payloads
associated with the command elements to local memory and execute the
SRP requests.

.. _`ibmvscsis_handle_crq.note`:

Note
----

this is an edge triggered interrupt. It can not be shared.

.. This file was automatic generated / don't edit.


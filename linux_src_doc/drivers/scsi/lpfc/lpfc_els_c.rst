.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_els.c

.. _`lpfc_els_chk_latt`:

lpfc_els_chk_latt
=================

.. c:function:: int lpfc_els_chk_latt(struct lpfc_vport *vport)

    Check host link attention event for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_els_chk_latt.description`:

Description
-----------

This routine checks whether there is an outstanding host link
attention event during the discovery process with the \ ``vport``\ . It is done
by reading the HBA's Host Attention (HA) register. If there is any host
link attention events during this \ ``vport``\ 's discovery process, the \ ``vport``\ 
shall be marked as FC_ABORT_DISCOVERY, a host link attention clear shall
be issued if the link state is not already in host link cleared state,
and a return code shall indicate whether the host link attention event
had happened.

Note that, if either the host link is in state LPFC_LINK_DOWN or \ ``vport``\ 
state in LPFC_VPORT_READY, the request for checking host link attention
event will be ignored and a return code shall indicate no host link
attention event had happened.

Return codes
0 - no host link attention event happened
1 - host link attention event happened

.. _`lpfc_prep_els_iocb`:

lpfc_prep_els_iocb
==================

.. c:function:: struct lpfc_iocbq *lpfc_prep_els_iocb(struct lpfc_vport *vport, uint8_t expectRsp, uint16_t cmdSize, uint8_t retry, struct lpfc_nodelist *ndlp, uint32_t did, uint32_t elscmd)

    Allocate and prepare a lpfc iocb data structure

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint8_t expectRsp:
        flag indicating whether response is expected.

    :param uint16_t cmdSize:
        size of the ELS command.

    :param uint8_t retry:
        number of retries to the command IOCB when it fails.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param uint32_t did:
        destination identifier.

    :param uint32_t elscmd:
        the ELS command code.

.. _`lpfc_prep_els_iocb.description`:

Description
-----------

This routine is used for allocating a lpfc-IOCB data structure from
the driver lpfc-IOCB free-list and prepare the IOCB with the parameters
passed into the routine for discovery state machine to issue an Extended
Link Service (ELS) commands. It is a generic lpfc-IOCB allocation
and preparation routine that is used by all the discovery state machine
routines and the ELS command-specific fields will be later set up by
the individual discovery machine routines after calling this routine
allocating and preparing a generic IOCB data structure. It fills in the
Buffer Descriptor Entries (BDEs), allocates buffers for both command
payload and response payload (if expected). The reference count on the
ndlp is incremented by 1 and the reference to the ndlp is put into
context1 of the IOCB data structure for this IOCB to hold the ndlp
reference for the command's callback function to access later.

Return code
Pointer to the newly allocated/prepared els iocb data structure
NULL - when els iocb data structure allocation/preparation failed

.. _`lpfc_issue_fabric_reglogin`:

lpfc_issue_fabric_reglogin
==========================

.. c:function:: int lpfc_issue_fabric_reglogin(struct lpfc_vport *vport)

    Issue fabric registration login for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_issue_fabric_reglogin.description`:

Description
-----------

This routine issues a fabric registration login for a \ ``vport``\ . An
active ndlp node with Fabric_DID must already exist for this \ ``vport``\ .
The routine invokes two mailbox commands to carry out fabric registration

.. _`lpfc_issue_fabric_reglogin.login-through-the-hba-firmware`:

login through the HBA firmware
------------------------------

the first mailbox command requests the
HBA to perform link configuration for the \ ``vport``\ ; and the second mailbox
command requests the HBA to perform the actual fabric registration login
with the \ ``vport``\ .

Return code
0 - successfully issued fabric registration login for \ ``vport``\ 
-ENXIO -- failed to issue fabric registration login for \ ``vport``\ 

.. _`lpfc_issue_reg_vfi`:

lpfc_issue_reg_vfi
==================

.. c:function:: int lpfc_issue_reg_vfi(struct lpfc_vport *vport)

    Register VFI for this vport's fabric login

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_issue_reg_vfi.description`:

Description
-----------

This routine issues a REG_VFI mailbox for the vfi, vpi, fcfi triplet for
the \ ``vport``\ . This mailbox command is necessary for SLI4 port only.

Return code
0 - successfully issued REG_VFI for \ ``vport``\ 
A failure code otherwise.

.. _`lpfc_issue_unreg_vfi`:

lpfc_issue_unreg_vfi
====================

.. c:function:: int lpfc_issue_unreg_vfi(struct lpfc_vport *vport)

    Unregister VFI for this vport's fabric login

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_issue_unreg_vfi.description`:

Description
-----------

This routine issues a UNREG_VFI mailbox with the vfi, vpi, fcfi triplet for
the \ ``vport``\ . This mailbox command is necessary for SLI4 port only.

Return code
0 - successfully issued REG_VFI for \ ``vport``\ 
A failure code otherwise.

.. _`lpfc_check_clean_addr_bit`:

lpfc_check_clean_addr_bit
=========================

.. c:function:: uint8_t lpfc_check_clean_addr_bit(struct lpfc_vport *vport, struct serv_parm *sp)

    Check whether assigned FCID is clean.

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct serv_parm \*sp:
        pointer to service parameter data structure.

.. _`lpfc_check_clean_addr_bit.description`:

Description
-----------

This routine is called from FLOGI/FDISC completion handler functions.
lpfc_check_clean_addr_bit return 1 when FCID/Fabric portname/ Fabric
node nodename is changed in the completion service parameter else return
0. This function also set flag in the vport data structure to delay
NP_Port discovery after the FLOGI/FDISC completion if Clean address bit
in FLOGI/FDISC response is cleared and FCID/Fabric portname/ Fabric
node nodename is changed in the completion service parameter.

Return code
0 - FCID and Fabric Nodename and Fabric portname is not changed.
1 - FCID or Fabric Nodename or Fabric portname is changed.

.. _`lpfc_cmpl_els_flogi_fabric`:

lpfc_cmpl_els_flogi_fabric
==========================

.. c:function:: int lpfc_cmpl_els_flogi_fabric(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, struct serv_parm *sp, IOCB_t *irsp)

    Completion function for flogi to a fabric port

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param struct serv_parm \*sp:
        pointer to service parameter data structure.

    :param IOCB_t \*irsp:
        pointer to the IOCB within the lpfc response IOCB.

.. _`lpfc_cmpl_els_flogi_fabric.description`:

Description
-----------

This routine is invoked by the \ :c:func:`lpfc_cmpl_els_flogi`\  completion callback
function to handle the completion of a Fabric Login (FLOGI) into a fabric
port in a fabric topology. It properly sets up the parameters to the \ ``ndlp``\ 
from the IOCB response. It also check the newly assigned N_Port ID to the
\ ``vport``\  against the previously assigned N_Port ID. If it is different from
the previously assigned Destination ID (DID), the \ :c:func:`lpfc_unreg_rpi`\  routine
is invoked on all the remaining nodes with the \ ``vport``\  to unregister the
Remote Port Indicators (RPIs). Finally, the \ :c:func:`lpfc_issue_fabric_reglogin`\ 
is invoked to register login to the fabric.

Return code
0 - Success (currently, always return 0)

.. _`lpfc_cmpl_els_flogi_nport`:

lpfc_cmpl_els_flogi_nport
=========================

.. c:function:: int lpfc_cmpl_els_flogi_nport(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, struct serv_parm *sp)

    Completion function for flogi to an N_Port

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param struct serv_parm \*sp:
        pointer to service parameter data structure.

.. _`lpfc_cmpl_els_flogi_nport.description`:

Description
-----------

This routine is invoked by the \ :c:func:`lpfc_cmpl_els_flogi`\  completion callback
function to handle the completion of a Fabric Login (FLOGI) into an N_Port
in a point-to-point topology. First, the \ ``vport``\ 's N_Port Name is compared

.. _`lpfc_cmpl_els_flogi_nport.with-the-received-n_port-name`:

with the received N_Port Name
-----------------------------

if the \ ``vport``\ 's N_Port Name is greater than
the received N_Port Name lexicographically, this node shall assign local
N_Port ID (PT2PT_LocalID: 1) and remote N_Port ID (PT2PT_RemoteID: 2) and
will send out Port Login (PLOGI) with the N_Port IDs assigned. Otherwise,
this node shall just wait for the remote node to issue PLOGI and assign
N_Port IDs.

Return code
0 - Success
-ENXIO - Fail

.. _`lpfc_cmpl_els_flogi`:

lpfc_cmpl_els_flogi
===================

.. c:function:: void lpfc_cmpl_els_flogi(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for flogi

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_flogi.description`:

Description
-----------

This routine is the top-level completion callback function for issuing
a Fabric Login (FLOGI) command. If the response IOCB reported error,
the \ :c:func:`lpfc_els_retry`\  routine shall be invoked to retry the FLOGI. If
retry has been made (either immediately or delayed with \ :c:func:`lpfc_els_retry`\ 
returning 1), the command IOCB will be released and function returned.
If the retry attempt has been given up (possibly reach the maximum
number of retries), one additional decrement of ndlp reference shall be
invoked before going out after releasing the command IOCB. This will
actually release the remote node (Note, \ :c:func:`lpfc_els_free_iocb`\  will also
invoke one decrement of ndlp reference count). If no error reported in
the IOCB status, the command Port ID field is used to determine whether
this is a point-to-point topology or a fabric topology: if the Port ID
field is assigned, it is a fabric topology; otherwise, it is a
point-to-point topology. The routine \ :c:func:`lpfc_cmpl_els_flogi_fabric`\  or
\ :c:func:`lpfc_cmpl_els_flogi_nport`\  shall be invoked accordingly to handle the
specific topology completion conditions.

.. _`lpfc_issue_els_flogi`:

lpfc_issue_els_flogi
====================

.. c:function:: int lpfc_issue_els_flogi(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint8_t retry)

    Issue an flogi iocb command for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_flogi.description`:

Description
-----------

This routine issues a Fabric Login (FLOGI) Request ELS command
for a \ ``vport``\ . The initiator service parameters are put into the payload
of the FLOGI Request IOCB and the top-level callback function pointer
to \ :c:func:`lpfc_cmpl_els_flogi`\  routine is put to the IOCB completion callback
function field. The lpfc_issue_fabric_iocb routine is invoked to send
out FLOGI ELS command with one outstanding fabric IOCB at a time.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the FLOGI ELS command.

Return code
0 - successfully issued flogi iocb for \ ``vport``\ 
1 - failed to issue flogi iocb for \ ``vport``\ 

.. _`lpfc_els_abort_flogi`:

lpfc_els_abort_flogi
====================

.. c:function:: int lpfc_els_abort_flogi(struct lpfc_hba *phba)

    Abort all outstanding flogi iocbs

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_els_abort_flogi.description`:

Description
-----------

This routine aborts all the outstanding Fabric Login (FLOGI) IOCBs
with a \ ``phba``\ . This routine walks all the outstanding IOCBs on the txcmplq
list and issues an abort IOCB commond on each outstanding IOCB that
contains a active Fabric_DID ndlp. Note that this function is to issue
the abort IOCB command on all the outstanding IOCBs, thus when this
function returns, it does not guarantee all the IOCBs are actually aborted.

Return code
0 - Successfully issued abort iocb on all outstanding flogis (Always 0)

.. _`lpfc_initial_flogi`:

lpfc_initial_flogi
==================

.. c:function:: int lpfc_initial_flogi(struct lpfc_vport *vport)

    Issue an initial fabric login for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_initial_flogi.description`:

Description
-----------

This routine issues an initial Fabric Login (FLOGI) for the \ ``vport``\ 
specified. It first searches the ndlp with the Fabric_DID (0xfffffe) from
the \ ``vport``\ 's ndlp list. If no such ndlp found, it will create an ndlp and
put it into the \ ``vport``\ 's ndlp list. If an inactive ndlp found on the list,
it will just be enabled and made active. The \ :c:func:`lpfc_issue_els_flogi`\  routine
is then invoked with the \ ``vport``\  and the ndlp to perform the FLOGI for the
\ ``vport``\ .

Return code
0 - failed to issue initial flogi for \ ``vport``\ 
1 - successfully issued initial flogi for \ ``vport``\ 

.. _`lpfc_initial_fdisc`:

lpfc_initial_fdisc
==================

.. c:function:: int lpfc_initial_fdisc(struct lpfc_vport *vport)

    Issue an initial fabric discovery for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_initial_fdisc.description`:

Description
-----------

This routine issues an initial Fabric Discover (FDISC) for the \ ``vport``\ 
specified. It first searches the ndlp with the Fabric_DID (0xfffffe) from
the \ ``vport``\ 's ndlp list. If no such ndlp found, it will create an ndlp and
put it into the \ ``vport``\ 's ndlp list. If an inactive ndlp found on the list,
it will just be enabled and made active. The \ :c:func:`lpfc_issue_els_fdisc`\  routine
is then invoked with the \ ``vport``\  and the ndlp to perform the FDISC for the
\ ``vport``\ .

Return code
0 - failed to issue initial fdisc for \ ``vport``\ 
1 - successfully issued initial fdisc for \ ``vport``\ 

.. _`lpfc_more_plogi`:

lpfc_more_plogi
===============

.. c:function:: void lpfc_more_plogi(struct lpfc_vport *vport)

    Check and issue remaining plogis for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_more_plogi.description`:

Description
-----------

This routine checks whether there are more remaining Port Logins
(PLOGI) to be issued for the \ ``vport``\ . If so, it will invoke the routine
\ :c:func:`lpfc_els_disc_plogi`\  to go through the Node Port Recovery (NPR) nodes
to issue ELS PLOGIs up to the configured discover threads with the
\ ``vport``\  (@vport->cfg_discovery_threads). The function also decrement
the \ ``vport``\ 's num_disc_node by 1 if it is not already 0.

.. _`lpfc_plogi_confirm_nport`:

lpfc_plogi_confirm_nport
========================

.. c:function:: struct lpfc_nodelist *lpfc_plogi_confirm_nport(struct lpfc_hba *phba, uint32_t *prsp, struct lpfc_nodelist *ndlp)

    Confirm pologi wwpn matches stored ndlp

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint32_t \*prsp:
        pointer to response IOCB payload.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_plogi_confirm_nport.description`:

Description
-----------

This routine checks and indicates whether the WWPN of an N_Port, retrieved
from a PLOGI, matches the WWPN that is stored in the \ ``ndlp``\  for that N_POrt.

.. _`lpfc_plogi_confirm_nport.the-following-cases-are-considered-n_port-confirmed`:

The following cases are considered N_Port confirmed
---------------------------------------------------

1) The N_Port is a Fabric ndlp; 2) The \ ``ndlp``\  is on vport list and matches
the WWPN of the N_Port logged into; 3) The \ ``ndlp``\  is not on vport list but
it does not have WWPN assigned either. If the WWPN is confirmed, the
pointer to the \ ``ndlp``\  will be returned. If the WWPN is not confirmed:
1) if there is a node on vport list other than the \ ``ndlp``\  with the same
WWPN of the N_Port PLOGI logged into, the \ :c:func:`lpfc_unreg_rpi`\  will be invoked
on that node to release the RPI associated with the node; 2) if there is
no node found on vport list with the same WWPN of the N_Port PLOGI logged
into, a new node shall be allocated (or activated). In either case, the
parameters of the \ ``ndlp``\  shall be copied to the new_ndlp, the \ ``ndlp``\  shall
be released and the new_ndlp shall be put on to the vport node list and
its pointer returned as the confirmed node.

Note that before the \ ``ndlp``\  got "released", the keepDID from not-matching
or inactive "new_ndlp" on the vport node list is assigned to the nlp_DID
of the \ ``ndlp``\ . This is because the release of \ ``ndlp``\  is actually to put it
into an inactive state on the vport node list and the vport node list
management algorithm does not allow two node with a same DID.

Return code
pointer to the PLOGI N_Port \ ``ndlp``\ 

.. _`lpfc_end_rscn`:

lpfc_end_rscn
=============

.. c:function:: void lpfc_end_rscn(struct lpfc_vport *vport)

    Check and handle more rscn for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_end_rscn.description`:

Description
-----------

This routine checks whether more Registration State Change
Notifications (RSCNs) came in while the discovery state machine was in
the FC_RSCN_MODE. If so, the \ :c:func:`lpfc_els_handle_rscn`\  routine will be
invoked to handle the additional RSCNs for the \ ``vport``\ . Otherwise, the
FC_RSCN_MODE bit will be cleared with the \ ``vport``\  to mark as the end of
handling the RSCNs.

.. _`lpfc_cmpl_els_rrq`:

lpfc_cmpl_els_rrq
=================

.. c:function:: void lpfc_cmpl_els_rrq(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion handled for els RRQs.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_rrq.description`:

Description
-----------

This routine will call the clear rrq function to free the rrq and
clear the xri's bit in the ndlp's xri_bitmap. If the ndlp does not
exist then the clear_rrq is still called because the rrq needs to
be freed.

.. _`lpfc_cmpl_els_plogi`:

lpfc_cmpl_els_plogi
===================

.. c:function:: void lpfc_cmpl_els_plogi(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for plogi

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_plogi.description`:

Description
-----------

This routine is the completion callback function for issuing the Port
Login (PLOGI) command. For PLOGI completion, there must be an active
ndlp on the vport node list that matches the remote node ID from the
PLOGI response IOCB. If such ndlp does not exist, the PLOGI is simply
ignored and command IOCB released. The PLOGI response IOCB status is
checked for error conditons. If there is error status reported, PLOGI
retry shall be attempted by invoking the \ :c:func:`lpfc_els_retry`\  routine.
Otherwise, the \ :c:func:`lpfc_plogi_confirm_nport`\  routine shall be invoked on
the ndlp and the NLP_EVT_CMPL_PLOGI state to the Discover State Machine
(DSM) is set for this PLOGI completion. Finally, it checks whether
there are additional N_Port nodes with the vport that need to perform
PLOGI. If so, the \ :c:func:`lpfc_more_plogi`\  routine is invoked to issue addition
PLOGIs.

.. _`lpfc_issue_els_plogi`:

lpfc_issue_els_plogi
====================

.. c:function:: int lpfc_issue_els_plogi(struct lpfc_vport *vport, uint32_t did, uint8_t retry)

    Issue an plogi iocb command for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint32_t did:
        destination port identifier.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_plogi.description`:

Description
-----------

This routine issues a Port Login (PLOGI) command to a remote N_Port
(with the \ ``did``\ ) for a \ ``vport``\ . Before issuing a PLOGI to a remote N_Port,
the ndlp with the remote N_Port DID must exist on the \ ``vport``\ 's ndlp list.
This routine constructs the proper feilds of the PLOGI IOCB and invokes
the \ :c:func:`lpfc_sli_issue_iocb`\  routine to send out PLOGI ELS command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the PLOGI ELS command.

Return code
0 - Successfully issued a plogi for \ ``vport``\ 
1 - failed to issue a plogi for \ ``vport``\ 

.. _`lpfc_cmpl_els_prli`:

lpfc_cmpl_els_prli
==================

.. c:function:: void lpfc_cmpl_els_prli(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for prli

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_prli.description`:

Description
-----------

This routine is the completion callback function for a Process Login
(PRLI) ELS command. The PRLI response IOCB status is checked for error
status. If there is error status reported, PRLI retry shall be attempted
by invoking the \ :c:func:`lpfc_els_retry`\  routine. Otherwise, the state
NLP_EVT_CMPL_PRLI is sent to the Discover State Machine (DSM) for this
ndlp to mark the PRLI completion.

.. _`lpfc_issue_els_prli`:

lpfc_issue_els_prli
===================

.. c:function:: int lpfc_issue_els_prli(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint8_t retry)

    Issue a prli iocb command for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_prli.description`:

Description
-----------

This routine issues a Process Login (PRLI) ELS command for the
\ ``vport``\ . The PRLI service parameters are set up in the payload of the
PRLI Request command and the pointer to \ :c:func:`lpfc_cmpl_els_prli`\  routine
is put to the IOCB completion callback func field before invoking the
routine \ :c:func:`lpfc_sli_issue_iocb`\  to send out PRLI command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the PRLI ELS command.

Return code
0 - successfully issued prli iocb command for \ ``vport``\ 
1 - failed to issue prli iocb command for \ ``vport``\ 

.. _`lpfc_rscn_disc`:

lpfc_rscn_disc
==============

.. c:function:: void lpfc_rscn_disc(struct lpfc_vport *vport)

    Perform rscn discovery for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_rscn_disc.description`:

Description
-----------

This routine performs Registration State Change Notification (RSCN)
discovery for a \ ``vport``\ . If the \ ``vport``\ 's node port recovery count is not
zero, it will invoke the \ :c:func:`lpfc_els_disc_plogi`\  to perform PLOGI for all
the nodes that need recovery. If none of the PLOGI were needed through
the \ :c:func:`lpfc_els_disc_plogi`\  routine, the \ :c:func:`lpfc_end_rscn`\  routine shall be
invoked to check and handle possible more RSCN came in during the period
of processing the current ones.

.. _`lpfc_adisc_done`:

lpfc_adisc_done
===============

.. c:function:: void lpfc_adisc_done(struct lpfc_vport *vport)

    Complete the adisc phase of discovery

    :param struct lpfc_vport \*vport:
        pointer to lpfc_vport hba data structure that finished all ADISCs.

.. _`lpfc_adisc_done.description`:

Description
-----------

This function is called when the final ADISC is completed during discovery.
This function handles clearing link attention or issuing reg_vpi depending
on whether npiv is enabled. This function also kicks off the PLOGI phase of
discovery.
This function is called with no locks held.

.. _`lpfc_more_adisc`:

lpfc_more_adisc
===============

.. c:function:: void lpfc_more_adisc(struct lpfc_vport *vport)

    Issue more adisc as needed

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_more_adisc.description`:

Description
-----------

This routine determines whether there are more ndlps on a \ ``vport``\ 
node list need to have Address Discover (ADISC) issued. If so, it will
invoke the \ :c:func:`lpfc_els_disc_adisc`\  routine to issue ADISC on the \ ``vport``\ 's
remaining nodes which need to have ADISC sent.

.. _`lpfc_cmpl_els_adisc`:

lpfc_cmpl_els_adisc
===================

.. c:function:: void lpfc_cmpl_els_adisc(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for adisc

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_adisc.description`:

Description
-----------

This routine is the completion function for issuing the Address Discover
(ADISC) command. It first checks to see whether link went down during
the discovery process. If so, the node will be marked as node port
recovery for issuing discover IOCB by the link attention handler and
exit. Otherwise, the response status is checked. If error was reported
in the response status, the ADISC command shall be retried by invoking
the \ :c:func:`lpfc_els_retry`\  routine. Otherwise, if no error was reported in
the response status, the state machine is invoked to set transition
with respect to NLP_EVT_CMPL_ADISC event.

.. _`lpfc_issue_els_adisc`:

lpfc_issue_els_adisc
====================

.. c:function:: int lpfc_issue_els_adisc(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint8_t retry)

    Issue an address discover iocb to an node on a vport

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_adisc.description`:

Description
-----------

This routine issues an Address Discover (ADISC) for an \ ``ndlp``\  on a
\ ``vport``\ . It prepares the payload of the ADISC ELS command, updates the
and states of the ndlp, and invokes the \ :c:func:`lpfc_sli_issue_iocb`\  routine
to issue the ADISC ELS command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the ADISC ELS command.

Return code
0 - successfully issued adisc
1 - failed to issue adisc

.. _`lpfc_cmpl_els_logo`:

lpfc_cmpl_els_logo
==================

.. c:function:: void lpfc_cmpl_els_logo(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for logo

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_logo.description`:

Description
-----------

This routine is the completion function for issuing the ELS Logout (LOGO)
command. If no error status was reported from the LOGO response, the
state machine of the associated ndlp shall be invoked for transition with
respect to NLP_EVT_CMPL_LOGO event. Otherwise, if error status was reported,
the \ :c:func:`lpfc_els_retry`\  routine will be invoked to retry the LOGO command.

.. _`lpfc_issue_els_logo`:

lpfc_issue_els_logo
===================

.. c:function:: int lpfc_issue_els_logo(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint8_t retry)

    Issue a logo to an node on a vport

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_logo.description`:

Description
-----------

This routine constructs and issues an ELS Logout (LOGO) iocb command
to a remote node, referred by an \ ``ndlp``\  on a \ ``vport``\ . It constructs the
payload of the IOCB, properly sets up the \ ``ndlp``\  state, and invokes the
\ :c:func:`lpfc_sli_issue_iocb`\  routine to send out the LOGO ELS command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the LOGO ELS command.

Return code
0 - successfully issued logo
1 - failed to issue logo

.. _`lpfc_cmpl_els_cmd`:

lpfc_cmpl_els_cmd
=================

.. c:function:: void lpfc_cmpl_els_cmd(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for generic els command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_cmd.description`:

Description
-----------

This routine is a generic completion callback function for ELS commands.
Specifically, it is the callback function which does not need to perform
any command specific operations. It is currently used by the ELS command
issuing routines for the ELS State Change  Request (SCR),
\ :c:func:`lpfc_issue_els_scr`\ , and the ELS Fibre Channel Address Resolution
Protocol Response (FARPR) routine, \ :c:func:`lpfc_issue_els_farpr`\ . Other than
certain debug loggings, this callback function simply invokes the
\ :c:func:`lpfc_els_chk_latt`\  routine to check whether link went down during the
discovery process.

.. _`lpfc_issue_els_scr`:

lpfc_issue_els_scr
==================

.. c:function:: int lpfc_issue_els_scr(struct lpfc_vport *vport, uint32_t nportid, uint8_t retry)

    Issue a scr to an node on a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint32_t nportid:
        N_Port identifier to the remote node.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_scr.description`:

Description
-----------

This routine issues a State Change Request (SCR) to a fabric node
on a \ ``vport``\ . The remote node \ ``nportid``\  is passed into the function. It
first search the \ ``vport``\  node list to find the matching ndlp. If no such
ndlp is found, a new ndlp shall be created for this (SCR) purpose. An
IOCB is allocated, payload prepared, and the \ :c:func:`lpfc_sli_issue_iocb`\ 
routine is invoked to send the SCR IOCB.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the SCR ELS command.

Return code
0 - Successfully issued scr command
1 - Failed to issue scr command

.. _`lpfc_issue_els_farpr`:

lpfc_issue_els_farpr
====================

.. c:function:: int lpfc_issue_els_farpr(struct lpfc_vport *vport, uint32_t nportid, uint8_t retry)

    Issue a farp to an node on a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint32_t nportid:
        N_Port identifier to the remote node.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_farpr.description`:

Description
-----------

This routine issues a Fibre Channel Address Resolution Response
(FARPR) to a node on a vport. The remote node N_Port identifier (@nportid)
is passed into the function. It first search the \ ``vport``\  node list to find
the matching ndlp. If no such ndlp is found, a new ndlp shall be created
for this (FARPR) purpose. An IOCB is allocated, payload prepared, and the
\ :c:func:`lpfc_sli_issue_iocb`\  routine is invoked to send the FARPR ELS command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the PARPR ELS command.

Return code
0 - Successfully issued farpr command
1 - Failed to issue farpr command

.. _`lpfc_cancel_retry_delay_tmo`:

lpfc_cancel_retry_delay_tmo
===========================

.. c:function:: void lpfc_cancel_retry_delay_tmo(struct lpfc_vport *vport, struct lpfc_nodelist *nlp)

    Cancel the timer with delayed iocb-cmd retry

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*nlp:
        pointer to a node-list data structure.

.. _`lpfc_cancel_retry_delay_tmo.description`:

Description
-----------

This routine cancels the timer with a delayed IOCB-command retry for
a \ ``vport``\ 's \ ``ndlp``\ . It stops the timer for the delayed function retrial and
removes the ELS retry event if it presents. In addition, if the
NLP_NPR_2B_DISC bit is set in the \ ``nlp``\ 's nlp_flag bitmap, ADISC IOCB
commands are sent for the \ ``vport``\ 's nodes that require issuing discovery
ADISC.

.. _`lpfc_els_retry_delay`:

lpfc_els_retry_delay
====================

.. c:function:: void lpfc_els_retry_delay(unsigned long ptr)

    Timer function with a ndlp delayed function timer

    :param unsigned long ptr:
        holder for the pointer to the timer function associated data (ndlp).

.. _`lpfc_els_retry_delay.description`:

Description
-----------

This routine is invoked by the ndlp delayed-function timer to check
whether there is any pending ELS retry event(s) with the node. If not, it
simply returns. Otherwise, if there is at least one ELS delayed event, it
adds the delayed events to the HBA work list and invokes the
\ :c:func:`lpfc_worker_wake_up`\  routine to wake up worker thread to process the
event. Note that \ :c:func:`lpfc_nlp_get`\  is called before posting the event to
the work list to hold reference count of ndlp so that it guarantees the
reference to ndlp will still be available when the worker thread gets
to the event associated with the ndlp.

.. _`lpfc_els_retry_delay_handler`:

lpfc_els_retry_delay_handler
============================

.. c:function:: void lpfc_els_retry_delay_handler(struct lpfc_nodelist *ndlp)

    Work thread handler for ndlp delayed function

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_retry_delay_handler.description`:

Description
-----------

This routine is the worker-thread handler for processing the \ ``ndlp``\  delayed
event(s), posted by the \ :c:func:`lpfc_els_retry_delay`\  routine. It simply retrieves
the last ELS command from the associated ndlp and invokes the proper ELS
function according to the delayed ELS command to retry the command.

.. _`lpfc_els_retry`:

lpfc_els_retry
==============

.. c:function:: int lpfc_els_retry(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Make retry decision on an els command iocb

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_els_retry.description`:

Description
-----------

This routine makes a retry decision on an ELS command IOCB, which has
failed. The following ELS IOCBs use this function for retrying the command

.. _`lpfc_els_retry.when-previously-issued-command-responsed-with-error-status`:

when previously issued command responsed with error status
----------------------------------------------------------

FLOGI, PLOGI,
PRLI, ADISC, LOGO, and FDISC. Based on the ELS command type and the
returned error status, it makes the decision whether a retry shall be
issued for the command, and whether a retry shall be made immediately or
delayed. In the former case, the corresponding ELS command issuing-function
is called to retry the command. In the later case, the ELS command shall
be posted to the ndlp delayed event and delayed function timer set to the
ndlp for the delayed command issusing.

Return code
0 - No retry of els command is made
1 - Immediate or delayed retry of els command is made

.. _`lpfc_els_free_data`:

lpfc_els_free_data
==================

.. c:function:: int lpfc_els_free_data(struct lpfc_hba *phba, struct lpfc_dmabuf *buf_ptr1)

    Free lpfc dma buffer and data structure with an iocb

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_dmabuf \*buf_ptr1:
        pointer to the lpfc DMA buffer data structure.

.. _`lpfc_els_free_data.description`:

Description
-----------

This routine releases the lpfc DMA (Direct Memory Access) buffer(s)
associated with a command IOCB back to the lpfc DMA buffer pool. It first
checks to see whether there is a lpfc DMA buffer associated with the
response of the command IOCB. If so, it will be released before releasing
the lpfc DMA buffer associated with the IOCB itself.

Return code
0 - Successfully released lpfc DMA buffer (currently, always return 0)

.. _`lpfc_els_free_bpl`:

lpfc_els_free_bpl
=================

.. c:function:: int lpfc_els_free_bpl(struct lpfc_hba *phba, struct lpfc_dmabuf *buf_ptr)

    Free lpfc dma buffer and data structure with bpl

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_dmabuf \*buf_ptr:
        pointer to the lpfc dma buffer data structure.

.. _`lpfc_els_free_bpl.description`:

Description
-----------

This routine releases the lpfc Direct Memory Access (DMA) buffer
associated with a Buffer Pointer List (BPL) back to the lpfc DMA buffer
pool.

Return code
0 - Successfully released lpfc DMA buffer (currently, always return 0)

.. _`lpfc_els_free_iocb`:

lpfc_els_free_iocb
==================

.. c:function:: int lpfc_els_free_iocb(struct lpfc_hba *phba, struct lpfc_iocbq *elsiocb)

    Free a command iocb and its associated resources

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*elsiocb:
        pointer to lpfc els command iocb data structure.

.. _`lpfc_els_free_iocb.description`:

Description
-----------

This routine frees a command IOCB and its associated resources. The
command IOCB data structure contains the reference to various associated
resources, these fields must be set to NULL if the associated reference

.. _`lpfc_els_free_iocb.not-present`:

not present
-----------

context1 - reference to ndlp
context2 - reference to cmd
context2->next - reference to rsp
context3 - reference to bpl

It first properly decrements the reference count held on ndlp for the
IOCB completion callback function. If LPFC_DELAY_MEM_FREE flag is not
set, it invokes the \ :c:func:`lpfc_els_free_data`\  routine to release the Direct
Memory Access (DMA) buffers associated with the IOCB. Otherwise, it
adds the DMA buffer the \ ``phba``\  data structure for the delayed release.
If reference to the Buffer Pointer List (BPL) is present, the
\ :c:func:`lpfc_els_free_bpl`\  routine is invoked to release the DMA memory
associated with BPL. Finally, the \ :c:func:`lpfc_sli_release_iocbq`\  routine is
invoked to release the IOCB data structure back to \ ``phba``\  IOCBQ list.

Return code
0 - Success (currently, always return 0)

.. _`lpfc_cmpl_els_logo_acc`:

lpfc_cmpl_els_logo_acc
======================

.. c:function:: void lpfc_cmpl_els_logo_acc(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function to logo acc response

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_logo_acc.description`:

Description
-----------

This routine is the completion callback function to the Logout (LOGO)
Accept (ACC) Response ELS command. This routine is invoked to indicate
the completion of the LOGO process. It invokes the \ :c:func:`lpfc_nlp_not_used`\  to
release the ndlp if it has the last reference remaining (reference count
is 1). If succeeded (meaning ndlp released), it sets the IOCB context1
field to NULL to inform the following \ :c:func:`lpfc_els_free_iocb`\  routine no
ndlp reference count needs to be decremented. Otherwise, the ndlp
reference use-count shall be decremented by the \ :c:func:`lpfc_els_free_iocb`\ 
routine. Finally, the \ :c:func:`lpfc_els_free_iocb`\  is invoked to release the
IOCB data structure.

.. _`lpfc_mbx_cmpl_dflt_rpi`:

lpfc_mbx_cmpl_dflt_rpi
======================

.. c:function:: void lpfc_mbx_cmpl_dflt_rpi(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Completion callbk func for unreg dflt rpi mbox cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_mbx_cmpl_dflt_rpi.description`:

Description
-----------

This routine is the completion callback function for unregister default
RPI (Remote Port Index) mailbox command to the \ ``phba``\ . It simply releases
the associated lpfc Direct Memory Access (DMA) buffer back to the pool and
decrements the ndlp reference count held for this completion callback
function. After that, it invokes the \ :c:func:`lpfc_nlp_not_used`\  to check
whether there is only one reference left on the ndlp. If so, it will
perform one more decrement and trigger the release of the ndlp.

.. _`lpfc_cmpl_els_rsp`:

lpfc_cmpl_els_rsp
=================

.. c:function:: void lpfc_cmpl_els_rsp(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for els response iocb cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_rsp.description`:

Description
-----------

This routine is the completion callback function for ELS Response IOCB
command. In normal case, this callback function just properly sets the
nlp_flag bitmap in the ndlp data structure, if the mbox command reference
field in the command IOCB is not NULL, the referred mailbox command will
be send out, and then invokes the \ :c:func:`lpfc_els_free_iocb`\  routine to release
the IOCB. Under error conditions, such as when a LS_RJT is returned or a
link down event occurred during the discovery, the \ :c:func:`lpfc_nlp_not_used`\ 
routine shall be invoked trying to release the ndlp if no other threads
are currently referring it.

.. _`lpfc_els_rsp_acc`:

lpfc_els_rsp_acc
================

.. c:function:: int lpfc_els_rsp_acc(struct lpfc_vport *vport, uint32_t flag, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp, LPFC_MBOXQ_t *mbox)

    Prepare and issue an acc response iocb command

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint32_t flag:
        the els command code to be accepted.

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param LPFC_MBOXQ_t \*mbox:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_els_rsp_acc.description`:

Description
-----------

This routine prepares and issues an Accept (ACC) response IOCB
command. It uses the \ ``flag``\  to properly set up the IOCB field for the
specific ACC response command to be issued and invokes the
\ :c:func:`lpfc_sli_issue_iocb`\  routine to send out ACC response IOCB. If a
\ ``mbox``\  pointer is passed in, it will be put into the context_un.mbox
field of the IOCB for the completion callback function to issue the
mailbox command to the HBA later when callback is invoked.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the corresponding response ELS IOCB command.

Return code
0 - Successfully issued acc response
1 - Failed to issue acc response

.. _`lpfc_els_rsp_reject`:

lpfc_els_rsp_reject
===================

.. c:function:: int lpfc_els_rsp_reject(struct lpfc_vport *vport, uint32_t rejectError, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp, LPFC_MBOXQ_t *mbox)

    Propare and issue a rjt response iocb command

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param uint32_t rejectError:
        *undescribed*

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param LPFC_MBOXQ_t \*mbox:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_els_rsp_reject.description`:

Description
-----------

This routine prepares and issue an Reject (RJT) response IOCB
command. If a \ ``mbox``\  pointer is passed in, it will be put into the
context_un.mbox field of the IOCB for the completion callback function
to issue to the HBA later.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the reject response ELS IOCB command.

Return code
0 - Successfully issued reject response
1 - Failed to issue reject response

.. _`lpfc_els_rsp_adisc_acc`:

lpfc_els_rsp_adisc_acc
======================

.. c:function:: int lpfc_els_rsp_adisc_acc(struct lpfc_vport *vport, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp)

    Prepare and issue acc response to adisc iocb cmd

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rsp_adisc_acc.description`:

Description
-----------

This routine prepares and issues an Accept (ACC) response to Address
Discover (ADISC) ELS command. It simply prepares the payload of the IOCB
and invokes the \ :c:func:`lpfc_sli_issue_iocb`\  routine to send out the command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the ADISC Accept response ELS IOCB command.

Return code
0 - Successfully issued acc adisc response
1 - Failed to issue adisc acc response

.. _`lpfc_els_rsp_prli_acc`:

lpfc_els_rsp_prli_acc
=====================

.. c:function:: int lpfc_els_rsp_prli_acc(struct lpfc_vport *vport, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp)

    Prepare and issue acc response to prli iocb cmd

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rsp_prli_acc.description`:

Description
-----------

This routine prepares and issues an Accept (ACC) response to Process
Login (PRLI) ELS command. It simply prepares the payload of the IOCB
and invokes the \ :c:func:`lpfc_sli_issue_iocb`\  routine to send out the command.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the PRLI Accept response ELS IOCB command.

Return code
0 - Successfully issued acc prli response
1 - Failed to issue acc prli response

.. _`lpfc_els_rsp_rnid_acc`:

lpfc_els_rsp_rnid_acc
=====================

.. c:function:: int lpfc_els_rsp_rnid_acc(struct lpfc_vport *vport, uint8_t format, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp)

    Issue rnid acc response iocb command

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param uint8_t format:
        rnid command format.

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rsp_rnid_acc.description`:

Description
-----------

This routine issues a Request Node Identification Data (RNID) Accept
(ACC) response. It constructs the RNID ACC response command according to
the proper \ ``format``\  and then calls the \ :c:func:`lpfc_sli_issue_iocb`\  routine to
issue the response. Note that this command does not need to hold the ndlp
reference count for the callback. So, the ndlp reference count taken by
the \ :c:func:`lpfc_prep_els_iocb`\  routine is put back and the context1 field of
IOCB is set to NULL to indicate to the \ :c:func:`lpfc_els_free_iocb`\  routine that
there is no ndlp reference available.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function. However, for the RNID Accept Response ELS command,
this is undone later by this routine after the IOCB is allocated.

Return code
0 - Successfully issued acc rnid response
1 - Failed to issue acc rnid response

.. _`lpfc_els_clear_rrq`:

lpfc_els_clear_rrq
==================

.. c:function:: void lpfc_els_clear_rrq(struct lpfc_vport *vport, struct lpfc_iocbq *iocb, struct lpfc_nodelist *ndlp)

    Clear the rq that this rrq describes.

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_iocbq \*iocb:
        pointer to the lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_clear_rrq.description`:

Description
-----------

Return

.. _`lpfc_els_rsp_echo_acc`:

lpfc_els_rsp_echo_acc
=====================

.. c:function:: int lpfc_els_rsp_echo_acc(struct lpfc_vport *vport, uint8_t *data, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp)

    Issue echo acc response

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param uint8_t \*data:
        pointer to echo data to return in the accept.

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rsp_echo_acc.description`:

Description
-----------

Return code
0 - Successfully issued acc echo response
1 - Failed to issue acc echo response

.. _`lpfc_els_disc_adisc`:

lpfc_els_disc_adisc
===================

.. c:function:: int lpfc_els_disc_adisc(struct lpfc_vport *vport)

    Issue remaining adisc iocbs to npr nodes of a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_els_disc_adisc.description`:

Description
-----------

This routine issues Address Discover (ADISC) ELS commands to those
N_Ports which are in node port recovery state and ADISC has not been issued
for the \ ``vport``\ . Each time an ELS ADISC IOCB is issued by invoking the
\ :c:func:`lpfc_issue_els_adisc`\  routine, the per \ ``vport``\  number of discover count
(num_disc_nodes) shall be incremented. If the num_disc_nodes reaches a
pre-configured threshold (cfg_discovery_threads), the \ ``vport``\  fc_flag will
be marked with FC_NLP_MORE bit and the process of issuing remaining ADISC
IOCBs quit for later pick up. On the other hand, after walking through
all the ndlps with the \ ``vport``\  and there is none ADISC IOCB issued, the
\ ``vport``\  fc_flag shall be cleared with FC_NLP_MORE bit indicating there is
no more ADISC need to be sent.

Return code
The number of N_Ports with adisc issued.

.. _`lpfc_els_disc_plogi`:

lpfc_els_disc_plogi
===================

.. c:function:: int lpfc_els_disc_plogi(struct lpfc_vport *vport)

    Issue plogi for all npr nodes of a vport before adisc

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_els_disc_plogi.description`:

Description
-----------

This routine issues Port Login (PLOGI) ELS commands to all the N_Ports
which are in node port recovery state, with a \ ``vport``\ . Each time an ELS
ADISC PLOGI IOCB is issued by invoking the \ :c:func:`lpfc_issue_els_plogi`\  routine,
the per \ ``vport``\  number of discover count (num_disc_nodes) shall be
incremented. If the num_disc_nodes reaches a pre-configured threshold
(cfg_discovery_threads), the \ ``vport``\  fc_flag will be marked with FC_NLP_MORE
bit set and quit the process of issuing remaining ADISC PLOGIN IOCBs for
later pick up. On the other hand, after walking through all the ndlps with
the \ ``vport``\  and there is none ADISC PLOGI IOCB issued, the \ ``vport``\  fc_flag
shall be cleared with the FC_NLP_MORE bit indicating there is no more ADISC
PLOGI need to be sent.

Return code
The number of N_Ports with plogi issued.

.. _`lpfc_els_rcv_lcb`:

lpfc_els_rcv_lcb
================

.. c:function:: int lpfc_els_rcv_lcb(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited LCB

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_lcb.description`:

Description
-----------

This routine processes an unsolicited LCB(LINK CABLE BEACON) IOCB.
First, the payload of the unsolicited LCB is checked.
Then based on Subcommand beacon will either turn on or off.

Return code
0 - Sent the acc response
1 - Sent the reject response.

.. _`lpfc_els_flush_rscn`:

lpfc_els_flush_rscn
===================

.. c:function:: void lpfc_els_flush_rscn(struct lpfc_vport *vport)

    Clean up any rscn activities with a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_els_flush_rscn.description`:

Description
-----------

This routine cleans up any Registration State Change Notification
(RSCN) activity with a \ ``vport``\ . Note that the fc_rscn_flush flag of the
\ ``vport``\  together with the host_lock is used to prevent multiple thread
trying to access the RSCN array on a same \ ``vport``\  at the same time.

.. _`lpfc_rscn_payload_check`:

lpfc_rscn_payload_check
=======================

.. c:function:: int lpfc_rscn_payload_check(struct lpfc_vport *vport, uint32_t did)

    Check whether there is a pending rscn to a did

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint32_t did:
        remote destination port identifier.

.. _`lpfc_rscn_payload_check.description`:

Description
-----------

This routine checks whether there is any pending Registration State
Configuration Notification (RSCN) to a \ ``did``\  on \ ``vport``\ .

Return code
None zero - The \ ``did``\  matched with a pending rscn
0 - not able to match \ ``did``\  with a pending rscn

.. _`lpfc_rscn_recovery_check`:

lpfc_rscn_recovery_check
========================

.. c:function:: int lpfc_rscn_recovery_check(struct lpfc_vport *vport)

    Send recovery event to vport nodes matching rscn

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_rscn_recovery_check.description`:

Description
-----------

This routine sends recovery (NLP_EVT_DEVICE_RECOVERY) event to the
state machine for a \ ``vport``\ 's nodes that are with pending RSCN (Registration
State Change Notification).

Return code
0 - Successful (currently alway return 0)

.. _`lpfc_send_rscn_event`:

lpfc_send_rscn_event
====================

.. c:function:: void lpfc_send_rscn_event(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb)

    Send an RSCN event to management application

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

.. _`lpfc_send_rscn_event.description`:

Description
-----------

lpfc_send_rscn_event sends an RSCN netlink event to management
applications.

.. _`lpfc_els_rcv_rscn`:

lpfc_els_rcv_rscn
=================

.. c:function:: int lpfc_els_rcv_rscn(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited rscn iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_rscn.description`:

Description
-----------

This routine processes an unsolicited RSCN (Registration State Change
Notification) IOCB. First, the payload of the unsolicited RSCN is walked
to invoke \ :c:func:`fc_host_post_event`\  routine to the FC transport layer. If the
discover state machine is about to begin discovery, it just accepts the
RSCN and the discovery process will satisfy the RSCN. If this RSCN only
contains N_Port IDs for other vports on this HBA, it just accepts the
RSCN and ignore processing it. If the state machine is in the recovery
state, the fc_rscn_id_list of this \ ``vport``\  is walked and the
\ :c:func:`lpfc_rscn_recovery_check`\  routine is invoked to send recovery event for
all nodes that match RSCN payload. Otherwise, the \ :c:func:`lpfc_els_handle_rscn`\ 
routine is invoked to handle the RSCN event.

Return code
0 - Just sent the acc response
1 - Sent the acc response and waited for name server completion

.. _`lpfc_els_handle_rscn`:

lpfc_els_handle_rscn
====================

.. c:function:: int lpfc_els_handle_rscn(struct lpfc_vport *vport)

    Handle rscn for a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_els_handle_rscn.description`:

Description
-----------

This routine handles the Registration State Configuration Notification
(RSCN) for a \ ``vport``\ . If login to NameServer does not exist, a new ndlp shall
be created and a Port Login (PLOGI) to the NameServer is issued. Otherwise,
if the ndlp to NameServer exists, a Common Transport (CT) command to the
NameServer shall be issued. If CT command to the NameServer fails to be
issued, the \ :c:func:`lpfc_els_flush_rscn`\  routine shall be invoked to clean up any
RSCN activities with the \ ``vport``\ .

Return code
0 - Cleaned up rscn on the \ ``vport``\ 
1 - Wait for plogi to name server before proceed

.. _`lpfc_els_rcv_flogi`:

lpfc_els_rcv_flogi
==================

.. c:function:: int lpfc_els_rcv_flogi(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited flogi iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_flogi.description`:

Description
-----------

This routine processes Fabric Login (FLOGI) IOCB received as an ELS
unsolicited event. An unsolicited FLOGI can be received in a point-to-
point topology. As an unsolicited FLOGI should not be received in a loop
mode, any unsolicited FLOGI received in loop mode shall be ignored. The
\ :c:func:`lpfc_check_sparm`\  routine is invoked to check the parameters in the
unsolicited FLOGI. If parameters validation failed, the routine
\ :c:func:`lpfc_els_rsp_reject`\  shall be called with reject reason code set to
LSEXP_SPARM_OPTIONS to reject the FLOGI. Otherwise, the Port WWN in the
FLOGI shall be compared with the Port WWN of the \ ``vport``\  to determine who
will initiate PLOGI. The higher lexicographical value party shall has
higher priority (as the winning port) and will initiate PLOGI and
communicate Port_IDs (Addresses) for both nodes in PLOGI. The result
of this will be marked in the \ ``vport``\  fc_flag field with FC_PT2PT_PLOGI
and then the \ :c:func:`lpfc_els_rsp_acc`\  routine is invoked to accept the FLOGI.

Return code
0 - Successfully processed the unsolicited flogi
1 - Failed to process the unsolicited flogi

.. _`lpfc_els_rcv_rnid`:

lpfc_els_rcv_rnid
=================

.. c:function:: int lpfc_els_rcv_rnid(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited rnid iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_rnid.description`:

Description
-----------

This routine processes Request Node Identification Data (RNID) IOCB
received as an ELS unsolicited event. Only when the RNID specified format
0x0 or 0xDF (Topology Discovery Specific Node Identification Data)
present, this routine will invoke the \ :c:func:`lpfc_els_rsp_rnid_acc`\  routine to
Accept (ACC) the RNID ELS command. All the other RNID formats are
rejected by invoking the \ :c:func:`lpfc_els_rsp_reject`\  routine.

Return code
0 - Successfully processed rnid iocb (currently always return 0)

.. _`lpfc_els_rcv_echo`:

lpfc_els_rcv_echo
=================

.. c:function:: int lpfc_els_rcv_echo(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited echo iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_echo.description`:

Description
-----------

Return code
0 - Successfully processed echo iocb (currently always return 0)

.. _`lpfc_els_rcv_lirr`:

lpfc_els_rcv_lirr
=================

.. c:function:: int lpfc_els_rcv_lirr(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited lirr iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_lirr.description`:

Description
-----------

This routine processes a Link Incident Report Registration(LIRR) IOCB
received as an ELS unsolicited event. Currently, this function just invokes
the \ :c:func:`lpfc_els_rsp_reject`\  routine to reject the LIRR IOCB unconditionally.

Return code
0 - Successfully processed lirr iocb (currently always return 0)

.. _`lpfc_els_rcv_rrq`:

lpfc_els_rcv_rrq
================

.. c:function:: void lpfc_els_rcv_rrq(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited rrq iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_rrq.description`:

Description
-----------

This routine processes a Reinstate Recovery Qualifier (RRQ) IOCB
received as an ELS unsolicited event. A request to RRQ shall only
be accepted if the Originator Nx_Port N_Port_ID or the Responder
Nx_Port N_Port_ID of the target Exchange is the same as the
N_Port_ID of the Nx_Port that makes the request. If the RRQ is
not accepted, an LS_RJT with reason code "Unable to perform
command request" and reason code explanation "Invalid Originator
S_ID" shall be returned. For now, we just unconditionally accept
RRQ from the target.

.. _`lpfc_els_rsp_rls_acc`:

lpfc_els_rsp_rls_acc
====================

.. c:function:: void lpfc_els_rsp_rls_acc(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Completion callbk func for MBX_READ_LNK_STAT mbox cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_els_rsp_rls_acc.description`:

Description
-----------

This routine is the completion callback function for the MBX_READ_LNK_STAT
mailbox command. This callback function is to actually send the Accept
(ACC) response to a Read Port Status (RPS) unsolicited IOCB event. It
collects the link statistics from the completion of the MBX_READ_LNK_STAT
mailbox command, constructs the RPS response with the link statistics
collected, and then invokes the \ :c:func:`lpfc_sli_issue_iocb`\  routine to send ACC
response to the RPS.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the RPS Accept Response ELS IOCB command.

.. _`lpfc_els_rsp_rps_acc`:

lpfc_els_rsp_rps_acc
====================

.. c:function:: void lpfc_els_rsp_rps_acc(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Completion callbk func for MBX_READ_LNK_STAT mbox cmd

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_els_rsp_rps_acc.description`:

Description
-----------

This routine is the completion callback function for the MBX_READ_LNK_STAT
mailbox command. This callback function is to actually send the Accept
(ACC) response to a Read Port Status (RPS) unsolicited IOCB event. It
collects the link statistics from the completion of the MBX_READ_LNK_STAT
mailbox command, constructs the RPS response with the link statistics
collected, and then invokes the \ :c:func:`lpfc_sli_issue_iocb`\  routine to send ACC
response to the RPS.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the RPS Accept Response ELS IOCB command.

.. _`lpfc_els_rcv_rls`:

lpfc_els_rcv_rls
================

.. c:function:: int lpfc_els_rcv_rls(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited rls iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_rls.description`:

Description
-----------

This routine processes Read Port Status (RPL) IOCB received as an
ELS unsolicited event. It first checks the remote port state. If the
remote port is not in NLP_STE_UNMAPPED_NODE state or NLP_STE_MAPPED_NODE
state, it invokes the \ :c:func:`lpfc_els_rsl_reject`\  routine to send the reject
response. Otherwise, it issue the MBX_READ_LNK_STAT mailbox command
for reading the HBA link statistics. It is for the callback function,
\ :c:func:`lpfc_els_rsp_rls_acc`\ , set to the MBX_READ_LNK_STAT mailbox command
to actually sending out RPL Accept (ACC) response.

Return codes
0 - Successfully processed rls iocb (currently always return 0)

.. _`lpfc_els_rcv_rtv`:

lpfc_els_rcv_rtv
================

.. c:function:: int lpfc_els_rcv_rtv(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited rtv iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_rtv.description`:

Description
-----------

This routine processes Read Timout Value (RTV) IOCB received as an
ELS unsolicited event. It first checks the remote port state. If the
remote port is not in NLP_STE_UNMAPPED_NODE state or NLP_STE_MAPPED_NODE
state, it invokes the \ :c:func:`lpfc_els_rsl_reject`\  routine to send the reject
response. Otherwise, it sends the Accept(ACC) response to a Read Timeout
Value (RTV) unsolicited IOCB event.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the RPS Accept Response ELS IOCB command.

Return codes
0 - Successfully processed rtv iocb (currently always return 0)

.. _`lpfc_send_rrq`:

lpfc_send_rrq
=============

.. c:function:: int lpfc_send_rrq(struct lpfc_hba *phba, struct lpfc_node_rrq *rrq)

    Sends ELS RRQ if needed.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_node_rrq \*rrq:
        pointer to the active rrq.

.. _`lpfc_send_rrq.description`:

Description
-----------

This routine will call the lpfc_issue_els_rrq if the rrq is
still active for the xri. If this function returns a failure then
the caller needs to clean up the RRQ by calling lpfc_clr_active_rrq.

Returns 0 Success.
1 Failure.

.. _`lpfc_els_rsp_rpl_acc`:

lpfc_els_rsp_rpl_acc
====================

.. c:function:: int lpfc_els_rsp_rpl_acc(struct lpfc_vport *vport, uint16_t cmdsize, struct lpfc_iocbq *oldiocb, struct lpfc_nodelist *ndlp)

    Issue an accept rpl els command

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param uint16_t cmdsize:
        size of the ELS command.

    :param struct lpfc_iocbq \*oldiocb:
        pointer to the original lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rsp_rpl_acc.description`:

Description
-----------

This routine issuees an Accept (ACC) Read Port List (RPL) ELS command.
It is to be called by the \ :c:func:`lpfc_els_rcv_rpl`\  routine to accept the RPL.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the RPL Accept Response ELS command.

Return code
0 - Successfully issued ACC RPL ELS command
1 - Failed to issue ACC RPL ELS command

.. _`lpfc_els_rcv_rpl`:

lpfc_els_rcv_rpl
================

.. c:function:: int lpfc_els_rcv_rpl(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited rpl iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_rpl.description`:

Description
-----------

This routine processes Read Port List (RPL) IOCB received as an ELS
unsolicited event. It first checks the remote port state. If the remote
port is not in NLP_STE_UNMAPPED_NODE and NLP_STE_MAPPED_NODE states, it
invokes the \ :c:func:`lpfc_els_rsp_reject`\  routine to send reject response.
Otherwise, this routine then invokes the \ :c:func:`lpfc_els_rsp_rpl_acc`\  routine
to accept the RPL.

Return code
0 - Successfully processed rpl iocb (currently always return 0)

.. _`lpfc_els_rcv_farp`:

lpfc_els_rcv_farp
=================

.. c:function:: int lpfc_els_rcv_farp(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited farp request els command

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_farp.description`:

Description
-----------

This routine processes Fibre Channel Address Resolution Protocol
(FARP) Request IOCB received as an ELS unsolicited event. Currently,
the lpfc driver only supports matching on WWPN or WWNN for FARP. As such,
FARP_MATCH_PORT flag and FARP_MATCH_NODE flag are checked against the

.. _`lpfc_els_rcv_farp.match-flag-in-the-farp-request-iocb`:

Match Flag in the FARP request IOCB
-----------------------------------

if FARP_MATCH_PORT flag is set, the
remote PortName is compared against the FC PortName stored in the \ ``vport``\ 
data structure; if FARP_MATCH_NODE flag is set, the remote NodeName is
compared against the FC NodeName stored in the \ ``vport``\  data structure.
If any of these matches and the FARP_REQUEST_FARPR flag is set in the
FARP request IOCB Response Flag, the \ :c:func:`lpfc_issue_els_farpr`\  routine is
invoked to send out FARP Response to the remote node. Before sending the
FARP Response, however, the FARP_REQUEST_PLOGI flag is check in the FARP
request IOCB Response Flag and, if it is set, the \ :c:func:`lpfc_issue_els_plogi`\ 
routine is invoked to log into the remote port first.

Return code
0 - Either the FARP Match Mode not supported or successfully processed

.. _`lpfc_els_rcv_farpr`:

lpfc_els_rcv_farpr
==================

.. c:function:: int lpfc_els_rcv_farpr(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *ndlp)

    Process an unsolicited farp response iocb

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_farpr.description`:

Description
-----------

This routine processes Fibre Channel Address Resolution Protocol
Response (FARPR) IOCB received as an ELS unsolicited event. It simply
invokes the \ :c:func:`lpfc_els_rsp_acc`\  routine to the remote node to accept
the FARP response request.

Return code
0 - Successfully processed FARPR IOCB (currently always return 0)

.. _`lpfc_els_rcv_fan`:

lpfc_els_rcv_fan
================

.. c:function:: int lpfc_els_rcv_fan(struct lpfc_vport *vport, struct lpfc_iocbq *cmdiocb, struct lpfc_nodelist *fan_ndlp)

    Process an unsolicited fan iocb command

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_nodelist \*fan_ndlp:
        pointer to a node-list data structure.

.. _`lpfc_els_rcv_fan.description`:

Description
-----------

This routine processes a Fabric Address Notification (FAN) IOCB
command received as an ELS unsolicited event. The FAN ELS command will
only be processed on a physical port (i.e., the \ ``vport``\  represents the
physical port). The fabric NodeName and PortName from the FAN IOCB are
compared against those in the phba data structure. If any of those is
different, the \ :c:func:`lpfc_initial_flogi`\  routine is invoked to initialize
Fabric Login (FLOGI) to the fabric to start the discover over. Otherwise,
if both of those are identical, the \ :c:func:`lpfc_issue_fabric_reglogin`\  routine
is invoked to register login to the fabric.

Return code
0 - Successfully processed fan iocb (currently always return 0).

.. _`lpfc_els_timeout`:

lpfc_els_timeout
================

.. c:function:: void lpfc_els_timeout(unsigned long ptr)

    Handler funciton to the els timer

    :param unsigned long ptr:
        holder for the timer function associated data.

.. _`lpfc_els_timeout.description`:

Description
-----------

This routine is invoked by the ELS timer after timeout. It posts the ELS
timer timeout event by setting the WORKER_ELS_TMO bit to the work port
event bitmap and then invokes the \ :c:func:`lpfc_worker_wake_up`\  routine to wake
up the worker thread. It is for the worker thread to invoke the routine
\ :c:func:`lpfc_els_timeout_handler`\  to work on the posted event WORKER_ELS_TMO.

.. _`lpfc_els_timeout_handler`:

lpfc_els_timeout_handler
========================

.. c:function:: void lpfc_els_timeout_handler(struct lpfc_vport *vport)

    Process an els timeout event

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

.. _`lpfc_els_timeout_handler.description`:

Description
-----------

This routine is the actual handler function that processes an ELS timeout
event. It walks the ELS ring to get and abort all the IOCBs (except the
ABORT/CLOSE/FARP/FARPR/FDISC), which are associated with the \ ``vport``\  by
invoking the \ :c:func:`lpfc_sli_issue_abort_iotag`\  routine.

.. _`lpfc_els_flush_cmd`:

lpfc_els_flush_cmd
==================

.. c:function:: void lpfc_els_flush_cmd(struct lpfc_vport *vport)

    Clean up the outstanding els commands to a vport

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

.. _`lpfc_els_flush_cmd.description`:

Description
-----------

This routine is used to clean up all the outstanding ELS commands on a
\ ``vport``\ . It first aborts the \ ``vport``\  by invoking \ :c:func:`lpfc_fabric_abort_vport`\ 
routine. After that, it walks the ELS transmit queue to remove all the
IOCBs with the \ ``vport``\  other than the QUE_RING and ABORT/CLOSE IOCBs. For
the IOCBs with a non-NULL completion callback function, the callback
function will be invoked with the status set to IOSTAT_LOCAL_REJECT and
un.ulpWord[4] set to IOERR_SLI_ABORTED. For IOCBs with a NULL completion
callback function, the IOCB will simply be released. Finally, it walks
the ELS transmit completion queue to issue an abort IOCB to any transmit
completion queue IOCB that is associated with the \ ``vport``\  and is not
an IOCB from libdfc (i.e., the management plane IOCBs that are not
part of the discovery state machine) out to HBA by invoking the
\ :c:func:`lpfc_sli_issue_abort_iotag`\  routine. Note that this function issues the
abort IOCB to any transmit completion queueed IOCB, it does not guarantee
the IOCBs are aborted when this function returns.

.. _`lpfc_els_flush_all_cmd`:

lpfc_els_flush_all_cmd
======================

.. c:function:: void lpfc_els_flush_all_cmd(struct lpfc_hba *phba)

    Clean up all the outstanding els commands to a HBA

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_els_flush_all_cmd.description`:

Description
-----------

This routine is used to clean up all the outstanding ELS commands on a
\ ``phba``\ . It first aborts the \ ``phba``\  by invoking the \ :c:func:`lpfc_fabric_abort_hba`\ 
routine. After that, it walks the ELS transmit queue to remove all the
IOCBs to the \ ``phba``\  other than the QUE_RING and ABORT/CLOSE IOCBs. For
the IOCBs with the completion callback function associated, the callback
function will be invoked with the status set to IOSTAT_LOCAL_REJECT and
un.ulpWord[4] set to IOERR_SLI_ABORTED. For IOCBs without the completion
callback function associated, the IOCB will simply be released. Finally,
it walks the ELS transmit completion queue to issue an abort IOCB to any
transmit completion queue IOCB that is not an IOCB from libdfc (i.e., the
management plane IOCBs that are not part of the discovery state machine)
out to HBA by invoking the \ :c:func:`lpfc_sli_issue_abort_iotag`\  routine.

.. _`lpfc_send_els_failure_event`:

lpfc_send_els_failure_event
===========================

.. c:function:: void lpfc_send_els_failure_event(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocbp, struct lpfc_iocbq *rspiocbp)

    Posts an ELS command failure event

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param struct lpfc_iocbq \*cmdiocbp:
        Pointer to command iocb which reported error.

    :param struct lpfc_iocbq \*rspiocbp:
        Pointer to response iocb which reported error.

.. _`lpfc_send_els_failure_event.description`:

Description
-----------

This function sends an event when there is an ELS command
failure.

.. _`lpfc_send_els_event`:

lpfc_send_els_event
===================

.. c:function:: void lpfc_send_els_event(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint32_t *payload)

    Posts unsolicited els event

    :param struct lpfc_vport \*vport:
        Pointer to vport object.

    :param struct lpfc_nodelist \*ndlp:
        Pointer FC node object.

    :param uint32_t \*payload:
        *undescribed*

.. _`lpfc_send_els_event.description`:

Description
-----------

This function posts an event when there is an incoming
unsolicited ELS command.

.. _`lpfc_els_unsol_buffer`:

lpfc_els_unsol_buffer
=====================

.. c:function:: void lpfc_els_unsol_buffer(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_vport *vport, struct lpfc_iocbq *elsiocb)

    Process an unsolicited event data buffer

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_sli_ring \*pring:
        pointer to a SLI ring.

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_iocbq \*elsiocb:
        pointer to lpfc els command iocb data structure.

.. _`lpfc_els_unsol_buffer.description`:

Description
-----------

This routine is used for processing the IOCB associated with a unsolicited
event. It first determines whether there is an existing ndlp that matches
the DID from the unsolicited IOCB. If not, it will create a new one with
the DID from the unsolicited IOCB. The ELS command from the unsolicited
IOCB is then used to invoke the proper routine and to set up proper state
of the discovery state machine.

.. _`lpfc_els_unsol_event`:

lpfc_els_unsol_event
====================

.. c:function:: void lpfc_els_unsol_event(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, struct lpfc_iocbq *elsiocb)

    Process an unsolicited event from an els sli ring

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_sli_ring \*pring:
        pointer to a SLI ring.

    :param struct lpfc_iocbq \*elsiocb:
        pointer to lpfc els iocb data structure.

.. _`lpfc_els_unsol_event.description`:

Description
-----------

This routine is used to process an unsolicited event received from a SLI
(Service Level Interface) ring. The actual processing of the data buffer
associated with the unsolicited event is done by invoking the routine
\ :c:func:`lpfc_els_unsol_buffer`\  after properly set up the iocb buffer from the
SLI ring on which the unsolicited event was received.

.. _`lpfc_do_scr_ns_plogi`:

lpfc_do_scr_ns_plogi
====================

.. c:function:: void lpfc_do_scr_ns_plogi(struct lpfc_hba *phba, struct lpfc_vport *vport)

    Issue a plogi to the name server for scr

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

.. _`lpfc_do_scr_ns_plogi.description`:

Description
-----------

This routine issues a Port Login (PLOGI) to the Name Server with
State Change Request (SCR) for a \ ``vport``\ . This routine will create an
ndlp for the Name Server associated to the \ ``vport``\  if such node does
not already exist. The PLOGI to Name Server is issued by invoking the
\ :c:func:`lpfc_issue_els_plogi`\  routine. If Fabric-Device Management Interface
(FDMI) is configured to the \ ``vport``\ , a FDMI node will be created and
the PLOGI to FDMI is issued by invoking \ :c:func:`lpfc_issue_els_plogi`\  routine.

.. _`lpfc_cmpl_reg_new_vport`:

lpfc_cmpl_reg_new_vport
=======================

.. c:function:: void lpfc_cmpl_reg_new_vport(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Completion callback function to register new vport

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*pmb:
        pointer to the driver internal queue element for mailbox command.

.. _`lpfc_cmpl_reg_new_vport.description`:

Description
-----------

This routine is the completion callback function to register new vport
mailbox command. If the new vport mailbox command completes successfully,
the fabric registration login shall be performed on physical port (the
new vport created is actually a physical port, with VPI 0) or the port
login to Name Server for State Change Request (SCR) will be performed
on virtual port (real virtual port, with VPI greater than 0).

.. _`lpfc_register_new_vport`:

lpfc_register_new_vport
=======================

.. c:function:: void lpfc_register_new_vport(struct lpfc_hba *phba, struct lpfc_vport *vport, struct lpfc_nodelist *ndlp)

    Register a new vport with a HBA

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_vport \*vport:
        pointer to a host virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_register_new_vport.description`:

Description
-----------

This routine registers the \ ``vport``\  as a new virtual port with a HBA.
It is done through a registering vpi mailbox command.

.. _`lpfc_cancel_all_vport_retry_delay_timer`:

lpfc_cancel_all_vport_retry_delay_timer
=======================================

.. c:function:: void lpfc_cancel_all_vport_retry_delay_timer(struct lpfc_hba *phba)

    Cancel all vport retry delay timer

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_cancel_all_vport_retry_delay_timer.description`:

Description
-----------

This routine cancels the retry delay timers to all the vports.

.. _`lpfc_retry_pport_discovery`:

lpfc_retry_pport_discovery
==========================

.. c:function:: void lpfc_retry_pport_discovery(struct lpfc_hba *phba)

    Start timer to retry FLOGI.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_retry_pport_discovery.description`:

Description
-----------

This routine abort all pending discovery commands and
start a timer to retry FLOGI for the physical port
discovery.

.. _`lpfc_fabric_login_reqd`:

lpfc_fabric_login_reqd
======================

.. c:function:: int lpfc_fabric_login_reqd(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Check if FLOGI required.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to FDISC command iocb.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to FDISC response iocb.

.. _`lpfc_fabric_login_reqd.description`:

Description
-----------

This routine checks if a FLOGI is reguired for FDISC
to succeed.

.. _`lpfc_cmpl_els_fdisc`:

lpfc_cmpl_els_fdisc
===================

.. c:function:: void lpfc_cmpl_els_fdisc(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion function for fdisc iocb command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_fdisc.description`:

Description
-----------

This routine is the completion callback function to a Fabric Discover
(FDISC) ELS command. Since all the FDISC ELS commands are issued
single threaded, each FDISC completion callback function will reset
the discovery timer for all vports such that the timers will not get
unnecessary timeout. The function checks the FDISC IOCB status. If error
detected, the vport will be set to FC_VPORT_FAILED state. Otherwise,the
vport will set to FC_VPORT_ACTIVE state. It then checks whether the DID
assigned to the vport has been changed with the completion of the FDISC
command. If so, both RPI (Remote Port Index) and VPI (Virtual Port Index)
are unregistered from the HBA, and then the \ :c:func:`lpfc_register_new_vport`\ 
routine is invoked to register new vport with the HBA. Otherwise, the
\ :c:func:`lpfc_do_scr_ns_plogi`\  routine is invoked to issue a PLOGI to the Name
Server for State Change Request (SCR).

.. _`lpfc_issue_els_fdisc`:

lpfc_issue_els_fdisc
====================

.. c:function:: int lpfc_issue_els_fdisc(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint8_t retry)

    Issue a fdisc iocb command

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

    :param uint8_t retry:
        number of retries to the command IOCB.

.. _`lpfc_issue_els_fdisc.description`:

Description
-----------

This routine prepares and issues a Fabric Discover (FDISC) IOCB to
a remote node (@ndlp) off a \ ``vport``\ . It uses the \ :c:func:`lpfc_issue_fabric_iocb`\ 
routine to issue the IOCB, which makes sure only one outstanding fabric
IOCB will be sent off HBA at any given time.

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the FDISC ELS command.

Return code
0 - Successfully issued fdisc iocb command
1 - Failed to issue fdisc iocb command

.. _`lpfc_cmpl_els_npiv_logo`:

lpfc_cmpl_els_npiv_logo
=======================

.. c:function:: void lpfc_cmpl_els_npiv_logo(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion function with vport logo

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_els_npiv_logo.description`:

Description
-----------

This routine is the completion callback function to the issuing of a LOGO
ELS command off a vport. It frees the command IOCB and then decrement the
reference count held on ndlp for this completion function, indicating that
the reference to the ndlp is no long needed. Note that the
\ :c:func:`lpfc_els_free_iocb`\  routine decrements the ndlp reference held for this
callback function and an additional explicit ndlp reference decrementation
will trigger the actual release of the ndlp.

.. _`lpfc_issue_els_npiv_logo`:

lpfc_issue_els_npiv_logo
========================

.. c:function:: int lpfc_issue_els_npiv_logo(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp)

    Issue a logo off a vport

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_issue_els_npiv_logo.description`:

Description
-----------

This routine issues a LOGO ELS command to an \ ``ndlp``\  off a \ ``vport``\ .

Note that, in \ :c:func:`lpfc_prep_els_iocb`\  routine, the reference count of ndlp
will be incremented by 1 for holding the ndlp and the reference to ndlp
will be stored into the context1 field of the IOCB for the completion
callback function to the LOGO ELS command.

Return codes
0 - Successfully issued logo off the \ ``vport``\ 
1 - Failed to issue logo off the \ ``vport``\ 

.. _`lpfc_fabric_block_timeout`:

lpfc_fabric_block_timeout
=========================

.. c:function:: void lpfc_fabric_block_timeout(unsigned long ptr)

    Handler function to the fabric block timer

    :param unsigned long ptr:
        holder for the timer function associated data.

.. _`lpfc_fabric_block_timeout.description`:

Description
-----------

This routine is invoked by the fabric iocb block timer after
timeout. It posts the fabric iocb block timeout event by setting the
WORKER_FABRIC_BLOCK_TMO bit to work port event bitmap and then invokes
\ :c:func:`lpfc_worker_wake_up`\  routine to wake up the worker thread. It is for
the worker thread to invoke the \ :c:func:`lpfc_unblock_fabric_iocbs`\  on the
posted event WORKER_FABRIC_BLOCK_TMO.

.. _`lpfc_resume_fabric_iocbs`:

lpfc_resume_fabric_iocbs
========================

.. c:function:: void lpfc_resume_fabric_iocbs(struct lpfc_hba *phba)

    Issue a fabric iocb from driver internal list

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_resume_fabric_iocbs.description`:

Description
-----------

This routine issues one fabric iocb from the driver internal list to
the HBA. It first checks whether it's ready to issue one fabric iocb to
the HBA (whether there is no outstanding fabric iocb). If so, it shall
remove one pending fabric iocb from the driver internal list and invokes
\ :c:func:`lpfc_sli_issue_iocb`\  routine to send the fabric iocb to the HBA.

.. _`lpfc_unblock_fabric_iocbs`:

lpfc_unblock_fabric_iocbs
=========================

.. c:function:: void lpfc_unblock_fabric_iocbs(struct lpfc_hba *phba)

    Unblock issuing fabric iocb command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_unblock_fabric_iocbs.description`:

Description
-----------

This routine unblocks the  issuing fabric iocb command. The function
will clear the fabric iocb block bit and then invoke the routine
\ :c:func:`lpfc_resume_fabric_iocbs`\  to issue one of the pending fabric iocb
from the driver internal fabric iocb list.

.. _`lpfc_block_fabric_iocbs`:

lpfc_block_fabric_iocbs
=======================

.. c:function:: void lpfc_block_fabric_iocbs(struct lpfc_hba *phba)

    Block issuing fabric iocb command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_block_fabric_iocbs.description`:

Description
-----------

This routine blocks the issuing fabric iocb for a specified amount of
time (currently 100 ms). This is done by set the fabric iocb block bit
and set up a timeout timer for 100ms. When the block bit is set, no more
fabric iocb will be issued out of the HBA.

.. _`lpfc_cmpl_fabric_iocb`:

lpfc_cmpl_fabric_iocb
=====================

.. c:function:: void lpfc_cmpl_fabric_iocb(struct lpfc_hba *phba, struct lpfc_iocbq *cmdiocb, struct lpfc_iocbq *rspiocb)

    Completion callback function for fabric iocb

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*cmdiocb:
        pointer to lpfc command iocb data structure.

    :param struct lpfc_iocbq \*rspiocb:
        pointer to lpfc response iocb data structure.

.. _`lpfc_cmpl_fabric_iocb.description`:

Description
-----------

This routine is the callback function that is put to the fabric iocb's
callback function pointer (iocb->iocb_cmpl). The original iocb's callback
function pointer has been stored in iocb->fabric_iocb_cmpl. This callback
function first restores and invokes the original iocb's callback function
and then invokes the \ :c:func:`lpfc_resume_fabric_iocbs`\  routine to issue the next
fabric bound iocb from the driver internal fabric iocb list onto the wire.

.. _`lpfc_issue_fabric_iocb`:

lpfc_issue_fabric_iocb
======================

.. c:function:: int lpfc_issue_fabric_iocb(struct lpfc_hba *phba, struct lpfc_iocbq *iocb)

    Issue a fabric iocb command

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_iocbq \*iocb:
        pointer to lpfc command iocb data structure.

.. _`lpfc_issue_fabric_iocb.description`:

Description
-----------

This routine is used as the top-level API for issuing a fabric iocb command
such as FLOGI and FDISC. To accommodate certain switch fabric, this driver
function makes sure that only one fabric bound iocb will be outstanding at
any given time. As such, this function will first check to see whether there
is already an outstanding fabric iocb on the wire. If so, it will put the
newly issued iocb onto the driver internal fabric iocb list, waiting to be
issued later. Otherwise, it will issue the iocb on the wire and update the
fabric iocb count it indicate that there is one fabric iocb on the wire.

Note, this implementation has a potential sending out fabric IOCBs out of
order. The problem is caused by the construction of the "ready" boolen does
not include the condition that the internal fabric IOCB list is empty. As
such, it is possible a fabric IOCB issued by this routine might be "jump"
ahead of the fabric IOCBs in the internal list.

Return code
IOCB_SUCCESS - either fabric iocb put on the list or issued successfully
IOCB_ERROR - failed to issue fabric iocb

.. _`lpfc_fabric_abort_vport`:

lpfc_fabric_abort_vport
=======================

.. c:function:: void lpfc_fabric_abort_vport(struct lpfc_vport *vport)

    Abort a vport's iocbs from driver fabric iocb list

    :param struct lpfc_vport \*vport:
        pointer to a virtual N_Port data structure.

.. _`lpfc_fabric_abort_vport.description`:

Description
-----------

This routine aborts all the IOCBs associated with a \ ``vport``\  from the
driver internal fabric IOCB list. The list contains fabric IOCBs to be
issued to the ELS IOCB ring. This abort function walks the fabric IOCB
list, removes each IOCB associated with the \ ``vport``\  off the list, set the
status feild to IOSTAT_LOCAL_REJECT, and invokes the callback function
associated with the IOCB.

.. _`lpfc_fabric_abort_nport`:

lpfc_fabric_abort_nport
=======================

.. c:function:: void lpfc_fabric_abort_nport(struct lpfc_nodelist *ndlp)

    Abort a ndlp's iocbs from driver fabric iocb list

    :param struct lpfc_nodelist \*ndlp:
        pointer to a node-list data structure.

.. _`lpfc_fabric_abort_nport.description`:

Description
-----------

This routine aborts all the IOCBs associated with an \ ``ndlp``\  from the
driver internal fabric IOCB list. The list contains fabric IOCBs to be
issued to the ELS IOCB ring. This abort function walks the fabric IOCB
list, removes each IOCB associated with the \ ``ndlp``\  off the list, set the
status feild to IOSTAT_LOCAL_REJECT, and invokes the callback function
associated with the IOCB.

.. _`lpfc_fabric_abort_hba`:

lpfc_fabric_abort_hba
=====================

.. c:function:: void lpfc_fabric_abort_hba(struct lpfc_hba *phba)

    Abort all iocbs on driver fabric iocb list

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_fabric_abort_hba.description`:

Description
-----------

This routine aborts all the IOCBs currently on the driver internal
fabric IOCB list. The list contains fabric IOCBs to be issued to the ELS
IOCB ring. This function takes the entire IOCB list off the fabric IOCB
list, removes IOCBs off the list, set the status feild to
IOSTAT_LOCAL_REJECT, and invokes the callback function associated with
the IOCB.

.. _`lpfc_sli4_vport_delete_els_xri_aborted`:

lpfc_sli4_vport_delete_els_xri_aborted
======================================

.. c:function:: void lpfc_sli4_vport_delete_els_xri_aborted(struct lpfc_vport *vport)

    Remove all ndlp references for vport

    :param struct lpfc_vport \*vport:
        pointer to lpfc vport data structure.

.. _`lpfc_sli4_vport_delete_els_xri_aborted.description`:

Description
-----------

This routine is invoked by the vport cleanup for deletions and the cleanup
for an ndlp on removal.

.. _`lpfc_sli4_els_xri_aborted`:

lpfc_sli4_els_xri_aborted
=========================

.. c:function:: void lpfc_sli4_els_xri_aborted(struct lpfc_hba *phba, struct sli4_wcqe_xri_aborted *axri)

    Slow-path process of els xri abort

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct sli4_wcqe_xri_aborted \*axri:
        pointer to the els xri abort wcqe structure.

.. _`lpfc_sli4_els_xri_aborted.description`:

Description
-----------

This routine is invoked by the worker thread to process a SLI4 slow-path
ELS aborted xri.

.. This file was automatic generated / don't edit.


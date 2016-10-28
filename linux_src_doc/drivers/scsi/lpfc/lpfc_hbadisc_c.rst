.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_hbadisc.c

.. _`lpfc_dev_loss_tmo_handler`:

lpfc_dev_loss_tmo_handler
=========================

.. c:function:: int lpfc_dev_loss_tmo_handler(struct lpfc_nodelist *ndlp)

    Remote node devloss timeout handler

    :param struct lpfc_nodelist \*ndlp:
        Pointer to remote node object.

.. _`lpfc_dev_loss_tmo_handler.description`:

Description
-----------

This function is called from the worker thread when devloss timeout timer
expires. For SLI4 host, this routine shall return 1 when at lease one
remote node, including this \ ``ndlp``\ , is still in use of FCF; otherwise, this
routine shall return 0 when there is no remote node is still in use of FCF
when devloss timeout happened to this \ ``ndlp``\ .

.. _`lpfc_sli4_post_dev_loss_tmo_handler`:

lpfc_sli4_post_dev_loss_tmo_handler
===================================

.. c:function:: void lpfc_sli4_post_dev_loss_tmo_handler(struct lpfc_hba *phba, int fcf_inuse, uint32_t nlp_did)

    SLI4 post devloss timeout handler

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param int fcf_inuse:
        SLI4 FCF in-use state reported from devloss timeout handler.

    :param uint32_t nlp_did:
        remote node identifer with devloss timeout.

.. _`lpfc_sli4_post_dev_loss_tmo_handler.description`:

Description
-----------

This function is called from the worker thread after invoking devloss
timeout handler and releasing the reference count for the ndlp with
which the devloss timeout was handled for SLI4 host. For the devloss
timeout of the last remote node which had been in use of FCF, when this
routine is invoked, it shall be guaranteed that none of the remote are
in-use of FCF. When devloss timeout to the last remote using the FCF,
if the FIP engine is neither in FCF table scan process nor roundrobin
failover process, the in-use FCF shall be unregistered. If the FIP
engine is in FCF discovery process, the devloss timeout state shall
be set for either the FCF table scan process or roundrobin failover
process to unregister the in-use FCF.

.. _`lpfc_alloc_fast_evt`:

lpfc_alloc_fast_evt
===================

.. c:function:: struct lpfc_fast_path_event *lpfc_alloc_fast_evt(struct lpfc_hba *phba)

    Allocates data structure for posting event

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_alloc_fast_evt.description`:

Description
-----------

This function is called from the functions which need to post
events from interrupt context. This function allocates data
structure required for posting event. It also keeps track of
number of events pending and prevent event storm when there are
too many events.

.. _`lpfc_free_fast_evt`:

lpfc_free_fast_evt
==================

.. c:function:: void lpfc_free_fast_evt(struct lpfc_hba *phba, struct lpfc_fast_path_event *evt)

    Frees event data structure

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param struct lpfc_fast_path_event \*evt:
        Event object which need to be freed.

.. _`lpfc_free_fast_evt.description`:

Description
-----------

This function frees the data structure required for posting
events.

.. _`lpfc_send_fastpath_evt`:

lpfc_send_fastpath_evt
======================

.. c:function:: void lpfc_send_fastpath_evt(struct lpfc_hba *phba, struct lpfc_work_evt *evtp)

    Posts events generated from fast path

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param struct lpfc_work_evt \*evtp:
        Event data structure.

.. _`lpfc_send_fastpath_evt.description`:

Description
-----------

This function is called from worker thread, when the interrupt
context need to post an event. This function posts the event
to fc transport netlink interface.

.. _`lpfc_sli4_clear_fcf_rr_bmask`:

lpfc_sli4_clear_fcf_rr_bmask
============================

.. c:function:: void lpfc_sli4_clear_fcf_rr_bmask(struct lpfc_hba *phba)

    \ ``phba``\  pointer to the struct lpfc_hba for this port. This fucnction resets the round robin bit mask and clears the fcf priority list. The list deletions are done while holding the hbalock. The ON_LIST flag and the FLOGI_FAILED flags are cleared from the lpfc_fcf_pri record.

    :param struct lpfc_hba \*phba:
        *undescribed*

.. _`lpfc_fab_name_match`:

lpfc_fab_name_match
===================

.. c:function:: uint32_t lpfc_fab_name_match(uint8_t *fab_name, struct fcf_record *new_fcf_record)

    Check if the fcf fabric name match.

    :param uint8_t \*fab_name:
        pointer to fabric name.

    :param struct fcf_record \*new_fcf_record:
        pointer to fcf record.

.. _`lpfc_fab_name_match.description`:

Description
-----------

This routine compare the fcf record's fabric name with provided
fabric name. If the fabric name are identical this function
returns 1 else return 0.

.. _`lpfc_sw_name_match`:

lpfc_sw_name_match
==================

.. c:function:: uint32_t lpfc_sw_name_match(uint8_t *sw_name, struct fcf_record *new_fcf_record)

    Check if the fcf switch name match.

    :param uint8_t \*sw_name:
        *undescribed*

    :param struct fcf_record \*new_fcf_record:
        pointer to fcf record.

.. _`lpfc_sw_name_match.description`:

Description
-----------

This routine compare the fcf record's switch name with provided
switch name. If the switch name are identical this function
returns 1 else return 0.

.. _`lpfc_mac_addr_match`:

lpfc_mac_addr_match
===================

.. c:function:: uint32_t lpfc_mac_addr_match(uint8_t *mac_addr, struct fcf_record *new_fcf_record)

    Check if the fcf mac address match.

    :param uint8_t \*mac_addr:
        pointer to mac address.

    :param struct fcf_record \*new_fcf_record:
        pointer to fcf record.

.. _`lpfc_mac_addr_match.description`:

Description
-----------

This routine compare the fcf record's mac address with HBA's
FCF mac address. If the mac addresses are identical this function
returns 1 else return 0.

.. _`__lpfc_update_fcf_record_pri`:

__lpfc_update_fcf_record_pri
============================

.. c:function:: void __lpfc_update_fcf_record_pri(struct lpfc_hba *phba, uint16_t fcf_index, struct fcf_record *new_fcf_record)

    Update driver fcf record \__lpfc_update_fcf_record_pri - update the lpfc_fcf_pri record.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t fcf_index:
        Index for the lpfc_fcf_record.

    :param struct fcf_record \*new_fcf_record:
        pointer to hba fcf record.

.. _`__lpfc_update_fcf_record_pri.description`:

Description
-----------

This routine updates the driver FCF priority record from the new HBA FCF
record. This routine is called with the host lock held.

.. _`lpfc_copy_fcf_record`:

lpfc_copy_fcf_record
====================

.. c:function:: void lpfc_copy_fcf_record(struct lpfc_fcf_rec *fcf_rec, struct fcf_record *new_fcf_record)

    Copy fcf information to lpfc_hba.

    :param struct lpfc_fcf_rec \*fcf_rec:
        *undescribed*

    :param struct fcf_record \*new_fcf_record:
        pointer to fcf record.

.. _`lpfc_copy_fcf_record.description`:

Description
-----------

This routine copies the FCF information from the FCF
record to lpfc_hba data structure.

.. _`__lpfc_update_fcf_record`:

__lpfc_update_fcf_record
========================

.. c:function:: void __lpfc_update_fcf_record(struct lpfc_hba *phba, struct lpfc_fcf_rec *fcf_rec, struct fcf_record *new_fcf_record, uint32_t addr_mode, uint16_t vlan_id, uint32_t flag)

    Update driver fcf record

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct lpfc_fcf_rec \*fcf_rec:
        pointer to driver fcf record.

    :param struct fcf_record \*new_fcf_record:
        pointer to hba fcf record.

    :param uint32_t addr_mode:
        address mode to be set to the driver fcf record.

    :param uint16_t vlan_id:
        vlan tag to be set to the driver fcf record.

    :param uint32_t flag:
        flag bits to be set to the driver fcf record.

.. _`__lpfc_update_fcf_record.description`:

Description
-----------

This routine updates the driver FCF record from the new HBA FCF record
together with the address mode, vlan_id, and other informations. This
routine is called with the host lock held.

.. _`lpfc_register_fcf`:

lpfc_register_fcf
=================

.. c:function:: void lpfc_register_fcf(struct lpfc_hba *phba)

    Register the FCF with hba.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_register_fcf.description`:

Description
-----------

This routine issues a register fcfi mailbox command to register
the fcf with HBA.

.. _`lpfc_match_fcf_conn_list`:

lpfc_match_fcf_conn_list
========================

.. c:function:: int lpfc_match_fcf_conn_list(struct lpfc_hba *phba, struct fcf_record *new_fcf_record, uint32_t *boot_flag, uint32_t *addr_mode, uint16_t *vlan_id)

    Check if the FCF record can be used for discovery.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct fcf_record \*new_fcf_record:
        pointer to fcf record.

    :param uint32_t \*boot_flag:
        Indicates if this record used by boot bios.

    :param uint32_t \*addr_mode:
        The address mode to be used by this FCF

    :param uint16_t \*vlan_id:
        The vlan id to be used as vlan tagging by this FCF.

.. _`lpfc_match_fcf_conn_list.description`:

Description
-----------

This routine compare the fcf record with connect list obtained from the
config region to decide if this FCF can be used for SAN discovery. It returns
1 if this record can be used for SAN discovery else return zero. If this FCF
record can be used for SAN discovery, the boot_flag will indicate if this FCF
is used by boot bios and addr_mode will indicate the addressing mode to be
used for this FCF when the function returns.
If the FCF record need to be used with a particular vlan id, the vlan is
set in the vlan_id on return of the function. If not VLAN tagging need to
be used with the FCF vlan_id will be set to LPFC_FCOE_NULL_VID;

.. _`lpfc_check_pending_fcoe_event`:

lpfc_check_pending_fcoe_event
=============================

.. c:function:: int lpfc_check_pending_fcoe_event(struct lpfc_hba *phba, uint8_t unreg_fcf)

    Check if there is pending fcoe event.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint8_t unreg_fcf:
        Unregister FCF if FCF table need to be re-scaned.

.. _`lpfc_check_pending_fcoe_event.description`:

Description
-----------

This function check if there is any fcoe event pending while driver
scan FCF entries. If there is any pending event, it will restart the
FCF saning and return 1 else return 0.

.. _`lpfc_sli4_new_fcf_random_select`:

lpfc_sli4_new_fcf_random_select
===============================

.. c:function:: bool lpfc_sli4_new_fcf_random_select(struct lpfc_hba *phba, uint32_t fcf_cnt)

    Randomly select an eligible new fcf record

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint32_t fcf_cnt:
        number of eligible fcf record seen so far.

.. _`lpfc_sli4_new_fcf_random_select.description`:

Description
-----------

This function makes an running random selection decision on FCF record to
use through a sequence of \ ``fcf_cnt``\  eligible FCF records with equal
probability. To perform integer manunipulation of random numbers with
size unit32_t, the lower 16 bits of the 32-bit random number returned
from \ :c:func:`prandom_u32`\  are taken as the random random number generated.

Returns true when outcome is for the newly read FCF record should be
chosen; otherwise, return false when outcome is for keeping the previously
chosen FCF record.

.. _`lpfc_sli4_fcf_rec_mbox_parse`:

lpfc_sli4_fcf_rec_mbox_parse
============================

.. c:function:: struct fcf_record *lpfc_sli4_fcf_rec_mbox_parse(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq, uint16_t *next_fcf_index)

    Parse read_fcf mbox command.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox object.

    :param uint16_t \*next_fcf_index:
        pointer to holder of next fcf index.

.. _`lpfc_sli4_fcf_rec_mbox_parse.description`:

Description
-----------

This routine parses the non-embedded fcf mailbox command by performing the
necessarily error checking, non-embedded read FCF record mailbox command
SGE parsing, and endianness swapping.

Returns the pointer to the new FCF record in the non-embedded mailbox
command DMA memory if successfully, other NULL.

.. _`lpfc_sli4_log_fcf_record_info`:

lpfc_sli4_log_fcf_record_info
=============================

.. c:function:: void lpfc_sli4_log_fcf_record_info(struct lpfc_hba *phba, struct fcf_record *fcf_record, uint16_t vlan_id, uint16_t next_fcf_index)

    Log the information of a fcf record

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param struct fcf_record \*fcf_record:
        pointer to the fcf record.

    :param uint16_t vlan_id:
        the lowest vlan identifier associated to this fcf record.

    :param uint16_t next_fcf_index:
        the index to the next fcf record in hba's fcf table.

.. _`lpfc_sli4_log_fcf_record_info.description`:

Description
-----------

This routine logs the detailed FCF record if the LOG_FIP loggin is
enabled.

.. _`lpfc_sli4_fcf_rr_next_proc`:

lpfc_sli4_fcf_rr_next_proc
==========================

.. c:function:: int lpfc_sli4_fcf_rr_next_proc(struct lpfc_vport *vport, uint16_t fcf_index)

    processing next roundrobin fcf

    :param struct lpfc_vport \*vport:
        Pointer to vport object.

    :param uint16_t fcf_index:
        index to next fcf.

.. _`lpfc_sli4_fcf_rr_next_proc.description`:

Description
-----------

This function processing the roundrobin fcf failover to next fcf index.
When this function is invoked, there will be a current fcf registered
for flogi.

.. _`lpfc_sli4_fcf_rr_next_proc.return`:

Return
------

0 for continue retrying flogi on currently registered fcf;
1 for stop flogi on currently registered fcf;

.. _`lpfc_sli4_fcf_pri_list_del`:

lpfc_sli4_fcf_pri_list_del
==========================

.. c:function:: void lpfc_sli4_fcf_pri_list_del(struct lpfc_hba *phba, uint16_t fcf_index)

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.
        \ ``fcf_index``\  the index of the fcf record to delete
        This routine checks the on list flag of the fcf_index to be deleted.
        If it is one the list then it is removed from the list, and the flag
        is cleared. This routine grab the hbalock before removing the fcf
        record from the list.

    :param uint16_t fcf_index:
        *undescribed*

.. _`lpfc_sli4_set_fcf_flogi_fail`:

lpfc_sli4_set_fcf_flogi_fail
============================

.. c:function:: void lpfc_sli4_set_fcf_flogi_fail(struct lpfc_hba *phba, uint16_t fcf_index)

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.
        \ ``fcf_index``\  the index of the fcf record to update
        This routine acquires the hbalock and then set the LPFC_FCF_FLOGI_FAILED
        flag so the the round robin slection for the particular priority level
        will try a different fcf record that does not have this bit set.
        If the fcf record is re-read for any reason this flag is cleared brfore
        adding it to the priority list.

    :param uint16_t fcf_index:
        *undescribed*

.. _`lpfc_sli4_fcf_pri_list_add`:

lpfc_sli4_fcf_pri_list_add
==========================

.. c:function:: int lpfc_sli4_fcf_pri_list_add(struct lpfc_hba *phba, uint16_t fcf_index, struct fcf_record *new_fcf_record)

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.
        \ ``fcf_index``\  the index of the fcf record to add
        This routine checks the priority of the fcf_index to be added.
        If it is a lower priority than the current head of the fcf_pri list
        then it is added to the list in the right order.
        If it is the same priority as the current head of the list then it
        is added to the head of the list and its bit in the rr_bmask is set.
        If the fcf_index to be added is of a higher priority than the current
        head of the list then the rr_bmask is cleared, its bit is set in the
        rr_bmask and it is added to the head of the list.

    :param uint16_t fcf_index:
        *undescribed*

    :param struct fcf_record \*new_fcf_record:
        *undescribed*

.. _`lpfc_sli4_fcf_pri_list_add.return`:

Return
------

0=success 1=failure

.. _`lpfc_mbx_cmpl_fcf_scan_read_fcf_rec`:

lpfc_mbx_cmpl_fcf_scan_read_fcf_rec
===================================

.. c:function:: void lpfc_mbx_cmpl_fcf_scan_read_fcf_rec(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    fcf scan read_fcf mbox cmpl handler.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox object.

.. _`lpfc_mbx_cmpl_fcf_scan_read_fcf_rec.description`:

Description
-----------

This function iterates through all the fcf records available in
HBA and chooses the optimal FCF record for discovery. After finding
the FCF for discovery it registers the FCF record and kicks start
discovery.
If FCF_IN_USE flag is set in currently used FCF, the routine tries to
use an FCF record which matches fabric name and mac address of the
currently used FCF record.
If the driver supports only one FCF, it will try to use the FCF record
used by BOOT_BIOS.

.. _`lpfc_mbx_cmpl_fcf_rr_read_fcf_rec`:

lpfc_mbx_cmpl_fcf_rr_read_fcf_rec
=================================

.. c:function:: void lpfc_mbx_cmpl_fcf_rr_read_fcf_rec(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    fcf roundrobin read_fcf mbox cmpl hdler

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox object.

.. _`lpfc_mbx_cmpl_fcf_rr_read_fcf_rec.description`:

Description
-----------

This is the callback function for FLOGI failure roundrobin FCF failover
read FCF record mailbox command from the eligible FCF record bmask for
performing the failover. If the FCF read back is not valid/available, it
fails through to retrying FLOGI to the currently registered FCF again.
Otherwise, if the FCF read back is valid and available, it will set the
newly read FCF record to the failover FCF record, unregister currently
registered FCF record, copy the failover FCF record to the current
FCF record, and then register the current FCF record before proceeding
to trying FLOGI on the new failover FCF.

.. _`lpfc_mbx_cmpl_read_fcf_rec`:

lpfc_mbx_cmpl_read_fcf_rec
==========================

.. c:function:: void lpfc_mbx_cmpl_read_fcf_rec(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    read fcf completion handler.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox object.

.. _`lpfc_mbx_cmpl_read_fcf_rec.description`:

Description
-----------

This is the callback function of read FCF record mailbox command for
updating the eligible FCF bmask for FLOGI failure roundrobin FCF
failover when a new FCF event happened. If the FCF read back is
valid/available and it passes the connection list check, it updates
the bmask for the eligible FCF record for roundrobin failover.

.. _`lpfc_init_vfi_cmpl`:

lpfc_init_vfi_cmpl
==================

.. c:function:: void lpfc_init_vfi_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Completion handler for init_vfi mbox command.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox data structure.

.. _`lpfc_init_vfi_cmpl.description`:

Description
-----------

This function handles completion of init vfi mailbox command.

.. _`lpfc_issue_init_vfi`:

lpfc_issue_init_vfi
===================

.. c:function:: void lpfc_issue_init_vfi(struct lpfc_vport *vport)

    Issue init_vfi mailbox command.

    :param struct lpfc_vport \*vport:
        pointer to lpfc_vport data structure.

.. _`lpfc_issue_init_vfi.description`:

Description
-----------

This function issue a init_vfi mailbox command to initialize the VFI and
VPI for the physical port.

.. _`lpfc_init_vpi_cmpl`:

lpfc_init_vpi_cmpl
==================

.. c:function:: void lpfc_init_vpi_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Completion handler for init_vpi mbox command.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox data structure.

.. _`lpfc_init_vpi_cmpl.description`:

Description
-----------

This function handles completion of init vpi mailbox command.

.. _`lpfc_issue_init_vpi`:

lpfc_issue_init_vpi
===================

.. c:function:: void lpfc_issue_init_vpi(struct lpfc_vport *vport)

    Issue init_vpi mailbox command.

    :param struct lpfc_vport \*vport:
        pointer to lpfc_vport data structure.

.. _`lpfc_issue_init_vpi.description`:

Description
-----------

This function issue a init_vpi mailbox command to initialize
VPI for the vport.

.. _`lpfc_start_fdiscs`:

lpfc_start_fdiscs
=================

.. c:function:: void lpfc_start_fdiscs(struct lpfc_hba *phba)

    send fdiscs for each vports on this port.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_start_fdiscs.description`:

Description
-----------

This function loops through the list of vports on the \ ``phba``\  and issues an
FDISC if possible.

.. _`lpfc_create_static_vport`:

lpfc_create_static_vport
========================

.. c:function:: void lpfc_create_static_vport(struct lpfc_hba *phba)

    Read HBA config region to create static vports.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_create_static_vport.description`:

Description
-----------

This routine issue a DUMP mailbox command for config region 22 to get
the list of static vports to be created. The function create vports
based on the information returned from the HBA.

.. _`lpfc_initialize_node`:

lpfc_initialize_node
====================

.. c:function:: void lpfc_initialize_node(struct lpfc_vport *vport, struct lpfc_nodelist *ndlp, uint32_t did)

    Initialize all fields of node object

    :param struct lpfc_vport \*vport:
        Pointer to Virtual Port object.

    :param struct lpfc_nodelist \*ndlp:
        Pointer to FC node object.

    :param uint32_t did:
        FC_ID of the node.

.. _`lpfc_initialize_node.description`:

Description
-----------

This function is always called when node object need to be initialized.
It initializes all the fields of the node object. Although the reference
to phba from \ ``ndlp``\  can be obtained indirectly through it's reference to
\ ``vport``\ , a direct reference to phba is taken here by \ ``ndlp``\ . This is due
to the life-span of the \ ``ndlp``\  might go beyond the existence of \ ``vport``\  as
the final release of ndlp is determined by its reference count. And, the
operation on \ ``ndlp``\  needs the reference to phba.

.. _`lpfc_nlp_logo_unreg`:

lpfc_nlp_logo_unreg
===================

.. c:function:: void lpfc_nlp_logo_unreg(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmb)

    Unreg mailbox completion handler before LOGO

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param LPFC_MBOXQ_t \*pmb:
        Pointer to mailbox object.

.. _`lpfc_nlp_logo_unreg.description`:

Description
-----------

This function will issue an ELS LOGO command after completing
the UNREG_RPI.

.. _`lpfc_unreg_hba_rpis`:

lpfc_unreg_hba_rpis
===================

.. c:function:: void lpfc_unreg_hba_rpis(struct lpfc_hba *phba)

    Unregister rpis registered to the hba.

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

.. _`lpfc_unreg_hba_rpis.description`:

Description
-----------

This routine is invoked to unregister all the currently registered RPIs
to the HBA.

.. _`lpfc_find_vport_by_vpid`:

lpfc_find_vport_by_vpid
=======================

.. c:function:: struct lpfc_vport *lpfc_find_vport_by_vpid(struct lpfc_hba *phba, uint16_t vpi)

    Find a vport on a HBA through vport identifier

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param uint16_t vpi:
        the physical host virtual N_Port identifier.

.. _`lpfc_find_vport_by_vpid.description`:

Description
-----------

This routine finds a vport on a HBA (referred by \ ``phba``\ ) through a
\ ``vpi``\ . The function walks the HBA's vport list and returns the address
of the vport with the matching \ ``vpi``\ .

Return code
NULL - No vport with the matching \ ``vpi``\  found
Otherwise - Address to the vport with the matching \ ``vpi``\ .

.. _`lpfc_fcf_inuse`:

lpfc_fcf_inuse
==============

.. c:function:: int lpfc_fcf_inuse(struct lpfc_hba *phba)

    Check if FCF can be unregistered.

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_fcf_inuse.description`:

Description
-----------

This function iterate through all FC nodes associated
will all vports to check if there is any node with
fc_rports associated with it. If there is an fc_rport
associated with the node, then the node is either in
discovered state or its devloss_timer is pending.

.. _`lpfc_unregister_vfi_cmpl`:

lpfc_unregister_vfi_cmpl
========================

.. c:function:: void lpfc_unregister_vfi_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Completion handler for unreg vfi.

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param LPFC_MBOXQ_t \*mboxq:
        Pointer to mailbox object.

.. _`lpfc_unregister_vfi_cmpl.description`:

Description
-----------

This function frees memory associated with the mailbox command.

.. _`lpfc_unregister_fcfi_cmpl`:

lpfc_unregister_fcfi_cmpl
=========================

.. c:function:: void lpfc_unregister_fcfi_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Completion handler for unreg fcfi.

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param LPFC_MBOXQ_t \*mboxq:
        Pointer to mailbox object.

.. _`lpfc_unregister_fcfi_cmpl.description`:

Description
-----------

This function frees memory associated with the mailbox command.

.. _`lpfc_unregister_fcf_prep`:

lpfc_unregister_fcf_prep
========================

.. c:function:: int lpfc_unregister_fcf_prep(struct lpfc_hba *phba)

    Unregister fcf record preparation

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_unregister_fcf_prep.description`:

Description
-----------

This function prepare the HBA for unregistering the currently registered
FCF from the HBA. It performs unregistering, in order, RPIs, VPIs, and
VFIs.

.. _`lpfc_sli4_unregister_fcf`:

lpfc_sli4_unregister_fcf
========================

.. c:function:: int lpfc_sli4_unregister_fcf(struct lpfc_hba *phba)

    Unregister currently registered FCF record

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_sli4_unregister_fcf.description`:

Description
-----------

This function issues synchronous unregister FCF mailbox command to HBA to
unregister the currently registered FCF record. The driver does not reset
the driver FCF usage state flags.

Return 0 if successfully issued, none-zero otherwise.

.. _`lpfc_unregister_fcf_rescan`:

lpfc_unregister_fcf_rescan
==========================

.. c:function:: void lpfc_unregister_fcf_rescan(struct lpfc_hba *phba)

    Unregister currently registered fcf and rescan

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_unregister_fcf_rescan.description`:

Description
-----------

This function unregisters the currently reigstered FCF. This function
also tries to find another FCF for discovery by rescan the HBA FCF table.

.. _`lpfc_unregister_fcf`:

lpfc_unregister_fcf
===================

.. c:function:: void lpfc_unregister_fcf(struct lpfc_hba *phba)

    Unregister the currently registered fcf record

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_unregister_fcf.description`:

Description
-----------

This function just unregisters the currently reigstered FCF. It does not
try to find another FCF for discovery.

.. _`lpfc_unregister_unused_fcf`:

lpfc_unregister_unused_fcf
==========================

.. c:function:: void lpfc_unregister_unused_fcf(struct lpfc_hba *phba)

    Unregister FCF if all devices are disconnected.

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

.. _`lpfc_unregister_unused_fcf.description`:

Description
-----------

This function check if there are any connected remote port for the FCF and
if all the devices are disconnected, this function unregister FCFI.
This function also tries to use another FCF for discovery.

.. _`lpfc_read_fcf_conn_tbl`:

lpfc_read_fcf_conn_tbl
======================

.. c:function:: void lpfc_read_fcf_conn_tbl(struct lpfc_hba *phba, uint8_t *buff)

    Create driver FCF connection table.

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param uint8_t \*buff:
        Buffer containing the FCF connection table as in the config
        region.
        This function create driver data structure for the FCF connection
        record table read from config region 23.

.. _`lpfc_read_fcoe_param`:

lpfc_read_fcoe_param
====================

.. c:function:: void lpfc_read_fcoe_param(struct lpfc_hba *phba, uint8_t *buff)

    Read FCoe parameters from conf region..

    :param struct lpfc_hba \*phba:
        Pointer to hba context object.

    :param uint8_t \*buff:
        Buffer containing the FCoE parameter data structure.

.. _`lpfc_read_fcoe_param.description`:

Description
-----------

This function update driver data structure with config
parameters read from config region 23.

.. _`lpfc_get_rec_conf23`:

lpfc_get_rec_conf23
===================

.. c:function:: uint8_t *lpfc_get_rec_conf23(uint8_t *buff, uint32_t size, uint8_t rec_type)

    Get a record type in config region data.

    :param uint8_t \*buff:
        Buffer containing config region 23 data.

    :param uint32_t size:
        Size of the data buffer.

    :param uint8_t rec_type:
        Record type to be searched.

.. _`lpfc_get_rec_conf23.description`:

Description
-----------

This function searches config region data to find the beginning
of the record specified by record_type. If record found, this
function return pointer to the record else return NULL.

.. _`lpfc_parse_fcoe_conf`:

lpfc_parse_fcoe_conf
====================

.. c:function:: void lpfc_parse_fcoe_conf(struct lpfc_hba *phba, uint8_t *buff, uint32_t size)

    Parse FCoE config data read from config region 23.

    :param struct lpfc_hba \*phba:
        Pointer to lpfc_hba data structure.

    :param uint8_t \*buff:
        Buffer containing config region 23 data.

    :param uint32_t size:
        Size of the data buffer.

.. _`lpfc_parse_fcoe_conf.description`:

Description
-----------

This function parses the FCoE config parameters in config region 23 and
populate driver data structure with the parameters.

.. This file was automatic generated / don't edit.


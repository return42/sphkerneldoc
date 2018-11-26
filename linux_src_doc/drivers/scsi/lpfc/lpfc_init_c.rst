.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_init.c

.. _`lpfc_config_port_prep`:

lpfc_config_port_prep
=====================

.. c:function:: int lpfc_config_port_prep(struct lpfc_hba *phba)

    Perform lpfc initialization prior to config port

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_config_port_prep.description`:

Description
-----------

This routine will do LPFC initialization prior to issuing the CONFIG_PORT
mailbox command. It retrieves the revision information from the HBA and
collects the Vital Product Data (VPD) about the HBA for preparing the
configuration of the HBA.

.. _`lpfc_config_port_prep.return-codes`:

Return codes
------------

0 - success.
-ERESTART - requests the SLI layer to reset the HBA and try again.
Any other value - indicates an error.

.. _`lpfc_config_async_cmpl`:

lpfc_config_async_cmpl
======================

.. c:function:: void lpfc_config_async_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    Completion handler for config async event mbox cmd

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param pmboxq:
        pointer to the driver internal queue element for mailbox command.
    :type pmboxq: LPFC_MBOXQ_t \*

.. _`lpfc_config_async_cmpl.description`:

Description
-----------

This is the completion handler for driver's configuring asynchronous event
mailbox command to the device. If the mailbox command returns successfully,
it will set internal async event support flag to 1; otherwise, it will
set internal async event support flag to 0.

.. _`lpfc_dump_wakeup_param_cmpl`:

lpfc_dump_wakeup_param_cmpl
===========================

.. c:function:: void lpfc_dump_wakeup_param_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    dump memory mailbox command completion handler

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param pmboxq:
        pointer to the driver internal queue element for mailbox command.
    :type pmboxq: LPFC_MBOXQ_t \*

.. _`lpfc_dump_wakeup_param_cmpl.description`:

Description
-----------

This is the completion handler for dump mailbox command for getting
wake up parameters. When this command complete, the response contain
Option rom version of the HBA. This function translate the version number
into a human readable string and store it in OptionROMVersion.

.. _`lpfc_update_vport_wwn`:

lpfc_update_vport_wwn
=====================

.. c:function:: void lpfc_update_vport_wwn(struct lpfc_vport *vport)

    Updates the fc_nodename, fc_portname, cfg_soft_wwnn, cfg_soft_wwpn

    :param vport:
        pointer to lpfc vport data structure.
    :type vport: struct lpfc_vport \*

.. _`lpfc_update_vport_wwn.description`:

Description
-----------


Return codes
None.

.. _`lpfc_config_port_post`:

lpfc_config_port_post
=====================

.. c:function:: int lpfc_config_port_post(struct lpfc_hba *phba)

    Perform lpfc initialization after config port

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_config_port_post.description`:

Description
-----------

This routine will do LPFC initialization after the CONFIG_PORT mailbox
command call. It performs all internal resource and state setups on the

.. _`lpfc_config_port_post.port`:

port
----

post IOCB buffers, enable appropriate host interrupt attentions,
ELS ring timers, etc.

Return codes
0 - success.
Any other value - error.

.. _`lpfc_hba_init_link`:

lpfc_hba_init_link
==================

.. c:function:: int lpfc_hba_init_link(struct lpfc_hba *phba, uint32_t flag)

    Initialize the FC link

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param flag:
        mailbox command issue mode - either MBX_POLL or MBX_NOWAIT
    :type flag: uint32_t

.. _`lpfc_hba_init_link.description`:

Description
-----------

This routine will issue the INIT_LINK mailbox command call.
It is available to other drivers through the lpfc_hba data
structure for use as a delayed link up mechanism with the
module parameter lpfc_suppress_link_up.

Return code
0 - success
Any other value - error

.. _`lpfc_hba_init_link_fc_topology`:

lpfc_hba_init_link_fc_topology
==============================

.. c:function:: int lpfc_hba_init_link_fc_topology(struct lpfc_hba *phba, uint32_t fc_topology, uint32_t flag)

    Initialize FC link with desired topology

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param fc_topology:
        desired fc topology.
    :type fc_topology: uint32_t

    :param flag:
        mailbox command issue mode - either MBX_POLL or MBX_NOWAIT
    :type flag: uint32_t

.. _`lpfc_hba_init_link_fc_topology.description`:

Description
-----------

This routine will issue the INIT_LINK mailbox command call.
It is available to other drivers through the lpfc_hba data
structure for use as a delayed link up mechanism with the
module parameter lpfc_suppress_link_up.

Return code
0 - success
Any other value - error

.. _`lpfc_hba_down_link`:

lpfc_hba_down_link
==================

.. c:function:: int lpfc_hba_down_link(struct lpfc_hba *phba, uint32_t flag)

    this routine downs the FC link

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param flag:
        mailbox command issue mode - either MBX_POLL or MBX_NOWAIT
    :type flag: uint32_t

.. _`lpfc_hba_down_link.description`:

Description
-----------

This routine will issue the DOWN_LINK mailbox command call.
It is available to other drivers through the lpfc_hba data
structure for use to stop the link.

Return code
0 - success
Any other value - error

.. _`lpfc_hba_down_prep`:

lpfc_hba_down_prep
==================

.. c:function:: int lpfc_hba_down_prep(struct lpfc_hba *phba)

    Perform lpfc uninitialization prior to HBA reset

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_down_prep.description`:

Description
-----------

This routine will do LPFC uninitialization before the HBA is reset when
bringing down the SLI Layer.

Return codes
0 - success.
Any other value - error.

.. _`lpfc_sli4_free_sp_events`:

lpfc_sli4_free_sp_events
========================

.. c:function:: void lpfc_sli4_free_sp_events(struct lpfc_hba *phba)

    Cleanup sp_queue_events to free rspiocb which got deferred

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_free_sp_events.description`:

Description
-----------

This routine will cleanup completed slow path events after HBA is reset
when bringing down the SLI Layer.


Return codes
void.

.. _`lpfc_hba_free_post_buf`:

lpfc_hba_free_post_buf
======================

.. c:function:: void lpfc_hba_free_post_buf(struct lpfc_hba *phba)

    Perform lpfc uninitialization after HBA reset

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_free_post_buf.description`:

Description
-----------

This routine will cleanup posted ELS buffers after the HBA is reset
when bringing down the SLI Layer.


Return codes
void.

.. _`lpfc_hba_clean_txcmplq`:

lpfc_hba_clean_txcmplq
======================

.. c:function:: void lpfc_hba_clean_txcmplq(struct lpfc_hba *phba)

    Perform lpfc uninitialization after HBA reset

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_clean_txcmplq.description`:

Description
-----------

This routine will cleanup the txcmplq after the HBA is reset when bringing
down the SLI Layer.

Return codes
void

.. _`lpfc_hba_down_post_s3`:

lpfc_hba_down_post_s3
=====================

.. c:function:: int lpfc_hba_down_post_s3(struct lpfc_hba *phba)

    Perform lpfc uninitialization after HBA reset

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_down_post_s3.description`:

Description
-----------

This routine will do uninitialization after the HBA is reset when bring
down the SLI Layer.

Return codes
0 - success.
Any other value - error.

.. _`lpfc_hba_down_post_s4`:

lpfc_hba_down_post_s4
=====================

.. c:function:: int lpfc_hba_down_post_s4(struct lpfc_hba *phba)

    Perform lpfc uninitialization after HBA reset

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_down_post_s4.description`:

Description
-----------

This routine will do uninitialization after the HBA is reset when bring
down the SLI Layer.

Return codes
0 - success.
Any other value - error.

.. _`lpfc_hba_down_post`:

lpfc_hba_down_post
==================

.. c:function:: int lpfc_hba_down_post(struct lpfc_hba *phba)

    Wrapper func for hba down post routine

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_down_post.description`:

Description
-----------

This routine wraps the actual SLI3 or SLI4 routine for performing
uninitialization after the HBA is reset when bring down the SLI Layer.

Return codes
0 - success.
Any other value - error.

.. _`lpfc_hb_timeout`:

lpfc_hb_timeout
===============

.. c:function:: void lpfc_hb_timeout(struct timer_list *t)

    The HBA-timer timeout handler

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`lpfc_hb_timeout.description`:

Description
-----------

This is the HBA-timer timeout handler registered to the lpfc driver. When
this timer fires, a HBA timeout event shall be posted to the lpfc driver
work-port-events bitmap and the worker thread is notified. This timeout
event will be used by the worker thread to invoke the actual timeout
handler routine, lpfc_hb_timeout_handler. Any periodical operations will
be performed in the timeout handler and the HBA timeout event bit shall
be cleared by the worker thread after it has taken the event bitmap out.

.. _`lpfc_rrq_timeout`:

lpfc_rrq_timeout
================

.. c:function:: void lpfc_rrq_timeout(struct timer_list *t)

    The RRQ-timer timeout handler

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`lpfc_rrq_timeout.description`:

Description
-----------

This is the RRQ-timer timeout handler registered to the lpfc driver. When
this timer fires, a RRQ timeout event shall be posted to the lpfc driver
work-port-events bitmap and the worker thread is notified. This timeout
event will be used by the worker thread to invoke the actual timeout
handler routine, lpfc_rrq_handler. Any periodical operations will
be performed in the timeout handler and the RRQ timeout event bit shall
be cleared by the worker thread after it has taken the event bitmap out.

.. _`lpfc_hb_mbox_cmpl`:

lpfc_hb_mbox_cmpl
=================

.. c:function:: void lpfc_hb_mbox_cmpl(struct lpfc_hba *phba, LPFC_MBOXQ_t *pmboxq)

    The lpfc heart-beat mailbox command callback function

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param pmboxq:
        pointer to the driver internal queue element for mailbox command.
    :type pmboxq: LPFC_MBOXQ_t \*

.. _`lpfc_hb_mbox_cmpl.description`:

Description
-----------

This is the callback function to the lpfc heart-beat mailbox command.
If configured, the lpfc driver issues the heart-beat mailbox command to
the HBA every LPFC_HB_MBOX_INTERVAL (current 5) seconds. At the time the
heart-beat mailbox command is issued, the driver shall set up heart-beat
timeout timer to LPFC_HB_MBOX_TIMEOUT (current 30) seconds and marks
heart-beat outstanding state. Once the mailbox command comes back and
no error conditions detected, the heart-beat mailbox command timer is
reset to LPFC_HB_MBOX_INTERVAL seconds and the heart-beat outstanding
state is cleared for the next heart-beat. If the timer expired with the
heart-beat outstanding state set, the driver will put the HBA offline.

.. _`lpfc_hb_timeout_handler`:

lpfc_hb_timeout_handler
=======================

.. c:function:: void lpfc_hb_timeout_handler(struct lpfc_hba *phba)

    The HBA-timer timeout handler

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hb_timeout_handler.description`:

Description
-----------

This is the actual HBA-timer timeout handler to be invoked by the worker
thread whenever the HBA timer fired and HBA-timeout event posted. This
handler performs any periodic operations needed for the device. If such
periodic event has already been attended to either in the interrupt handler
or by processing slow-ring or fast-ring events within the HBA-timer
timeout window (LPFC_HB_MBOX_INTERVAL), this handler just simply resets
the timer for the next timeout period. If lpfc heart-beat mailbox command
is configured and there is no heart-beat mailbox command outstanding, a
heart-beat mailbox is issued and timer set properly. Otherwise, if there
has been a heart-beat mailbox command outstanding, the HBA shall be put
to offline.

.. _`lpfc_offline_eratt`:

lpfc_offline_eratt
==================

.. c:function:: void lpfc_offline_eratt(struct lpfc_hba *phba)

    Bring lpfc offline on hardware error attention

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_offline_eratt.description`:

Description
-----------

This routine is called to bring the HBA offline when HBA hardware error
other than Port Error 6 has been detected.

.. _`lpfc_sli4_offline_eratt`:

lpfc_sli4_offline_eratt
=======================

.. c:function:: void lpfc_sli4_offline_eratt(struct lpfc_hba *phba)

    Bring lpfc offline on SLI4 hardware error attention

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_offline_eratt.description`:

Description
-----------

This routine is called to bring a SLI4 HBA offline when HBA hardware error
other than Port Error 6 has been detected.

.. _`lpfc_handle_deferred_eratt`:

lpfc_handle_deferred_eratt
==========================

.. c:function:: void lpfc_handle_deferred_eratt(struct lpfc_hba *phba)

    The HBA hardware deferred error handler

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_handle_deferred_eratt.description`:

Description
-----------

This routine is invoked to handle the deferred HBA hardware error
conditions. This type of error is indicated by HBA by setting ER1
and another ER bit in the host status register. The driver will
wait until the ER1 bit clears before handling the error condition.

.. _`lpfc_handle_eratt_s3`:

lpfc_handle_eratt_s3
====================

.. c:function:: void lpfc_handle_eratt_s3(struct lpfc_hba *phba)

    The SLI3 HBA hardware error handler

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_handle_eratt_s3.description`:

Description
-----------

This routine is invoked to handle the following HBA hardware error

.. _`lpfc_handle_eratt_s3.conditions`:

conditions
----------

1 - HBA error attention interrupt
2 - DMA ring index out of range
3 - Mailbox command came back as unknown

.. _`lpfc_sli4_port_sta_fn_reset`:

lpfc_sli4_port_sta_fn_reset
===========================

.. c:function:: int lpfc_sli4_port_sta_fn_reset(struct lpfc_hba *phba, int mbx_action, bool en_rn_msg)

    The SLI4 function reset due to port status reg

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param mbx_action:
        flag for mailbox shutdown action.
    :type mbx_action: int

    :param en_rn_msg:
        *undescribed*
    :type en_rn_msg: bool

.. _`lpfc_sli4_port_sta_fn_reset.description`:

Description
-----------

This routine is invoked to perform an SLI4 port PCI function reset in
response to port status register polling attention. It waits for port
status register (ERR, RDY, RN) bits before proceeding with function reset.
During this process, interrupt vectors are freed and later requested
for handling possible port resource change.

.. _`lpfc_handle_eratt_s4`:

lpfc_handle_eratt_s4
====================

.. c:function:: void lpfc_handle_eratt_s4(struct lpfc_hba *phba)

    The SLI4 HBA hardware error handler

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_handle_eratt_s4.description`:

Description
-----------

This routine is invoked to handle the SLI4 HBA hardware error attention
conditions.

.. _`lpfc_handle_eratt`:

lpfc_handle_eratt
=================

.. c:function:: void lpfc_handle_eratt(struct lpfc_hba *phba)

    Wrapper func for handling hba error attention

    :param phba:
        pointer to lpfc HBA data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_handle_eratt.description`:

Description
-----------

This routine wraps the actual SLI3 or SLI4 hba error attention handling
routine from the API jump table function pointer from the lpfc_hba struct.

Return codes
0 - success.
Any other value - error.

.. _`lpfc_handle_latt`:

lpfc_handle_latt
================

.. c:function:: void lpfc_handle_latt(struct lpfc_hba *phba)

    The HBA link event handler

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_handle_latt.description`:

Description
-----------

This routine is invoked from the worker thread to handle a HBA host
attention link event. SLI3 only.

.. _`lpfc_parse_vpd`:

lpfc_parse_vpd
==============

.. c:function:: int lpfc_parse_vpd(struct lpfc_hba *phba, uint8_t *vpd, int len)

    Parse VPD (Vital Product Data)

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param vpd:
        pointer to the vital product data.
    :type vpd: uint8_t \*

    :param len:
        length of the vital product data in bytes.
    :type len: int

.. _`lpfc_parse_vpd.description`:

Description
-----------

This routine parses the Vital Product Data (VPD). The VPD is treated as
an array of characters. In this routine, the ModelName, ProgramType, and
ModelDesc, etc. fields of the phba data structure will be populated.

Return codes
0 - pointer to the VPD passed in is NULL
1 - success

.. _`lpfc_get_hba_model_desc`:

lpfc_get_hba_model_desc
=======================

.. c:function:: void lpfc_get_hba_model_desc(struct lpfc_hba *phba, uint8_t *mdp, uint8_t *descp)

    Retrieve HBA device model name and description

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param mdp:
        pointer to the data structure to hold the derived model name.
    :type mdp: uint8_t \*

    :param descp:
        pointer to the data structure to hold the derived description.
    :type descp: uint8_t \*

.. _`lpfc_get_hba_model_desc.description`:

Description
-----------

This routine retrieves HBA's description based on its registered PCI device
ID. The \ ``descp``\  passed into this function points to an array of 256 chars. It
shall be returned with the model name, maximum speed, and the host bus type.
The \ ``mdp``\  passed into this function points to an array of 80 chars. When the
function returns, the \ ``mdp``\  will be filled with the model name.

.. _`lpfc_post_buffer`:

lpfc_post_buffer
================

.. c:function:: int lpfc_post_buffer(struct lpfc_hba *phba, struct lpfc_sli_ring *pring, int cnt)

    Post IOCB(s) with DMA buffer descriptor(s) to a IOCB ring

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param pring:
        pointer to a IOCB ring.
    :type pring: struct lpfc_sli_ring \*

    :param cnt:
        the number of IOCBs to be posted to the IOCB ring.
    :type cnt: int

.. _`lpfc_post_buffer.description`:

Description
-----------

This routine posts a given number of IOCBs with the associated DMA buffer
descriptors specified by the cnt argument to the given IOCB ring.

Return codes
The number of IOCBs NOT able to be posted to the IOCB ring.

.. _`lpfc_post_rcv_buf`:

lpfc_post_rcv_buf
=================

.. c:function:: int lpfc_post_rcv_buf(struct lpfc_hba *phba)

    Post the initial receive IOCB buffers to ELS ring

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_post_rcv_buf.description`:

Description
-----------

This routine posts initial receive IOCB buffers to the ELS ring. The
current number of initial IOCB buffers specified by LPFC_BUF_RING0 is
set to 64 IOCBs. SLI3 only.

Return codes
0 - success (currently always success)

.. _`lpfc_sha_init`:

lpfc_sha_init
=============

.. c:function:: void lpfc_sha_init(uint32_t *HashResultPointer)

    Set up initial array of hash table entries

    :param HashResultPointer:
        pointer to an array as hash table.
    :type HashResultPointer: uint32_t \*

.. _`lpfc_sha_init.description`:

Description
-----------

This routine sets up the initial values to the array of hash table entries
for the LC HBAs.

.. _`lpfc_sha_iterate`:

lpfc_sha_iterate
================

.. c:function:: void lpfc_sha_iterate(uint32_t *HashResultPointer, uint32_t *HashWorkingPointer)

    Iterate initial hash table with the working hash table

    :param HashResultPointer:
        pointer to an initial/result hash table.
    :type HashResultPointer: uint32_t \*

    :param HashWorkingPointer:
        pointer to an working hash table.
    :type HashWorkingPointer: uint32_t \*

.. _`lpfc_sha_iterate.description`:

Description
-----------

This routine iterates an initial hash table pointed by \ ``HashResultPointer``\ 
with the values from the working hash table pointeed by \ ``HashWorkingPointer``\ .
The results are putting back to the initial hash table, returned through
the \ ``HashResultPointer``\  as the result hash table.

.. _`lpfc_challenge_key`:

lpfc_challenge_key
==================

.. c:function:: void lpfc_challenge_key(uint32_t *RandomChallenge, uint32_t *HashWorking)

    Create challenge key based on WWPN of the HBA

    :param RandomChallenge:
        pointer to the entry of host challenge random number array.
    :type RandomChallenge: uint32_t \*

    :param HashWorking:
        pointer to the entry of the working hash array.
    :type HashWorking: uint32_t \*

.. _`lpfc_challenge_key.description`:

Description
-----------

This routine calculates the working hash array referred by \ ``HashWorking``\ 
from the challenge random numbers associated with the host, referred by
\ ``RandomChallenge``\ . The result is put into the entry of the working hash
array and returned by reference through \ ``HashWorking``\ .

.. _`lpfc_hba_init`:

lpfc_hba_init
=============

.. c:function:: void lpfc_hba_init(struct lpfc_hba *phba, uint32_t *hbainit)

    Perform special handling for LC HBA initialization

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param hbainit:
        pointer to an array of unsigned 32-bit integers.
    :type hbainit: uint32_t \*

.. _`lpfc_hba_init.description`:

Description
-----------

This routine performs the special handling for LC HBA initialization.

.. _`lpfc_cleanup`:

lpfc_cleanup
============

.. c:function:: void lpfc_cleanup(struct lpfc_vport *vport)

    Performs vport cleanups before deleting a vport

    :param vport:
        pointer to a virtual N_Port data structure.
    :type vport: struct lpfc_vport \*

.. _`lpfc_cleanup.description`:

Description
-----------

This routine performs the necessary cleanups before deleting the \ ``vport``\ .
It invokes the discovery state machine to perform necessary state
transitions and to release the ndlps associated with the \ ``vport``\ . Note,
the physical port is treated as \ ``vport``\  0.

.. _`lpfc_stop_vport_timers`:

lpfc_stop_vport_timers
======================

.. c:function:: void lpfc_stop_vport_timers(struct lpfc_vport *vport)

    Stop all the timers associated with a vport

    :param vport:
        pointer to a virtual N_Port data structure.
    :type vport: struct lpfc_vport \*

.. _`lpfc_stop_vport_timers.description`:

Description
-----------

This routine stops all the timers associated with a \ ``vport``\ . This function
is invoked before disabling or deleting a \ ``vport``\ . Note that the physical
port is treated as \ ``vport``\  0.

.. _`__lpfc_sli4_stop_fcf_redisc_wait_timer`:

\__lpfc_sli4_stop_fcf_redisc_wait_timer
=======================================

.. c:function:: void __lpfc_sli4_stop_fcf_redisc_wait_timer(struct lpfc_hba *phba)

    Stop FCF rediscovery wait timer

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`__lpfc_sli4_stop_fcf_redisc_wait_timer.description`:

Description
-----------

This routine stops the SLI4 FCF rediscover wait timer if it's on. The
caller of this routine should already hold the host lock.

.. _`lpfc_sli4_stop_fcf_redisc_wait_timer`:

lpfc_sli4_stop_fcf_redisc_wait_timer
====================================

.. c:function:: void lpfc_sli4_stop_fcf_redisc_wait_timer(struct lpfc_hba *phba)

    Stop FCF rediscovery wait timer

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_stop_fcf_redisc_wait_timer.description`:

Description
-----------

This routine stops the SLI4 FCF rediscover wait timer if it's on. It
checks whether the FCF rediscovery wait timer is pending with the host
lock held before proceeding with disabling the timer and clearing the
wait timer pendig flag.

.. _`lpfc_stop_hba_timers`:

lpfc_stop_hba_timers
====================

.. c:function:: void lpfc_stop_hba_timers(struct lpfc_hba *phba)

    Stop all the timers associated with an HBA

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_stop_hba_timers.description`:

Description
-----------

This routine stops all the timers associated with a HBA. This function is
invoked before either putting a HBA offline or unloading the driver.

.. _`lpfc_block_mgmt_io`:

lpfc_block_mgmt_io
==================

.. c:function:: void lpfc_block_mgmt_io(struct lpfc_hba *phba, int mbx_action)

    Mark a HBA's management interface as blocked

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param mbx_action:
        *undescribed*
    :type mbx_action: int

.. _`lpfc_block_mgmt_io.description`:

Description
-----------

This routine marks a HBA's management interface as blocked. Once the HBA's
management interface is marked as blocked, all the user space access to
the HBA, whether they are from sysfs interface or libdfc interface will
all be blocked. The HBA is set to block the management interface when the
driver prepares the HBA interface for online or offline.

.. _`lpfc_sli4_node_prep`:

lpfc_sli4_node_prep
===================

.. c:function:: void lpfc_sli4_node_prep(struct lpfc_hba *phba)

    Assign RPIs for active nodes.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_node_prep.description`:

Description
-----------

Allocate RPIs for all active remote nodes. This is needed whenever
an SLI4 adapter is reset and the driver is not unloading. Its purpose
is to fixup the temporary rpi assignments.

.. _`lpfc_online`:

lpfc_online
===========

.. c:function:: int lpfc_online(struct lpfc_hba *phba)

    Initialize and bring a HBA online

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_online.description`:

Description
-----------

This routine initializes the HBA and brings a HBA online. During this
process, the management interface is blocked to prevent user space access
to the HBA interfering with the driver initialization.

Return codes
0 - successful
1 - failed

.. _`lpfc_unblock_mgmt_io`:

lpfc_unblock_mgmt_io
====================

.. c:function:: void lpfc_unblock_mgmt_io(struct lpfc_hba *phba)

    Mark a HBA's management interface to be not blocked

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_unblock_mgmt_io.description`:

Description
-----------

This routine marks a HBA's management interface as not blocked. Once the
HBA's management interface is marked as not blocked, all the user space
access to the HBA, whether they are from sysfs interface or libdfc
interface will be allowed. The HBA is set to block the management interface
when the driver prepares the HBA interface for online or offline and then
set to unblock the management interface afterwards.

.. _`lpfc_offline_prep`:

lpfc_offline_prep
=================

.. c:function:: void lpfc_offline_prep(struct lpfc_hba *phba, int mbx_action)

    Prepare a HBA to be brought offline

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param mbx_action:
        *undescribed*
    :type mbx_action: int

.. _`lpfc_offline_prep.description`:

Description
-----------

This routine is invoked to prepare a HBA to be brought offline. It performs
unregistration login to all the nodes on all vports and flushes the mailbox
queue to make it ready to be brought offline.

.. _`lpfc_offline`:

lpfc_offline
============

.. c:function:: void lpfc_offline(struct lpfc_hba *phba)

    Bring a HBA offline

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_offline.description`:

Description
-----------

This routine actually brings a HBA offline. It stops all the timers
associated with the HBA, brings down the SLI layer, and eventually
marks the HBA as in offline state for the upper layer protocol.

.. _`lpfc_scsi_free`:

lpfc_scsi_free
==============

.. c:function:: void lpfc_scsi_free(struct lpfc_hba *phba)

    Free all the SCSI buffers and IOCBs from driver lists

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_scsi_free.description`:

Description
-----------

This routine is to free all the SCSI buffers and IOCBs from the driver
list back to kernel. It is called from lpfc_pci_remove_one to free
the internal resources before the device is removed from the system.

.. _`lpfc_nvme_free`:

lpfc_nvme_free
==============

.. c:function:: void lpfc_nvme_free(struct lpfc_hba *phba)

    Free all the NVME buffers and IOCBs from driver lists

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_nvme_free.description`:

Description
-----------

This routine is to free all the NVME buffers and IOCBs from the driver
list back to kernel. It is called from lpfc_pci_remove_one to free
the internal resources before the device is removed from the system.

.. _`lpfc_sli4_els_sgl_update`:

lpfc_sli4_els_sgl_update
========================

.. c:function:: int lpfc_sli4_els_sgl_update(struct lpfc_hba *phba)

    update ELS xri-sgl sizing and mapping

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_els_sgl_update.description`:

Description
-----------

This routine first calculates the sizes of the current els and allocated
scsi sgl lists, and then goes through all sgls to updates the physical
XRIs assigned due to port function reset. During port initialization, the
current els and allocated scsi sgl lists are 0s.

Return codes
0 - successful (for now, it always returns 0)

.. _`lpfc_sli4_nvmet_sgl_update`:

lpfc_sli4_nvmet_sgl_update
==========================

.. c:function:: int lpfc_sli4_nvmet_sgl_update(struct lpfc_hba *phba)

    update xri-sgl sizing and mapping

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_nvmet_sgl_update.description`:

Description
-----------

This routine first calculates the sizes of the current els and allocated
scsi sgl lists, and then goes through all sgls to updates the physical
XRIs assigned due to port function reset. During port initialization, the
current els and allocated scsi sgl lists are 0s.

Return codes
0 - successful (for now, it always returns 0)

.. _`lpfc_sli4_scsi_sgl_update`:

lpfc_sli4_scsi_sgl_update
=========================

.. c:function:: int lpfc_sli4_scsi_sgl_update(struct lpfc_hba *phba)

    update xri-sgl sizing and mapping

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_scsi_sgl_update.description`:

Description
-----------

This routine first calculates the sizes of the current els and allocated
scsi sgl lists, and then goes through all sgls to updates the physical
XRIs assigned due to port function reset. During port initialization, the
current els and allocated scsi sgl lists are 0s.

Return codes
0 - successful (for now, it always returns 0)

.. _`lpfc_sli4_nvme_sgl_update`:

lpfc_sli4_nvme_sgl_update
=========================

.. c:function:: int lpfc_sli4_nvme_sgl_update(struct lpfc_hba *phba)

    update xri-sgl sizing and mapping

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_nvme_sgl_update.description`:

Description
-----------

This routine first calculates the sizes of the current els and allocated
scsi sgl lists, and then goes through all sgls to updates the physical
XRIs assigned due to port function reset. During port initialization, the
current els and allocated scsi sgl lists are 0s.

Return codes
0 - successful (for now, it always returns 0)

.. _`lpfc_create_port`:

lpfc_create_port
================

.. c:function:: struct lpfc_vport *lpfc_create_port(struct lpfc_hba *phba, int instance, struct device *dev)

    Create an FC port

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param instance:
        a unique integer ID to this FC port.
    :type instance: int

    :param dev:
        pointer to the device data structure.
    :type dev: struct device \*

.. _`lpfc_create_port.description`:

Description
-----------

This routine creates a FC port for the upper layer protocol. The FC port
can be created on top of either a physical port or a virtual port provided
by the HBA. This routine also allocates a SCSI host data structure (shost)
and associates the FC port created before adding the shost into the SCSI
layer.

Return codes
\ ``vport``\  - pointer to the virtual N_Port data structure.
NULL - port create failed.

.. _`destroy_port`:

destroy_port
============

.. c:function:: void destroy_port(struct lpfc_vport *vport)

    destroy an FC port

    :param vport:
        pointer to an lpfc virtual N_Port data structure.
    :type vport: struct lpfc_vport \*

.. _`destroy_port.description`:

Description
-----------

This routine destroys a FC port from the upper layer protocol. All the
resources associated with the port are released.

.. _`lpfc_get_instance`:

lpfc_get_instance
=================

.. c:function:: int lpfc_get_instance( void)

    Get a unique integer ID

    :param void:
        no arguments
    :type void: 

.. _`lpfc_get_instance.description`:

Description
-----------

This routine allocates a unique integer ID from lpfc_hba_index pool. It
uses the kernel idr facility to perform the task.

.. _`lpfc_get_instance.return-codes`:

Return codes
------------

instance - a unique integer ID allocated as the new instance.
-1 - lpfc get instance failed.

.. _`lpfc_scan_finished`:

lpfc_scan_finished
==================

.. c:function:: int lpfc_scan_finished(struct Scsi_Host *shost, unsigned long time)

    method for SCSI layer to detect whether scan is done

    :param shost:
        pointer to SCSI host data structure.
    :type shost: struct Scsi_Host \*

    :param time:
        elapsed time of the scan in jiffies.
    :type time: unsigned long

.. _`lpfc_scan_finished.description`:

Description
-----------

This routine is called by the SCSI layer with a SCSI host to determine
whether the scan host is finished.

.. _`lpfc_scan_finished.note`:

Note
----

there is no scan_start function as adapter initialization will have
asynchronously kicked off the link initialization.

Return codes
0 - SCSI host scan is not over yet.
1 - SCSI host scan is over.

.. _`lpfc_host_attrib_init`:

lpfc_host_attrib_init
=====================

.. c:function:: void lpfc_host_attrib_init(struct Scsi_Host *shost)

    Initialize SCSI host attributes on a FC port

    :param shost:
        pointer to SCSI host data structure.
    :type shost: struct Scsi_Host \*

.. _`lpfc_host_attrib_init.description`:

Description
-----------

This routine initializes a given SCSI host attributes on a FC port. The
SCSI host can be either on top of a physical port or a virtual port.

.. _`lpfc_stop_port_s3`:

lpfc_stop_port_s3
=================

.. c:function:: void lpfc_stop_port_s3(struct lpfc_hba *phba)

    Stop SLI3 device port

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_stop_port_s3.description`:

Description
-----------

This routine is invoked to stop an SLI3 device port, it stops the device
from generating interrupts and stops the device driver's timers for the
device.

.. _`lpfc_stop_port_s4`:

lpfc_stop_port_s4
=================

.. c:function:: void lpfc_stop_port_s4(struct lpfc_hba *phba)

    Stop SLI4 device port

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_stop_port_s4.description`:

Description
-----------

This routine is invoked to stop an SLI4 device port, it stops the device
from generating interrupts and stops the device driver's timers for the
device.

.. _`lpfc_stop_port`:

lpfc_stop_port
==============

.. c:function:: void lpfc_stop_port(struct lpfc_hba *phba)

    Wrapper function for stopping hba port

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_stop_port.description`:

Description
-----------

This routine wraps the actual SLI3 or SLI4 hba stop port routine from
the API jump table function pointer from the lpfc_hba struct.

.. _`lpfc_fcf_redisc_wait_start_timer`:

lpfc_fcf_redisc_wait_start_timer
================================

.. c:function:: void lpfc_fcf_redisc_wait_start_timer(struct lpfc_hba *phba)

    Start fcf rediscover wait timer

    :param phba:
        Pointer to hba for which this call is being executed.
    :type phba: struct lpfc_hba \*

.. _`lpfc_fcf_redisc_wait_start_timer.description`:

Description
-----------

This routine starts the timer waiting for the FCF rediscovery to complete.

.. _`lpfc_sli4_fcf_redisc_wait_tmo`:

lpfc_sli4_fcf_redisc_wait_tmo
=============================

.. c:function:: void lpfc_sli4_fcf_redisc_wait_tmo(struct timer_list *t)

    FCF table rediscover wait timeout

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`lpfc_sli4_fcf_redisc_wait_tmo.description`:

Description
-----------

This routine is invoked when waiting for FCF table rediscover has been
timed out. If new FCF record(s) has (have) been discovered during the
wait period, a new FCF event shall be added to the FCOE async event
list, and then worker thread shall be waked up for processing from the
worker thread context.

.. _`lpfc_sli4_parse_latt_fault`:

lpfc_sli4_parse_latt_fault
==========================

.. c:function:: void lpfc_sli4_parse_latt_fault(struct lpfc_hba *phba, struct lpfc_acqe_link *acqe_link)

    Parse sli4 link-attention link fault code

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_link:
        pointer to the async link completion queue entry.
    :type acqe_link: struct lpfc_acqe_link \*

.. _`lpfc_sli4_parse_latt_fault.description`:

Description
-----------

This routine is to parse the SLI4 link-attention link fault code.

.. _`lpfc_sli4_parse_latt_type`:

lpfc_sli4_parse_latt_type
=========================

.. c:function:: uint8_t lpfc_sli4_parse_latt_type(struct lpfc_hba *phba, struct lpfc_acqe_link *acqe_link)

    Parse sli4 link attention type

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_link:
        pointer to the async link completion queue entry.
    :type acqe_link: struct lpfc_acqe_link \*

.. _`lpfc_sli4_parse_latt_type.description`:

Description
-----------

This routine is to parse the SLI4 link attention type and translate it
into the base driver's link attention type coding.

.. _`lpfc_sli4_parse_latt_type.return`:

Return
------

Link attention type in terms of base driver's coding.

.. _`lpfc_sli_port_speed_get`:

lpfc_sli_port_speed_get
=======================

.. c:function:: uint32_t lpfc_sli_port_speed_get(struct lpfc_hba *phba)

    Get sli3 link speed code to link speed

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_port_speed_get.description`:

Description
-----------

This routine is to get an SLI3 FC port's link speed in Mbps.

.. _`lpfc_sli_port_speed_get.return`:

Return
------

link speed in terms of Mbps.

.. _`lpfc_sli4_port_speed_parse`:

lpfc_sli4_port_speed_parse
==========================

.. c:function:: uint32_t lpfc_sli4_port_speed_parse(struct lpfc_hba *phba, uint32_t evt_code, uint8_t speed_code)

    Parse async evt link speed code to link speed

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param evt_code:
        asynchronous event code.
    :type evt_code: uint32_t

    :param speed_code:
        asynchronous event link speed code.
    :type speed_code: uint8_t

.. _`lpfc_sli4_port_speed_parse.description`:

Description
-----------

This routine is to parse the giving SLI4 async event link speed code into
value of Mbps for the link speed.

.. _`lpfc_sli4_port_speed_parse.return`:

Return
------

link speed in terms of Mbps.

.. _`lpfc_sli4_async_link_evt`:

lpfc_sli4_async_link_evt
========================

.. c:function:: void lpfc_sli4_async_link_evt(struct lpfc_hba *phba, struct lpfc_acqe_link *acqe_link)

    Process the asynchronous FCoE link event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_link:
        pointer to the async link completion queue entry.
    :type acqe_link: struct lpfc_acqe_link \*

.. _`lpfc_sli4_async_link_evt.description`:

Description
-----------

This routine is to handle the SLI4 asynchronous FCoE link event.

.. _`lpfc_sli4_async_fc_evt`:

lpfc_sli4_async_fc_evt
======================

.. c:function:: void lpfc_sli4_async_fc_evt(struct lpfc_hba *phba, struct lpfc_acqe_fc_la *acqe_fc)

    Process the asynchronous FC link event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_fc:
        pointer to the async fc completion queue entry.
    :type acqe_fc: struct lpfc_acqe_fc_la \*

.. _`lpfc_sli4_async_fc_evt.description`:

Description
-----------

This routine is to handle the SLI4 asynchronous FC event. It will simply log
that the event was received and then issue a read_topology mailbox command so
that the rest of the driver will treat it the same as SLI3.

.. _`lpfc_sli4_async_sli_evt`:

lpfc_sli4_async_sli_evt
=======================

.. c:function:: void lpfc_sli4_async_sli_evt(struct lpfc_hba *phba, struct lpfc_acqe_sli *acqe_sli)

    Process the asynchronous SLI link event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_sli:
        *undescribed*
    :type acqe_sli: struct lpfc_acqe_sli \*

.. _`lpfc_sli4_async_sli_evt.description`:

Description
-----------

This routine is to handle the SLI4 asynchronous SLI events.

.. _`lpfc_sli4_perform_vport_cvl`:

lpfc_sli4_perform_vport_cvl
===========================

.. c:function:: struct lpfc_nodelist *lpfc_sli4_perform_vport_cvl(struct lpfc_vport *vport)

    Perform clear virtual link on a vport

    :param vport:
        pointer to vport data structure.
    :type vport: struct lpfc_vport \*

.. _`lpfc_sli4_perform_vport_cvl.description`:

Description
-----------

This routine is to perform Clear Virtual Link (CVL) on a vport in
response to a CVL event.

Return the pointer to the ndlp with the vport if successful, otherwise
return NULL.

.. _`lpfc_sli4_perform_all_vport_cvl`:

lpfc_sli4_perform_all_vport_cvl
===============================

.. c:function:: void lpfc_sli4_perform_all_vport_cvl(struct lpfc_hba *phba)

    Perform clear virtual link on all vports

    :param phba:
        *undescribed*
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_perform_all_vport_cvl.description`:

Description
-----------

This routine is to perform Clear Virtual Link (CVL) on all vports in
response to a FCF dead event.

.. _`lpfc_sli4_async_fip_evt`:

lpfc_sli4_async_fip_evt
=======================

.. c:function:: void lpfc_sli4_async_fip_evt(struct lpfc_hba *phba, struct lpfc_acqe_fip *acqe_fip)

    Process the asynchronous FCoE FIP event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_fip:
        *undescribed*
    :type acqe_fip: struct lpfc_acqe_fip \*

.. _`lpfc_sli4_async_fip_evt.description`:

Description
-----------

This routine is to handle the SLI4 asynchronous fcoe event.

.. _`lpfc_sli4_async_dcbx_evt`:

lpfc_sli4_async_dcbx_evt
========================

.. c:function:: void lpfc_sli4_async_dcbx_evt(struct lpfc_hba *phba, struct lpfc_acqe_dcbx *acqe_dcbx)

    Process the asynchronous dcbx event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_dcbx:
        *undescribed*
    :type acqe_dcbx: struct lpfc_acqe_dcbx \*

.. _`lpfc_sli4_async_dcbx_evt.description`:

Description
-----------

This routine is to handle the SLI4 asynchronous dcbx event.

.. _`lpfc_sli4_async_grp5_evt`:

lpfc_sli4_async_grp5_evt
========================

.. c:function:: void lpfc_sli4_async_grp5_evt(struct lpfc_hba *phba, struct lpfc_acqe_grp5 *acqe_grp5)

    Process the asynchronous group5 event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param acqe_grp5:
        *undescribed*
    :type acqe_grp5: struct lpfc_acqe_grp5 \*

.. _`lpfc_sli4_async_grp5_evt.description`:

Description
-----------

This routine is to handle the SLI4 asynchronous grp5 event. A grp5 event
is an asynchronous notified of a logical link speed change.  The Port
reports the logical link speed in units of 10Mbps.

.. _`lpfc_sli4_async_event_proc`:

lpfc_sli4_async_event_proc
==========================

.. c:function:: void lpfc_sli4_async_event_proc(struct lpfc_hba *phba)

    Process all the pending asynchronous event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_async_event_proc.description`:

Description
-----------

This routine is invoked by the worker thread to process all the pending
SLI4 asynchronous events.

.. _`lpfc_sli4_fcf_redisc_event_proc`:

lpfc_sli4_fcf_redisc_event_proc
===============================

.. c:function:: void lpfc_sli4_fcf_redisc_event_proc(struct lpfc_hba *phba)

    Process fcf table rediscovery event

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_fcf_redisc_event_proc.description`:

Description
-----------

This routine is invoked by the worker thread to process FCF table
rediscovery pending completion event.

.. _`lpfc_api_table_setup`:

lpfc_api_table_setup
====================

.. c:function:: int lpfc_api_table_setup(struct lpfc_hba *phba, uint8_t dev_grp)

    Set up per hba pci-device group func api jump table

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param dev_grp:
        The HBA PCI-Device group number.
    :type dev_grp: uint8_t

.. _`lpfc_api_table_setup.description`:

Description
-----------

This routine is invoked to set up the per HBA PCI-Device group function
API jump table entries.

.. _`lpfc_api_table_setup.return`:

Return
------

0 if success, otherwise -ENODEV

.. _`lpfc_log_intr_mode`:

lpfc_log_intr_mode
==================

.. c:function:: void lpfc_log_intr_mode(struct lpfc_hba *phba, uint32_t intr_mode)

    Log the active interrupt mode

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param intr_mode:
        active interrupt mode adopted.
    :type intr_mode: uint32_t

.. _`lpfc_log_intr_mode.description`:

Description
-----------

This routine it invoked to log the currently used active interrupt mode
to the device.

.. _`lpfc_enable_pci_dev`:

lpfc_enable_pci_dev
===================

.. c:function:: int lpfc_enable_pci_dev(struct lpfc_hba *phba)

    Enable a generic PCI device.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_enable_pci_dev.description`:

Description
-----------

This routine is invoked to enable the PCI device that is common to all
PCI devices.

Return codes
0 - successful
other values - error

.. _`lpfc_disable_pci_dev`:

lpfc_disable_pci_dev
====================

.. c:function:: void lpfc_disable_pci_dev(struct lpfc_hba *phba)

    Disable a generic PCI device.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_disable_pci_dev.description`:

Description
-----------

This routine is invoked to disable the PCI device that is common to all
PCI devices.

.. _`lpfc_reset_hba`:

lpfc_reset_hba
==============

.. c:function:: void lpfc_reset_hba(struct lpfc_hba *phba)

    Reset a hba

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_reset_hba.description`:

Description
-----------

This routine is invoked to reset a hba device. It brings the HBA
offline, performs a board restart, and then brings the board back
online. The lpfc_offline calls lpfc_sli_hba_down which will clean up
on outstanding mailbox commands.

.. _`lpfc_sli_sriov_nr_virtfn_get`:

lpfc_sli_sriov_nr_virtfn_get
============================

.. c:function:: uint16_t lpfc_sli_sriov_nr_virtfn_get(struct lpfc_hba *phba)

    Get the number of sr-iov virtual functions

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_sriov_nr_virtfn_get.description`:

Description
-----------

This function enables the PCI SR-IOV virtual functions to a physical
function. It invokes the PCI SR-IOV api with the \ ``nr_vfn``\  provided to
enable the number of virtual functions to the physical function. As
not all devices support SR-IOV, the return code from the \ :c:func:`pci_enable_sriov`\ 
API call does not considered as an error condition for most of the device.

.. _`lpfc_sli_probe_sriov_nr_virtfn`:

lpfc_sli_probe_sriov_nr_virtfn
==============================

.. c:function:: int lpfc_sli_probe_sriov_nr_virtfn(struct lpfc_hba *phba, int nr_vfn)

    Enable a number of sr-iov virtual functions

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param nr_vfn:
        number of virtual functions to be enabled.
    :type nr_vfn: int

.. _`lpfc_sli_probe_sriov_nr_virtfn.description`:

Description
-----------

This function enables the PCI SR-IOV virtual functions to a physical
function. It invokes the PCI SR-IOV api with the \ ``nr_vfn``\  provided to
enable the number of virtual functions to the physical function. As
not all devices support SR-IOV, the return code from the \ :c:func:`pci_enable_sriov`\ 
API call does not considered as an error condition for most of the device.

.. _`lpfc_setup_driver_resource_phase1`:

lpfc_setup_driver_resource_phase1
=================================

.. c:function:: int lpfc_setup_driver_resource_phase1(struct lpfc_hba *phba)

    Phase1 etup driver internal resources.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_setup_driver_resource_phase1.description`:

Description
-----------

This routine is invoked to set up the driver internal resources before the
device specific resource setup to support the HBA device it attached to.

Return codes
0 - successful
other values - error

.. _`lpfc_sli_driver_resource_setup`:

lpfc_sli_driver_resource_setup
==============================

.. c:function:: int lpfc_sli_driver_resource_setup(struct lpfc_hba *phba)

    Setup driver internal resources for SLI3 dev

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_driver_resource_setup.description`:

Description
-----------

This routine is invoked to set up the driver internal resources specific to
support the SLI-3 HBA device it attached to.

Return codes
0 - successful
other values - error

.. _`lpfc_sli_driver_resource_unset`:

lpfc_sli_driver_resource_unset
==============================

.. c:function:: void lpfc_sli_driver_resource_unset(struct lpfc_hba *phba)

    Unset drvr internal resources for SLI3 dev

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_driver_resource_unset.description`:

Description
-----------

This routine is invoked to unset the driver internal resources set up
specific for supporting the SLI-3 HBA device it attached to.

.. _`lpfc_sli4_driver_resource_setup`:

lpfc_sli4_driver_resource_setup
===============================

.. c:function:: int lpfc_sli4_driver_resource_setup(struct lpfc_hba *phba)

    Setup drvr internal resources for SLI4 dev

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_driver_resource_setup.description`:

Description
-----------

This routine is invoked to set up the driver internal resources specific to
support the SLI-4 HBA device it attached to.

Return codes
0 - successful
other values - error

.. _`lpfc_sli4_driver_resource_unset`:

lpfc_sli4_driver_resource_unset
===============================

.. c:function:: void lpfc_sli4_driver_resource_unset(struct lpfc_hba *phba)

    Unset drvr internal resources for SLI4 dev

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_driver_resource_unset.description`:

Description
-----------

This routine is invoked to unset the driver internal resources set up
specific for supporting the SLI-4 HBA device it attached to.

.. _`lpfc_init_api_table_setup`:

lpfc_init_api_table_setup
=========================

.. c:function:: int lpfc_init_api_table_setup(struct lpfc_hba *phba, uint8_t dev_grp)

    Set up init api function jump table

    :param phba:
        The hba struct for which this call is being executed.
    :type phba: struct lpfc_hba \*

    :param dev_grp:
        The HBA PCI-Device group number.
    :type dev_grp: uint8_t

.. _`lpfc_init_api_table_setup.description`:

Description
-----------

This routine sets up the device INIT interface API function jump table
in \ ``phba``\  struct.

.. _`lpfc_init_api_table_setup.return`:

Return
------

0 - success, -ENODEV - failure.

.. _`lpfc_setup_driver_resource_phase2`:

lpfc_setup_driver_resource_phase2
=================================

.. c:function:: int lpfc_setup_driver_resource_phase2(struct lpfc_hba *phba)

    Phase2 setup driver internal resources.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_setup_driver_resource_phase2.description`:

Description
-----------

This routine is invoked to set up the driver internal resources after the
device specific resource setup to support the HBA device it attached to.

Return codes
0 - successful
other values - error

.. _`lpfc_unset_driver_resource_phase2`:

lpfc_unset_driver_resource_phase2
=================================

.. c:function:: void lpfc_unset_driver_resource_phase2(struct lpfc_hba *phba)

    Phase2 unset driver internal resources.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_unset_driver_resource_phase2.description`:

Description
-----------

This routine is invoked to unset the driver internal resources set up after
the device specific resource setup for supporting the HBA device it
attached to.

.. _`lpfc_free_iocb_list`:

lpfc_free_iocb_list
===================

.. c:function:: void lpfc_free_iocb_list(struct lpfc_hba *phba)

    Free iocb list.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_free_iocb_list.description`:

Description
-----------

This routine is invoked to free the driver's IOCB list and memory.

.. _`lpfc_init_iocb_list`:

lpfc_init_iocb_list
===================

.. c:function:: int lpfc_init_iocb_list(struct lpfc_hba *phba, int iocb_count)

    Allocate and initialize iocb list.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param iocb_count:
        *undescribed*
    :type iocb_count: int

.. _`lpfc_init_iocb_list.description`:

Description
-----------

This routine is invoked to allocate and initizlize the driver's IOCB
list and set up the IOCB tag array accordingly.

Return codes
0 - successful
other values - error

.. _`lpfc_free_sgl_list`:

lpfc_free_sgl_list
==================

.. c:function:: void lpfc_free_sgl_list(struct lpfc_hba *phba, struct list_head *sglq_list)

    Free a given sgl list.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param sglq_list:
        pointer to the head of sgl list.
    :type sglq_list: struct list_head \*

.. _`lpfc_free_sgl_list.description`:

Description
-----------

This routine is invoked to free a give sgl list and memory.

.. _`lpfc_free_els_sgl_list`:

lpfc_free_els_sgl_list
======================

.. c:function:: void lpfc_free_els_sgl_list(struct lpfc_hba *phba)

    Free els sgl list.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_free_els_sgl_list.description`:

Description
-----------

This routine is invoked to free the driver's els sgl list and memory.

.. _`lpfc_free_nvmet_sgl_list`:

lpfc_free_nvmet_sgl_list
========================

.. c:function:: void lpfc_free_nvmet_sgl_list(struct lpfc_hba *phba)

    Free nvmet sgl list.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_free_nvmet_sgl_list.description`:

Description
-----------

This routine is invoked to free the driver's nvmet sgl list and memory.

.. _`lpfc_init_active_sgl_array`:

lpfc_init_active_sgl_array
==========================

.. c:function:: int lpfc_init_active_sgl_array(struct lpfc_hba *phba)

    Allocate the buf to track active ELS XRIs.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_init_active_sgl_array.description`:

Description
-----------

This routine is invoked to allocate the driver's active sgl memory.
This array will hold the sglq_entry's for active IOs.

.. _`lpfc_free_active_sgl`:

lpfc_free_active_sgl
====================

.. c:function:: void lpfc_free_active_sgl(struct lpfc_hba *phba)

    Free the buf that tracks active ELS XRIs.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_free_active_sgl.description`:

Description
-----------

This routine is invoked to walk through the array of active sglq entries
and free all of the resources.
This is just a place holder for now.

.. _`lpfc_init_sgl_list`:

lpfc_init_sgl_list
==================

.. c:function:: void lpfc_init_sgl_list(struct lpfc_hba *phba)

    Allocate and initialize sgl list.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_init_sgl_list.description`:

Description
-----------

This routine is invoked to allocate and initizlize the driver's sgl
list and set up the sgl xritag tag array accordingly.

.. _`lpfc_sli4_init_rpi_hdrs`:

lpfc_sli4_init_rpi_hdrs
=======================

.. c:function:: int lpfc_sli4_init_rpi_hdrs(struct lpfc_hba *phba)

    Post the rpi header memory region to the port

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_init_rpi_hdrs.description`:

Description
-----------

This routine is invoked to post rpi header templates to the
port for those SLI4 ports that do not support extents.  This routine
posts a PAGE_SIZE memory region to the port to hold up to
PAGE_SIZE modulo 64 rpi context headers.  This is an initialization routine
and should be called only when interrupts are disabled.

Return codes
0 - successful
-ERROR - otherwise.

.. _`lpfc_sli4_create_rpi_hdr`:

lpfc_sli4_create_rpi_hdr
========================

.. c:function:: struct lpfc_rpi_hdr *lpfc_sli4_create_rpi_hdr(struct lpfc_hba *phba)

    Allocate an rpi header memory region

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_create_rpi_hdr.description`:

Description
-----------

This routine is invoked to allocate a single 4KB memory region to
support rpis and stores them in the phba.  This single region
provides support for up to 64 rpis.  The region is used globally
by the device.

.. _`lpfc_sli4_create_rpi_hdr.return`:

Return
------

A valid rpi hdr on success.
A NULL pointer on any failure.

.. _`lpfc_sli4_remove_rpi_hdrs`:

lpfc_sli4_remove_rpi_hdrs
=========================

.. c:function:: void lpfc_sli4_remove_rpi_hdrs(struct lpfc_hba *phba)

    Remove all rpi header memory regions

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_remove_rpi_hdrs.description`:

Description
-----------

This routine is invoked to remove all memory resources allocated
to support rpis for SLI4 ports not supporting extents. This routine
presumes the caller has released all rpis consumed by fabric or port
logins and is prepared to have the header pages removed.

.. _`lpfc_hba_alloc`:

lpfc_hba_alloc
==============

.. c:function:: struct lpfc_hba *lpfc_hba_alloc(struct pci_dev *pdev)

    Allocate driver hba data structure for a device.

    :param pdev:
        pointer to pci device data structure.
    :type pdev: struct pci_dev \*

.. _`lpfc_hba_alloc.description`:

Description
-----------

This routine is invoked to allocate the driver hba data structure for an
HBA device. If the allocation is successful, the phba reference to the
PCI device data structure is set.

Return codes
pointer to \ ``phba``\  - successful
NULL - error

.. _`lpfc_hba_free`:

lpfc_hba_free
=============

.. c:function:: void lpfc_hba_free(struct lpfc_hba *phba)

    Free driver hba data structure with a device.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_hba_free.description`:

Description
-----------

This routine is invoked to free the driver hba data structure with an
HBA device.

.. _`lpfc_create_shost`:

lpfc_create_shost
=================

.. c:function:: int lpfc_create_shost(struct lpfc_hba *phba)

    Create hba physical port with associated scsi host.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_create_shost.description`:

Description
-----------

This routine is invoked to create HBA physical port and associate a SCSI
host with it.

Return codes
0 - successful
other values - error

.. _`lpfc_destroy_shost`:

lpfc_destroy_shost
==================

.. c:function:: void lpfc_destroy_shost(struct lpfc_hba *phba)

    Destroy hba physical port with associated scsi host.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_destroy_shost.description`:

Description
-----------

This routine is invoked to destroy HBA physical port and the associated
SCSI host.

.. _`lpfc_setup_bg`:

lpfc_setup_bg
=============

.. c:function:: void lpfc_setup_bg(struct lpfc_hba *phba, struct Scsi_Host *shost)

    Setup Block guard structures and debug areas.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param shost:
        the shost to be used to detect Block guard settings.
    :type shost: struct Scsi_Host \*

.. _`lpfc_setup_bg.description`:

Description
-----------

This routine sets up the local Block guard protocol settings for \ ``shost``\ .
This routine also allocates memory for debugging bg buffers.

.. _`lpfc_post_init_setup`:

lpfc_post_init_setup
====================

.. c:function:: void lpfc_post_init_setup(struct lpfc_hba *phba)

    Perform necessary device post initialization setup.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_post_init_setup.description`:

Description
-----------

This routine is invoked to perform all the necessary post initialization
setup for the device.

.. _`lpfc_sli_pci_mem_setup`:

lpfc_sli_pci_mem_setup
======================

.. c:function:: int lpfc_sli_pci_mem_setup(struct lpfc_hba *phba)

    Setup SLI3 HBA PCI memory space.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_pci_mem_setup.description`:

Description
-----------

This routine is invoked to set up the PCI device memory space for device
with SLI-3 interface spec.

Return codes
0 - successful
other values - error

.. _`lpfc_sli_pci_mem_unset`:

lpfc_sli_pci_mem_unset
======================

.. c:function:: void lpfc_sli_pci_mem_unset(struct lpfc_hba *phba)

    Unset SLI3 HBA PCI memory space.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_pci_mem_unset.description`:

Description
-----------

This routine is invoked to unset the PCI device memory space for device
with SLI-3 interface spec.

.. _`lpfc_sli4_post_status_check`:

lpfc_sli4_post_status_check
===========================

.. c:function:: int lpfc_sli4_post_status_check(struct lpfc_hba *phba)

    Wait for SLI4 POST done and check status

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_post_status_check.description`:

Description
-----------

This routine is invoked to wait for SLI4 device Power On Self Test (POST)
done and check status.

Return 0 if successful, otherwise -ENODEV.

.. _`lpfc_sli4_bar0_register_memmap`:

lpfc_sli4_bar0_register_memmap
==============================

.. c:function:: void lpfc_sli4_bar0_register_memmap(struct lpfc_hba *phba, uint32_t if_type)

    Set up SLI4 BAR0 register memory map.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param if_type:
        The SLI4 interface type getting configured.
    :type if_type: uint32_t

.. _`lpfc_sli4_bar0_register_memmap.description`:

Description
-----------

This routine is invoked to set up SLI4 BAR0 PCI config space register
memory map.

.. _`lpfc_sli4_bar1_register_memmap`:

lpfc_sli4_bar1_register_memmap
==============================

.. c:function:: void lpfc_sli4_bar1_register_memmap(struct lpfc_hba *phba, uint32_t if_type)

    Set up SLI4 BAR1 register memory map.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param if_type:
        *undescribed*
    :type if_type: uint32_t

.. _`lpfc_sli4_bar1_register_memmap.description`:

Description
-----------

This routine is invoked to set up SLI4 BAR1 register memory map.

.. _`lpfc_sli4_bar2_register_memmap`:

lpfc_sli4_bar2_register_memmap
==============================

.. c:function:: int lpfc_sli4_bar2_register_memmap(struct lpfc_hba *phba, uint32_t vf)

    Set up SLI4 BAR2 register memory map.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param vf:
        virtual function number
    :type vf: uint32_t

.. _`lpfc_sli4_bar2_register_memmap.description`:

Description
-----------

This routine is invoked to set up SLI4 BAR2 doorbell register memory map
based on the given viftual function number, \ ``vf``\ .

Return 0 if successful, otherwise -ENODEV.

.. _`lpfc_create_bootstrap_mbox`:

lpfc_create_bootstrap_mbox
==========================

.. c:function:: int lpfc_create_bootstrap_mbox(struct lpfc_hba *phba)

    Create the bootstrap mailbox

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_create_bootstrap_mbox.description`:

Description
-----------

This routine is invoked to create the bootstrap mailbox
region consistent with the SLI-4 interface spec.  This
routine allocates all memory necessary to communicate
mailbox commands to the port and sets up all alignment
needs.  No locks are expected to be held when calling
this routine.

Return codes
0 - successful
-ENOMEM - could not allocated memory.

.. _`lpfc_destroy_bootstrap_mbox`:

lpfc_destroy_bootstrap_mbox
===========================

.. c:function:: void lpfc_destroy_bootstrap_mbox(struct lpfc_hba *phba)

    Destroy all bootstrap mailbox resources

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_destroy_bootstrap_mbox.description`:

Description
-----------

This routine is invoked to teardown the bootstrap mailbox
region and release all host resources. This routine requires
the caller to ensure all mailbox commands recovered, no
additional mailbox comands are sent, and interrupts are disabled
before calling this routine.

.. _`lpfc_sli4_read_config`:

lpfc_sli4_read_config
=====================

.. c:function:: int lpfc_sli4_read_config(struct lpfc_hba *phba)

    Get the config parameters.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_read_config.description`:

Description
-----------

This routine is invoked to read the configuration parameters from the HBA.
The configuration parameters are used to set the base and maximum values
for RPI's XRI's VPI's VFI's and FCFIs. These values also affect the resource
allocation for the port.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_setup_endian_order`:

lpfc_setup_endian_order
=======================

.. c:function:: int lpfc_setup_endian_order(struct lpfc_hba *phba)

    Write endian order to an SLI4 if_type 0 port.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_setup_endian_order.description`:

Description
-----------

This routine is invoked to setup the port-side endian order when
the port if_type is 0.  This routine has no function for other
if_types.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_queue_verify`:

lpfc_sli4_queue_verify
======================

.. c:function:: int lpfc_sli4_queue_verify(struct lpfc_hba *phba)

    Verify and update EQ counts

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_queue_verify.description`:

Description
-----------

This routine is invoked to check the user settable queue counts for EQs.
After this routine is called the counts will be set to valid values that
adhere to the constraints of the system's interrupt vectors and the port's
queue resources.

Return codes
0 - successful
-ENOMEM - No available memory

.. _`lpfc_sli4_queue_create`:

lpfc_sli4_queue_create
======================

.. c:function:: int lpfc_sli4_queue_create(struct lpfc_hba *phba)

    Create all the SLI4 queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_queue_create.description`:

Description
-----------

This routine is invoked to allocate all the SLI4 queues for the FCoE HBA
operation. For each SLI4 queue type, the parameters such as queue entry
count (queue depth) shall be taken from the module parameter. For now,
we just use some constant number as place holder.

Return codes
0 - successful
-ENOMEM - No availble memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_queue_destroy`:

lpfc_sli4_queue_destroy
=======================

.. c:function:: void lpfc_sli4_queue_destroy(struct lpfc_hba *phba)

    Destroy all the SLI4 queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_queue_destroy.description`:

Description
-----------

This routine is invoked to release all the SLI4 queues with the FCoE HBA
operation.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_queue_setup`:

lpfc_sli4_queue_setup
=====================

.. c:function:: int lpfc_sli4_queue_setup(struct lpfc_hba *phba)

    Set up all the SLI4 queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_queue_setup.description`:

Description
-----------

This routine is invoked to set up all the SLI4 queues for the FCoE HBA
operation.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_queue_unset`:

lpfc_sli4_queue_unset
=====================

.. c:function:: void lpfc_sli4_queue_unset(struct lpfc_hba *phba)

    Unset all the SLI4 queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_queue_unset.description`:

Description
-----------

This routine is invoked to unset all the SLI4 queues with the FCoE HBA
operation.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_cq_event_pool_create`:

lpfc_sli4_cq_event_pool_create
==============================

.. c:function:: int lpfc_sli4_cq_event_pool_create(struct lpfc_hba *phba)

    Create completion-queue event free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_cq_event_pool_create.description`:

Description
-----------

This routine is invoked to allocate and set up a pool of completion queue
events. The body of the completion queue event is a completion queue entry
CQE. For now, this pool is used for the interrupt service routine to queue

.. _`lpfc_sli4_cq_event_pool_create.the-following-hba-completion-queue-events-for-the-worker-thread-to-process`:

the following HBA completion queue events for the worker thread to process
--------------------------------------------------------------------------

- Mailbox asynchronous events
- Receive queue completion unsolicited events
Later, this can be used for all the slow-path events.

Return codes
0 - successful
-ENOMEM - No available memory

.. _`lpfc_sli4_cq_event_pool_destroy`:

lpfc_sli4_cq_event_pool_destroy
===============================

.. c:function:: void lpfc_sli4_cq_event_pool_destroy(struct lpfc_hba *phba)

    Free completion-queue event free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_cq_event_pool_destroy.description`:

Description
-----------

This routine is invoked to free the pool of completion queue events at
driver unload time. Note that, it is the responsibility of the driver
cleanup routine to free all the outstanding completion-queue events
allocated from this pool back into the pool before invoking this routine
to destroy the pool.

.. _`__lpfc_sli4_cq_event_alloc`:

\__lpfc_sli4_cq_event_alloc
===========================

.. c:function:: struct lpfc_cq_event *__lpfc_sli4_cq_event_alloc(struct lpfc_hba *phba)

    Allocate a completion-queue event from free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`__lpfc_sli4_cq_event_alloc.description`:

Description
-----------

This routine is the lock free version of the API invoked to allocate a
completion-queue event from the free pool.

.. _`__lpfc_sli4_cq_event_alloc.return`:

Return
------

Pointer to the newly allocated completion-queue event if successful
NULL otherwise.

.. _`lpfc_sli4_cq_event_alloc`:

lpfc_sli4_cq_event_alloc
========================

.. c:function:: struct lpfc_cq_event *lpfc_sli4_cq_event_alloc(struct lpfc_hba *phba)

    Allocate a completion-queue event from free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_cq_event_alloc.description`:

Description
-----------

This routine is the lock version of the API invoked to allocate a
completion-queue event from the free pool.

.. _`lpfc_sli4_cq_event_alloc.return`:

Return
------

Pointer to the newly allocated completion-queue event if successful
NULL otherwise.

.. _`__lpfc_sli4_cq_event_release`:

\__lpfc_sli4_cq_event_release
=============================

.. c:function:: void __lpfc_sli4_cq_event_release(struct lpfc_hba *phba, struct lpfc_cq_event *cq_event)

    Release a completion-queue event to free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param cq_event:
        pointer to the completion queue event to be freed.
    :type cq_event: struct lpfc_cq_event \*

.. _`__lpfc_sli4_cq_event_release.description`:

Description
-----------

This routine is the lock free version of the API invoked to release a
completion-queue event back into the free pool.

.. _`lpfc_sli4_cq_event_release`:

lpfc_sli4_cq_event_release
==========================

.. c:function:: void lpfc_sli4_cq_event_release(struct lpfc_hba *phba, struct lpfc_cq_event *cq_event)

    Release a completion-queue event to free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param cq_event:
        pointer to the completion queue event to be freed.
    :type cq_event: struct lpfc_cq_event \*

.. _`lpfc_sli4_cq_event_release.description`:

Description
-----------

This routine is the lock version of the API invoked to release a
completion-queue event back into the free pool.

.. _`lpfc_sli4_cq_event_release_all`:

lpfc_sli4_cq_event_release_all
==============================

.. c:function:: void lpfc_sli4_cq_event_release_all(struct lpfc_hba *phba)

    Release all cq events to the free pool

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_cq_event_release_all.description`:

Description
-----------

This routine is to free all the pending completion-queue events to the
back into the free pool for device reset.

.. _`lpfc_pci_function_reset`:

lpfc_pci_function_reset
=======================

.. c:function:: int lpfc_pci_function_reset(struct lpfc_hba *phba)

    Reset pci function.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_pci_function_reset.description`:

Description
-----------

This routine is invoked to request a PCI function reset. It will destroys
all resources assigned to the PCI function which originates this request.

Return codes
0 - successful
-ENOMEM - No available memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_sli4_pci_mem_setup`:

lpfc_sli4_pci_mem_setup
=======================

.. c:function:: int lpfc_sli4_pci_mem_setup(struct lpfc_hba *phba)

    Setup SLI4 HBA PCI memory space.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_pci_mem_setup.description`:

Description
-----------

This routine is invoked to set up the PCI device memory space for device
with SLI-4 interface spec.

Return codes
0 - successful
other values - error

.. _`lpfc_sli4_pci_mem_unset`:

lpfc_sli4_pci_mem_unset
=======================

.. c:function:: void lpfc_sli4_pci_mem_unset(struct lpfc_hba *phba)

    Unset SLI4 HBA PCI memory space.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_pci_mem_unset.description`:

Description
-----------

This routine is invoked to unset the PCI device memory space for device
with SLI-4 interface spec.

.. _`lpfc_sli_enable_msix`:

lpfc_sli_enable_msix
====================

.. c:function:: int lpfc_sli_enable_msix(struct lpfc_hba *phba)

    Enable MSI-X interrupt mode on SLI-3 device

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_enable_msix.description`:

Description
-----------

This routine is invoked to enable the MSI-X interrupt vectors to device
with SLI-3 interface specs.

Return codes
0 - successful
other values - error

.. _`lpfc_sli_enable_msi`:

lpfc_sli_enable_msi
===================

.. c:function:: int lpfc_sli_enable_msi(struct lpfc_hba *phba)

    Enable MSI interrupt mode on SLI-3 device.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_enable_msi.description`:

Description
-----------

This routine is invoked to enable the MSI interrupt mode to device with
SLI-3 interface spec. The kernel function \ :c:func:`pci_enable_msi`\  is called to
enable the MSI vector. The device driver is responsible for calling the
\ :c:func:`request_irq`\  to register MSI vector with a interrupt the handler, which
is done in this function.

Return codes
0 - successful
other values - error

.. _`lpfc_sli_enable_intr`:

lpfc_sli_enable_intr
====================

.. c:function:: uint32_t lpfc_sli_enable_intr(struct lpfc_hba *phba, uint32_t cfg_mode)

    Enable device interrupt to SLI-3 device.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param cfg_mode:
        *undescribed*
    :type cfg_mode: uint32_t

.. _`lpfc_sli_enable_intr.description`:

Description
-----------

This routine is invoked to enable device interrupt and associate driver's
interrupt handler(s) to interrupt vector(s) to device with SLI-3 interface
spec. Depends on the interrupt mode configured to the driver, the driver
will try to fallback from the configured interrupt mode to an interrupt
mode which is supported by the platform, kernel, and device in the order
of:
MSI-X -> MSI -> IRQ.

Return codes
0 - successful
other values - error

.. _`lpfc_sli_disable_intr`:

lpfc_sli_disable_intr
=====================

.. c:function:: void lpfc_sli_disable_intr(struct lpfc_hba *phba)

    Disable device interrupt to SLI-3 device.

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_disable_intr.description`:

Description
-----------

This routine is invoked to disable device interrupt and disassociate the
driver's interrupt handler(s) from interrupt vector(s) to device with
SLI-3 interface spec. Depending on the interrupt mode, the driver will
release the interrupt vector(s) for the message signaled interrupt.

.. _`lpfc_cpu_affinity_check`:

lpfc_cpu_affinity_check
=======================

.. c:function:: void lpfc_cpu_affinity_check(struct lpfc_hba *phba, int vectors)

    Check vector CPU affinity mappings

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param vectors:
        number of msix vectors allocated.
    :type vectors: int

.. _`lpfc_cpu_affinity_check.description`:

Description
-----------

The routine will figure out the CPU affinity assignment for every
MSI-X vector allocated for the HBA.  The hba_eq_hdl will be updated
with a pointer to the CPU mask that defines ALL the CPUs this vector
can be associated with. If the vector can be unquely associated with
a single CPU, that CPU will be recorded in hba_eq_hdl[index].cpu.
In addition, the CPU to IO channel mapping will be calculated
and the phba->sli4_hba.cpu_map array will reflect this.

.. _`lpfc_sli4_enable_msix`:

lpfc_sli4_enable_msix
=====================

.. c:function:: int lpfc_sli4_enable_msix(struct lpfc_hba *phba)

    Enable MSI-X interrupt mode to SLI-4 device

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_enable_msix.description`:

Description
-----------

This routine is invoked to enable the MSI-X interrupt vectors to device
with SLI-4 interface spec.

Return codes
0 - successful
other values - error

.. _`lpfc_sli4_enable_msi`:

lpfc_sli4_enable_msi
====================

.. c:function:: int lpfc_sli4_enable_msi(struct lpfc_hba *phba)

    Enable MSI interrupt mode to SLI-4 device

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_enable_msi.description`:

Description
-----------

This routine is invoked to enable the MSI interrupt mode to device with
SLI-4 interface spec. The kernel function \ :c:func:`pci_enable_msi`\  is called
to enable the MSI vector. The device driver is responsible for calling
the \ :c:func:`request_irq`\  to register MSI vector with a interrupt the handler,
which is done in this function.

Return codes
0 - successful
other values - error

.. _`lpfc_sli4_enable_intr`:

lpfc_sli4_enable_intr
=====================

.. c:function:: uint32_t lpfc_sli4_enable_intr(struct lpfc_hba *phba, uint32_t cfg_mode)

    Enable device interrupt to SLI-4 device

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param cfg_mode:
        *undescribed*
    :type cfg_mode: uint32_t

.. _`lpfc_sli4_enable_intr.description`:

Description
-----------

This routine is invoked to enable device interrupt and associate driver's
interrupt handler(s) to interrupt vector(s) to device with SLI-4
interface spec. Depends on the interrupt mode configured to the driver,
the driver will try to fallback from the configured interrupt mode to an
interrupt mode which is supported by the platform, kernel, and device in

.. _`lpfc_sli4_enable_intr.the-order-of`:

the order of
------------

MSI-X -> MSI -> IRQ.

Return codes
0 - successful
other values - error

.. _`lpfc_sli4_disable_intr`:

lpfc_sli4_disable_intr
======================

.. c:function:: void lpfc_sli4_disable_intr(struct lpfc_hba *phba)

    Disable device interrupt to SLI-4 device

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_disable_intr.description`:

Description
-----------

This routine is invoked to disable device interrupt and disassociate
the driver's interrupt handler(s) from interrupt vector(s) to device
with SLI-4 interface spec. Depending on the interrupt mode, the driver
will release the interrupt vector(s) for the message signaled interrupt.

.. _`lpfc_unset_hba`:

lpfc_unset_hba
==============

.. c:function:: void lpfc_unset_hba(struct lpfc_hba *phba)

    Unset SLI3 hba device initialization

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_unset_hba.description`:

Description
-----------

This routine is invoked to unset the HBA device initialization steps to
a device with SLI-3 interface spec.

.. _`lpfc_sli4_xri_exchange_busy_wait`:

lpfc_sli4_xri_exchange_busy_wait
================================

.. c:function:: void lpfc_sli4_xri_exchange_busy_wait(struct lpfc_hba *phba)

    Wait for device XRI exchange busy

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_xri_exchange_busy_wait.description`:

Description
-----------

This function is called in the SLI4 code path to wait for completion
of device's XRIs exchange busy. It will check the XRI exchange busy
on outstanding FCP and ELS I/Os every 10ms for up to 10 seconds; after
that, it will check the XRI exchange busy on outstanding FCP and ELS
I/Os every 30 seconds, log error message, and wait forever. Only when
all XRI exchange busy complete, the driver unload shall proceed with
invoking the function reset ioctl mailbox command to the CNA and the
the rest of the driver unload resource release.

.. _`lpfc_sli4_hba_unset`:

lpfc_sli4_hba_unset
===================

.. c:function:: void lpfc_sli4_hba_unset(struct lpfc_hba *phba)

    Unset the fcoe hba

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_hba_unset.description`:

Description
-----------

This function is called in the SLI4 code path to reset the HBA's FCoE
function. The caller is not required to hold any lock. This routine
issues PCI function reset mailbox command to reset the FCoE function.
At the end of the function, it calls lpfc_hba_down_post function to
free any pending commands.

.. _`lpfc_get_sli4_parameters`:

lpfc_get_sli4_parameters
========================

.. c:function:: int lpfc_get_sli4_parameters(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Get the SLI4 Config PARAMETERS.

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param mboxq:
        Pointer to the mailboxq memory for the mailbox command response.
    :type mboxq: LPFC_MBOXQ_t \*

.. _`lpfc_get_sli4_parameters.description`:

Description
-----------

This function is called in the SLI4 code path to read the port's
sli4 capabilities.

This function may be be called from any context that can block-wait
for the completion.  The expectation is that this routine is called
typically from probe_one or from the online routine.

.. _`lpfc_pci_probe_one_s3`:

lpfc_pci_probe_one_s3
=====================

.. c:function:: int lpfc_pci_probe_one_s3(struct pci_dev *pdev, const struct pci_device_id *pid)

    PCI probe func to reg SLI-3 device to PCI subsystem.

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

    :param pid:
        pointer to PCI device identifier
    :type pid: const struct pci_device_id \*

.. _`lpfc_pci_probe_one_s3.description`:

Description
-----------

This routine is to be called to attach a device with SLI-3 interface spec
to the PCI subsystem. When an Emulex HBA with SLI-3 interface spec is
presented on PCI bus, the kernel PCI subsystem looks at PCI device-specific
information of the device and driver to see if the driver state that it can
support this kind of device. If the match is successful, the driver core
invokes this routine. If this routine determines it can claim the HBA, it
does all the initialization that it needs to do to handle the HBA properly.

Return code
0 - driver can claim the device
negative value - driver can not claim the device

.. _`lpfc_pci_remove_one_s3`:

lpfc_pci_remove_one_s3
======================

.. c:function:: void lpfc_pci_remove_one_s3(struct pci_dev *pdev)

    PCI func to unreg SLI-3 device from PCI subsystem.

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_pci_remove_one_s3.description`:

Description
-----------

This routine is to be called to disattach a device with SLI-3 interface
spec from PCI subsystem. When an Emulex HBA with SLI-3 interface spec is
removed from PCI bus, it performs all the necessary cleanup for the HBA
device to be removed from the PCI subsystem properly.

.. _`lpfc_pci_suspend_one_s3`:

lpfc_pci_suspend_one_s3
=======================

.. c:function:: int lpfc_pci_suspend_one_s3(struct pci_dev *pdev, pm_message_t msg)

    PCI func to suspend SLI-3 device for power mgmnt

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

    :param msg:
        power management message
    :type msg: pm_message_t

.. _`lpfc_pci_suspend_one_s3.description`:

Description
-----------

This routine is to be called from the kernel's PCI subsystem to support
system Power Management (PM) to device with SLI-3 interface spec. When
PM invokes this method, it quiesces the device by stopping the driver's
worker thread for the device, turning off device's interrupt and DMA,
and bring the device offline. Note that as the driver implements the
minimum PM requirements to a power-aware driver's PM support for the
suspend/resume -- all the possible PM messages (SUSPEND, HIBERNATE, FREEZE)
to the \ :c:func:`suspend`\  method call will be treated as SUSPEND and the driver will
fully reinitialize its device during \ :c:func:`resume`\  method call, the driver will
set device to PCI_D3hot state in PCI config space instead of setting it
according to the \ ``msg``\  provided by the PM.

Return code
0 - driver suspended the device
Error otherwise

.. _`lpfc_pci_resume_one_s3`:

lpfc_pci_resume_one_s3
======================

.. c:function:: int lpfc_pci_resume_one_s3(struct pci_dev *pdev)

    PCI func to resume SLI-3 device for power mgmnt

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_pci_resume_one_s3.description`:

Description
-----------

This routine is to be called from the kernel's PCI subsystem to support
system Power Management (PM) to device with SLI-3 interface spec. When PM
invokes this method, it restores the device's PCI config space state and
fully reinitializes the device and brings it online. Note that as the
driver implements the minimum PM requirements to a power-aware driver's
PM for suspend/resume -- all the possible PM messages (SUSPEND, HIBERNATE,
FREEZE) to the \ :c:func:`suspend`\  method call will be treated as SUSPEND and the
driver will fully reinitialize its device during \ :c:func:`resume`\  method call,
the device will be set to PCI_D0 directly in PCI config space before
restoring the state.

Return code
0 - driver suspended the device
Error otherwise

.. _`lpfc_sli_prep_dev_for_recover`:

lpfc_sli_prep_dev_for_recover
=============================

.. c:function:: void lpfc_sli_prep_dev_for_recover(struct lpfc_hba *phba)

    Prepare SLI3 device for pci slot recover

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_prep_dev_for_recover.description`:

Description
-----------

This routine is called to prepare the SLI3 device for PCI slot recover. It
aborts all the outstanding SCSI I/Os to the pci device.

.. _`lpfc_sli_prep_dev_for_reset`:

lpfc_sli_prep_dev_for_reset
===========================

.. c:function:: void lpfc_sli_prep_dev_for_reset(struct lpfc_hba *phba)

    Prepare SLI3 device for pci slot reset

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_prep_dev_for_reset.description`:

Description
-----------

This routine is called to prepare the SLI3 device for PCI slot reset. It
disables the device interrupt and pci device, and aborts the internal FCP
pending I/Os.

.. _`lpfc_sli_prep_dev_for_perm_failure`:

lpfc_sli_prep_dev_for_perm_failure
==================================

.. c:function:: void lpfc_sli_prep_dev_for_perm_failure(struct lpfc_hba *phba)

    Prepare SLI3 dev for pci slot disable

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli_prep_dev_for_perm_failure.description`:

Description
-----------

This routine is called to prepare the SLI3 device for PCI slot permanently
disabling. It blocks the SCSI transport layer traffic and flushes the FCP
pending I/Os.

.. _`lpfc_io_error_detected_s3`:

lpfc_io_error_detected_s3
=========================

.. c:function:: pci_ers_result_t lpfc_io_error_detected_s3(struct pci_dev *pdev, pci_channel_state_t state)

    Method for handling SLI-3 device PCI I/O error

    :param pdev:
        pointer to PCI device.
    :type pdev: struct pci_dev \*

    :param state:
        the current PCI connection state.
    :type state: pci_channel_state_t

.. _`lpfc_io_error_detected_s3.description`:

Description
-----------

This routine is called from the PCI subsystem for I/O error handling to
device with SLI-3 interface spec. This function is called by the PCI
subsystem after a PCI bus error affecting this device has been detected.
When this function is invoked, it will need to stop all the I/Os and
interrupt(s) to the device. Once that is done, it will return
PCI_ERS_RESULT_NEED_RESET for the PCI subsystem to perform proper recovery
as desired.

Return codes
PCI_ERS_RESULT_CAN_RECOVER - can be recovered with reset_link
PCI_ERS_RESULT_NEED_RESET - need to reset before recovery
PCI_ERS_RESULT_DISCONNECT - device could not be recovered

.. _`lpfc_io_slot_reset_s3`:

lpfc_io_slot_reset_s3
=====================

.. c:function:: pci_ers_result_t lpfc_io_slot_reset_s3(struct pci_dev *pdev)

    Method for restarting PCI SLI-3 device from scratch.

    :param pdev:
        pointer to PCI device.
    :type pdev: struct pci_dev \*

.. _`lpfc_io_slot_reset_s3.description`:

Description
-----------

This routine is called from the PCI subsystem for error handling to
device with SLI-3 interface spec. This is called after PCI bus has been
reset to restart the PCI card from scratch, as if from a cold-boot.
During the PCI subsystem error recovery, after driver returns
PCI_ERS_RESULT_NEED_RESET, the PCI subsystem will perform proper error
recovery and then call this routine before calling the .resume method
to recover the device. This function will initialize the HBA device,
enable the interrupt, but it will just put the HBA to offline state
without passing any I/O traffic.

Return codes
PCI_ERS_RESULT_RECOVERED - the device has been recovered
PCI_ERS_RESULT_DISCONNECT - device could not be recovered

.. _`lpfc_io_resume_s3`:

lpfc_io_resume_s3
=================

.. c:function:: void lpfc_io_resume_s3(struct pci_dev *pdev)

    Method for resuming PCI I/O operation on SLI-3 device.

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_io_resume_s3.description`:

Description
-----------

This routine is called from the PCI subsystem for error handling to device
with SLI-3 interface spec. It is called when kernel error recovery tells
the lpfc driver that it is ok to resume normal PCI operation after PCI bus
error recovery. After this call, traffic can start to flow from this device
again.

.. _`lpfc_sli4_get_els_iocb_cnt`:

lpfc_sli4_get_els_iocb_cnt
==========================

.. c:function:: int lpfc_sli4_get_els_iocb_cnt(struct lpfc_hba *phba)

    Calculate the # of ELS IOCBs to reserve

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_get_els_iocb_cnt.description`:

Description
-----------

returns the number of ELS/CT IOCBs to reserve

.. _`lpfc_sli4_get_iocb_cnt`:

lpfc_sli4_get_iocb_cnt
======================

.. c:function:: int lpfc_sli4_get_iocb_cnt(struct lpfc_hba *phba)

    Calculate the # of total IOCBs to reserve

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_get_iocb_cnt.description`:

Description
-----------

returns the number of ELS/CT + NVMET IOCBs to reserve

.. _`lpfc_write_firmware`:

lpfc_write_firmware
===================

.. c:function:: void lpfc_write_firmware(const struct firmware *fw, void *context)

    attempt to write a firmware image to the port

    :param fw:
        pointer to firmware image returned from request_firmware.
    :type fw: const struct firmware \*

    :param context:
        *undescribed*
    :type context: void \*

.. _`lpfc_sli4_request_firmware_update`:

lpfc_sli4_request_firmware_update
=================================

.. c:function:: int lpfc_sli4_request_firmware_update(struct lpfc_hba *phba, uint8_t fw_upgrade)

    Request linux generic firmware upgrade

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

    :param fw_upgrade:
        *undescribed*
    :type fw_upgrade: uint8_t

.. _`lpfc_sli4_request_firmware_update.description`:

Description
-----------

This routine is called to perform Linux generic firmware upgrade on device
that supports such feature.

.. _`lpfc_pci_probe_one_s4`:

lpfc_pci_probe_one_s4
=====================

.. c:function:: int lpfc_pci_probe_one_s4(struct pci_dev *pdev, const struct pci_device_id *pid)

    PCI probe func to reg SLI-4 device to PCI subsys

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

    :param pid:
        pointer to PCI device identifier
    :type pid: const struct pci_device_id \*

.. _`lpfc_pci_probe_one_s4.description`:

Description
-----------

This routine is called from the kernel's PCI subsystem to device with
SLI-4 interface spec. When an Emulex HBA with SLI-4 interface spec is
presented on PCI bus, the kernel PCI subsystem looks at PCI device-specific
information of the device and driver to see if the driver state that it
can support this kind of device. If the match is successful, the driver
core invokes this routine. If this routine determines it can claim the HBA,
it does all the initialization that it needs to do to handle the HBA
properly.

Return code
0 - driver can claim the device
negative value - driver can not claim the device

.. _`lpfc_pci_remove_one_s4`:

lpfc_pci_remove_one_s4
======================

.. c:function:: void lpfc_pci_remove_one_s4(struct pci_dev *pdev)

    PCI func to unreg SLI-4 device from PCI subsystem

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_pci_remove_one_s4.description`:

Description
-----------

This routine is called from the kernel's PCI subsystem to device with
SLI-4 interface spec. When an Emulex HBA with SLI-4 interface spec is
removed from PCI bus, it performs all the necessary cleanup for the HBA
device to be removed from the PCI subsystem properly.

.. _`lpfc_pci_suspend_one_s4`:

lpfc_pci_suspend_one_s4
=======================

.. c:function:: int lpfc_pci_suspend_one_s4(struct pci_dev *pdev, pm_message_t msg)

    PCI func to suspend SLI-4 device for power mgmnt

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

    :param msg:
        power management message
    :type msg: pm_message_t

.. _`lpfc_pci_suspend_one_s4.description`:

Description
-----------

This routine is called from the kernel's PCI subsystem to support system
Power Management (PM) to device with SLI-4 interface spec. When PM invokes
this method, it quiesces the device by stopping the driver's worker
thread for the device, turning off device's interrupt and DMA, and bring
the device offline. Note that as the driver implements the minimum PM
requirements to a power-aware driver's PM support for suspend/resume -- all
the possible PM messages (SUSPEND, HIBERNATE, FREEZE) to the \ :c:func:`suspend`\ 
method call will be treated as SUSPEND and the driver will fully
reinitialize its device during \ :c:func:`resume`\  method call, the driver will set
device to PCI_D3hot state in PCI config space instead of setting it
according to the \ ``msg``\  provided by the PM.

Return code
0 - driver suspended the device
Error otherwise

.. _`lpfc_pci_resume_one_s4`:

lpfc_pci_resume_one_s4
======================

.. c:function:: int lpfc_pci_resume_one_s4(struct pci_dev *pdev)

    PCI func to resume SLI-4 device for power mgmnt

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_pci_resume_one_s4.description`:

Description
-----------

This routine is called from the kernel's PCI subsystem to support system
Power Management (PM) to device with SLI-4 interface spac. When PM invokes
this method, it restores the device's PCI config space state and fully
reinitializes the device and brings it online. Note that as the driver
implements the minimum PM requirements to a power-aware driver's PM for
suspend/resume -- all the possible PM messages (SUSPEND, HIBERNATE, FREEZE)
to the \ :c:func:`suspend`\  method call will be treated as SUSPEND and the driver
will fully reinitialize its device during \ :c:func:`resume`\  method call, the device
will be set to PCI_D0 directly in PCI config space before restoring the
state.

Return code
0 - driver suspended the device
Error otherwise

.. _`lpfc_sli4_prep_dev_for_recover`:

lpfc_sli4_prep_dev_for_recover
==============================

.. c:function:: void lpfc_sli4_prep_dev_for_recover(struct lpfc_hba *phba)

    Prepare SLI4 device for pci slot recover

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_prep_dev_for_recover.description`:

Description
-----------

This routine is called to prepare the SLI4 device for PCI slot recover. It
aborts all the outstanding SCSI I/Os to the pci device.

.. _`lpfc_sli4_prep_dev_for_reset`:

lpfc_sli4_prep_dev_for_reset
============================

.. c:function:: void lpfc_sli4_prep_dev_for_reset(struct lpfc_hba *phba)

    Prepare SLI4 device for pci slot reset

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_prep_dev_for_reset.description`:

Description
-----------

This routine is called to prepare the SLI4 device for PCI slot reset. It
disables the device interrupt and pci device, and aborts the internal FCP
pending I/Os.

.. _`lpfc_sli4_prep_dev_for_perm_failure`:

lpfc_sli4_prep_dev_for_perm_failure
===================================

.. c:function:: void lpfc_sli4_prep_dev_for_perm_failure(struct lpfc_hba *phba)

    Prepare SLI4 dev for pci slot disable

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_prep_dev_for_perm_failure.description`:

Description
-----------

This routine is called to prepare the SLI4 device for PCI slot permanently
disabling. It blocks the SCSI transport layer traffic and flushes the FCP
pending I/Os.

.. _`lpfc_io_error_detected_s4`:

lpfc_io_error_detected_s4
=========================

.. c:function:: pci_ers_result_t lpfc_io_error_detected_s4(struct pci_dev *pdev, pci_channel_state_t state)

    Method for handling PCI I/O error to SLI-4 device

    :param pdev:
        pointer to PCI device.
    :type pdev: struct pci_dev \*

    :param state:
        the current PCI connection state.
    :type state: pci_channel_state_t

.. _`lpfc_io_error_detected_s4.description`:

Description
-----------

This routine is called from the PCI subsystem for error handling to device
with SLI-4 interface spec. This function is called by the PCI subsystem
after a PCI bus error affecting this device has been detected. When this
function is invoked, it will need to stop all the I/Os and interrupt(s)
to the device. Once that is done, it will return PCI_ERS_RESULT_NEED_RESET
for the PCI subsystem to perform proper recovery as desired.

Return codes
PCI_ERS_RESULT_NEED_RESET - need to reset before recovery
PCI_ERS_RESULT_DISCONNECT - device could not be recovered

.. _`lpfc_io_slot_reset_s4`:

lpfc_io_slot_reset_s4
=====================

.. c:function:: pci_ers_result_t lpfc_io_slot_reset_s4(struct pci_dev *pdev)

    Method for restart PCI SLI-4 device from scratch

    :param pdev:
        pointer to PCI device.
    :type pdev: struct pci_dev \*

.. _`lpfc_io_slot_reset_s4.description`:

Description
-----------

This routine is called from the PCI subsystem for error handling to device
with SLI-4 interface spec. It is called after PCI bus has been reset to
restart the PCI card from scratch, as if from a cold-boot. During the
PCI subsystem error recovery, after the driver returns
PCI_ERS_RESULT_NEED_RESET, the PCI subsystem will perform proper error
recovery and then call this routine before calling the .resume method to
recover the device. This function will initialize the HBA device, enable
the interrupt, but it will just put the HBA to offline state without
passing any I/O traffic.

Return codes
PCI_ERS_RESULT_RECOVERED - the device has been recovered
PCI_ERS_RESULT_DISCONNECT - device could not be recovered

.. _`lpfc_io_resume_s4`:

lpfc_io_resume_s4
=================

.. c:function:: void lpfc_io_resume_s4(struct pci_dev *pdev)

    Method for resuming PCI I/O operation to SLI-4 device

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_io_resume_s4.description`:

Description
-----------

This routine is called from the PCI subsystem for error handling to device
with SLI-4 interface spec. It is called when kernel error recovery tells
the lpfc driver that it is ok to resume normal PCI operation after PCI bus
error recovery. After this call, traffic can start to flow from this device
again.

.. _`lpfc_pci_probe_one`:

lpfc_pci_probe_one
==================

.. c:function:: int lpfc_pci_probe_one(struct pci_dev *pdev, const struct pci_device_id *pid)

    lpfc PCI probe func to reg dev to PCI subsystem

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

    :param pid:
        pointer to PCI device identifier
    :type pid: const struct pci_device_id \*

.. _`lpfc_pci_probe_one.description`:

Description
-----------

This routine is to be registered to the kernel's PCI subsystem. When an
Emulex HBA device is presented on PCI bus, the kernel PCI subsystem looks
at PCI device-specific information of the device and driver to see if the
driver state that it can support this kind of device. If the match is
successful, the driver core invokes this routine. This routine dispatches
the action to the proper SLI-3 or SLI-4 device probing routine, which will
do all the initialization that it needs to do to handle the HBA device
properly.

Return code
0 - driver can claim the device
negative value - driver can not claim the device

.. _`lpfc_pci_remove_one`:

lpfc_pci_remove_one
===================

.. c:function:: void lpfc_pci_remove_one(struct pci_dev *pdev)

    lpfc PCI func to unreg dev from PCI subsystem

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_pci_remove_one.description`:

Description
-----------

This routine is to be registered to the kernel's PCI subsystem. When an
Emulex HBA is removed from PCI bus, the driver core invokes this routine.
This routine dispatches the action to the proper SLI-3 or SLI-4 device
remove routine, which will perform all the necessary cleanup for the
device to be removed from the PCI subsystem properly.

.. _`lpfc_pci_suspend_one`:

lpfc_pci_suspend_one
====================

.. c:function:: int lpfc_pci_suspend_one(struct pci_dev *pdev, pm_message_t msg)

    lpfc PCI func to suspend dev for power management

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

    :param msg:
        power management message
    :type msg: pm_message_t

.. _`lpfc_pci_suspend_one.description`:

Description
-----------

This routine is to be registered to the kernel's PCI subsystem to support
system Power Management (PM). When PM invokes this method, it dispatches
the action to the proper SLI-3 or SLI-4 device suspend routine, which will
suspend the device.

Return code
0 - driver suspended the device
Error otherwise

.. _`lpfc_pci_resume_one`:

lpfc_pci_resume_one
===================

.. c:function:: int lpfc_pci_resume_one(struct pci_dev *pdev)

    lpfc PCI func to resume dev for power management

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_pci_resume_one.description`:

Description
-----------

This routine is to be registered to the kernel's PCI subsystem to support
system Power Management (PM). When PM invokes this method, it dispatches
the action to the proper SLI-3 or SLI-4 device resume routine, which will
resume the device.

Return code
0 - driver suspended the device
Error otherwise

.. _`lpfc_io_error_detected`:

lpfc_io_error_detected
======================

.. c:function:: pci_ers_result_t lpfc_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    lpfc method for handling PCI I/O error

    :param pdev:
        pointer to PCI device.
    :type pdev: struct pci_dev \*

    :param state:
        the current PCI connection state.
    :type state: pci_channel_state_t

.. _`lpfc_io_error_detected.description`:

Description
-----------

This routine is registered to the PCI subsystem for error handling. This
function is called by the PCI subsystem after a PCI bus error affecting
this device has been detected. When this routine is invoked, it dispatches
the action to the proper SLI-3 or SLI-4 device error detected handling
routine, which will perform the proper error detected operation.

Return codes
PCI_ERS_RESULT_NEED_RESET - need to reset before recovery
PCI_ERS_RESULT_DISCONNECT - device could not be recovered

.. _`lpfc_io_slot_reset`:

lpfc_io_slot_reset
==================

.. c:function:: pci_ers_result_t lpfc_io_slot_reset(struct pci_dev *pdev)

    lpfc method for restart PCI dev from scratch

    :param pdev:
        pointer to PCI device.
    :type pdev: struct pci_dev \*

.. _`lpfc_io_slot_reset.description`:

Description
-----------

This routine is registered to the PCI subsystem for error handling. This
function is called after PCI bus has been reset to restart the PCI card
from scratch, as if from a cold-boot. When this routine is invoked, it
dispatches the action to the proper SLI-3 or SLI-4 device reset handling
routine, which will perform the proper device reset.

Return codes
PCI_ERS_RESULT_RECOVERED - the device has been recovered
PCI_ERS_RESULT_DISCONNECT - device could not be recovered

.. _`lpfc_io_resume`:

lpfc_io_resume
==============

.. c:function:: void lpfc_io_resume(struct pci_dev *pdev)

    lpfc method for resuming PCI I/O operation

    :param pdev:
        pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`lpfc_io_resume.description`:

Description
-----------

This routine is registered to the PCI subsystem for error handling. It
is called when kernel error recovery tells the lpfc driver that it is
OK to resume normal PCI operation after PCI bus error recovery. When
this routine is invoked, it dispatches the action to the proper SLI-3
or SLI-4 device io_resume routine, which will resume the device operation.

.. _`lpfc_sli4_oas_verify`:

lpfc_sli4_oas_verify
====================

.. c:function:: void lpfc_sli4_oas_verify(struct lpfc_hba *phba)

    Verify OAS is supported by this adapter

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_oas_verify.description`:

Description
-----------

This routine checks to see if OAS is supported for this adapter. If
supported, the configure Flash Optimized Fabric flag is set.  Otherwise,
the enable oas flag is cleared and the pool created for OAS device data
is destroyed.

.. _`lpfc_sli4_ras_init`:

lpfc_sli4_ras_init
==================

.. c:function:: void lpfc_sli4_ras_init(struct lpfc_hba *phba)

    Verify RAS-FW log is supported by this adapter

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_sli4_ras_init.description`:

Description
-----------

This routine checks to see if RAS is supported by the adapter. Check the
function through which RAS support enablement is to be done.

.. _`lpfc_fof_queue_setup`:

lpfc_fof_queue_setup
====================

.. c:function:: int lpfc_fof_queue_setup(struct lpfc_hba *phba)

    Set up all the fof queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_fof_queue_setup.description`:

Description
-----------

This routine is invoked to set up all the fof queues for the FC HBA
operation.

Return codes
0 - successful
-ENOMEM - No available memory

.. _`lpfc_fof_queue_create`:

lpfc_fof_queue_create
=====================

.. c:function:: int lpfc_fof_queue_create(struct lpfc_hba *phba)

    Create all the fof queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_fof_queue_create.description`:

Description
-----------

This routine is invoked to allocate all the fof queues for the FC HBA
operation. For each SLI4 queue type, the parameters such as queue entry
count (queue depth) shall be taken from the module parameter. For now,
we just use some constant number as place holder.

Return codes
0 - successful
-ENOMEM - No availble memory
-EIO - The mailbox failed to complete successfully.

.. _`lpfc_fof_queue_destroy`:

lpfc_fof_queue_destroy
======================

.. c:function:: int lpfc_fof_queue_destroy(struct lpfc_hba *phba)

    Destroy all the fof queues

    :param phba:
        pointer to lpfc hba data structure.
    :type phba: struct lpfc_hba \*

.. _`lpfc_fof_queue_destroy.description`:

Description
-----------

This routine is invoked to release all the SLI4 queues with the FC HBA
operation.

Return codes
0 - successful

.. _`lpfc_init`:

lpfc_init
=========

.. c:function:: int lpfc_init( void)

    lpfc module initialization routine

    :param void:
        no arguments
    :type void: 

.. _`lpfc_init.description`:

Description
-----------

This routine is to be invoked when the lpfc module is loaded into the
kernel. The special kernel macro \ :c:func:`module_init`\  is used to indicate the
role of this routine to the kernel as lpfc module entry point.

Return codes
0 - successful
-ENOMEM - FC attach transport failed
all others - failed

.. _`lpfc_exit`:

lpfc_exit
=========

.. c:function:: void __exit lpfc_exit( void)

    lpfc module removal routine

    :param void:
        no arguments
    :type void: 

.. _`lpfc_exit.description`:

Description
-----------

This routine is invoked when the lpfc module is removed from the kernel.
The special kernel macro \ :c:func:`module_exit`\  is used to indicate the role of
this routine to the kernel as lpfc module exit point.

.. This file was automatic generated / don't edit.


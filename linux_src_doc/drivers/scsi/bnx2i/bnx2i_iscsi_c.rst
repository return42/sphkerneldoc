.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2i/bnx2i_iscsi.c

.. _`bnx2i_get_write_cmd_bd_idx`:

bnx2i_get_write_cmd_bd_idx
==========================

.. c:function:: void bnx2i_get_write_cmd_bd_idx(struct bnx2i_cmd *cmd, u32 buf_off, u32 *start_bd_off, u32 *start_bd_idx)

    identifies various BD bookmarks

    :param cmd:
        iscsi cmd struct pointer
    :type cmd: struct bnx2i_cmd \*

    :param buf_off:
        absolute buffer offset
    :type buf_off: u32

    :param start_bd_off:
        u32 pointer to return the offset within the BD
        indicated by 'start_bd_idx' on which 'buf_off' falls
    :type start_bd_off: u32 \*

    :param start_bd_idx:
        index of the BD on which 'buf_off' falls
    :type start_bd_idx: u32 \*

.. _`bnx2i_get_write_cmd_bd_idx.description`:

Description
-----------

identifies & marks various bd info for scsi command's imm data,
unsolicited data and the first solicited data seq.

.. _`bnx2i_setup_write_cmd_bd_info`:

bnx2i_setup_write_cmd_bd_info
=============================

.. c:function:: void bnx2i_setup_write_cmd_bd_info(struct iscsi_task *task)

    sets up BD various information

    :param task:
        transport layer's cmd struct pointer
    :type task: struct iscsi_task \*

.. _`bnx2i_setup_write_cmd_bd_info.description`:

Description
-----------

identifies & marks various bd info for scsi command's immediate data,
unsolicited data and first solicited data seq which includes BD start
index & BD buf off. his function takes into account iscsi parameter such
as immediate data and unsolicited data is support on this connection.

.. _`bnx2i_map_scsi_sg`:

bnx2i_map_scsi_sg
=================

.. c:function:: int bnx2i_map_scsi_sg(struct bnx2i_hba *hba, struct bnx2i_cmd *cmd)

    maps IO buffer and prepares the BD table

    :param hba:
        adapter instance
    :type hba: struct bnx2i_hba \*

    :param cmd:
        iscsi cmd struct pointer
    :type cmd: struct bnx2i_cmd \*

.. _`bnx2i_map_scsi_sg.description`:

Description
-----------

map SG list

.. _`bnx2i_iscsi_map_sg_list`:

bnx2i_iscsi_map_sg_list
=======================

.. c:function:: void bnx2i_iscsi_map_sg_list(struct bnx2i_cmd *cmd)

    maps SG list

    :param cmd:
        iscsi cmd struct pointer
    :type cmd: struct bnx2i_cmd \*

.. _`bnx2i_iscsi_map_sg_list.description`:

Description
-----------

creates BD list table for the command

.. _`bnx2i_iscsi_unmap_sg_list`:

bnx2i_iscsi_unmap_sg_list
=========================

.. c:function:: void bnx2i_iscsi_unmap_sg_list(struct bnx2i_cmd *cmd)

    unmaps SG list

    :param cmd:
        iscsi cmd struct pointer
    :type cmd: struct bnx2i_cmd \*

.. _`bnx2i_iscsi_unmap_sg_list.description`:

Description
-----------

unmap IO buffers and invalidate the BD table

.. _`bnx2i_bind_conn_to_iscsi_cid`:

bnx2i_bind_conn_to_iscsi_cid
============================

.. c:function:: int bnx2i_bind_conn_to_iscsi_cid(struct bnx2i_hba *hba, struct bnx2i_conn *bnx2i_conn, u32 iscsi_cid)

    bind conn structure to 'iscsi_cid'

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param bnx2i_conn:
        *undescribed*
    :type bnx2i_conn: struct bnx2i_conn \*

    :param iscsi_cid:
        iscsi context ID, range 0 - (MAX_CONN - 1)
    :type iscsi_cid: u32

.. _`bnx2i_bind_conn_to_iscsi_cid.description`:

Description
-----------

update iscsi cid table entry with connection pointer. This enables
driver to quickly get hold of connection structure pointer in
completion/interrupt thread using iscsi context ID

.. _`bnx2i_get_conn_from_id`:

bnx2i_get_conn_from_id
======================

.. c:function:: struct bnx2i_conn *bnx2i_get_conn_from_id(struct bnx2i_hba *hba, u16 iscsi_cid)

    maps an iscsi cid to corresponding conn ptr

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param iscsi_cid:
        iscsi context ID, range 0 - (MAX_CONN - 1)
    :type iscsi_cid: u16

.. _`bnx2i_alloc_iscsi_cid`:

bnx2i_alloc_iscsi_cid
=====================

.. c:function:: u32 bnx2i_alloc_iscsi_cid(struct bnx2i_hba *hba)

    allocates a iscsi_cid from free pool

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_free_iscsi_cid`:

bnx2i_free_iscsi_cid
====================

.. c:function:: void bnx2i_free_iscsi_cid(struct bnx2i_hba *hba, u16 iscsi_cid)

    returns tcp port to free list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param iscsi_cid:
        iscsi context ID to free
    :type iscsi_cid: u16

.. _`bnx2i_setup_free_cid_que`:

bnx2i_setup_free_cid_que
========================

.. c:function:: int bnx2i_setup_free_cid_que(struct bnx2i_hba *hba)

    sets up free iscsi cid queue

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_setup_free_cid_que.description`:

Description
-----------

allocates memory for iscsi cid queue & 'cid - conn ptr' mapping table,
and initialize table attributes

.. _`bnx2i_release_free_cid_que`:

bnx2i_release_free_cid_que
==========================

.. c:function:: void bnx2i_release_free_cid_que(struct bnx2i_hba *hba)

    releases 'iscsi_cid' queue resources

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_alloc_ep`:

bnx2i_alloc_ep
==============

.. c:function:: struct iscsi_endpoint *bnx2i_alloc_ep(struct bnx2i_hba *hba)

    allocates ep structure from global pool

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_alloc_ep.description`:

Description
-----------

routine allocates a free endpoint structure from global pool and
a tcp port to be used for this connection.  Global resource lock,
'bnx2i_resc_lock' is held while accessing shared global data structures

.. _`bnx2i_free_ep`:

bnx2i_free_ep
=============

.. c:function:: void bnx2i_free_ep(struct iscsi_endpoint *ep)

    free endpoint

    :param ep:
        pointer to iscsi endpoint structure
    :type ep: struct iscsi_endpoint \*

.. _`bnx2i_alloc_bdt`:

bnx2i_alloc_bdt
===============

.. c:function:: int bnx2i_alloc_bdt(struct bnx2i_hba *hba, struct iscsi_session *session, struct bnx2i_cmd *cmd)

    allocates buffer descriptor (BD) table for the command

    :param hba:
        adapter instance pointer
    :type hba: struct bnx2i_hba \*

    :param session:
        iscsi session pointer
    :type session: struct iscsi_session \*

    :param cmd:
        iscsi command structure
    :type cmd: struct bnx2i_cmd \*

.. _`bnx2i_destroy_cmd_pool`:

bnx2i_destroy_cmd_pool
======================

.. c:function:: void bnx2i_destroy_cmd_pool(struct bnx2i_hba *hba, struct iscsi_session *session)

    destroys iscsi command pool and release BD table

    :param hba:
        adapter instance pointer
    :type hba: struct bnx2i_hba \*

    :param session:
        iscsi session pointer
    :type session: struct iscsi_session \*

.. _`bnx2i_setup_cmd_pool`:

bnx2i_setup_cmd_pool
====================

.. c:function:: int bnx2i_setup_cmd_pool(struct bnx2i_hba *hba, struct iscsi_session *session)

    sets up iscsi command pool for the session

    :param hba:
        adapter instance pointer
    :type hba: struct bnx2i_hba \*

    :param session:
        iscsi session pointer
    :type session: struct iscsi_session \*

.. _`bnx2i_setup_mp_bdt`:

bnx2i_setup_mp_bdt
==================

.. c:function:: int bnx2i_setup_mp_bdt(struct bnx2i_hba *hba)

    allocate BD table resources

    :param hba:
        pointer to adapter structure
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_setup_mp_bdt.description`:

Description
-----------

Allocate memory for dummy buffer and associated BD
table to be used by middle path (MP) requests

.. _`bnx2i_free_mp_bdt`:

bnx2i_free_mp_bdt
=================

.. c:function:: void bnx2i_free_mp_bdt(struct bnx2i_hba *hba)

    releases ITT back to free pool

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_free_mp_bdt.description`:

Description
-----------

free MP dummy buffer and associated BD table

.. _`bnx2i_drop_session`:

bnx2i_drop_session
==================

.. c:function:: void bnx2i_drop_session(struct iscsi_cls_session *cls_session)

    notifies iscsid of connection error.

    :param cls_session:
        *undescribed*
    :type cls_session: struct iscsi_cls_session \*

.. _`bnx2i_drop_session.description`:

Description
-----------

This notifies iscsid that there is a error, so it can initiate
recovery.

This relies on caller using the iscsi class iterator so the object
is refcounted and does not disapper from under us.

.. _`bnx2i_ep_destroy_list_add`:

bnx2i_ep_destroy_list_add
=========================

.. c:function:: int bnx2i_ep_destroy_list_add(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    add an entry to EP destroy list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        pointer to endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_destroy_list_add.description`:

Description
-----------

EP destroy queue manager

.. _`bnx2i_ep_destroy_list_del`:

bnx2i_ep_destroy_list_del
=========================

.. c:function:: int bnx2i_ep_destroy_list_del(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    add an entry to EP destroy list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        pointer to endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_destroy_list_del.description`:

Description
-----------

EP destroy queue manager

.. _`bnx2i_ep_ofld_list_add`:

bnx2i_ep_ofld_list_add
======================

.. c:function:: int bnx2i_ep_ofld_list_add(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    add an entry to ep offload pending list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        pointer to endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_ofld_list_add.description`:

Description
-----------

pending conn offload completion queue manager

.. _`bnx2i_ep_ofld_list_del`:

bnx2i_ep_ofld_list_del
======================

.. c:function:: int bnx2i_ep_ofld_list_del(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    add an entry to ep offload pending list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        pointer to endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_ofld_list_del.description`:

Description
-----------

pending conn offload completion queue manager

.. _`bnx2i_find_ep_in_ofld_list`:

bnx2i_find_ep_in_ofld_list
==========================

.. c:function:: struct bnx2i_endpoint *bnx2i_find_ep_in_ofld_list(struct bnx2i_hba *hba, u32 iscsi_cid)

    find iscsi_cid in pending list of endpoints

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param iscsi_cid:
        iscsi context ID to find
    :type iscsi_cid: u32

.. _`bnx2i_find_ep_in_destroy_list`:

bnx2i_find_ep_in_destroy_list
=============================

.. c:function:: struct bnx2i_endpoint *bnx2i_find_ep_in_destroy_list(struct bnx2i_hba *hba, u32 iscsi_cid)

    find iscsi_cid in destroy list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param iscsi_cid:
        iscsi context ID to find
    :type iscsi_cid: u32

.. _`bnx2i_ep_active_list_add`:

bnx2i_ep_active_list_add
========================

.. c:function:: void bnx2i_ep_active_list_add(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    add an entry to ep active list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        pointer to endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_active_list_add.description`:

Description
-----------

current active conn queue manager

.. _`bnx2i_ep_active_list_del`:

bnx2i_ep_active_list_del
========================

.. c:function:: void bnx2i_ep_active_list_del(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    deletes an entry to ep active list

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        pointer to endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_active_list_del.description`:

Description
-----------

current active conn queue manager

.. _`bnx2i_setup_host_queue_size`:

bnx2i_setup_host_queue_size
===========================

.. c:function:: void bnx2i_setup_host_queue_size(struct bnx2i_hba *hba, struct Scsi_Host *shost)

    assigns shost->can_queue param

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param shost:
        scsi host pointer
    :type shost: struct Scsi_Host \*

.. _`bnx2i_setup_host_queue_size.description`:

Description
-----------

Initializes 'can_queue' parameter based on how many outstanding commands
the device can handle. Each device 5708/5709/57710 has different
capabilities

.. _`bnx2i_alloc_hba`:

bnx2i_alloc_hba
===============

.. c:function:: struct bnx2i_hba *bnx2i_alloc_hba(struct cnic_dev *cnic)

    allocate and init adapter instance

    :param cnic:
        cnic device pointer
    :type cnic: struct cnic_dev \*

.. _`bnx2i_alloc_hba.description`:

Description
-----------

allocate & initialize adapter structure and call other
support routines to do per adapter initialization

.. _`bnx2i_free_hba`:

bnx2i_free_hba
==============

.. c:function:: void bnx2i_free_hba(struct bnx2i_hba *hba)

    releases hba structure and resources held by the adapter

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

.. _`bnx2i_free_hba.description`:

Description
-----------

free adapter structure and call various cleanup routines.

.. _`bnx2i_conn_free_login_resources`:

bnx2i_conn_free_login_resources
===============================

.. c:function:: void bnx2i_conn_free_login_resources(struct bnx2i_hba *hba, struct bnx2i_conn *bnx2i_conn)

    free DMA resources used for login process

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param bnx2i_conn:
        iscsi connection pointer
    :type bnx2i_conn: struct bnx2i_conn \*

.. _`bnx2i_conn_free_login_resources.description`:

Description
-----------

Login related resources, mostly BDT & payload DMA memory is freed

.. _`bnx2i_conn_alloc_login_resources`:

bnx2i_conn_alloc_login_resources
================================

.. c:function:: int bnx2i_conn_alloc_login_resources(struct bnx2i_hba *hba, struct bnx2i_conn *bnx2i_conn)

    alloc DMA resources for login/nop.

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param bnx2i_conn:
        iscsi connection pointer
    :type bnx2i_conn: struct bnx2i_conn \*

.. _`bnx2i_conn_alloc_login_resources.description`:

Description
-----------

Mgmt task DNA resources are allocated in this routine.

.. _`bnx2i_iscsi_prep_generic_pdu_bd`:

bnx2i_iscsi_prep_generic_pdu_bd
===============================

.. c:function:: void bnx2i_iscsi_prep_generic_pdu_bd(struct bnx2i_conn *bnx2i_conn)

    prepares BD table.

    :param bnx2i_conn:
        iscsi connection pointer
    :type bnx2i_conn: struct bnx2i_conn \*

.. _`bnx2i_iscsi_prep_generic_pdu_bd.description`:

Description
-----------

Allocates buffers and BD tables before shipping requests to cnic
for PDUs prepared by 'iscsid' daemon

.. _`bnx2i_iscsi_send_generic_request`:

bnx2i_iscsi_send_generic_request
================================

.. c:function:: int bnx2i_iscsi_send_generic_request(struct iscsi_task *task)

    called to send mgmt tasks.

    :param task:
        transport layer task pointer
    :type task: struct iscsi_task \*

.. _`bnx2i_iscsi_send_generic_request.description`:

Description
-----------

called to transmit PDUs prepared by the 'iscsid' daemon. iSCSI login,
Nop-out and Logout requests flow through this path.

.. _`bnx2i_cpy_scsi_cdb`:

bnx2i_cpy_scsi_cdb
==================

.. c:function:: void bnx2i_cpy_scsi_cdb(struct scsi_cmnd *sc, struct bnx2i_cmd *cmd)

    copies LUN & CDB fields in required format to sq wqe

    :param sc:
        SCSI-ML command pointer
    :type sc: struct scsi_cmnd \*

    :param cmd:
        iscsi cmd pointer
    :type cmd: struct bnx2i_cmd \*

.. _`bnx2i_mtask_xmit`:

bnx2i_mtask_xmit
================

.. c:function:: int bnx2i_mtask_xmit(struct iscsi_conn *conn, struct iscsi_task *task)

    transmit mtask to chip for further processing

    :param conn:
        transport layer conn structure pointer
    :type conn: struct iscsi_conn \*

    :param task:
        transport layer command structure pointer
    :type task: struct iscsi_task \*

.. _`bnx2i_task_xmit`:

bnx2i_task_xmit
===============

.. c:function:: int bnx2i_task_xmit(struct iscsi_task *task)

    transmit iscsi command to chip for further processing

    :param task:
        transport layer command structure pointer
    :type task: struct iscsi_task \*

.. _`bnx2i_task_xmit.description`:

Description
-----------

maps SG buffers and send request to chip/firmware in the form of SQ WQE

.. _`bnx2i_session_create`:

bnx2i_session_create
====================

.. c:function:: struct iscsi_cls_session *bnx2i_session_create(struct iscsi_endpoint *ep, uint16_t cmds_max, uint16_t qdepth, uint32_t initial_cmdsn)

    create a new iscsi session

    :param ep:
        *undescribed*
    :type ep: struct iscsi_endpoint \*

    :param cmds_max:
        max commands supported
    :type cmds_max: uint16_t

    :param qdepth:
        scsi queue depth to support
    :type qdepth: uint16_t

    :param initial_cmdsn:
        initial iscsi CMDSN to be used for this session
    :type initial_cmdsn: uint32_t

.. _`bnx2i_session_create.description`:

Description
-----------

Creates a new iSCSI session instance on given device.

.. _`bnx2i_session_destroy`:

bnx2i_session_destroy
=====================

.. c:function:: void bnx2i_session_destroy(struct iscsi_cls_session *cls_session)

    destroys iscsi session

    :param cls_session:
        pointer to iscsi cls session
    :type cls_session: struct iscsi_cls_session \*

.. _`bnx2i_session_destroy.description`:

Description
-----------

Destroys previously created iSCSI session instance and releases
all resources held by it

.. _`bnx2i_conn_create`:

bnx2i_conn_create
=================

.. c:function:: struct iscsi_cls_conn *bnx2i_conn_create(struct iscsi_cls_session *cls_session, uint32_t cid)

    create iscsi connection instance

    :param cls_session:
        pointer to iscsi cls session
    :type cls_session: struct iscsi_cls_session \*

    :param cid:
        iscsi cid as per rfc (not NX2's CID terminology)
    :type cid: uint32_t

.. _`bnx2i_conn_create.description`:

Description
-----------

Creates a new iSCSI connection instance for a given session

.. _`bnx2i_conn_bind`:

bnx2i_conn_bind
===============

.. c:function:: int bnx2i_conn_bind(struct iscsi_cls_session *cls_session, struct iscsi_cls_conn *cls_conn, uint64_t transport_fd, int is_leading)

    binds iscsi sess, conn and ep objects together

    :param cls_session:
        pointer to iscsi cls session
    :type cls_session: struct iscsi_cls_session \*

    :param cls_conn:
        pointer to iscsi cls conn
    :type cls_conn: struct iscsi_cls_conn \*

    :param transport_fd:
        64-bit EP handle
    :type transport_fd: uint64_t

    :param is_leading:
        leading connection on this session?
    :type is_leading: int

.. _`bnx2i_conn_bind.description`:

Description
-----------

Binds together iSCSI session instance, iSCSI connection instance
and the TCP connection. This routine returns error code if
TCP connection does not belong on the device iSCSI sess/conn
is bound

.. _`bnx2i_conn_destroy`:

bnx2i_conn_destroy
==================

.. c:function:: void bnx2i_conn_destroy(struct iscsi_cls_conn *cls_conn)

    destroy iscsi connection instance & release resources

    :param cls_conn:
        pointer to iscsi cls conn
    :type cls_conn: struct iscsi_cls_conn \*

.. _`bnx2i_conn_destroy.description`:

Description
-----------

Destroy an iSCSI connection instance and release memory resources held by
this connection

.. _`bnx2i_ep_get_param`:

bnx2i_ep_get_param
==================

.. c:function:: int bnx2i_ep_get_param(struct iscsi_endpoint *ep, enum iscsi_param param, char *buf)

    return iscsi ep parameter to caller

    :param ep:
        pointer to iscsi endpoint
    :type ep: struct iscsi_endpoint \*

    :param param:
        parameter type identifier
    :type param: enum iscsi_param

    :param buf:
        buffer pointer
    :type buf: char \*

.. _`bnx2i_ep_get_param.description`:

Description
-----------

returns iSCSI ep parameters

.. _`bnx2i_host_get_param`:

bnx2i_host_get_param
====================

.. c:function:: int bnx2i_host_get_param(struct Scsi_Host *shost, enum iscsi_host_param param, char *buf)

    returns host (adapter) related parameters

    :param shost:
        scsi host pointer
    :type shost: struct Scsi_Host \*

    :param param:
        parameter type identifier
    :type param: enum iscsi_host_param

    :param buf:
        buffer pointer
    :type buf: char \*

.. _`bnx2i_conn_start`:

bnx2i_conn_start
================

.. c:function:: int bnx2i_conn_start(struct iscsi_cls_conn *cls_conn)

    completes iscsi connection migration to FFP

    :param cls_conn:
        pointer to iscsi cls conn
    :type cls_conn: struct iscsi_cls_conn \*

.. _`bnx2i_conn_start.description`:

Description
-----------

last call in FFP migration to handover iscsi conn to the driver

.. _`bnx2i_conn_get_stats`:

bnx2i_conn_get_stats
====================

.. c:function:: void bnx2i_conn_get_stats(struct iscsi_cls_conn *cls_conn, struct iscsi_stats *stats)

    returns iSCSI stats

    :param cls_conn:
        pointer to iscsi cls conn
    :type cls_conn: struct iscsi_cls_conn \*

    :param stats:
        pointer to iscsi statistic struct
    :type stats: struct iscsi_stats \*

.. _`bnx2i_check_route`:

bnx2i_check_route
=================

.. c:function:: struct bnx2i_hba *bnx2i_check_route(struct sockaddr *dst_addr)

    checks if target IP route belongs to one of NX2 devices

    :param dst_addr:
        target IP address
    :type dst_addr: struct sockaddr \*

.. _`bnx2i_check_route.description`:

Description
-----------

check if route resolves to BNX2 device

.. _`bnx2i_tear_down_conn`:

bnx2i_tear_down_conn
====================

.. c:function:: int bnx2i_tear_down_conn(struct bnx2i_hba *hba, struct bnx2i_endpoint *ep)

    tear down iscsi/tcp connection and free resources

    :param hba:
        pointer to adapter instance
    :type hba: struct bnx2i_hba \*

    :param ep:
        endpoint (transport identifier) structure
    :type ep: struct bnx2i_endpoint \*

.. _`bnx2i_tear_down_conn.description`:

Description
-----------

destroys cm_sock structure and on chip iscsi context

.. _`bnx2i_ep_connect`:

bnx2i_ep_connect
================

.. c:function:: struct iscsi_endpoint *bnx2i_ep_connect(struct Scsi_Host *shost, struct sockaddr *dst_addr, int non_blocking)

    establish TCP connection to target portal

    :param shost:
        scsi host
    :type shost: struct Scsi_Host \*

    :param dst_addr:
        target IP address
    :type dst_addr: struct sockaddr \*

    :param non_blocking:
        blocking or non-blocking call
    :type non_blocking: int

.. _`bnx2i_ep_connect.description`:

Description
-----------

this routine initiates the TCP/IP connection by invoking Option-2 i/f
with l5_core and the CNIC. This is a multi-step process of resolving
route to target, create a iscsi connection context, handshaking with
CNIC module to create/initialize the socket struct and finally
sending down option-2 request to complete TCP 3-way handshake

.. _`bnx2i_ep_poll`:

bnx2i_ep_poll
=============

.. c:function:: int bnx2i_ep_poll(struct iscsi_endpoint *ep, int timeout_ms)

    polls for TCP connection establishement

    :param ep:
        TCP connection (endpoint) handle
    :type ep: struct iscsi_endpoint \*

    :param timeout_ms:
        timeout value in milli secs
    :type timeout_ms: int

.. _`bnx2i_ep_poll.description`:

Description
-----------

polls for TCP connect request to complete

.. _`bnx2i_ep_tcp_conn_active`:

bnx2i_ep_tcp_conn_active
========================

.. c:function:: int bnx2i_ep_tcp_conn_active(struct bnx2i_endpoint *bnx2i_ep)

    check EP state transition

    :param bnx2i_ep:
        *undescribed*
    :type bnx2i_ep: struct bnx2i_endpoint \*

.. _`bnx2i_ep_tcp_conn_active.description`:

Description
-----------

check if underlying TCP connection is active

.. _`bnx2i_ep_disconnect`:

bnx2i_ep_disconnect
===================

.. c:function:: void bnx2i_ep_disconnect(struct iscsi_endpoint *ep)

    executes TCP connection teardown process

    :param ep:
        TCP connection (iscsi endpoint) handle
    :type ep: struct iscsi_endpoint \*

.. _`bnx2i_ep_disconnect.description`:

Description
-----------

executes  TCP connection teardown process

.. _`bnx2i_nl_set_path`:

bnx2i_nl_set_path
=================

.. c:function:: int bnx2i_nl_set_path(struct Scsi_Host *shost, struct iscsi_path *params)

    ISCSI_UEVENT_PATH_UPDATE user message handler

    :param shost:
        *undescribed*
    :type shost: struct Scsi_Host \*

    :param params:
        *undescribed*
    :type params: struct iscsi_path \*

.. This file was automatic generated / don't edit.


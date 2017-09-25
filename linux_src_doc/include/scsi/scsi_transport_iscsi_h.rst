.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/scsi_transport_iscsi.h

.. _`iscsi_transport`:

struct iscsi_transport
======================

.. c:type:: struct iscsi_transport

    iSCSI Transport template

.. _`iscsi_transport.definition`:

Definition
----------

.. code-block:: c

    struct iscsi_transport {
        struct module *owner;
        char *name;
        unsigned int caps;
        struct iscsi_cls_session *(*create_session) (struct iscsi_endpoint *ep,uint16_t cmds_max, uint16_t qdepth, uint32_t sn);
        void (*destroy_session) (struct iscsi_cls_session *session);
        struct iscsi_cls_conn *(*create_conn) (struct iscsi_cls_session *sess, uint32_t cid);
        int (*bind_conn) (struct iscsi_cls_session *session,struct iscsi_cls_conn *cls_conn, uint64_t transport_eph, int is_leading);
        int (*start_conn) (struct iscsi_cls_conn *conn);
        void (*stop_conn) (struct iscsi_cls_conn *conn, int flag);
        void (*destroy_conn) (struct iscsi_cls_conn *conn);
        int (*set_param) (struct iscsi_cls_conn *conn, enum iscsi_param param, char *buf, int buflen);
        int (*get_ep_param) (struct iscsi_endpoint *ep, enum iscsi_param param, char *buf);
        int (*get_conn_param) (struct iscsi_cls_conn *conn, enum iscsi_param param, char *buf);
        int (*get_session_param) (struct iscsi_cls_session *session, enum iscsi_param param, char *buf);
        int (*get_host_param) (struct Scsi_Host *shost, enum iscsi_host_param param, char *buf);
        int (*set_host_param) (struct Scsi_Host *shost,enum iscsi_host_param param, char *buf, int buflen);
        int (*send_pdu) (struct iscsi_cls_conn *conn, struct iscsi_hdr *hdr, char *data, uint32_t data_size);
        void (*get_stats) (struct iscsi_cls_conn *conn, struct iscsi_stats *stats);
        int (*init_task) (struct iscsi_task *task);
        int (*xmit_task) (struct iscsi_task *task);
        void (*cleanup_task) (struct iscsi_task *task);
        int (*alloc_pdu) (struct iscsi_task *task, uint8_t opcode);
        int (*xmit_pdu) (struct iscsi_task *task);
        int (*init_pdu) (struct iscsi_task *task, unsigned int offset, unsigned int count);
        void (*parse_pdu_itt) (struct iscsi_conn *conn, itt_t itt, int *index, int *age);
        void (*session_recovery_timedout) (struct iscsi_cls_session *session);
        struct iscsi_endpoint *(*ep_connect) (struct Scsi_Host *shost,struct sockaddr *dst_addr, int non_blocking);
        int (*ep_poll) (struct iscsi_endpoint *ep, int timeout_ms);
        void (*ep_disconnect) (struct iscsi_endpoint *ep);
        int (*tgt_dscvr) (struct Scsi_Host *shost, enum iscsi_tgt_dscvr type, uint32_t enable, struct sockaddr *dst_addr);
        int (*set_path) (struct Scsi_Host *shost, struct iscsi_path *params);
        int (*set_iface_param) (struct Scsi_Host *shost, void *data, uint32_t len);
        int (*get_iface_param) (struct iscsi_iface *iface,enum iscsi_param_type param_type, int param, char *buf);
        umode_t (*attr_is_visible)(int param_type, int param);
        int (*bsg_request)(struct bsg_job *job);
        int (*send_ping) (struct Scsi_Host *shost, uint32_t iface_num,uint32_t iface_type, uint32_t payload_size, uint32_t pid, struct sockaddr *dst_addr);
        int (*get_chap) (struct Scsi_Host *shost, uint16_t chap_tbl_idx, uint32_t *num_entries, char *buf);
        int (*delete_chap) (struct Scsi_Host *shost, uint16_t chap_tbl_idx);
        int (*set_chap) (struct Scsi_Host *shost, void *data, int len);
        int (*get_flashnode_param) (struct iscsi_bus_flash_session *fnode_sess, int param, char *buf);
        int (*set_flashnode_param) (struct iscsi_bus_flash_session *fnode_sess,struct iscsi_bus_flash_conn *fnode_conn, void *data, int len);
        int (*new_flashnode) (struct Scsi_Host *shost, const char *buf, int len);
        int (*del_flashnode) (struct iscsi_bus_flash_session *fnode_sess);
        int (*login_flashnode) (struct iscsi_bus_flash_session *fnode_sess, struct iscsi_bus_flash_conn *fnode_conn);
        int (*logout_flashnode) (struct iscsi_bus_flash_session *fnode_sess, struct iscsi_bus_flash_conn *fnode_conn);
        int (*logout_flashnode_sid) (struct iscsi_cls_session *cls_sess);
        int (*get_host_stats) (struct Scsi_Host *shost, char *buf, int len);
        u8 (*check_protection)(struct iscsi_task *task, sector_t *sector);
    }

.. _`iscsi_transport.members`:

Members
-------

owner
    *undescribed*

name
    transport name

caps
    iSCSI Data-Path capabilities

create_session
    create new iSCSI session object

destroy_session
    destroy existing iSCSI session object

create_conn
    create new iSCSI connection

bind_conn
    associate this connection with existing iSCSI session
    and specified transport descriptor

start_conn
    set connection to be operational

stop_conn
    suspend/recover/terminate connection

destroy_conn
    destroy inactive iSCSI connection

set_param
    set iSCSI parameter. Return 0 on success, -ENODATA
    when param is not supported, and a -Exx value on other
    error.
    \ ``get_param``\            get iSCSI parameter. Must return number of bytes
    copied to buffer on success, -ENODATA when param
    is not supported, and a -Exx value on other error

get_ep_param
    *undescribed*

get_conn_param
    *undescribed*

get_session_param
    *undescribed*

get_host_param
    *undescribed*

set_host_param
    *undescribed*

send_pdu
    send iSCSI PDU, Login, Logout, NOP-Out, Reject, Text.

get_stats
    *undescribed*

init_task
    Initialize a iscsi_task and any internal structs.
    When offloading the data path, this is called from
    queuecommand with the session lock, or from the
    iscsi_conn_send_pdu context with the session lock.
    When not offloading the data path, this is called
    from the scsi work queue without the session lock.
    \ ``xmit_task``\            Requests LLD to transfer cmd task. Returns 0 or the
    the number of bytes transferred on success, and -Exyz
    value on error. When offloading the data path, this
    is called from queuecommand with the session lock, or
    from the iscsi_conn_send_pdu context with the session
    lock. When not offloading the data path, this is called
    from the scsi work queue without the session lock.

xmit_task
    *undescribed*

cleanup_task
    requests LLD to fail task. Called with session lock
    and after the connection has been suspended and
    terminated during recovery. If called
    from abort task then connection is not suspended
    or terminated but sk_callback_lock is held

alloc_pdu
    *undescribed*

xmit_pdu
    *undescribed*

init_pdu
    *undescribed*

parse_pdu_itt
    *undescribed*

session_recovery_timedout
    notify LLD a block during recovery timed out

ep_connect
    *undescribed*

ep_poll
    *undescribed*

ep_disconnect
    *undescribed*

tgt_dscvr
    *undescribed*

set_path
    *undescribed*

set_iface_param
    *undescribed*

get_iface_param
    *undescribed*

attr_is_visible
    *undescribed*

bsg_request
    *undescribed*

send_ping
    *undescribed*

get_chap
    *undescribed*

delete_chap
    *undescribed*

set_chap
    *undescribed*

get_flashnode_param
    *undescribed*

set_flashnode_param
    *undescribed*

new_flashnode
    *undescribed*

del_flashnode
    *undescribed*

login_flashnode
    *undescribed*

logout_flashnode
    *undescribed*

logout_flashnode_sid
    *undescribed*

get_host_stats
    *undescribed*

check_protection
    *undescribed*

.. _`iscsi_transport.description`:

Description
-----------

Template API provided by iSCSI Transport

.. This file was automatic generated / don't edit.


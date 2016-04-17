.. -*- coding: utf-8; mode: rst -*-

======================
scsi_transport_iscsi.h
======================


.. _`iscsi_transport`:

struct iscsi_transport
======================

.. c:type:: iscsi_transport

    iSCSI Transport template


.. _`iscsi_transport.definition`:

Definition
----------

.. code-block:: c

  struct iscsi_transport {
    char * name;
    unsigned int caps;
    struct iscsi_cls_session *(* create_session) (struct iscsi_endpoint *ep,uint16_t cmds_max, uint16_t qdepth,uint32_t sn);
    void (* destroy_session) (struct iscsi_cls_session *session);
    struct iscsi_cls_conn *(* create_conn) (struct iscsi_cls_session *sess,uint32_t cid);
    int (* bind_conn) (struct iscsi_cls_session *session,struct iscsi_cls_conn *cls_conn,uint64_t transport_eph, int is_leading);
    int (* start_conn) (struct iscsi_cls_conn *conn);
    void (* stop_conn) (struct iscsi_cls_conn *conn, int flag);
    void (* destroy_conn) (struct iscsi_cls_conn *conn);
    int (* set_param) (struct iscsi_cls_conn *conn, enum iscsi_param param,char *buf, int buflen);
    int (* send_pdu) (struct iscsi_cls_conn *conn, struct iscsi_hdr *hdr,char *data, uint32_t data_size);
    int (* init_task) (struct iscsi_task *task);
    void (* cleanup_task) (struct iscsi_task *task);
    void (* session_recovery_timedout) (struct iscsi_cls_session *session);
  };


.. _`iscsi_transport.members`:

Members
-------

:``name``:
    transport name

:``caps``:
    iSCSI Data-Path capabilities

:``create_session``:
    create new iSCSI session object

:``destroy_session``:
    destroy existing iSCSI session object

:``create_conn``:
    create new iSCSI connection

:``bind_conn``:
    associate this connection with existing iSCSI session
    and specified transport descriptor

:``start_conn``:
    set connection to be operational

:``stop_conn``:
    suspend/recover/terminate connection

:``destroy_conn``:
    destroy inactive iSCSI connection

:``set_param``:
    set iSCSI parameter. Return 0 on success, -ENODATA
    when param is not supported, and a -Exx value on other
    error.

    ``get_param``                get iSCSI parameter. Must return number of bytes
    copied to buffer on success, -ENODATA when param
    is not supported, and a -Exx value on other error

:``send_pdu``:
    send iSCSI PDU, Login, Logout, NOP-Out, Reject, Text.

:``init_task``:
    Initialize a iscsi_task and any internal structs.
    When offloading the data path, this is called from
    queuecommand with the session lock, or from the
    iscsi_conn_send_pdu context with the session lock.
    When not offloading the data path, this is called
    from the scsi work queue without the session lock.

    ``xmit_task``                Requests LLD to transfer cmd task. Returns 0 or the
    the number of bytes transferred on success, and -Exyz
    value on error. When offloading the data path, this
    is called from queuecommand with the session lock, or
    from the iscsi_conn_send_pdu context with the session
    lock. When not offloading the data path, this is called
    from the scsi work queue without the session lock.

:``cleanup_task``:
    requests LLD to fail task. Called with session lock
    and after the connection has been suspended and
    terminated during recovery. If called
    from abort task then connection is not suspended
    or terminated but sk_callback_lock is held

:``session_recovery_timedout``:
    notify LLD a block during recovery timed out




.. _`iscsi_transport.description`:

Description
-----------

Template API provided by iSCSI Transport


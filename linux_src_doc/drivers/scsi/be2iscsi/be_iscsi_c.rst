.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_iscsi.c

.. _`beiscsi_session_create`:

beiscsi_session_create
======================

.. c:function:: struct iscsi_cls_session *beiscsi_session_create(struct iscsi_endpoint *ep, u16 cmds_max, u16 qdepth, u32 initial_cmdsn)

    creates a new iscsi session

    :param ep:
        *undescribed*
    :type ep: struct iscsi_endpoint \*

    :param cmds_max:
        max commands supported
    :type cmds_max: u16

    :param qdepth:
        max queue depth supported
    :type qdepth: u16

    :param initial_cmdsn:
        initial iscsi CMDSN
    :type initial_cmdsn: u32

.. _`beiscsi_session_destroy`:

beiscsi_session_destroy
=======================

.. c:function:: void beiscsi_session_destroy(struct iscsi_cls_session *cls_session)

    destroys iscsi session

    :param cls_session:
        pointer to iscsi cls session
    :type cls_session: struct iscsi_cls_session \*

.. _`beiscsi_session_destroy.description`:

Description
-----------

Destroys iSCSI session instance and releases
resources allocated for it.

.. _`beiscsi_session_fail`:

beiscsi_session_fail
====================

.. c:function:: void beiscsi_session_fail(struct iscsi_cls_session *cls_session)

    Closing session with appropriate error

    :param cls_session:
        ptr to session
    :type cls_session: struct iscsi_cls_session \*

.. _`beiscsi_conn_create`:

beiscsi_conn_create
===================

.. c:function:: struct iscsi_cls_conn *beiscsi_conn_create(struct iscsi_cls_session *cls_session, u32 cid)

    create an instance of iscsi connection

    :param cls_session:
        ptr to iscsi_cls_session
    :type cls_session: struct iscsi_cls_session \*

    :param cid:
        iscsi cid
    :type cid: u32

.. _`beiscsi_conn_bind`:

beiscsi_conn_bind
=================

.. c:function:: int beiscsi_conn_bind(struct iscsi_cls_session *cls_session, struct iscsi_cls_conn *cls_conn, u64 transport_fd, int is_leading)

    Binds iscsi session/connection with TCP connection

    :param cls_session:
        pointer to iscsi cls session
    :type cls_session: struct iscsi_cls_session \*

    :param cls_conn:
        pointer to iscsi cls conn
    :type cls_conn: struct iscsi_cls_conn \*

    :param transport_fd:
        EP handle(64 bit)
    :type transport_fd: u64

    :param is_leading:
        *undescribed*
    :type is_leading: int

.. _`beiscsi_conn_bind.description`:

Description
-----------

This function binds the TCP Conn with iSCSI Connection and Session.

.. _`beiscsi_iface_config_vlan`:

beiscsi_iface_config_vlan
=========================

.. c:function:: int beiscsi_iface_config_vlan(struct Scsi_Host *shost, struct iscsi_iface_param_info *iface_param)

    Set the VLAN TAG

    :param shost:
        Scsi Host for the driver instance
    :type shost: struct Scsi_Host \*

    :param iface_param:
        Interface paramters
    :type iface_param: struct iscsi_iface_param_info \*

.. _`beiscsi_iface_config_vlan.description`:

Description
-----------

Set the VLAN TAG for the adapter or disable
the VLAN config

returns

.. _`beiscsi_iface_config_vlan.success`:

Success
-------

0

.. _`beiscsi_iface_config_vlan.failure`:

Failure
-------

Non-Zero Value

.. _`beiscsi_ep_get_param`:

beiscsi_ep_get_param
====================

.. c:function:: int beiscsi_ep_get_param(struct iscsi_endpoint *ep, enum iscsi_param param, char *buf)

    get the iscsi parameter

    :param ep:
        pointer to iscsi ep
    :type ep: struct iscsi_endpoint \*

    :param param:
        parameter type identifier
    :type param: enum iscsi_param

    :param buf:
        buffer pointer
    :type buf: char \*

.. _`beiscsi_ep_get_param.description`:

Description
-----------

returns iscsi parameter

.. _`beiscsi_get_port_state`:

beiscsi_get_port_state
======================

.. c:function:: void beiscsi_get_port_state(struct Scsi_Host *shost)

    Get the Port State

    :param shost:
        pointer to scsi_host structure
    :type shost: struct Scsi_Host \*

.. _`beiscsi_get_port_speed`:

beiscsi_get_port_speed
======================

.. c:function:: void beiscsi_get_port_speed(struct Scsi_Host *shost)

    Get the Port Speed from Adapter

    :param shost:
        pointer to scsi_host structure
    :type shost: struct Scsi_Host \*

.. _`beiscsi_get_host_param`:

beiscsi_get_host_param
======================

.. c:function:: int beiscsi_get_host_param(struct Scsi_Host *shost, enum iscsi_host_param param, char *buf)

    get the iscsi parameter

    :param shost:
        pointer to scsi_host structure
    :type shost: struct Scsi_Host \*

    :param param:
        parameter type identifier
    :type param: enum iscsi_host_param

    :param buf:
        buffer pointer
    :type buf: char \*

.. _`beiscsi_conn_get_stats`:

beiscsi_conn_get_stats
======================

.. c:function:: void beiscsi_conn_get_stats(struct iscsi_cls_conn *cls_conn, struct iscsi_stats *stats)

    get the iscsi stats

    :param cls_conn:
        pointer to iscsi cls conn
    :type cls_conn: struct iscsi_cls_conn \*

    :param stats:
        pointer to iscsi_stats structure
    :type stats: struct iscsi_stats \*

.. _`beiscsi_conn_get_stats.description`:

Description
-----------

returns iscsi stats

.. _`beiscsi_set_params_for_offld`:

beiscsi_set_params_for_offld
============================

.. c:function:: void beiscsi_set_params_for_offld(struct beiscsi_conn *beiscsi_conn, struct beiscsi_offload_params *params)

    get the parameters for offload

    :param beiscsi_conn:
        pointer to beiscsi_conn
    :type beiscsi_conn: struct beiscsi_conn \*

    :param params:
        pointer to offload_params structure
    :type params: struct beiscsi_offload_params \*

.. _`beiscsi_conn_start`:

beiscsi_conn_start
==================

.. c:function:: int beiscsi_conn_start(struct iscsi_cls_conn *cls_conn)

    offload of session to chip

    :param cls_conn:
        pointer to beiscsi_conn
    :type cls_conn: struct iscsi_cls_conn \*

.. _`beiscsi_get_cid`:

beiscsi_get_cid
===============

.. c:function:: int beiscsi_get_cid(struct beiscsi_hba *phba)

    Allocate a cid

    :param phba:
        The phba instance
    :type phba: struct beiscsi_hba \*

.. _`beiscsi_put_cid`:

beiscsi_put_cid
===============

.. c:function:: void beiscsi_put_cid(struct beiscsi_hba *phba, unsigned short cid)

    Free the cid

    :param phba:
        The phba for which the cid is being freed
    :type phba: struct beiscsi_hba \*

    :param cid:
        The cid to free
    :type cid: unsigned short

.. _`beiscsi_free_ep`:

beiscsi_free_ep
===============

.. c:function:: void beiscsi_free_ep(struct beiscsi_endpoint *beiscsi_ep)

    free endpoint

    :param beiscsi_ep:
        *undescribed*
    :type beiscsi_ep: struct beiscsi_endpoint \*

.. _`beiscsi_open_conn`:

beiscsi_open_conn
=================

.. c:function:: int beiscsi_open_conn(struct iscsi_endpoint *ep, struct sockaddr *src_addr, struct sockaddr *dst_addr, int non_blocking)

    Ask FW to open a TCP connection

    :param ep:
        endpoint to be used
    :type ep: struct iscsi_endpoint \*

    :param src_addr:
        The source IP address
    :type src_addr: struct sockaddr \*

    :param dst_addr:
        The Destination  IP address
    :type dst_addr: struct sockaddr \*

    :param non_blocking:
        *undescribed*
    :type non_blocking: int

.. _`beiscsi_open_conn.description`:

Description
-----------

Asks the FW to open a TCP connection

.. _`beiscsi_ep_connect`:

beiscsi_ep_connect
==================

.. c:function:: struct iscsi_endpoint *beiscsi_ep_connect(struct Scsi_Host *shost, struct sockaddr *dst_addr, int non_blocking)

    Ask chip to create TCP Conn

    :param shost:
        *undescribed*
    :type shost: struct Scsi_Host \*

    :param dst_addr:
        The IP address of Target
    :type dst_addr: struct sockaddr \*

    :param non_blocking:
        blocking or non-blocking call
    :type non_blocking: int

.. _`beiscsi_ep_connect.description`:

Description
-----------

This routines first asks chip to create a connection and then allocates an EP

.. _`beiscsi_ep_poll`:

beiscsi_ep_poll
===============

.. c:function:: int beiscsi_ep_poll(struct iscsi_endpoint *ep, int timeout_ms)

    Poll to see if connection is established

    :param ep:
        endpoint to be used
    :type ep: struct iscsi_endpoint \*

    :param timeout_ms:
        timeout specified in millisecs
    :type timeout_ms: int

.. _`beiscsi_ep_poll.description`:

Description
-----------

Poll to see if TCP connection established

.. _`beiscsi_flush_cq`:

beiscsi_flush_cq
================

.. c:function:: void beiscsi_flush_cq(struct beiscsi_hba *phba)

    Flush the CQ created.

    :param phba:
        ptr device priv structure.
    :type phba: struct beiscsi_hba \*

.. _`beiscsi_flush_cq.description`:

Description
-----------

Before the connection resource are freed flush
all the CQ enteries

.. _`beiscsi_conn_close`:

beiscsi_conn_close
==================

.. c:function:: int beiscsi_conn_close(struct beiscsi_endpoint *beiscsi_ep)

    Invalidate and upload connection

    :param beiscsi_ep:
        *undescribed*
    :type beiscsi_ep: struct beiscsi_endpoint \*

.. _`beiscsi_conn_close.description`:

Description
-----------

Returns 0 on success,  -1 on failure.

.. _`beiscsi_ep_disconnect`:

beiscsi_ep_disconnect
=====================

.. c:function:: void beiscsi_ep_disconnect(struct iscsi_endpoint *ep)

    Tears down the TCP connection

    :param ep:
        endpoint to be used
    :type ep: struct iscsi_endpoint \*

.. _`beiscsi_ep_disconnect.description`:

Description
-----------

Tears down the TCP connection

.. This file was automatic generated / don't edit.


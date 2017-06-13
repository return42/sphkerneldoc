.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_iscsi.c

.. _`beiscsi_session_create`:

beiscsi_session_create
======================

.. c:function:: struct iscsi_cls_session *beiscsi_session_create(struct iscsi_endpoint *ep, u16 cmds_max, u16 qdepth, u32 initial_cmdsn)

    creates a new iscsi session

    :param struct iscsi_endpoint \*ep:
        *undescribed*

    :param u16 cmds_max:
        max commands supported

    :param u16 qdepth:
        max queue depth supported

    :param u32 initial_cmdsn:
        initial iscsi CMDSN

.. _`beiscsi_session_destroy`:

beiscsi_session_destroy
=======================

.. c:function:: void beiscsi_session_destroy(struct iscsi_cls_session *cls_session)

    destroys iscsi session

    :param struct iscsi_cls_session \*cls_session:
        pointer to iscsi cls session

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

    :param struct iscsi_cls_session \*cls_session:
        ptr to session

.. _`beiscsi_conn_create`:

beiscsi_conn_create
===================

.. c:function:: struct iscsi_cls_conn *beiscsi_conn_create(struct iscsi_cls_session *cls_session, u32 cid)

    create an instance of iscsi connection

    :param struct iscsi_cls_session \*cls_session:
        ptr to iscsi_cls_session

    :param u32 cid:
        iscsi cid

.. _`beiscsi_conn_bind`:

beiscsi_conn_bind
=================

.. c:function:: int beiscsi_conn_bind(struct iscsi_cls_session *cls_session, struct iscsi_cls_conn *cls_conn, u64 transport_fd, int is_leading)

    Binds iscsi session/connection with TCP connection

    :param struct iscsi_cls_session \*cls_session:
        pointer to iscsi cls session

    :param struct iscsi_cls_conn \*cls_conn:
        pointer to iscsi cls conn

    :param u64 transport_fd:
        EP handle(64 bit)

    :param int is_leading:
        *undescribed*

.. _`beiscsi_conn_bind.description`:

Description
-----------

This function binds the TCP Conn with iSCSI Connection and Session.

.. _`beiscsi_iface_config_vlan`:

beiscsi_iface_config_vlan
=========================

.. c:function:: int beiscsi_iface_config_vlan(struct Scsi_Host *shost, struct iscsi_iface_param_info *iface_param)

    Set the VLAN TAG

    :param struct Scsi_Host \*shost:
        Scsi Host for the driver instance

    :param struct iscsi_iface_param_info \*iface_param:
        Interface paramters

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

    :param struct iscsi_endpoint \*ep:
        pointer to iscsi ep

    :param enum iscsi_param param:
        parameter type identifier

    :param char \*buf:
        buffer pointer

.. _`beiscsi_ep_get_param.description`:

Description
-----------

returns iscsi parameter

.. _`beiscsi_get_initname`:

beiscsi_get_initname
====================

.. c:function:: int beiscsi_get_initname(char *buf, struct beiscsi_hba *phba)

    Read Initiator Name from flash

    :param char \*buf:
        buffer bointer

    :param struct beiscsi_hba \*phba:
        The device priv structure instance

.. _`beiscsi_get_initname.description`:

Description
-----------

returns number of bytes

.. _`beiscsi_get_port_state`:

beiscsi_get_port_state
======================

.. c:function:: void beiscsi_get_port_state(struct Scsi_Host *shost)

    Get the Port State

    :param struct Scsi_Host \*shost:
        pointer to scsi_host structure

.. _`beiscsi_get_port_speed`:

beiscsi_get_port_speed
======================

.. c:function:: void beiscsi_get_port_speed(struct Scsi_Host *shost)

    Get the Port Speed from Adapter

    :param struct Scsi_Host \*shost:
        pointer to scsi_host structure

.. _`beiscsi_get_host_param`:

beiscsi_get_host_param
======================

.. c:function:: int beiscsi_get_host_param(struct Scsi_Host *shost, enum iscsi_host_param param, char *buf)

    get the iscsi parameter

    :param struct Scsi_Host \*shost:
        pointer to scsi_host structure

    :param enum iscsi_host_param param:
        parameter type identifier

    :param char \*buf:
        buffer pointer

.. _`beiscsi_get_host_param.description`:

Description
-----------

returns host parameter

.. _`beiscsi_conn_get_stats`:

beiscsi_conn_get_stats
======================

.. c:function:: void beiscsi_conn_get_stats(struct iscsi_cls_conn *cls_conn, struct iscsi_stats *stats)

    get the iscsi stats

    :param struct iscsi_cls_conn \*cls_conn:
        pointer to iscsi cls conn

    :param struct iscsi_stats \*stats:
        pointer to iscsi_stats structure

.. _`beiscsi_conn_get_stats.description`:

Description
-----------

returns iscsi stats

.. _`beiscsi_set_params_for_offld`:

beiscsi_set_params_for_offld
============================

.. c:function:: void beiscsi_set_params_for_offld(struct beiscsi_conn *beiscsi_conn, struct beiscsi_offload_params *params)

    get the parameters for offload

    :param struct beiscsi_conn \*beiscsi_conn:
        pointer to beiscsi_conn

    :param struct beiscsi_offload_params \*params:
        pointer to offload_params structure

.. _`beiscsi_conn_start`:

beiscsi_conn_start
==================

.. c:function:: int beiscsi_conn_start(struct iscsi_cls_conn *cls_conn)

    offload of session to chip

    :param struct iscsi_cls_conn \*cls_conn:
        pointer to beiscsi_conn

.. _`beiscsi_get_cid`:

beiscsi_get_cid
===============

.. c:function:: int beiscsi_get_cid(struct beiscsi_hba *phba)

    Allocate a cid

    :param struct beiscsi_hba \*phba:
        The phba instance

.. _`beiscsi_put_cid`:

beiscsi_put_cid
===============

.. c:function:: void beiscsi_put_cid(struct beiscsi_hba *phba, unsigned short cid)

    Free the cid

    :param struct beiscsi_hba \*phba:
        The phba for which the cid is being freed

    :param unsigned short cid:
        The cid to free

.. _`beiscsi_free_ep`:

beiscsi_free_ep
===============

.. c:function:: void beiscsi_free_ep(struct beiscsi_endpoint *beiscsi_ep)

    free endpoint

    :param struct beiscsi_endpoint \*beiscsi_ep:
        *undescribed*

.. _`beiscsi_open_conn`:

beiscsi_open_conn
=================

.. c:function:: int beiscsi_open_conn(struct iscsi_endpoint *ep, struct sockaddr *src_addr, struct sockaddr *dst_addr, int non_blocking)

    Ask FW to open a TCP connection

    :param struct iscsi_endpoint \*ep:
        endpoint to be used

    :param struct sockaddr \*src_addr:
        The source IP address

    :param struct sockaddr \*dst_addr:
        The Destination  IP address

    :param int non_blocking:
        *undescribed*

.. _`beiscsi_open_conn.description`:

Description
-----------

Asks the FW to open a TCP connection

.. _`beiscsi_ep_connect`:

beiscsi_ep_connect
==================

.. c:function:: struct iscsi_endpoint *beiscsi_ep_connect(struct Scsi_Host *shost, struct sockaddr *dst_addr, int non_blocking)

    Ask chip to create TCP Conn

    :param struct Scsi_Host \*shost:
        *undescribed*

    :param struct sockaddr \*dst_addr:
        The IP address of Target

    :param int non_blocking:
        blocking or non-blocking call

.. _`beiscsi_ep_connect.description`:

Description
-----------

This routines first asks chip to create a connection and then allocates an EP

.. _`beiscsi_ep_poll`:

beiscsi_ep_poll
===============

.. c:function:: int beiscsi_ep_poll(struct iscsi_endpoint *ep, int timeout_ms)

    Poll to see if connection is established

    :param struct iscsi_endpoint \*ep:
        endpoint to be used

    :param int timeout_ms:
        timeout specified in millisecs

.. _`beiscsi_ep_poll.description`:

Description
-----------

Poll to see if TCP connection established

.. _`beiscsi_flush_cq`:

beiscsi_flush_cq
================

.. c:function:: void beiscsi_flush_cq(struct beiscsi_hba *phba)

    Flush the CQ created.

    :param struct beiscsi_hba \*phba:
        ptr device priv structure.

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

    :param struct beiscsi_endpoint \*beiscsi_ep:
        *undescribed*

.. _`beiscsi_conn_close.description`:

Description
-----------

Returns 0 on success,  -1 on failure.

.. _`beiscsi_ep_disconnect`:

beiscsi_ep_disconnect
=====================

.. c:function:: void beiscsi_ep_disconnect(struct iscsi_endpoint *ep)

    Tears down the TCP connection

    :param struct iscsi_endpoint \*ep:
        endpoint to be used

.. _`beiscsi_ep_disconnect.description`:

Description
-----------

Tears down the TCP connection

.. This file was automatic generated / don't edit.


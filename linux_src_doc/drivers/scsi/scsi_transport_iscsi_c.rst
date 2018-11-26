.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_transport_iscsi.c

.. _`iscsi_create_flashnode_sess`:

iscsi_create_flashnode_sess
===========================

.. c:function:: struct iscsi_bus_flash_session *iscsi_create_flashnode_sess(struct Scsi_Host *shost, int index, struct iscsi_transport *transport, int dd_size)

    Add flashnode session entry in sysfs

    :param shost:
        pointer to host data
    :type shost: struct Scsi_Host \*

    :param index:
        index of flashnode to add in sysfs
    :type index: int

    :param transport:
        pointer to transport data
    :type transport: struct iscsi_transport \*

    :param dd_size:
        total size to allocate
    :type dd_size: int

.. _`iscsi_create_flashnode_sess.description`:

Description
-----------

Adds a sysfs entry for the flashnode session attributes

.. _`iscsi_create_flashnode_sess.return`:

Return
------

 pointer to allocated flashnode sess on success
 \ ``NULL``\  on failure

.. _`iscsi_create_flashnode_conn`:

iscsi_create_flashnode_conn
===========================

.. c:function:: struct iscsi_bus_flash_conn *iscsi_create_flashnode_conn(struct Scsi_Host *shost, struct iscsi_bus_flash_session *fnode_sess, struct iscsi_transport *transport, int dd_size)

    Add flashnode conn entry in sysfs

    :param shost:
        pointer to host data
    :type shost: struct Scsi_Host \*

    :param fnode_sess:
        pointer to the parent flashnode session entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

    :param transport:
        pointer to transport data
    :type transport: struct iscsi_transport \*

    :param dd_size:
        total size to allocate
    :type dd_size: int

.. _`iscsi_create_flashnode_conn.description`:

Description
-----------

Adds a sysfs entry for the flashnode connection attributes

.. _`iscsi_create_flashnode_conn.return`:

Return
------

 pointer to allocated flashnode conn on success
 \ ``NULL``\  on failure

.. _`iscsi_is_flashnode_conn_dev`:

iscsi_is_flashnode_conn_dev
===========================

.. c:function:: int iscsi_is_flashnode_conn_dev(struct device *dev, void *data)

    verify passed device is to be flashnode conn

    :param dev:
        device to verify
    :type dev: struct device \*

    :param data:
        pointer to data containing value to use for verification
    :type data: void \*

.. _`iscsi_is_flashnode_conn_dev.description`:

Description
-----------

Verifies if the passed device is flashnode conn device

.. _`iscsi_is_flashnode_conn_dev.return`:

Return
------

 1 on success
 0 on failure

.. _`iscsi_get_flashnode_by_index`:

iscsi_get_flashnode_by_index
============================

.. c:function:: struct iscsi_bus_flash_session *iscsi_get_flashnode_by_index(struct Scsi_Host *shost, uint32_t idx)

    finds flashnode session entry by index

    :param shost:
        pointer to host data
    :type shost: struct Scsi_Host \*

    :param idx:
        index to match
    :type idx: uint32_t

.. _`iscsi_get_flashnode_by_index.description`:

Description
-----------

Finds the flashnode session object for the passed index

.. _`iscsi_get_flashnode_by_index.return`:

Return
------

 pointer to found flashnode session object on success
 \ ``NULL``\  on failure

.. _`iscsi_find_flashnode_sess`:

iscsi_find_flashnode_sess
=========================

.. c:function:: struct device *iscsi_find_flashnode_sess(struct Scsi_Host *shost, void *data, int (*fn)(struct device *dev, void *data))

    finds flashnode session entry

    :param shost:
        pointer to host data
    :type shost: struct Scsi_Host \*

    :param data:
        pointer to data containing value to use for comparison
    :type data: void \*

    :param int (\*fn)(struct device \*dev, void \*data):
        function pointer that does actual comparison

.. _`iscsi_find_flashnode_sess.description`:

Description
-----------

Finds the flashnode session object comparing the data passed using logic
defined in passed function pointer

.. _`iscsi_find_flashnode_sess.return`:

Return
------

 pointer to found flashnode session device object on success
 \ ``NULL``\  on failure

.. _`iscsi_find_flashnode_conn`:

iscsi_find_flashnode_conn
=========================

.. c:function:: struct device *iscsi_find_flashnode_conn(struct iscsi_bus_flash_session *fnode_sess)

    finds flashnode connection entry

    :param fnode_sess:
        pointer to parent flashnode session entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

.. _`iscsi_find_flashnode_conn.description`:

Description
-----------

Finds the flashnode connection object comparing the data passed using logic
defined in passed function pointer

.. _`iscsi_find_flashnode_conn.return`:

Return
------

 pointer to found flashnode connection device object on success
 \ ``NULL``\  on failure

.. _`iscsi_destroy_flashnode_sess`:

iscsi_destroy_flashnode_sess
============================

.. c:function:: void iscsi_destroy_flashnode_sess(struct iscsi_bus_flash_session *fnode_sess)

    destroy flashnode session entry

    :param fnode_sess:
        pointer to flashnode session entry to be destroyed
    :type fnode_sess: struct iscsi_bus_flash_session \*

.. _`iscsi_destroy_flashnode_sess.description`:

Description
-----------

Deletes the flashnode session entry and all children flashnode connection
entries from sysfs

.. _`iscsi_destroy_all_flashnode`:

iscsi_destroy_all_flashnode
===========================

.. c:function:: void iscsi_destroy_all_flashnode(struct Scsi_Host *shost)

    destroy all flashnode session entries

    :param shost:
        pointer to host data
    :type shost: struct Scsi_Host \*

.. _`iscsi_destroy_all_flashnode.description`:

Description
-----------

Destroys all the flashnode session entries and all corresponding children
flashnode connection entries from sysfs

.. _`iscsi_bsg_host_dispatch`:

iscsi_bsg_host_dispatch
=======================

.. c:function:: int iscsi_bsg_host_dispatch(struct bsg_job *job)

    Dispatch command to LLD.

    :param job:
        bsg job to be processed
    :type job: struct bsg_job \*

.. _`iscsi_bsg_host_add`:

iscsi_bsg_host_add
==================

.. c:function:: int iscsi_bsg_host_add(struct Scsi_Host *shost, struct iscsi_cls_host *ihost)

    Create and add the bsg hooks to receive requests

    :param shost:
        shost for iscsi_host
    :type shost: struct Scsi_Host \*

    :param ihost:
        iscsi_cls_host adding the structures to
    :type ihost: struct iscsi_cls_host \*

.. _`iscsi_scan_finished`:

iscsi_scan_finished
===================

.. c:function:: int iscsi_scan_finished(struct Scsi_Host *shost, unsigned long time)

    helper to report when running scans are done

    :param shost:
        scsi host
    :type shost: struct Scsi_Host \*

    :param time:
        scan run time
    :type time: unsigned long

.. _`iscsi_scan_finished.description`:

Description
-----------

This function can be used by drives like qla4xxx to report to the scsi
layer when the scans it kicked off at module load time are done.

.. _`iscsi_block_scsi_eh`:

iscsi_block_scsi_eh
===================

.. c:function:: int iscsi_block_scsi_eh(struct scsi_cmnd *cmd)

    block scsi eh until session state has transistioned

    :param cmd:
        scsi cmd passed to scsi eh handler
    :type cmd: struct scsi_cmnd \*

.. _`iscsi_block_scsi_eh.description`:

Description
-----------

If the session is down this function will wait for the recovery
timer to fire or for the session to be logged back in. If the
recovery timer fires then FAST_IO_FAIL is returned. The caller
should pass this error value to the scsi eh.

.. _`iscsi_unblock_session`:

iscsi_unblock_session
=====================

.. c:function:: void iscsi_unblock_session(struct iscsi_cls_session *session)

    set a session as logged in and start IO.

    :param session:
        iscsi session
    :type session: struct iscsi_cls_session \*

.. _`iscsi_unblock_session.description`:

Description
-----------

Mark a session as ready to accept IO.

.. _`iscsi_create_session`:

iscsi_create_session
====================

.. c:function:: struct iscsi_cls_session *iscsi_create_session(struct Scsi_Host *shost, struct iscsi_transport *transport, int dd_size, unsigned int target_id)

    create iscsi class session

    :param shost:
        scsi host
    :type shost: struct Scsi_Host \*

    :param transport:
        iscsi transport
    :type transport: struct iscsi_transport \*

    :param dd_size:
        private driver data size
    :type dd_size: int

    :param target_id:
        which target
    :type target_id: unsigned int

.. _`iscsi_create_session.description`:

Description
-----------

This can be called from a LLD or iscsi_transport.

.. _`iscsi_create_conn`:

iscsi_create_conn
=================

.. c:function:: struct iscsi_cls_conn *iscsi_create_conn(struct iscsi_cls_session *session, int dd_size, uint32_t cid)

    create iscsi class connection

    :param session:
        iscsi cls session
    :type session: struct iscsi_cls_session \*

    :param dd_size:
        private driver data size
    :type dd_size: int

    :param cid:
        connection id
    :type cid: uint32_t

.. _`iscsi_create_conn.description`:

Description
-----------

This can be called from a LLD or iscsi_transport. The connection
is child of the session so cid must be unique for all connections
on the session.

Since we do not support MCS, cid will normally be zero. In some cases
for software iscsi we could be trying to preallocate a connection struct
in which case there could be two connection structs and cid would be
non-zero.

.. _`iscsi_destroy_conn`:

iscsi_destroy_conn
==================

.. c:function:: int iscsi_destroy_conn(struct iscsi_cls_conn *conn)

    destroy iscsi class connection

    :param conn:
        iscsi cls session
    :type conn: struct iscsi_cls_conn \*

.. _`iscsi_destroy_conn.description`:

Description
-----------

This can be called from a LLD or iscsi_transport.

.. _`iscsi_session_event`:

iscsi_session_event
===================

.. c:function:: int iscsi_session_event(struct iscsi_cls_session *session, enum iscsi_uevent_e event)

    send session destr. completion event

    :param session:
        iscsi class session
    :type session: struct iscsi_cls_session \*

    :param event:
        type of event
    :type event: enum iscsi_uevent_e

.. This file was automatic generated / don't edit.


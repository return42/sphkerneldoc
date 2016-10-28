.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/client.c

.. _`mei_me_cl_init`:

mei_me_cl_init
==============

.. c:function:: void mei_me_cl_init(struct mei_me_client *me_cl)

    initialize me client

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_me_cl_get`:

mei_me_cl_get
=============

.. c:function:: struct mei_me_client *mei_me_cl_get(struct mei_me_client *me_cl)

    increases me client refcount

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_me_cl_get.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_get.return`:

Return
------

me client or NULL

.. _`mei_me_cl_release`:

mei_me_cl_release
=================

.. c:function:: void mei_me_cl_release(struct kref *ref)

    free me client

    :param struct kref \*ref:
        me_client refcount

.. _`mei_me_cl_release.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_put`:

mei_me_cl_put
=============

.. c:function:: void mei_me_cl_put(struct mei_me_client *me_cl)

    decrease me client refcount and free client if necessary

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_me_cl_put.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`__mei_me_cl_del`:

__mei_me_cl_del
===============

.. c:function:: void __mei_me_cl_del(struct mei_device *dev, struct mei_me_client *me_cl)

    delete me client from the list and decrease reference counter

    :param struct mei_device \*dev:
        mei device

    :param struct mei_me_client \*me_cl:
        me client

.. _`__mei_me_cl_del.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`mei_me_cl_del`:

mei_me_cl_del
=============

.. c:function:: void mei_me_cl_del(struct mei_device *dev, struct mei_me_client *me_cl)

    delete me client from the list and decrease reference counter

    :param struct mei_device \*dev:
        mei device

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_me_cl_add`:

mei_me_cl_add
=============

.. c:function:: void mei_me_cl_add(struct mei_device *dev, struct mei_me_client *me_cl)

    add me client to the list

    :param struct mei_device \*dev:
        mei device

    :param struct mei_me_client \*me_cl:
        me client

.. _`__mei_me_cl_by_uuid`:

__mei_me_cl_by_uuid
===================

.. c:function:: struct mei_me_client *__mei_me_cl_by_uuid(struct mei_device *dev, const uuid_le *uuid)

    locate me client by uuid increases ref count

    :param struct mei_device \*dev:
        mei device

    :param const uuid_le \*uuid:
        me client uuid

.. _`__mei_me_cl_by_uuid.return`:

Return
------

me client or NULL if not found

.. _`__mei_me_cl_by_uuid.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`mei_me_cl_by_uuid`:

mei_me_cl_by_uuid
=================

.. c:function:: struct mei_me_client *mei_me_cl_by_uuid(struct mei_device *dev, const uuid_le *uuid)

    locate me client by uuid increases ref count

    :param struct mei_device \*dev:
        mei device

    :param const uuid_le \*uuid:
        me client uuid

.. _`mei_me_cl_by_uuid.return`:

Return
------

me client or NULL if not found

.. _`mei_me_cl_by_uuid.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`mei_me_cl_by_id`:

mei_me_cl_by_id
===============

.. c:function:: struct mei_me_client *mei_me_cl_by_id(struct mei_device *dev, u8 client_id)

    locate me client by client id increases ref count

    :param struct mei_device \*dev:
        the device structure

    :param u8 client_id:
        me client id

.. _`mei_me_cl_by_id.return`:

Return
------

me client or NULL if not found

.. _`mei_me_cl_by_id.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`__mei_me_cl_by_uuid_id`:

__mei_me_cl_by_uuid_id
======================

.. c:function:: struct mei_me_client *__mei_me_cl_by_uuid_id(struct mei_device *dev, const uuid_le *uuid, u8 client_id)

    locate me client by client id and uuid increases ref count

    :param struct mei_device \*dev:
        the device structure

    :param const uuid_le \*uuid:
        me client uuid

    :param u8 client_id:
        me client id

.. _`__mei_me_cl_by_uuid_id.return`:

Return
------

me client or null if not found

.. _`__mei_me_cl_by_uuid_id.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`mei_me_cl_by_uuid_id`:

mei_me_cl_by_uuid_id
====================

.. c:function:: struct mei_me_client *mei_me_cl_by_uuid_id(struct mei_device *dev, const uuid_le *uuid, u8 client_id)

    locate me client by client id and uuid increases ref count

    :param struct mei_device \*dev:
        the device structure

    :param const uuid_le \*uuid:
        me client uuid

    :param u8 client_id:
        me client id

.. _`mei_me_cl_by_uuid_id.return`:

Return
------

me client or null if not found

.. _`mei_me_cl_rm_by_uuid`:

mei_me_cl_rm_by_uuid
====================

.. c:function:: void mei_me_cl_rm_by_uuid(struct mei_device *dev, const uuid_le *uuid)

    remove all me clients matching uuid

    :param struct mei_device \*dev:
        the device structure

    :param const uuid_le \*uuid:
        me client uuid

.. _`mei_me_cl_rm_by_uuid.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_rm_by_uuid_id`:

mei_me_cl_rm_by_uuid_id
=======================

.. c:function:: void mei_me_cl_rm_by_uuid_id(struct mei_device *dev, const uuid_le *uuid, u8 id)

    remove all me clients matching client id

    :param struct mei_device \*dev:
        the device structure

    :param const uuid_le \*uuid:
        me client uuid

    :param u8 id:
        me client id

.. _`mei_me_cl_rm_by_uuid_id.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_rm_all`:

mei_me_cl_rm_all
================

.. c:function:: void mei_me_cl_rm_all(struct mei_device *dev)

    remove all me clients

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_cl_rm_all.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_cmp_id`:

mei_cl_cmp_id
=============

.. c:function:: bool mei_cl_cmp_id(const struct mei_cl *cl1, const struct mei_cl *cl2)

    tells if the clients are the same

    :param const struct mei_cl \*cl1:
        host client 1

    :param const struct mei_cl \*cl2:
        host client 2

.. _`mei_cl_cmp_id.return`:

Return
------

true  - if the clients has same host and me ids
false - otherwise

.. _`mei_io_cb_free`:

mei_io_cb_free
==============

.. c:function:: void mei_io_cb_free(struct mei_cl_cb *cb)

    free mei_cb_private related memory

    :param struct mei_cl_cb \*cb:
        mei callback struct

.. _`mei_io_cb_init`:

mei_io_cb_init
==============

.. c:function:: struct mei_cl_cb *mei_io_cb_init(struct mei_cl *cl, enum mei_cb_file_ops type, const struct file *fp)

    allocate and initialize io callback

    :param struct mei_cl \*cl:
        mei client

    :param enum mei_cb_file_ops type:
        operation type

    :param const struct file \*fp:
        pointer to file structure

.. _`mei_io_cb_init.return`:

Return
------

mei_cl_cb pointer or NULL;

.. _`__mei_io_list_flush`:

__mei_io_list_flush
===================

.. c:function:: void __mei_io_list_flush(struct mei_cl_cb *list, struct mei_cl *cl, bool free)

    removes and frees cbs belonging to cl.

    :param struct mei_cl_cb \*list:
        an instance of our list structure

    :param struct mei_cl \*cl:
        host client, can be NULL for flushing the whole list

    :param bool free:
        whether to free the cbs

.. _`mei_io_list_flush`:

mei_io_list_flush
=================

.. c:function:: void mei_io_list_flush(struct mei_cl_cb *list, struct mei_cl *cl)

    removes list entry belonging to cl.

    :param struct mei_cl_cb \*list:
        An instance of our list structure

    :param struct mei_cl \*cl:
        host client

.. _`mei_io_list_free`:

mei_io_list_free
================

.. c:function:: void mei_io_list_free(struct mei_cl_cb *list, struct mei_cl *cl)

    removes cb belonging to cl and free them

    :param struct mei_cl_cb \*list:
        An instance of our list structure

    :param struct mei_cl \*cl:
        host client

.. _`mei_io_cb_alloc_buf`:

mei_io_cb_alloc_buf
===================

.. c:function:: int mei_io_cb_alloc_buf(struct mei_cl_cb *cb, size_t length)

    allocate callback buffer

    :param struct mei_cl_cb \*cb:
        io callback structure

    :param size_t length:
        size of the buffer

.. _`mei_io_cb_alloc_buf.return`:

Return
------

0 on success
-EINVAL if cb is NULL
-ENOMEM if allocation failed

.. _`mei_cl_alloc_cb`:

mei_cl_alloc_cb
===============

.. c:function:: struct mei_cl_cb *mei_cl_alloc_cb(struct mei_cl *cl, size_t length, enum mei_cb_file_ops type, const struct file *fp)

    a convenient wrapper for allocating read cb

    :param struct mei_cl \*cl:
        host client

    :param size_t length:
        size of the buffer

    :param enum mei_cb_file_ops type:
        operation type

    :param const struct file \*fp:
        associated file pointer (might be NULL)

.. _`mei_cl_alloc_cb.return`:

Return
------

cb on success and NULL on failure

.. _`mei_cl_read_cb`:

mei_cl_read_cb
==============

.. c:function:: struct mei_cl_cb *mei_cl_read_cb(const struct mei_cl *cl, const struct file *fp)

    find this cl's callback in the read list for a specific file

    :param const struct mei_cl \*cl:
        host client

    :param const struct file \*fp:
        file pointer (matching cb file object), may be NULL

.. _`mei_cl_read_cb.return`:

Return
------

cb on success, NULL if cb is not found

.. _`mei_cl_read_cb_flush`:

mei_cl_read_cb_flush
====================

.. c:function:: void mei_cl_read_cb_flush(const struct mei_cl *cl, const struct file *fp)

    free client's read pending and completed cbs for a specific file

    :param const struct mei_cl \*cl:
        host client

    :param const struct file \*fp:
        file pointer (matching cb file object), may be NULL

.. _`mei_cl_flush_queues`:

mei_cl_flush_queues
===================

.. c:function:: int mei_cl_flush_queues(struct mei_cl *cl, const struct file *fp)

    flushes queue lists belonging to cl.

    :param struct mei_cl \*cl:
        host client

    :param const struct file \*fp:
        file pointer (matching cb file object), may be NULL

.. _`mei_cl_flush_queues.return`:

Return
------

0 on success, -EINVAL if cl or cl->dev is NULL.

.. _`mei_cl_init`:

mei_cl_init
===========

.. c:function:: void mei_cl_init(struct mei_cl *cl, struct mei_device *dev)

    initializes cl.

    :param struct mei_cl \*cl:
        host client to be initialized

    :param struct mei_device \*dev:
        mei device

.. _`mei_cl_allocate`:

mei_cl_allocate
===============

.. c:function:: struct mei_cl *mei_cl_allocate(struct mei_device *dev)

    allocates cl  structure and sets it up.

    :param struct mei_device \*dev:
        mei device

.. _`mei_cl_allocate.return`:

Return
------

The allocated file or NULL on failure

.. _`mei_cl_link`:

mei_cl_link
===========

.. c:function:: int mei_cl_link(struct mei_cl *cl)

    allocate host id in the host map

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_link.return`:

Return
------

0 on success
-EINVAL on incorrect values
-EMFILE if open count exceeded.

.. _`mei_cl_unlink`:

mei_cl_unlink
=============

.. c:function:: int mei_cl_unlink(struct mei_cl *cl)

    remove host client from the list

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_unlink.return`:

Return
------

always 0

.. _`mei_hbuf_acquire`:

mei_hbuf_acquire
================

.. c:function:: bool mei_hbuf_acquire(struct mei_device *dev)

    try to acquire host buffer

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbuf_acquire.return`:

Return
------

true if host buffer was acquired

.. _`mei_cl_wake_all`:

mei_cl_wake_all
===============

.. c:function:: void mei_cl_wake_all(struct mei_cl *cl)

    wake up readers, writers and event waiters so they can be interrupted

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_set_disconnected`:

mei_cl_set_disconnected
=======================

.. c:function:: void mei_cl_set_disconnected(struct mei_cl *cl)

    set disconnected state and clear associated states and resources

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_irq_disconnect`:

mei_cl_irq_disconnect
=====================

.. c:function:: int mei_cl_irq_disconnect(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    processes close related operation from interrupt thread context - send disconnect request

    :param struct mei_cl \*cl:
        client

    :param struct mei_cl_cb \*cb:
        callback block.

    :param struct mei_cl_cb \*cmpl_list:
        complete list.

.. _`mei_cl_irq_disconnect.return`:

Return
------

0, OK; otherwise, error.

.. _`__mei_cl_disconnect`:

__mei_cl_disconnect
===================

.. c:function:: int __mei_cl_disconnect(struct mei_cl *cl)

    disconnect host client from the me one internal function runtime pm has to be already acquired

    :param struct mei_cl \*cl:
        host client

.. _`__mei_cl_disconnect.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_cl_disconnect`:

mei_cl_disconnect
=================

.. c:function:: int mei_cl_disconnect(struct mei_cl *cl)

    disconnect host client from the me one

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_disconnect.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_disconnect.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_cl_is_other_connecting`:

mei_cl_is_other_connecting
==========================

.. c:function:: bool mei_cl_is_other_connecting(struct mei_cl *cl)

    checks if other client with the same me client id is connecting

    :param struct mei_cl \*cl:
        private data of the file object

.. _`mei_cl_is_other_connecting.return`:

Return
------

true if other client is connected, false - otherwise.

.. _`mei_cl_send_connect`:

mei_cl_send_connect
===================

.. c:function:: int mei_cl_send_connect(struct mei_cl *cl, struct mei_cl_cb *cb)

    send connect request

    :param struct mei_cl \*cl:
        host client

    :param struct mei_cl_cb \*cb:
        callback block

.. _`mei_cl_send_connect.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_cl_irq_connect`:

mei_cl_irq_connect
==================

.. c:function:: int mei_cl_irq_connect(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    send connect request in irq_thread context

    :param struct mei_cl \*cl:
        host client

    :param struct mei_cl_cb \*cb:
        callback block

    :param struct mei_cl_cb \*cmpl_list:
        complete list

.. _`mei_cl_irq_connect.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_cl_connect`:

mei_cl_connect
==============

.. c:function:: int mei_cl_connect(struct mei_cl *cl, struct mei_me_client *me_cl, const struct file *file)

    connect host client to the me one

    :param struct mei_cl \*cl:
        host client

    :param struct mei_me_client \*me_cl:
        me client

    :param const struct file \*file:
        pointer to file structure

.. _`mei_cl_connect.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_connect.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_cl_alloc_linked`:

mei_cl_alloc_linked
===================

.. c:function:: struct mei_cl *mei_cl_alloc_linked(struct mei_device *dev)

    allocate and link host client

    :param struct mei_device \*dev:
        the device structure

.. _`mei_cl_alloc_linked.return`:

Return
------

cl on success ERR_PTR on failure

.. _`mei_cl_flow_ctrl_creds`:

mei_cl_flow_ctrl_creds
======================

.. c:function:: int mei_cl_flow_ctrl_creds(struct mei_cl *cl, const struct file *fp)

    checks flow_control credits for cl.

    :param struct mei_cl \*cl:
        host client

    :param const struct file \*fp:
        the file pointer associated with the pointer

.. _`mei_cl_flow_ctrl_creds.return`:

Return
------

1 if mei_flow_ctrl_creds >0, 0 - otherwise.

.. _`mei_cl_flow_ctrl_reduce`:

mei_cl_flow_ctrl_reduce
=======================

.. c:function:: int mei_cl_flow_ctrl_reduce(struct mei_cl *cl)

    reduces flow_control.

    :param struct mei_cl \*cl:
        private data of the file object

.. _`mei_cl_flow_ctrl_reduce.return`:

Return
------

0 on success
-EINVAL when ctrl credits are <= 0

.. _`mei_cl_notify_fop2req`:

mei_cl_notify_fop2req
=====================

.. c:function:: u8 mei_cl_notify_fop2req(enum mei_cb_file_ops fop)

    convert fop to proper request

    :param enum mei_cb_file_ops fop:
        client notification start response command

.. _`mei_cl_notify_fop2req.return`:

Return
------

MEI_HBM_NOTIFICATION_START/STOP

.. _`mei_cl_notify_req2fop`:

mei_cl_notify_req2fop
=====================

.. c:function:: enum mei_cb_file_ops mei_cl_notify_req2fop(u8 req)

    convert notification request top file operation type

    :param u8 req:
        hbm notification request type

.. _`mei_cl_notify_req2fop.return`:

Return
------

MEI_FOP_NOTIFY_START/STOP

.. _`mei_cl_irq_notify`:

mei_cl_irq_notify
=================

.. c:function:: int mei_cl_irq_notify(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    send notification request in irq_thread context

    :param struct mei_cl \*cl:
        client

    :param struct mei_cl_cb \*cb:
        callback block.

    :param struct mei_cl_cb \*cmpl_list:
        complete list.

.. _`mei_cl_irq_notify.return`:

Return
------

0 on such and error otherwise.

.. _`mei_cl_notify_request`:

mei_cl_notify_request
=====================

.. c:function:: int mei_cl_notify_request(struct mei_cl *cl, const struct file *file, u8 request)

    send notification stop/start request

    :param struct mei_cl \*cl:
        host client

    :param const struct file \*file:
        associate request with file

    :param u8 request:
        1 for start or 0 for stop

.. _`mei_cl_notify_request.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_notify_request.return`:

Return
------

0 on such and error otherwise.

.. _`mei_cl_notify`:

mei_cl_notify
=============

.. c:function:: void mei_cl_notify(struct mei_cl *cl)

    raise notification

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_notify.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_notify_get`:

mei_cl_notify_get
=================

.. c:function:: int mei_cl_notify_get(struct mei_cl *cl, bool block, bool *notify_ev)

    get or wait for notification event

    :param struct mei_cl \*cl:
        host client

    :param bool block:
        this request is blocking

    :param bool \*notify_ev:
        true if notification event was received

.. _`mei_cl_notify_get.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_notify_get.return`:

Return
------

0 on such and error otherwise.

.. _`mei_cl_is_read_fc_cb`:

mei_cl_is_read_fc_cb
====================

.. c:function:: bool mei_cl_is_read_fc_cb(struct mei_cl *cl)

    check if read cb is waiting for flow control for given host client

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_is_read_fc_cb.return`:

Return
------

true, if found at least one cb.

.. _`mei_cl_read_start`:

mei_cl_read_start
=================

.. c:function:: int mei_cl_read_start(struct mei_cl *cl, size_t length, const struct file *fp)

    the start read client message function.

    :param struct mei_cl \*cl:
        host client

    :param size_t length:
        number of bytes to read

    :param const struct file \*fp:
        pointer to file structure

.. _`mei_cl_read_start.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_cl_irq_write`:

mei_cl_irq_write
================

.. c:function:: int mei_cl_irq_write(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    write a message to device from the interrupt thread context

    :param struct mei_cl \*cl:
        client

    :param struct mei_cl_cb \*cb:
        callback block.

    :param struct mei_cl_cb \*cmpl_list:
        complete list.

.. _`mei_cl_irq_write.return`:

Return
------

0, OK; otherwise error.

.. _`mei_cl_write`:

mei_cl_write
============

.. c:function:: int mei_cl_write(struct mei_cl *cl, struct mei_cl_cb *cb, bool blocking)

    submit a write cb to mei device assumes device_lock is locked

    :param struct mei_cl \*cl:
        host client

    :param struct mei_cl_cb \*cb:
        write callback with filled data

    :param bool blocking:
        block until completed

.. _`mei_cl_write.return`:

Return
------

number of bytes sent on success, <0 on failure.

.. _`mei_cl_complete`:

mei_cl_complete
===============

.. c:function:: void mei_cl_complete(struct mei_cl *cl, struct mei_cl_cb *cb)

    processes completed operation for a client

    :param struct mei_cl \*cl:
        private data of the file object.

    :param struct mei_cl_cb \*cb:
        callback block.

.. _`mei_cl_all_disconnect`:

mei_cl_all_disconnect
=====================

.. c:function:: void mei_cl_all_disconnect(struct mei_device *dev)

    disconnect forcefully all connected clients

    :param struct mei_device \*dev:
        mei device

.. This file was automatic generated / don't edit.


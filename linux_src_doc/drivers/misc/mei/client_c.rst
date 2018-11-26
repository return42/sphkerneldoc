.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/client.c

.. _`mei_me_cl_init`:

mei_me_cl_init
==============

.. c:function:: void mei_me_cl_init(struct mei_me_client *me_cl)

    initialize me client

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`mei_me_cl_get`:

mei_me_cl_get
=============

.. c:function:: struct mei_me_client *mei_me_cl_get(struct mei_me_client *me_cl)

    increases me client refcount

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

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

    :param ref:
        me_client refcount
    :type ref: struct kref \*

.. _`mei_me_cl_release.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_put`:

mei_me_cl_put
=============

.. c:function:: void mei_me_cl_put(struct mei_me_client *me_cl)

    decrease me client refcount and free client if necessary

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`mei_me_cl_put.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`__mei_me_cl_del`:

\__mei_me_cl_del
================

.. c:function:: void __mei_me_cl_del(struct mei_device *dev, struct mei_me_client *me_cl)

    delete me client from the list and decrease reference counter

    :param dev:
        mei device
    :type dev: struct mei_device \*

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`__mei_me_cl_del.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`mei_me_cl_del`:

mei_me_cl_del
=============

.. c:function:: void mei_me_cl_del(struct mei_device *dev, struct mei_me_client *me_cl)

    delete me client from the list and decrease reference counter

    :param dev:
        mei device
    :type dev: struct mei_device \*

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`mei_me_cl_add`:

mei_me_cl_add
=============

.. c:function:: void mei_me_cl_add(struct mei_device *dev, struct mei_me_client *me_cl)

    add me client to the list

    :param dev:
        mei device
    :type dev: struct mei_device \*

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`__mei_me_cl_by_uuid`:

\__mei_me_cl_by_uuid
====================

.. c:function:: struct mei_me_client *__mei_me_cl_by_uuid(struct mei_device *dev, const uuid_le *uuid)

    locate me client by uuid increases ref count

    :param dev:
        mei device
    :type dev: struct mei_device \*

    :param uuid:
        me client uuid
    :type uuid: const uuid_le \*

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

    :param dev:
        mei device
    :type dev: struct mei_device \*

    :param uuid:
        me client uuid
    :type uuid: const uuid_le \*

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

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param client_id:
        me client id
    :type client_id: u8

.. _`mei_me_cl_by_id.return`:

Return
------

me client or NULL if not found

.. _`mei_me_cl_by_id.locking`:

Locking
-------

dev->me_clients_rwsem

.. _`__mei_me_cl_by_uuid_id`:

\__mei_me_cl_by_uuid_id
=======================

.. c:function:: struct mei_me_client *__mei_me_cl_by_uuid_id(struct mei_device *dev, const uuid_le *uuid, u8 client_id)

    locate me client by client id and uuid increases ref count

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param uuid:
        me client uuid
    :type uuid: const uuid_le \*

    :param client_id:
        me client id
    :type client_id: u8

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

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param uuid:
        me client uuid
    :type uuid: const uuid_le \*

    :param client_id:
        me client id
    :type client_id: u8

.. _`mei_me_cl_by_uuid_id.return`:

Return
------

me client or null if not found

.. _`mei_me_cl_rm_by_uuid`:

mei_me_cl_rm_by_uuid
====================

.. c:function:: void mei_me_cl_rm_by_uuid(struct mei_device *dev, const uuid_le *uuid)

    remove all me clients matching uuid

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param uuid:
        me client uuid
    :type uuid: const uuid_le \*

.. _`mei_me_cl_rm_by_uuid.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_rm_by_uuid_id`:

mei_me_cl_rm_by_uuid_id
=======================

.. c:function:: void mei_me_cl_rm_by_uuid_id(struct mei_device *dev, const uuid_le *uuid, u8 id)

    remove all me clients matching client id

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param uuid:
        me client uuid
    :type uuid: const uuid_le \*

    :param id:
        me client id
    :type id: u8

.. _`mei_me_cl_rm_by_uuid_id.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_me_cl_rm_all`:

mei_me_cl_rm_all
================

.. c:function:: void mei_me_cl_rm_all(struct mei_device *dev)

    remove all me clients

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_me_cl_rm_all.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_cmp_id`:

mei_cl_cmp_id
=============

.. c:function:: bool mei_cl_cmp_id(const struct mei_cl *cl1, const struct mei_cl *cl2)

    tells if the clients are the same

    :param cl1:
        host client 1
    :type cl1: const struct mei_cl \*

    :param cl2:
        host client 2
    :type cl2: const struct mei_cl \*

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

    :param cb:
        mei callback struct
    :type cb: struct mei_cl_cb \*

.. _`mei_tx_cb_enqueue`:

mei_tx_cb_enqueue
=================

.. c:function:: void mei_tx_cb_enqueue(struct mei_cl_cb *cb, struct list_head *head)

    queue tx callback

    :param cb:
        mei callback struct
    :type cb: struct mei_cl_cb \*

    :param head:
        an instance of list to queue on
    :type head: struct list_head \*

.. _`mei_tx_cb_enqueue.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_tx_cb_dequeue`:

mei_tx_cb_dequeue
=================

.. c:function:: void mei_tx_cb_dequeue(struct mei_cl_cb *cb)

    dequeue tx callback

    :param cb:
        mei callback struct to dequeue and free
    :type cb: struct mei_cl_cb \*

.. _`mei_tx_cb_dequeue.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_io_cb_init`:

mei_io_cb_init
==============

.. c:function:: struct mei_cl_cb *mei_io_cb_init(struct mei_cl *cl, enum mei_cb_file_ops type, const struct file *fp)

    allocate and initialize io callback

    :param cl:
        mei client
    :type cl: struct mei_cl \*

    :param type:
        operation type
    :type type: enum mei_cb_file_ops

    :param fp:
        pointer to file structure
    :type fp: const struct file \*

.. _`mei_io_cb_init.return`:

Return
------

mei_cl_cb pointer or NULL;

.. _`mei_io_list_flush_cl`:

mei_io_list_flush_cl
====================

.. c:function:: void mei_io_list_flush_cl(struct list_head *head, const struct mei_cl *cl)

    removes cbs belonging to the cl.

    :param head:
        an instance of our list structure
    :type head: struct list_head \*

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_io_tx_list_free_cl`:

mei_io_tx_list_free_cl
======================

.. c:function:: void mei_io_tx_list_free_cl(struct list_head *head, const struct mei_cl *cl)

    removes cb belonging to the cl and free them

    :param head:
        An instance of our list structure
    :type head: struct list_head \*

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_io_list_free_fp`:

mei_io_list_free_fp
===================

.. c:function:: void mei_io_list_free_fp(struct list_head *head, const struct file *fp)

    free cb from a list that matches file pointer

    :param head:
        io list
    :type head: struct list_head \*

    :param fp:
        file pointer (matching cb file object), may be NULL
    :type fp: const struct file \*

.. _`mei_cl_alloc_cb`:

mei_cl_alloc_cb
===============

.. c:function:: struct mei_cl_cb *mei_cl_alloc_cb(struct mei_cl *cl, size_t length, enum mei_cb_file_ops fop_type, const struct file *fp)

    a convenient wrapper for allocating read cb

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param length:
        size of the buffer
    :type length: size_t

    :param fop_type:
        operation type
    :type fop_type: enum mei_cb_file_ops

    :param fp:
        associated file pointer (might be NULL)
    :type fp: const struct file \*

.. _`mei_cl_alloc_cb.return`:

Return
------

cb on success and NULL on failure

.. _`mei_cl_enqueue_ctrl_wr_cb`:

mei_cl_enqueue_ctrl_wr_cb
=========================

.. c:function:: struct mei_cl_cb *mei_cl_enqueue_ctrl_wr_cb(struct mei_cl *cl, size_t length, enum mei_cb_file_ops fop_type, const struct file *fp)

    a convenient wrapper for allocating and enqueuing of the control commands cb

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param length:
        size of the buffer
    :type length: size_t

    :param fop_type:
        operation type
    :type fop_type: enum mei_cb_file_ops

    :param fp:
        associated file pointer (might be NULL)
    :type fp: const struct file \*

.. _`mei_cl_enqueue_ctrl_wr_cb.return`:

Return
------

cb on success and NULL on failure

.. _`mei_cl_enqueue_ctrl_wr_cb.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_read_cb`:

mei_cl_read_cb
==============

.. c:function:: struct mei_cl_cb *mei_cl_read_cb(const struct mei_cl *cl, const struct file *fp)

    find this cl's callback in the read list for a specific file

    :param cl:
        host client
    :type cl: const struct mei_cl \*

    :param fp:
        file pointer (matching cb file object), may be NULL
    :type fp: const struct file \*

.. _`mei_cl_read_cb.return`:

Return
------

cb on success, NULL if cb is not found

.. _`mei_cl_flush_queues`:

mei_cl_flush_queues
===================

.. c:function:: int mei_cl_flush_queues(struct mei_cl *cl, const struct file *fp)

    flushes queue lists belonging to cl.

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param fp:
        file pointer (matching cb file object), may be NULL
    :type fp: const struct file \*

.. _`mei_cl_flush_queues.return`:

Return
------

0 on success, -EINVAL if cl or cl->dev is NULL.

.. _`mei_cl_init`:

mei_cl_init
===========

.. c:function:: void mei_cl_init(struct mei_cl *cl, struct mei_device *dev)

    initializes cl.

    :param cl:
        host client to be initialized
    :type cl: struct mei_cl \*

    :param dev:
        mei device
    :type dev: struct mei_device \*

.. _`mei_cl_allocate`:

mei_cl_allocate
===============

.. c:function:: struct mei_cl *mei_cl_allocate(struct mei_device *dev)

    allocates cl  structure and sets it up.

    :param dev:
        mei device
    :type dev: struct mei_device \*

.. _`mei_cl_allocate.return`:

Return
------

The allocated file or NULL on failure

.. _`mei_cl_link`:

mei_cl_link
===========

.. c:function:: int mei_cl_link(struct mei_cl *cl)

    allocate host id in the host map

    :param cl:
        host client
    :type cl: struct mei_cl \*

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

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_unlink.return`:

Return
------

always 0

.. _`mei_hbuf_acquire`:

mei_hbuf_acquire
================

.. c:function:: bool mei_hbuf_acquire(struct mei_device *dev)

    try to acquire host buffer

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_hbuf_acquire.return`:

Return
------

true if host buffer was acquired

.. _`mei_cl_wake_all`:

mei_cl_wake_all
===============

.. c:function:: void mei_cl_wake_all(struct mei_cl *cl)

    wake up readers, writers and event waiters so they can be interrupted

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_set_disconnected`:

mei_cl_set_disconnected
=======================

.. c:function:: void mei_cl_set_disconnected(struct mei_cl *cl)

    set disconnected state and clear associated states and resources

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_irq_disconnect`:

mei_cl_irq_disconnect
=====================

.. c:function:: int mei_cl_irq_disconnect(struct mei_cl *cl, struct mei_cl_cb *cb, struct list_head *cmpl_list)

    processes close related operation from interrupt thread context - send disconnect request

    :param cl:
        client
    :type cl: struct mei_cl \*

    :param cb:
        callback block.
    :type cb: struct mei_cl_cb \*

    :param cmpl_list:
        complete list.
    :type cmpl_list: struct list_head \*

.. _`mei_cl_irq_disconnect.return`:

Return
------

0, OK; otherwise, error.

.. _`__mei_cl_disconnect`:

\__mei_cl_disconnect
====================

.. c:function:: int __mei_cl_disconnect(struct mei_cl *cl)

    disconnect host client from the me one internal function runtime pm has to be already acquired

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`__mei_cl_disconnect.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_cl_disconnect`:

mei_cl_disconnect
=================

.. c:function:: int mei_cl_disconnect(struct mei_cl *cl)

    disconnect host client from the me one

    :param cl:
        host client
    :type cl: struct mei_cl \*

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

    :param cl:
        private data of the file object
    :type cl: struct mei_cl \*

.. _`mei_cl_is_other_connecting.return`:

Return
------

true if other client is connected, false - otherwise.

.. _`mei_cl_send_connect`:

mei_cl_send_connect
===================

.. c:function:: int mei_cl_send_connect(struct mei_cl *cl, struct mei_cl_cb *cb)

    send connect request

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param cb:
        callback block
    :type cb: struct mei_cl_cb \*

.. _`mei_cl_send_connect.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_cl_irq_connect`:

mei_cl_irq_connect
==================

.. c:function:: int mei_cl_irq_connect(struct mei_cl *cl, struct mei_cl_cb *cb, struct list_head *cmpl_list)

    send connect request in irq_thread context

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param cb:
        callback block
    :type cb: struct mei_cl_cb \*

    :param cmpl_list:
        complete list
    :type cmpl_list: struct list_head \*

.. _`mei_cl_irq_connect.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_cl_connect`:

mei_cl_connect
==============

.. c:function:: int mei_cl_connect(struct mei_cl *cl, struct mei_me_client *me_cl, const struct file *fp)

    connect host client to the me one

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

    :param fp:
        pointer to file structure
    :type fp: const struct file \*

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

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_cl_alloc_linked.return`:

Return
------

cl on success ERR_PTR on failure

.. _`mei_cl_tx_flow_ctrl_creds`:

mei_cl_tx_flow_ctrl_creds
=========================

.. c:function:: int mei_cl_tx_flow_ctrl_creds(struct mei_cl *cl)

    checks flow_control credits for cl.

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_tx_flow_ctrl_creds.return`:

Return
------

1 if tx_flow_ctrl_creds >0, 0 - otherwise.

.. _`mei_cl_tx_flow_ctrl_creds_reduce`:

mei_cl_tx_flow_ctrl_creds_reduce
================================

.. c:function:: int mei_cl_tx_flow_ctrl_creds_reduce(struct mei_cl *cl)

    reduces transmit flow control credits for a client

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_tx_flow_ctrl_creds_reduce.return`:

Return
------

0 on success
-EINVAL when ctrl credits are <= 0

.. _`mei_cl_notify_fop2req`:

mei_cl_notify_fop2req
=====================

.. c:function:: u8 mei_cl_notify_fop2req(enum mei_cb_file_ops fop)

    convert fop to proper request

    :param fop:
        client notification start response command
    :type fop: enum mei_cb_file_ops

.. _`mei_cl_notify_fop2req.return`:

Return
------

MEI_HBM_NOTIFICATION_START/STOP

.. _`mei_cl_notify_req2fop`:

mei_cl_notify_req2fop
=====================

.. c:function:: enum mei_cb_file_ops mei_cl_notify_req2fop(u8 req)

    convert notification request top file operation type

    :param req:
        hbm notification request type
    :type req: u8

.. _`mei_cl_notify_req2fop.return`:

Return
------

MEI_FOP_NOTIFY_START/STOP

.. _`mei_cl_irq_notify`:

mei_cl_irq_notify
=================

.. c:function:: int mei_cl_irq_notify(struct mei_cl *cl, struct mei_cl_cb *cb, struct list_head *cmpl_list)

    send notification request in irq_thread context

    :param cl:
        client
    :type cl: struct mei_cl \*

    :param cb:
        callback block.
    :type cb: struct mei_cl_cb \*

    :param cmpl_list:
        complete list.
    :type cmpl_list: struct list_head \*

.. _`mei_cl_irq_notify.return`:

Return
------

0 on such and error otherwise.

.. _`mei_cl_notify_request`:

mei_cl_notify_request
=====================

.. c:function:: int mei_cl_notify_request(struct mei_cl *cl, const struct file *fp, u8 request)

    send notification stop/start request

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param fp:
        associate request with file
    :type fp: const struct file \*

    :param request:
        1 for start or 0 for stop
    :type request: u8

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

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_notify.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_notify_get`:

mei_cl_notify_get
=================

.. c:function:: int mei_cl_notify_get(struct mei_cl *cl, bool block, bool *notify_ev)

    get or wait for notification event

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param block:
        this request is blocking
    :type block: bool

    :param notify_ev:
        true if notification event was received
    :type notify_ev: bool \*

.. _`mei_cl_notify_get.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_cl_notify_get.return`:

Return
------

0 on such and error otherwise.

.. _`mei_cl_read_start`:

mei_cl_read_start
=================

.. c:function:: int mei_cl_read_start(struct mei_cl *cl, size_t length, const struct file *fp)

    the start read client message function.

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param length:
        number of bytes to read
    :type length: size_t

    :param fp:
        pointer to file structure
    :type fp: const struct file \*

.. _`mei_cl_read_start.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_msg_hdr_init`:

mei_msg_hdr_init
================

.. c:function:: void mei_msg_hdr_init(struct mei_msg_hdr *mei_hdr, struct mei_cl_cb *cb)

    initialize mei message header

    :param mei_hdr:
        mei message header
    :type mei_hdr: struct mei_msg_hdr \*

    :param cb:
        message callback structure
    :type cb: struct mei_cl_cb \*

.. _`mei_cl_irq_write`:

mei_cl_irq_write
================

.. c:function:: int mei_cl_irq_write(struct mei_cl *cl, struct mei_cl_cb *cb, struct list_head *cmpl_list)

    write a message to device from the interrupt thread context

    :param cl:
        client
    :type cl: struct mei_cl \*

    :param cb:
        callback block.
    :type cb: struct mei_cl_cb \*

    :param cmpl_list:
        complete list.
    :type cmpl_list: struct list_head \*

.. _`mei_cl_irq_write.return`:

Return
------

0, OK; otherwise error.

.. _`mei_cl_write`:

mei_cl_write
============

.. c:function:: ssize_t mei_cl_write(struct mei_cl *cl, struct mei_cl_cb *cb)

    submit a write cb to mei device assumes device_lock is locked

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param cb:
        write callback with filled data
    :type cb: struct mei_cl_cb \*

.. _`mei_cl_write.return`:

Return
------

number of bytes sent on success, <0 on failure.

.. _`mei_cl_complete`:

mei_cl_complete
===============

.. c:function:: void mei_cl_complete(struct mei_cl *cl, struct mei_cl_cb *cb)

    processes completed operation for a client

    :param cl:
        private data of the file object.
    :type cl: struct mei_cl \*

    :param cb:
        callback block.
    :type cb: struct mei_cl_cb \*

.. _`mei_cl_all_disconnect`:

mei_cl_all_disconnect
=====================

.. c:function:: void mei_cl_all_disconnect(struct mei_device *dev)

    disconnect forcefully all connected clients

    :param dev:
        mei device
    :type dev: struct mei_device \*

.. This file was automatic generated / don't edit.


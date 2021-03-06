.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/ctl.c

.. _`tb_ctl`:

struct tb_ctl
=============

.. c:type:: struct tb_ctl

    thunderbolt control channel

.. _`tb_ctl.definition`:

Definition
----------

.. code-block:: c

    struct tb_ctl {
        struct tb_nhi *nhi;
        struct tb_ring *tx;
        struct tb_ring *rx;
        struct dma_pool *frame_pool;
        struct ctl_pkg *rx_packets[TB_CTL_RX_PKG_COUNT];
        struct mutex request_queue_lock;
        struct list_head request_queue;
        bool running;
        event_cb callback;
        void *callback_data;
    }

.. _`tb_ctl.members`:

Members
-------

nhi
    *undescribed*

tx
    *undescribed*

rx
    *undescribed*

frame_pool
    *undescribed*

rx_packets
    *undescribed*

request_queue_lock
    *undescribed*

request_queue
    *undescribed*

running
    *undescribed*

callback
    *undescribed*

callback_data
    *undescribed*

.. _`tb_cfg_request_alloc`:

tb_cfg_request_alloc
====================

.. c:function:: struct tb_cfg_request *tb_cfg_request_alloc( void)

    Allocates a new config request

    :param void:
        no arguments
    :type void: 

.. _`tb_cfg_request_alloc.description`:

Description
-----------

This is refcounted object so when you are done with this, call
\ :c:func:`tb_cfg_request_put`\  to it.

.. _`tb_cfg_request_get`:

tb_cfg_request_get
==================

.. c:function:: void tb_cfg_request_get(struct tb_cfg_request *req)

    Increase refcount of a request

    :param req:
        Request whose refcount is increased
    :type req: struct tb_cfg_request \*

.. _`tb_cfg_request_put`:

tb_cfg_request_put
==================

.. c:function:: void tb_cfg_request_put(struct tb_cfg_request *req)

    Decrease refcount and possibly release the request

    :param req:
        Request whose refcount is decreased
    :type req: struct tb_cfg_request \*

.. _`tb_cfg_request_put.description`:

Description
-----------

Call this function when you are done with the request. When refcount
goes to \ ``0``\  the object is released.

.. _`tb_ctl_tx`:

tb_ctl_tx
=========

.. c:function:: int tb_ctl_tx(struct tb_ctl *ctl, const void *data, size_t len, enum tb_cfg_pkg_type type)

    transmit a packet on the control channel

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param data:
        *undescribed*
    :type data: const void \*

    :param len:
        *undescribed*
    :type len: size_t

    :param type:
        *undescribed*
    :type type: enum tb_cfg_pkg_type

.. _`tb_ctl_tx.description`:

Description
-----------

len must be a multiple of four.

.. _`tb_ctl_tx.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_ctl_handle_event`:

tb_ctl_handle_event
===================

.. c:function:: bool tb_ctl_handle_event(struct tb_ctl *ctl, enum tb_cfg_pkg_type type, struct ctl_pkg *pkg, size_t size)

    acknowledge a plug event, invoke ctl->callback

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param type:
        *undescribed*
    :type type: enum tb_cfg_pkg_type

    :param pkg:
        *undescribed*
    :type pkg: struct ctl_pkg \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`tb_cfg_request`:

tb_cfg_request
==============

.. c:function:: int tb_cfg_request(struct tb_ctl *ctl, struct tb_cfg_request *req, void (*callback)(void *), void *callback_data)

    Start control request not waiting for it to complete

    :param ctl:
        Control channel to use
    :type ctl: struct tb_ctl \*

    :param req:
        Request to start
    :type req: struct tb_cfg_request \*

    :param void (\*callback)(void \*):
        Callback called when the request is completed

    :param callback_data:
        Data to be passed to \ ``callback``\ 
    :type callback_data: void \*

.. _`tb_cfg_request.description`:

Description
-----------

This queues \ ``req``\  on the given control channel without waiting for it
to complete. When the request completes \ ``callback``\  is called.

.. _`tb_cfg_request_cancel`:

tb_cfg_request_cancel
=====================

.. c:function:: void tb_cfg_request_cancel(struct tb_cfg_request *req, int err)

    Cancel a control request

    :param req:
        Request to cancel
    :type req: struct tb_cfg_request \*

    :param err:
        Error to assign to the request
    :type err: int

.. _`tb_cfg_request_cancel.description`:

Description
-----------

This function can be used to cancel ongoing request. It will wait
until the request is not active anymore.

.. _`tb_cfg_request_sync`:

tb_cfg_request_sync
===================

.. c:function:: struct tb_cfg_result tb_cfg_request_sync(struct tb_ctl *ctl, struct tb_cfg_request *req, int timeout_msec)

    Start control request and wait until it completes

    :param ctl:
        Control channel to use
    :type ctl: struct tb_ctl \*

    :param req:
        Request to start
    :type req: struct tb_cfg_request \*

    :param timeout_msec:
        Timeout how long to wait \ ``req``\  to complete
    :type timeout_msec: int

.. _`tb_cfg_request_sync.description`:

Description
-----------

Starts a control request and waits until it completes. If timeout
triggers the request is canceled before function returns. Note the
caller needs to make sure only one message for given switch is active
at a time.

.. _`tb_ctl_alloc`:

tb_ctl_alloc
============

.. c:function:: struct tb_ctl *tb_ctl_alloc(struct tb_nhi *nhi, event_cb cb, void *cb_data)

    allocate a control channel

    :param nhi:
        *undescribed*
    :type nhi: struct tb_nhi \*

    :param cb:
        *undescribed*
    :type cb: event_cb

    :param cb_data:
        *undescribed*
    :type cb_data: void \*

.. _`tb_ctl_alloc.description`:

Description
-----------

cb will be invoked once for every hot plug event.

.. _`tb_ctl_alloc.return`:

Return
------

Returns a pointer on success or NULL on failure.

.. _`tb_ctl_free`:

tb_ctl_free
===========

.. c:function:: void tb_ctl_free(struct tb_ctl *ctl)

    free a control channel

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

.. _`tb_ctl_free.description`:

Description
-----------

Must be called after tb_ctl_stop.

Must NOT be called from ctl->callback.

.. _`tb_ctl_start`:

tb_ctl_start
============

.. c:function:: void tb_ctl_start(struct tb_ctl *ctl)

    start/resume the control channel

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

.. _`tb_ctl_stop`:

tb_ctl_stop
===========

.. c:function:: void tb_ctl_stop(struct tb_ctl *ctl)

    pause the control channel

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

.. _`tb_ctl_stop.description`:

Description
-----------

All invocations of ctl->callback will have finished after this method
returns.

Must NOT be called from ctl->callback.

.. _`tb_cfg_error`:

tb_cfg_error
============

.. c:function:: int tb_cfg_error(struct tb_ctl *ctl, u64 route, u32 port, enum tb_cfg_error error)

    send error packet

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param route:
        *undescribed*
    :type route: u64

    :param port:
        *undescribed*
    :type port: u32

    :param error:
        *undescribed*
    :type error: enum tb_cfg_error

.. _`tb_cfg_error.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_cfg_reset`:

tb_cfg_reset
============

.. c:function:: struct tb_cfg_result tb_cfg_reset(struct tb_ctl *ctl, u64 route, int timeout_msec)

    send a reset packet and wait for a response

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param route:
        *undescribed*
    :type route: u64

    :param timeout_msec:
        *undescribed*
    :type timeout_msec: int

.. _`tb_cfg_reset.description`:

Description
-----------

If the switch at route is incorrectly configured then we will not receive a
reply (even though the switch will reset). The caller should check for
-ETIMEDOUT and attempt to reconfigure the switch.

.. _`tb_cfg_read_raw`:

tb_cfg_read_raw
===============

.. c:function:: struct tb_cfg_result tb_cfg_read_raw(struct tb_ctl *ctl, void *buffer, u64 route, u32 port, enum tb_cfg_space space, u32 offset, u32 length, int timeout_msec)

    read from config space into buffer

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param buffer:
        *undescribed*
    :type buffer: void \*

    :param route:
        *undescribed*
    :type route: u64

    :param port:
        *undescribed*
    :type port: u32

    :param space:
        *undescribed*
    :type space: enum tb_cfg_space

    :param offset:
        *undescribed*
    :type offset: u32

    :param length:
        *undescribed*
    :type length: u32

    :param timeout_msec:
        *undescribed*
    :type timeout_msec: int

.. _`tb_cfg_read_raw.description`:

Description
-----------

Offset and length are in dwords.

.. _`tb_cfg_write_raw`:

tb_cfg_write_raw
================

.. c:function:: struct tb_cfg_result tb_cfg_write_raw(struct tb_ctl *ctl, const void *buffer, u64 route, u32 port, enum tb_cfg_space space, u32 offset, u32 length, int timeout_msec)

    write from buffer into config space

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param buffer:
        *undescribed*
    :type buffer: const void \*

    :param route:
        *undescribed*
    :type route: u64

    :param port:
        *undescribed*
    :type port: u32

    :param space:
        *undescribed*
    :type space: enum tb_cfg_space

    :param offset:
        *undescribed*
    :type offset: u32

    :param length:
        *undescribed*
    :type length: u32

    :param timeout_msec:
        *undescribed*
    :type timeout_msec: int

.. _`tb_cfg_write_raw.description`:

Description
-----------

Offset and length are in dwords.

.. _`tb_cfg_get_upstream_port`:

tb_cfg_get_upstream_port
========================

.. c:function:: int tb_cfg_get_upstream_port(struct tb_ctl *ctl, u64 route)

    get upstream port number of switch at route

    :param ctl:
        *undescribed*
    :type ctl: struct tb_ctl \*

    :param route:
        *undescribed*
    :type route: u64

.. _`tb_cfg_get_upstream_port.description`:

Description
-----------

Reads the first dword from the switches TB_CFG_SWITCH config area and
returns the port number from which the reply originated.

.. _`tb_cfg_get_upstream_port.return`:

Return
------

Returns the upstream port number on success or an error code on
failure.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/service.c

.. _`ptlrpc_hr_select`:

ptlrpc_hr_select
================

.. c:function:: struct ptlrpc_hr_thread *ptlrpc_hr_select(struct ptlrpc_service_part *svcpt)

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`ptlrpc_dispatch_difficult_reply`:

ptlrpc_dispatch_difficult_reply
===============================

.. c:function:: void ptlrpc_dispatch_difficult_reply(struct ptlrpc_reply_state *rs)

    ACK from the client

    :param struct ptlrpc_reply_state \*rs:
        *undescribed*

.. _`ptlrpc_service_part_init`:

ptlrpc_service_part_init
========================

.. c:function:: int ptlrpc_service_part_init(struct ptlrpc_service *svc, struct ptlrpc_service_part *svcpt, int cpt)

    :param struct ptlrpc_service \*svc:
        *undescribed*

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`ptlrpc_register_service`:

ptlrpc_register_service
=======================

.. c:function:: struct ptlrpc_service *ptlrpc_register_service(struct ptlrpc_service_conf *conf, struct kset *parent, struct dentry *debugfs_entry)

    This includes starting serving threads , allocating and posting rqbds and so on.

    :param struct ptlrpc_service_conf \*conf:
        *undescribed*

    :param struct kset \*parent:
        *undescribed*

    :param struct dentry \*debugfs_entry:
        *undescribed*

.. _`ptlrpc_server_free_request`:

ptlrpc_server_free_request
==========================

.. c:function:: void ptlrpc_server_free_request(struct ptlrpc_request *req)

    note it's caller's responsibility to unlink req->rq_list.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_server_drop_request`:

ptlrpc_server_drop_request
==========================

.. c:function:: void ptlrpc_server_drop_request(struct ptlrpc_request *req)

    put it into history list, or free it immediately.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_server_finish_request`:

ptlrpc_server_finish_request
============================

.. c:function:: void ptlrpc_server_finish_request(struct ptlrpc_service_part *svcpt, struct ptlrpc_request *req)

    stop sending more early replies, and release the request.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_server_finish_active_request`:

ptlrpc_server_finish_active_request
===================================

.. c:function:: void ptlrpc_server_finish_active_request(struct ptlrpc_service_part *svcpt, struct ptlrpc_request *req)

    stop sending more early replies, and release the request. should be called after we finished handling the request.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_check_req`:

ptlrpc_check_req
================

.. c:function:: int ptlrpc_check_req(struct ptlrpc_request *req)

    Return 0 if all is ok, error code otherwise.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_server_hpreq_init`:

ptlrpc_server_hpreq_init
========================

.. c:function:: int ptlrpc_server_hpreq_init(struct ptlrpc_service_part *svcpt, struct ptlrpc_request *req)

    a high priority one.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_server_allow_high`:

ptlrpc_server_allow_high
========================

.. c:function:: bool ptlrpc_server_allow_high(struct ptlrpc_service_part *svcpt, bool force)

    User can call it w/o any lock but need to hold ptlrpc_service_part::scp_req_lock to get reliable result

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`ptlrpc_server_allow_normal`:

ptlrpc_server_allow_normal
==========================

.. c:function:: bool ptlrpc_server_allow_normal(struct ptlrpc_service_part *svcpt, bool force)

    priority queue if forced (i.e. cleanup), if there are other high priority requests already being processed (i.e. those threads can service more high-priority requests), or if there are enough idle threads that a later thread can do a high priority request. User can call it w/o any lock but need to hold ptlrpc_service_part::scp_req_lock to get reliable result

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`ptlrpc_server_request_pending`:

ptlrpc_server_request_pending
=============================

.. c:function:: bool ptlrpc_server_request_pending(struct ptlrpc_service_part *svcpt, bool force)

    request queue for processing and it is allowed to fetch them. User can call it w/o any lock but need to hold ptlrpc_service::scp_req_lock to get reliable result \see ptlrpc_server_allow_normal \see ptlrpc_server_allow high

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`ptlrpc_server_request_get`:

ptlrpc_server_request_get
=========================

.. c:function:: struct ptlrpc_request *ptlrpc_server_request_get(struct ptlrpc_service_part *svcpt, bool force)

    Favors high-priority requests. Returns a pointer to fetched request.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`ptlrpc_server_handle_req_in`:

ptlrpc_server_handle_req_in
===========================

.. c:function:: int ptlrpc_server_handle_req_in(struct ptlrpc_service_part *svcpt, struct ptlrpc_thread *thread)

    pass on to regular request queue. All incoming requests pass through here before getting into ptlrpc_server_handle_req later on.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_thread \*thread:
        *undescribed*

.. _`ptlrpc_server_handle_request`:

ptlrpc_server_handle_request
============================

.. c:function:: int ptlrpc_server_handle_request(struct ptlrpc_service_part *svcpt, struct ptlrpc_thread *thread)

    Calls handler function from service to do actual processing.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_thread \*thread:
        *undescribed*

.. _`ptlrpc_handle_rs`:

ptlrpc_handle_rs
================

.. c:function:: int ptlrpc_handle_rs(struct ptlrpc_reply_state *rs)

    :param struct ptlrpc_reply_state \*rs:
        *undescribed*

.. _`ptlrpc_threads_increasable`:

ptlrpc_threads_increasable
==========================

.. c:function:: int ptlrpc_threads_increasable(struct ptlrpc_service_part *svcpt)

    user can call it w/o any lock but need to hold ptlrpc_service_part::scp_lock to get reliable result

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`ptlrpc_threads_need_create`:

ptlrpc_threads_need_create
==========================

.. c:function:: int ptlrpc_threads_need_create(struct ptlrpc_service_part *svcpt)

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`ptlrpc_server_request_incoming`:

ptlrpc_server_request_incoming
==============================

.. c:function:: int ptlrpc_server_request_incoming(struct ptlrpc_service_part *svcpt)

    user can call it w/o any lock but need to hold ptlrpc_service_part::scp_lock to get reliable result

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`ptlrpc_main`:

ptlrpc_main
===========

.. c:function:: int ptlrpc_main(void *arg)

    Waits in a loop waiting for new requests to process to appear. Every time an incoming requests is added to its queue, a waitq is woken up and one of the threads will handle it.

    :param void \*arg:
        *undescribed*

.. _`ptlrpc_hr_main`:

ptlrpc_hr_main
==============

.. c:function:: int ptlrpc_hr_main(void *arg)

    It processes acked reply states

    :param void \*arg:
        *undescribed*

.. _`ptlrpc_stop_all_threads`:

ptlrpc_stop_all_threads
=======================

.. c:function:: void ptlrpc_stop_all_threads(struct ptlrpc_service *svc)

    :param struct ptlrpc_service \*svc:
        *undescribed*

.. _`ptlrpc_wait_replies`:

ptlrpc_wait_replies
===================

.. c:function:: void ptlrpc_wait_replies(struct ptlrpc_service_part *svcpt)

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. This file was automatic generated / don't edit.


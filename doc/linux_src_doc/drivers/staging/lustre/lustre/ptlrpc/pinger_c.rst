.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/pinger.c

.. _`ptlrpc_new_timeout`:

ptlrpc_new_timeout
==================

.. c:function:: struct timeout_item *ptlrpc_new_timeout(int time, enum timeout_event event, timeout_cb_t cb, void *data)

    be called when timeout happens.

    :param int time:
        *undescribed*

    :param enum timeout_event event:
        *undescribed*

    :param timeout_cb_t cb:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ptlrpc_pinger_register_timeout`:

ptlrpc_pinger_register_timeout
==============================

.. c:function:: struct timeout_item*ptlrpc_pinger_register_timeout(int time, enum timeout_event event, timeout_cb_t cb, void *data)

    :param int time:
        *undescribed*

    :param enum timeout_event event:
        *undescribed*

    :param timeout_cb_t cb:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ptlrpc_pinger_register_timeout.note`:

Note
----

the timeout list is an sorted list with increased timeout value.

.. This file was automatic generated / don't edit.


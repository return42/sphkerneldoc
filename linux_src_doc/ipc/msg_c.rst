.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/msg.c

.. _`newque`:

newque
======

.. c:function:: int newque(struct ipc_namespace *ns, struct ipc_params *params)

    Create a new msg queue

    :param ns:
        namespace
    :type ns: struct ipc_namespace \*

    :param params:
        ptr to the structure that contains the key and msgflg
    :type params: struct ipc_params \*

.. _`newque.description`:

Description
-----------

Called with msg_ids.rwsem held (writer)

.. This file was automatic generated / don't edit.


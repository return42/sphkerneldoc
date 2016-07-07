.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/msg.c

.. _`newque`:

newque
======

.. c:function:: int newque(struct ipc_namespace *ns, struct ipc_params *params)

    Create a new msg queue

    :param struct ipc_namespace \*ns:
        namespace

    :param struct ipc_params \*params:
        ptr to the structure that contains the key and msgflg

.. _`newque.description`:

Description
-----------

Called with msg_ids.rwsem held (writer)

.. This file was automatic generated / don't edit.


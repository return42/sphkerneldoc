.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/shm.c

.. _`newseg`:

newseg
======

.. c:function:: int newseg(struct ipc_namespace *ns, struct ipc_params *params)

    Create a new shared memory segment

    :param ns:
        namespace
    :type ns: struct ipc_namespace \*

    :param params:
        ptr to the structure that contains key, size and shmflg
    :type params: struct ipc_params \*

.. _`newseg.description`:

Description
-----------

Called with shm_ids.rwsem held as a writer.

.. This file was automatic generated / don't edit.


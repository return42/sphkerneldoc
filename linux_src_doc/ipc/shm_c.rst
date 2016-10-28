.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/shm.c

.. _`newseg`:

newseg
======

.. c:function:: int newseg(struct ipc_namespace *ns, struct ipc_params *params)

    Create a new shared memory segment

    :param struct ipc_namespace \*ns:
        namespace

    :param struct ipc_params \*params:
        ptr to the structure that contains key, size and shmflg

.. _`newseg.description`:

Description
-----------

Called with shm_ids.rwsem held as a writer.

.. This file was automatic generated / don't edit.


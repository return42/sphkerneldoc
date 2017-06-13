.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/lockd/clntproc.c

.. _`nlmclnt_proc`:

nlmclnt_proc
============

.. c:function:: int nlmclnt_proc(struct nlm_host *host, int cmd, struct file_lock *fl, void *data)

    Perform a single client-side lock request

    :param struct nlm_host \*host:
        address of a valid nlm_host context representing the NLM server

    :param int cmd:
        fcntl-style file lock operation to perform

    :param struct file_lock \*fl:
        address of arguments for the lock operation

    :param void \*data:
        address of data to be sent to callback operations

.. This file was automatic generated / don't edit.


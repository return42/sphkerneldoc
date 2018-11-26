.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/lockd/clntproc.c

.. _`nlmclnt_proc`:

nlmclnt_proc
============

.. c:function:: int nlmclnt_proc(struct nlm_host *host, int cmd, struct file_lock *fl, void *data)

    Perform a single client-side lock request

    :param host:
        address of a valid nlm_host context representing the NLM server
    :type host: struct nlm_host \*

    :param cmd:
        fcntl-style file lock operation to perform
    :type cmd: int

    :param fl:
        address of arguments for the lock operation
    :type fl: struct file_lock \*

    :param data:
        address of data to be sent to callback operations
    :type data: void \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/lockd/clntlock.c

.. _`nlmclnt_init`:

nlmclnt_init
============

.. c:function:: struct nlm_host *nlmclnt_init(const struct nlmclnt_initdata *nlm_init)

    Set up per-NFS mount point lockd data structures

    :param nlm_init:
        pointer to arguments structure
    :type nlm_init: const struct nlmclnt_initdata \*

.. _`nlmclnt_init.description`:

Description
-----------

Returns pointer to an appropriate nlm_host struct,
or an ERR_PTR value.

.. _`nlmclnt_done`:

nlmclnt_done
============

.. c:function:: void nlmclnt_done(struct nlm_host *host)

    Release resources allocated by \ :c:func:`nlmclnt_init`\ 

    :param host:
        nlm_host structure reserved by \ :c:func:`nlmclnt_init`\ 
    :type host: struct nlm_host \*

.. This file was automatic generated / don't edit.


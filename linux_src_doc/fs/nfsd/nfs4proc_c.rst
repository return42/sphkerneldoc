.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfs4proc.c

.. _`nfsd4_spo_must_allow`:

nfsd4_spo_must_allow
====================

.. c:function:: bool nfsd4_spo_must_allow(struct svc_rqst *rqstp)

    Determine if the compound op contains an operation that is allowed to be sent with machine credentials

    :param rqstp:
        a pointer to the struct svc_rqst
    :type rqstp: struct svc_rqst \*

.. _`nfsd4_spo_must_allow.description`:

Description
-----------

Checks to see if the compound contains a spo_must_allow op
and confirms that it was sent with the proper machine creds.

.. This file was automatic generated / don't edit.


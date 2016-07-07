.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfsfh.c

.. _`fh_verify`:

fh_verify
=========

.. c:function:: __be32 fh_verify(struct svc_rqst *rqstp, struct svc_fh *fhp, umode_t type, int access)

    filehandle lookup and access checking

    :param struct svc_rqst \*rqstp:
        pointer to current rpc request

    :param struct svc_fh \*fhp:
        filehandle to be verified

    :param umode_t type:
        expected type of object pointed to by filehandle

    :param int access:
        type of access needed to object

.. _`fh_verify.description`:

Description
-----------

Look up a dentry from the on-the-wire filehandle, check the client's
access to the export, and set the current task's credentials.

Regardless of success or failure of \ :c:func:`fh_verify`\ , \ :c:func:`fh_put`\  should be
called on \ ``fhp``\  when the caller is finished with the filehandle.

\ :c:func:`fh_verify`\  may be called multiple times on a given filehandle, for
example, when processing an NFSv4 compound.  The first call will look
up a dentry using the on-the-wire filehandle.  Subsequent calls will
skip the lookup and just perform the other checks and possibly change
the current task's credentials.

\ ``type``\  specifies the type of object expected using one of the S_IF\*
constants defined in include/linux/stat.h.  The caller may use zero
to indicate that it doesn't care, or a negative integer to indicate
that it expects something not of the given type.

\ ``access``\  is formed from the NFSD_MAY\_\* constants defined in
include/linux/nfsd/nfsd.h.

.. This file was automatic generated / don't edit.


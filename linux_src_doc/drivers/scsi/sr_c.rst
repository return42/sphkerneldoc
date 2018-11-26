.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/sr.c

.. _`sr_kref_release`:

sr_kref_release
===============

.. c:function:: void sr_kref_release(struct kref *kref)

    Called to free the scsi_cd structure

    :param kref:
        pointer to embedded kref
    :type kref: struct kref \*

.. _`sr_kref_release.description`:

Description
-----------

sr_ref_mutex must be held entering this routine.  Because it is
called on last put, you should always use the \ :c:func:`scsi_cd_get`\ 
\ :c:func:`scsi_cd_put`\  helpers which manipulate the semaphore directly
and never do a direct \ :c:func:`kref_put`\ .

.. This file was automatic generated / don't edit.


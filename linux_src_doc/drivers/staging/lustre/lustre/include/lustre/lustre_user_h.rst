.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre/lustre_user.h

.. _`lma_old_size`:

LMA_OLD_SIZE
============

.. c:function::  LMA_OLD_SIZE()

    been moved to a dedicated xattr lma_flags was also removed because of lma_compat/incompat fields.

.. _`changelog_remap_rec`:

changelog_remap_rec
===================

.. c:function:: void changelog_remap_rec(struct changelog_rec *rec, enum changelog_rec_flags crf_wanted)

    The record must be big enough to contain the final remapped version. Superfluous extension fields are removed and missing ones are added and zeroed. The flags of the record are updated accordingly.

    :param struct changelog_rec \*rec:
        *undescribed*

    :param enum changelog_rec_flags crf_wanted:
        *undescribed*

.. _`changelog_remap_rec.description`:

Description
-----------

The jobid and rename extensions can be added to a record, to match the
format an application expects, typically. In this case, the newly added
fields will be zeroed.
The Jobid field can be removed, to guarantee compatibility with older
clients that don't expect this field in the records they process.

.. _`changelog_remap_rec.the-following-assumptions-are-being-made`:

The following assumptions are being made
----------------------------------------

- CLF_RENAME will not be removed
- CLF_JOBID will not be added without CLF_RENAME being added too

\ ``param``\ [in,out]  rec          The record to remap.
\ ``param``\ [in]      crf_wanted   Flags describing the desired extensions.

.. _`hur_len`:

hur_len
=======

.. c:function:: ssize_t hur_len(struct hsm_user_request *hur)

    1 instead of an errno because ssize_t is defined to be only [ -1, SSIZE_MAX ]

    :param struct hsm_user_request \*hur:
        *undescribed*

.. _`hur_len.description`:

Description
-----------

return -1 on bounds check error.

.. This file was automatic generated / don't edit.


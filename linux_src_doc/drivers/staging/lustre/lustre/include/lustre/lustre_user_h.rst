.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre/lustre_user.h

.. _`lma_old_size`:

LMA_OLD_SIZE
============

.. c:function::  LMA_OLD_SIZE()

    been moved to a dedicated xattr lma_flags was also removed because of lma_compat/incompat fields.

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


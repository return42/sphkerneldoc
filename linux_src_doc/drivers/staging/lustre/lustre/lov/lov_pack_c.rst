.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lov_pack.c

.. _`lov_lsm_pack`:

lov_lsm_pack
============

.. c:function:: ssize_t lov_lsm_pack(const struct lov_stripe_md *lsm, void *buf, size_t buf_size)

    endian byte order).

    :param const struct lov_stripe_md \*lsm:
        *undescribed*

    :param void \*buf:
        *undescribed*

    :param size_t buf_size:
        *undescribed*

.. _`lov_lsm_pack.description`:

Description
-----------

This follows the \ :c:func:`getxattr`\  conventions. If \a buf_size is zero
then return the size needed. If \a buf_size is too small then
return -ERANGE. Otherwise return the size of the result.

.. This file was automatic generated / don't edit.


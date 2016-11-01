.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/mdc/mdc_lib.c

.. _`mdc_pack_name`:

mdc_pack_name
=============

.. c:function:: void mdc_pack_name(struct ptlrpc_request *req, const struct req_msg_field *field, const char *name, size_t name_len)

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param size_t name_len:
        *undescribed*

.. _`mdc_pack_name.description`:

Description
-----------

\param[in] req       request
\param[in] field     request field (usually RMF_NAME)
\param[in] name      path component
\param[in] name_len  length of path component

\a field must be present in \a req and of size \a name_len + 1.

\a name must be '\0' terminated of length \a name_len and represent
a single path component (not contain '/').

.. This file was automatic generated / don't edit.


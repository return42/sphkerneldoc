.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/userfaultfd.c

.. _`userfaultfd_ctx_get`:

userfaultfd_ctx_get
===================

.. c:function:: void userfaultfd_ctx_get(struct userfaultfd_ctx *ctx)

    Acquires a reference to the internal userfaultfd context.

    :param ctx:
        [in] Pointer to the userfaultfd context.
    :type ctx: struct userfaultfd_ctx \*

.. _`userfaultfd_ctx_put`:

userfaultfd_ctx_put
===================

.. c:function:: void userfaultfd_ctx_put(struct userfaultfd_ctx *ctx)

    Releases a reference to the internal userfaultfd context.

    :param ctx:
        [in] Pointer to userfaultfd context.
    :type ctx: struct userfaultfd_ctx \*

.. _`userfaultfd_ctx_put.description`:

Description
-----------

The userfaultfd context reference must have been previously acquired either
with \ :c:func:`userfaultfd_ctx_get`\  or \ :c:func:`userfaultfd_ctx_fdget`\ .

.. This file was automatic generated / don't edit.


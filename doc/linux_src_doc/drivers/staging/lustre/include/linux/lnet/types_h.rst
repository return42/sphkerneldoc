.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/linux/lnet/types.h

.. _`lnetinvalidatehandle`:

LNetInvalidateHandle
====================

.. c:function:: void LNetInvalidateHandle(lnet_handle_any_t *h)

    :param lnet_handle_any_t \*h:
        *undescribed*

.. _`lnethandleisequal`:

LNetHandleIsEqual
=================

.. c:function:: int LNetHandleIsEqual(lnet_handle_any_t h1, lnet_handle_any_t h2)

    :param lnet_handle_any_t h1:
        *undescribed*

    :param lnet_handle_any_t h2:
        *undescribed*

.. _`lnethandleisequal.description`:

Description
-----------

\return 1 if handles are equal, 0 if otherwise.

.. _`lnethandleisinvalid`:

LNetHandleIsInvalid
===================

.. c:function:: int LNetHandleIsInvalid(lnet_handle_any_t h)

    :param lnet_handle_any_t h:
        *undescribed*

.. _`lnethandleisinvalid.description`:

Description
-----------

\return 1 if handle is invalid, 0 if valid.

.. _`lnet_md_op_put`:

LNET_MD_OP_PUT
==============

.. c:function::  LNET_MD_OP_PUT()

    :options.

.. _`void`:

void
====

.. c:function:: typedef void(*lnet_eq_handler_t)

    :param \*lnet_eq_handler_t:
        *undescribed*

.. _`void.description`:

Description
-----------

The EQ handler runs for each event that is deposited into the EQ. The
handler is supplied with a pointer to the event that triggered the
handler invocation.

The handler must not block, must be reentrant, and must not call any LNet
API functions. It should return as quickly as possible.

.. This file was automatic generated / don't edit.


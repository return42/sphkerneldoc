.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/uapi/linux/lnet/lnet-types.h

.. _`lnet_nid_t`:

typedef lnet_nid_t
==================

.. c:type:: typedef lnet_nid_t

    point in an LNet network.

.. _`lnet_nid_t.description`:

Description
-----------

A node can have multiple end-points and hence multiple addresses.
An LNet network can be a simple network (e.g. tcp0) or a network of
LNet networks connected by LNet routers. Therefore an end-point address

.. _`lnet_nid_t.has-two-parts`:

has two parts
-------------

network ID, and address within a network.

\see LNET_NIDNET, LNET_NIDADDR, and LNET_MKNID.

.. _`lnet_pid_t`:

typedef lnet_pid_t
==================

.. c:type:: typedef lnet_pid_t

    lnet_process_id, the global process ID.

.. _`lnet_wire_handle_cookie_none`:

LNET_WIRE_HANDLE_COOKIE_NONE
============================

.. c:function::  LNET_WIRE_HANDLE_COOKIE_NONE()

    have names of the form lnet_handle_xx, where xx is one of the two letter object type codes ('eq' for event queue, 'md' for memory descriptor, and 'me' for match entry). Each type of object is given a unique handle type to enhance type checking.

.. _`lnetinvalidateeqhandle`:

LNetInvalidateEQHandle
======================

.. c:function:: void LNetInvalidateEQHandle(struct lnet_handle_eq *h)

    :param struct lnet_handle_eq \*h:
        *undescribed*

.. _`lneteqhandleisinvalid`:

LNetEQHandleIsInvalid
=====================

.. c:function:: int LNetEQHandleIsInvalid(struct lnet_handle_eq h)

    :param struct lnet_handle_eq h:
        *undescribed*

.. _`lneteqhandleisinvalid.description`:

Description
-----------

\ ``return``\  1 if handle is invalid, 0 if valid.

.. _`lnetinvalidatemdhandle`:

LNetInvalidateMDHandle
======================

.. c:function:: void LNetInvalidateMDHandle(struct lnet_handle_md *h)

    :param struct lnet_handle_md \*h:
        *undescribed*

.. _`lnetmdhandleisinvalid`:

LNetMDHandleIsInvalid
=====================

.. c:function:: int LNetMDHandleIsInvalid(struct lnet_handle_md h)

    :param struct lnet_handle_md h:
        *undescribed*

.. _`lnetmdhandleisinvalid.description`:

Description
-----------

\ ``return``\  1 if handle is invalid, 0 if valid.

.. _`lnet_md_op_put`:

LNET_MD_OP_PUT
==============

.. c:function::  LNET_MD_OP_PUT()

    :options.

.. _`lnet_eq_handler_t`:

lnet_eq_handler_t
=================

.. c:function:: void lnet_eq_handler_t(struct lnet_event *event)

    :param struct lnet_event \*event:
        *undescribed*

.. _`lnet_eq_handler_t.description`:

Description
-----------

The EQ handler runs for each event that is deposited into the EQ. The
handler is supplied with a pointer to the event that triggered the
handler invocation.

The handler must not block, must be reentrant, and must not call any LNet
API functions. It should return as quickly as possible.

.. This file was automatic generated / don't edit.


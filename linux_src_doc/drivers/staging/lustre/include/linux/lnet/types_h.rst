.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/linux/lnet/types.h

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

    lnet_process_id_t, the global process ID.

.. _`lnet_handle_any_t`:

typedef lnet_handle_any_t
=========================

.. c:type:: typedef lnet_handle_any_t

    have names of the form lnet_handle_xx_t, where xx is one of the two letter object type codes ('eq' for event queue, 'md' for memory descriptor, and 'me' for match entry). Each type of object is given a unique handle type to enhance type checking. The type lnet_handle_any_t can be used when a generic handle is needed. Every handle value can be converted into a value of type lnet_handle_any_t without loss of information.

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

.. _`lnet_process_id_t`:

typedef lnet_process_id_t
=========================

.. c:type:: typedef lnet_process_id_t


.. _`lnet_unlink_t`:

typedef lnet_unlink_t
=====================

.. c:type:: typedef lnet_unlink_t

    automatically (LNET_UNLINK) or not (LNET_RETAIN).

.. _`lnet_ins_pos_t`:

typedef lnet_ins_pos_t
======================

.. c:type:: typedef lnet_ins_pos_t

    entry is inserted. The value LNET_INS_BEFORE is used to insert the new entry before the current entry or before the head of the list. The value LNET_INS_AFTER is used to insert the new entry after the current entry or after the last item in the list.

.. _`lnet_md_t`:

typedef lnet_md_t
=================

.. c:type:: typedef lnet_md_t

    are used to initialize memory descriptors.

.. _`lnet_md_op_put`:

LNET_MD_OP_PUT
==============

.. c:function::  LNET_MD_OP_PUT()

    :options.

.. _`lnet_event_kind_t`:

typedef lnet_event_kind_t
=========================

.. c:type:: typedef lnet_event_kind_t


.. _`lnet_event_t`:

typedef lnet_event_t
====================

.. c:type:: typedef lnet_event_t


.. _`lnet_eq_handler_t`:

lnet_eq_handler_t
=================

.. c:function:: void lnet_eq_handler_t(lnet_event_t *event)

    :param lnet_event_t \*event:
        *undescribed*

.. _`lnet_eq_handler_t.description`:

Description
-----------

The EQ handler runs for each event that is deposited into the EQ. The
handler is supplied with a pointer to the event that triggered the
handler invocation.

The handler must not block, must be reentrant, and must not call any LNet
API functions. It should return as quickly as possible.

.. _`lnet_ack_req_t`:

typedef lnet_ack_req_t
======================

.. c:type:: typedef lnet_ack_req_t

    operation completes (i.e., when the data has been written to a MD of the target process).

.. _`lnet_ack_req_t.description`:

Description
-----------

\see lnet_md_t::options for the discussion on LNET_MD_ACK_DISABLE by which
acknowledgments can be disabled for a MD.

.. This file was automatic generated / don't edit.


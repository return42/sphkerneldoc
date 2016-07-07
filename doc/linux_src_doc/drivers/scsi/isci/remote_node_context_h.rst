.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/remote_node_context.h

.. _`scic_sds_remote_node_context_invalid_index`:

SCIC_SDS_REMOTE_NODE_CONTEXT_INVALID_INDEX
==========================================

.. c:function::  SCIC_SDS_REMOTE_NODE_CONTEXT_INVALID_INDEX()

    the remote node context in the silicon.  It exists to model and manage the remote node context in the silicon.

.. _`scic_sds_remote_node_context_invalid_index.description`:

Description
-----------



.. _`sci_remote_node_context`:

struct sci_remote_node_context
==============================

.. c:type:: struct sci_remote_node_context

    This structure contains the data associated with the remote node context object.  The remote node context (RNC) object models the the remote device information necessary to manage the silicon RNC.

.. _`sci_remote_node_context.definition`:

Definition
----------

.. code-block:: c

    struct sci_remote_node_context {
        u16 remote_node_index;
        u32 suspend_type;
        enum sci_remote_node_suspension_reasons suspend_reason;
        u32 suspend_count;
        enum sci_remote_node_context_destination_state destination_state;
        scics_sds_remote_node_context_callback user_callback;
        void *user_cookie;
        struct sci_base_state_machine sm;
    }

.. _`sci_remote_node_context.members`:

Members
-------

remote_node_index
    *undescribed*

suspend_type
    *undescribed*

suspend_reason
    *undescribed*

suspend_count
    *undescribed*

destination_state
    *undescribed*

user_callback
    *undescribed*

user_cookie
    *undescribed*

sm
    *undescribed*

.. This file was automatic generated / don't edit.


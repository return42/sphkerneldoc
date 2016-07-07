.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/ops.c

.. _`iwl_rx_handler_context`:

enum iwl_rx_handler_context
===========================

.. c:type:: enum iwl_rx_handler_context


.. _`iwl_rx_handler_context.definition`:

Definition
----------

.. code-block:: c

    enum iwl_rx_handler_context {
        RX_HANDLER_SYNC,
        RX_HANDLER_ASYNC_LOCKED,
        RX_HANDLER_ASYNC_UNLOCKED
    };

.. _`iwl_rx_handler_context.constants`:

Constants
---------

RX_HANDLER_SYNC
    this means that it will be called in the Rx path
    which can't acquire mvm->mutex.

RX_HANDLER_ASYNC_LOCKED
    If the handler needs to hold mvm->mutex
    (and only in this case!), it should be set as ASYNC. In that case,
    it will be called from a worker with mvm->mutex held.

RX_HANDLER_ASYNC_UNLOCKED
    in case the handler needs to lock the
    mutex itself, it will be called from a worker without mvm->mutex held.

.. _`iwl_rx_handlers`:

struct iwl_rx_handlers
======================

.. c:type:: struct iwl_rx_handlers


.. _`iwl_rx_handlers.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_handlers {
        u16 cmd_id;
        enum iwl_rx_handler_context context;
        void (* fn) (struct iwl_mvm *mvm, struct iwl_rx_cmd_buffer *rxb);
    }

.. _`iwl_rx_handlers.members`:

Members
-------

cmd_id
    command id

context
    see \ :c:type:`struct iwl_rx_handler_context <iwl_rx_handler_context>`

fn
    the function is called when notification is received

.. This file was automatic generated / don't edit.


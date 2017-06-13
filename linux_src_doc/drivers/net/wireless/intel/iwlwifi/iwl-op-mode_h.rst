.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-op-mode.h

.. _`iwl_op_mode_ops`:

struct iwl_op_mode_ops
======================

.. c:type:: struct iwl_op_mode_ops

    op_mode specific operations

.. _`iwl_op_mode_ops.definition`:

Definition
----------

.. code-block:: c

    struct iwl_op_mode_ops {
        struct iwl_op_mode *(*start)(struct iwl_trans *trans,const struct iwl_cfg *cfg,const struct iwl_fw *fw, struct dentry *dbgfs_dir);
        void (*stop)(struct iwl_op_mode *op_mode);
        void (*rx)(struct iwl_op_mode *op_mode, struct napi_struct *napi, struct iwl_rx_cmd_buffer *rxb);
        void (*rx_rss)(struct iwl_op_mode *op_mode, struct napi_struct *napi, struct iwl_rx_cmd_buffer *rxb, unsigned int queue);
        void (*async_cb)(struct iwl_op_mode *op_mode, const struct iwl_device_cmd *cmd);
        void (*queue_full)(struct iwl_op_mode *op_mode, int queue);
        void (*queue_not_full)(struct iwl_op_mode *op_mode, int queue);
        bool (*hw_rf_kill)(struct iwl_op_mode *op_mode, bool state);
        void (*free_skb)(struct iwl_op_mode *op_mode, struct sk_buff *skb);
        void (*nic_error)(struct iwl_op_mode *op_mode);
        void (*cmd_queue_full)(struct iwl_op_mode *op_mode);
        void (*nic_config)(struct iwl_op_mode *op_mode);
        void (*wimax_active)(struct iwl_op_mode *op_mode);
        int (*enter_d0i3)(struct iwl_op_mode *op_mode);
        int (*exit_d0i3)(struct iwl_op_mode *op_mode);
    }

.. _`iwl_op_mode_ops.members`:

Members
-------

start
    start the op_mode. The transport layer is already allocated.
    May sleep

stop
    stop the op_mode. Must free all the memory allocated.
    May sleep

rx
    Rx notification to the op_mode. rxb is the Rx buffer itself. Cmd is the
    HCMD this Rx responds to. Can't sleep.

rx_rss
    data queue RX notification to the op_mode, for (data) notifications
    received on the RSS queue(s). The queue parameter indicates which of the
    RSS queues received this frame; it will always be non-zero.
    This method must not sleep.

async_cb
    called when an ASYNC command with CMD_WANT_ASYNC_CALLBACK set
    completes. Must be atomic.

queue_full
    notifies that a HW queue is full.
    Must be atomic and called with BH disabled.

queue_not_full
    notifies that a HW queue is not full any more.
    Must be atomic and called with BH disabled.

hw_rf_kill
    notifies of a change in the HW rf kill switch. True means that
    the radio is killed. Return \ ``true``\  if the device should be stopped by
    the transport immediately after the call. May sleep.

free_skb
    allows the transport layer to free skbs that haven't been
    reclaimed by the op_mode. This can happen when the driver is freed and
    there are Tx packets pending in the transport layer.
    Must be atomic

nic_error
    error notification. Must be atomic and must be called with BH
    disabled.

cmd_queue_full
    Called when the command queue gets full. Must be atomic and
    called with BH disabled.

nic_config
    configure NIC, called before firmware is started.
    May sleep

wimax_active
    invoked when WiMax becomes active. May sleep

enter_d0i3
    configure the fw to enter d0i3. return 1 to indicate d0i3
    entrance is aborted (e.g. due to held reference). May sleep.

exit_d0i3
    configure the fw to exit d0i3. May sleep.

.. _`iwl_op_mode_ops.description`:

Description
-----------

The op_mode exports its ops so that external components can start it and
interact with it. The driver layer typically calls the start and stop
handlers, the transport layer calls the others.

All the handlers MUST be implemented, except \ ``rx_rss``\  which can be left
out \*iff\* the opmode will never run on hardware with multi-queue capability.

.. _`iwl_op_mode`:

struct iwl_op_mode
==================

.. c:type:: struct iwl_op_mode

    operational mode

.. _`iwl_op_mode.definition`:

Definition
----------

.. code-block:: c

    struct iwl_op_mode {
        const struct iwl_op_mode_ops *ops;
        char op_mode_specific;
    }

.. _`iwl_op_mode.members`:

Members
-------

ops
    pointer to its own ops

op_mode_specific
    *undescribed*

.. _`iwl_op_mode.description`:

Description
-----------

This holds an implementation of the mac80211 / fw API.

.. This file was automatic generated / don't edit.


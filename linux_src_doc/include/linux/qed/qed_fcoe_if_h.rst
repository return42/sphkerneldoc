.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/qed/qed_fcoe_if.h

.. _`qed_fcoe_ops`:

struct qed_fcoe_ops
===================

.. c:type:: struct qed_fcoe_ops

    qed FCoE operations.

.. _`qed_fcoe_ops.definition`:

Definition
----------

.. code-block:: c

    struct qed_fcoe_ops {
        const struct qed_common_ops *common;
        int (*fill_dev_info)(struct qed_dev *cdev,struct qed_dev_fcoe_info *info);
        void (*register_ops)(struct qed_dev *cdev,struct qed_fcoe_cb_ops *ops, void *cookie);
        const struct qed_ll2_ops *ll2;
        int (*start)(struct qed_dev *cdev, struct qed_fcoe_tid *tasks);
        int (*stop)(struct qed_dev *cdev);
        int (*acquire_conn)(struct qed_dev *cdev,u32 *handle,u32 *fw_cid, void __iomem **p_doorbell);
        int (*release_conn)(struct qed_dev *cdev, u32 handle);
        int (*offload_conn)(struct qed_dev *cdev,u32 handle,struct qed_fcoe_params_offload *conn_info);
        int (*destroy_conn)(struct qed_dev *cdev,u32 handle, dma_addr_t terminate_params);
        int (*get_stats)(struct qed_dev *cdev, struct qed_fcoe_stats *stats);
    }

.. _`qed_fcoe_ops.members`:

Members
-------

common
    common operations pointer

fill_dev_info
    fills FCoE specific information
    \ ``param``\  cdev
    \ ``param``\  info
    \ ``return``\  0 on sucesss, otherwise error value.

register_ops
    register FCoE operations
    \ ``param``\  cdev
    \ ``param``\  ops - specified using qed_iscsi_cb_ops
    \ ``param``\  cookie - driver private

ll2
    light L2 operations pointer

start
    fcoe in FW
    \ ``param``\  cdev
    \ ``param``\  tasks - qed will fill information about tasks
    return 0 on success, otherwise error value.

stop
    stops fcoe in FW
    \ ``param``\  cdev
    return 0 on success, otherwise error value.

acquire_conn
    acquire a new fcoe connection
    \ ``param``\  cdev
    \ ``param``\  handle - qed will fill handle that should be
    used henceforth as identifier of the
    connection.
    \ ``param``\  p_doorbell - qed will fill the address of the
    doorbell.
    return 0 on sucesss, otherwise error value.

release_conn
    release a previously acquired fcoe connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    return 0 on success, otherwise error value.

offload_conn
    configures an offloaded connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``param``\  conn_info - the configuration to use for the
    offload.
    return 0 on success, otherwise error value.

destroy_conn
    stops an offloaded connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``param``\  terminate_params
    return 0 on success, otherwise error value.

get_stats
    gets FCoE related statistics
    \ ``param``\  cdev
    \ ``param``\  stats - pointer to struck that would be filled
    we stats
    return 0 on success, error otherwise.

.. This file was automatic generated / don't edit.


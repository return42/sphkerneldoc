.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/qed/qed_iscsi_if.h

.. _`qed_iscsi_ops`:

struct qed_iscsi_ops
====================

.. c:type:: struct qed_iscsi_ops

    qed iSCSI operations.

.. _`qed_iscsi_ops.definition`:

Definition
----------

.. code-block:: c

    struct qed_iscsi_ops {
        const struct qed_common_ops *common;
        const struct qed_ll2_ops *ll2;
        int (*fill_dev_info)(struct qed_dev *cdev, struct qed_dev_iscsi_info *info);
        void (*register_ops)(struct qed_dev *cdev, struct qed_iscsi_cb_ops *ops, void *cookie);
        int (*start)(struct qed_dev *cdev,struct qed_iscsi_tid *tasks, void *event_context, iscsi_event_cb_t async_event_cb);
        int (*stop)(struct qed_dev *cdev);
        int (*acquire_conn)(struct qed_dev *cdev,u32 *handle, u32 *fw_cid, void __iomem **p_doorbell);
        int (*release_conn)(struct qed_dev *cdev, u32 handle);
        int (*offload_conn)(struct qed_dev *cdev,u32 handle, struct qed_iscsi_params_offload *conn_info);
        int (*update_conn)(struct qed_dev *cdev,u32 handle, struct qed_iscsi_params_update *conn_info);
        int (*destroy_conn)(struct qed_dev *cdev, u32 handle, u8 abrt_conn);
        int (*clear_sq)(struct qed_dev *cdev, u32 handle);
        int (*get_stats)(struct qed_dev *cdev, struct qed_iscsi_stats *stats);
        int (*change_mac)(struct qed_dev *cdev, u32 handle, const u8 *mac);
    }

.. _`qed_iscsi_ops.members`:

Members
-------

common
    common operations pointer

ll2
    light L2 operations pointer

fill_dev_info
    fills iSCSI specific information
    \ ``param``\  cdev
    \ ``param``\  info
    \ ``return``\  0 on sucesss, otherwise error value.

register_ops
    register iscsi operations
    \ ``param``\  cdev
    \ ``param``\  ops - specified using qed_iscsi_cb_ops
    \ ``param``\  cookie - driver private

start
    iscsi in FW
    \ ``param``\  cdev
    \ ``param``\  tasks - qed will fill information about tasks
    return 0 on success, otherwise error value.

stop
    iscsi in FW
    \ ``param``\  cdev
    return 0 on success, otherwise error value.

acquire_conn
    acquire a new iscsi connection
    \ ``param``\  cdev
    \ ``param``\  handle - qed will fill handle that should be
    used henceforth as identifier of the
    connection.
    \ ``param``\  p_doorbell - qed will fill the address of the
    doorbell.
    \ ``return``\  0 on sucesss, otherwise error value.

release_conn
    release a previously acquired iscsi connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``return``\  0 on success, otherwise error value.

offload_conn
    configures an offloaded connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``param``\  conn_info - the configuration to use for the
    offload.
    \ ``return``\  0 on success, otherwise error value.

update_conn
    updates an offloaded connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``param``\  conn_info - the configuration to use for the
    offload.
    \ ``return``\  0 on success, otherwise error value.

destroy_conn
    stops an offloaded connection
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``return``\  0 on success, otherwise error value.

clear_sq
    clear all task in sq
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``return``\  0 on success, otherwise error value.

get_stats
    iSCSI related statistics
    \ ``param``\  cdev
    \ ``param``\  stats - pointer to struck that would be filled
    we stats
    \ ``return``\  0 on success, error otherwise.
    \ ``change_mac``\           Change MAC of interface
    \ ``param``\  cdev
    \ ``param``\  handle - the connection handle.
    \ ``param``\  mac - new MAC to configure.
    \ ``return``\  0 on success, otherwise error value.

change_mac
    *undescribed*

.. This file was automatic generated / don't edit.


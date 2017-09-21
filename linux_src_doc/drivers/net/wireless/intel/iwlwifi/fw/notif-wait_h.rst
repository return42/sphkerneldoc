.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/notif-wait.h

.. _`iwl_notification_wait`:

struct iwl_notification_wait
============================

.. c:type:: struct iwl_notification_wait

    notification wait entry

.. _`iwl_notification_wait.definition`:

Definition
----------

.. code-block:: c

    struct iwl_notification_wait {
        struct list_head list;
        bool (*fn)(struct iwl_notif_wait_data *notif_data, struct iwl_rx_packet *pkt, void *data);
        void *fn_data;
        u16 cmds;
        u8 n_cmds;
        bool triggered;
        bool aborted;
    }

.. _`iwl_notification_wait.members`:

Members
-------

list
    list head for global list

fn
    Function called with the notification. If the function
    returns true, the wait is over, if it returns false then
    the waiter stays blocked. If no function is given, any
    of the listed commands will unblock the waiter.

fn_data
    *undescribed*

cmds
    command IDs

n_cmds
    number of command IDs

triggered
    waiter should be woken up

aborted
    wait was aborted

.. _`iwl_notification_wait.description`:

Description
-----------

This structure is not used directly, to wait for a
notification declare it on the stack, and call
\ :c:func:`iwl_init_notification_wait`\  with appropriate
parameters. Then do whatever will cause the ucode
to notify the driver, and to wait for that then
call \ :c:func:`iwl_wait_notification`\ .

Each notification is one-shot. If at some point we
need to support multi-shot notifications (which
can't be allocated on the stack) we need to modify
the code for them.

.. This file was automatic generated / don't edit.


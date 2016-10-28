.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/async_tx.h

.. _`async_submit_ctl`:

struct async_submit_ctl
=======================

.. c:type:: struct async_submit_ctl

    async_tx submission/completion modifiers

.. _`async_submit_ctl.definition`:

Definition
----------

.. code-block:: c

    struct async_submit_ctl {
        enum async_tx_flags flags;
        struct dma_async_tx_descriptor *depend_tx;
        dma_async_tx_callback cb_fn;
        void *cb_param;
        void *scribble;
    }

.. _`async_submit_ctl.members`:

Members
-------

flags
    submission modifiers

depend_tx
    parent dependency of the current operation being submitted

cb_fn
    callback routine to run at operation completion

cb_param
    parameter for the callback routine

scribble
    caller provided space for dma/page address conversions

.. _`async_tx_issue_pending`:

async_tx_issue_pending
======================

.. c:function:: void async_tx_issue_pending(struct dma_async_tx_descriptor *tx)

    send pending descriptor to the hardware channel

    :param struct dma_async_tx_descriptor \*tx:
        descriptor handle to retrieve hardware context

.. _`async_tx_issue_pending.note`:

Note
----

any dependent operations will have already been issued by
async_tx_channel_switch, or (in the case of no channel switch) will
be already pending on this channel.

.. _`async_tx_sync_epilog`:

async_tx_sync_epilog
====================

.. c:function:: void async_tx_sync_epilog(struct async_submit_ctl *submit)

    actions to take if an operation is run synchronously

    :param struct async_submit_ctl \*submit:
        *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/omap_remoteproc.c

.. _`omap_rproc`:

struct omap_rproc
=================

.. c:type:: struct omap_rproc

    omap remote processor state

.. _`omap_rproc.definition`:

Definition
----------

.. code-block:: c

    struct omap_rproc {
        struct mbox_chan *mbox;
        struct mbox_client client;
        struct rproc *rproc;
    }

.. _`omap_rproc.members`:

Members
-------

mbox
    mailbox channel handle

client
    mailbox client to request the mailbox channel

rproc
    rproc handle

.. _`omap_rproc_mbox_callback`:

omap_rproc_mbox_callback
========================

.. c:function:: void omap_rproc_mbox_callback(struct mbox_client *client, void *data)

    inbound mailbox message handler

    :param client:
        mailbox client pointer used for requesting the mailbox channel
    :type client: struct mbox_client \*

    :param data:
        mailbox payload
    :type data: void \*

.. _`omap_rproc_mbox_callback.description`:

Description
-----------

This handler is invoked by omap's mailbox driver whenever a mailbox
message is received. Usually, the mailbox payload simply contains
the index of the virtqueue that is kicked by the remote processor,
and we let remoteproc core handle it.

In addition to virtqueue indices, we also have some out-of-band values
that indicates different events. Those values are deliberately very
big so they don't coincide with virtqueue indices.

.. This file was automatic generated / don't edit.


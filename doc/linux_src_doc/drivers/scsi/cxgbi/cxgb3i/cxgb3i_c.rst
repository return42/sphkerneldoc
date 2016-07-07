.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxgbi/cxgb3i/cxgb3i.c

.. _`arp_failure_skb_discard`:

arp_failure_skb_discard
=======================

.. c:function:: void arp_failure_skb_discard(struct t3cdev *dev, struct sk_buff *skb)

    - start transmit

    :param struct t3cdev \*dev:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`arp_failure_skb_discard.description`:

Description
-----------

Prepends TX_DATA_WR or CPL_CLOSE_CON_REQ headers to buffers waiting in a
connection's send queue and sends them on to T3.  Must be called with the
connection's lock held.  Returns the amount of send buffer space that was
freed as a result of sending queued data to T3.

.. _`l2t_put`:

l2t_put
=======

.. c:function:: void l2t_put(struct cxgbi_sock *csk)

    release offload resource

    :param struct cxgbi_sock \*csk:
        *undescribed*

.. _`cxgb3i_ofld_init`:

cxgb3i_ofld_init
================

.. c:function:: int cxgb3i_ofld_init(struct cxgbi_device *cdev)

    allocate and initialize resources for each adapter found

    :param struct cxgbi_device \*cdev:
        cxgbi adapter

.. _`ddp_setup_conn_digest`:

ddp_setup_conn_digest
=====================

.. c:function:: int ddp_setup_conn_digest(struct cxgbi_sock *csk, unsigned int tid, int hcrc, int dcrc, int reply)

    setup conn. digest setting

    :param struct cxgbi_sock \*csk:
        cxgb tcp socket

    :param unsigned int tid:
        connection id

    :param int hcrc:
        header digest enabled

    :param int dcrc:
        data digest enabled

    :param int reply:
        request reply from h/w
        set up the iscsi digest settings for a connection identified by tid

.. _`t3_ddp_cleanup`:

t3_ddp_cleanup
==============

.. c:function:: void t3_ddp_cleanup(struct cxgbi_device *cdev)

    release the cxgb3 adapter's ddp resource

    :param struct cxgbi_device \*cdev:
        cxgb3i adapter
        release all the resource held by the ddp pagepod manager for a given
        adapter if needed

.. _`cxgb3i_ddp_init`:

cxgb3i_ddp_init
===============

.. c:function:: int cxgb3i_ddp_init(struct cxgbi_device *cdev)

    initialize the cxgb3 adapter's ddp resource

    :param struct cxgbi_device \*cdev:
        cxgb3i adapter
        initialize the ddp pagepod manager for a given adapter

.. _`cxgb3i_dev_open`:

cxgb3i_dev_open
===============

.. c:function:: void cxgb3i_dev_open(struct t3cdev *t3dev)

    init a t3 adapter structure and any h/w settings

    :param struct t3cdev \*t3dev:
        t3cdev adapter

.. _`cxgb3i_init_module`:

cxgb3i_init_module
==================

.. c:function:: int cxgb3i_init_module( void)

    module init entry point

    :param  void:
        no arguments

.. _`cxgb3i_init_module.description`:

Description
-----------

initialize any driver wide global data structures and register itself
with the cxgb3 module

.. _`cxgb3i_exit_module`:

cxgb3i_exit_module
==================

.. c:function:: void __exit cxgb3i_exit_module( void)

    module cleanup/exit entry point

    :param  void:
        no arguments

.. _`cxgb3i_exit_module.description`:

Description
-----------

go through the driver hba list and for each hba, release any resource held.
and unregisters iscsi transport and the cxgb3 module

.. This file was automatic generated / don't edit.


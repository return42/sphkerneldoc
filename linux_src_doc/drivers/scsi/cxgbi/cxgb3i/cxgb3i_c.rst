.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxgbi/cxgb3i/cxgb3i.c

.. _`arp_failure_skb_discard`:

arp_failure_skb_discard
=======================

.. c:function:: void arp_failure_skb_discard(struct t3cdev *dev, struct sk_buff *skb)

    - start transmit

    :param dev:
        *undescribed*
    :type dev: struct t3cdev \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

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

    :param csk:
        *undescribed*
    :type csk: struct cxgbi_sock \*

.. _`cxgb3i_ofld_init`:

cxgb3i_ofld_init
================

.. c:function:: int cxgb3i_ofld_init(struct cxgbi_device *cdev)

    allocate and initialize resources for each adapter found

    :param cdev:
        cxgbi adapter
    :type cdev: struct cxgbi_device \*

.. _`ddp_setup_conn_digest`:

ddp_setup_conn_digest
=====================

.. c:function:: int ddp_setup_conn_digest(struct cxgbi_sock *csk, unsigned int tid, int hcrc, int dcrc, int reply)

    setup conn. digest setting

    :param csk:
        cxgb tcp socket
    :type csk: struct cxgbi_sock \*

    :param tid:
        connection id
    :type tid: unsigned int

    :param hcrc:
        header digest enabled
    :type hcrc: int

    :param dcrc:
        data digest enabled
    :type dcrc: int

    :param reply:
        request reply from h/w
        set up the iscsi digest settings for a connection identified by tid
    :type reply: int

.. _`cxgb3i_ddp_init`:

cxgb3i_ddp_init
===============

.. c:function:: int cxgb3i_ddp_init(struct cxgbi_device *cdev)

    initialize the cxgb3 adapter's ddp resource

    :param cdev:
        cxgb3i adapter
        initialize the ddp pagepod manager for a given adapter
    :type cdev: struct cxgbi_device \*

.. _`cxgb3i_dev_open`:

cxgb3i_dev_open
===============

.. c:function:: void cxgb3i_dev_open(struct t3cdev *t3dev)

    init a t3 adapter structure and any h/w settings

    :param t3dev:
        t3cdev adapter
    :type t3dev: struct t3cdev \*

.. _`cxgb3i_init_module`:

cxgb3i_init_module
==================

.. c:function:: int cxgb3i_init_module( void)

    module init entry point

    :param void:
        no arguments
    :type void: 

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

    :param void:
        no arguments
    :type void: 

.. _`cxgb3i_exit_module.description`:

Description
-----------

go through the driver hba list and for each hba, release any resource held.
and unregisters iscsi transport and the cxgb3 module

.. This file was automatic generated / don't edit.


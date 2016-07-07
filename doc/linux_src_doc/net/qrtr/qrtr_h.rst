.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/qrtr/qrtr.h

.. _`qrtr_endpoint`:

struct qrtr_endpoint
====================

.. c:type:: struct qrtr_endpoint

    endpoint handle

.. _`qrtr_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct qrtr_endpoint {
        int (* xmit) (struct qrtr_endpoint *ep, struct sk_buff *skb);
    }

.. _`qrtr_endpoint.members`:

Members
-------

xmit
    Callback for outgoing packets

.. _`qrtr_endpoint.description`:

Description
-----------

The socket buffer passed to the xmit function becomes owned by the endpoint
driver.  As such, when the driver is done with the buffer, it should
call \ :c:func:`kfree_skb`\  on failure, or \ :c:func:`consume_skb`\  on success.

.. This file was automatic generated / don't edit.


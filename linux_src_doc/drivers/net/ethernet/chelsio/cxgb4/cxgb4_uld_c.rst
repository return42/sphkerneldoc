.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_uld.c

.. _`uldrx_handler`:

uldrx_handler
=============

.. c:function:: int uldrx_handler(struct sge_rspq *q, const __be64 *rsp, const struct pkt_gl *gl)

    response queue handler for ULD queues

    :param struct sge_rspq \*q:
        the response queue that received the packet

    :param const __be64 \*rsp:
        the response queue descriptor holding the offload message

    :param const struct pkt_gl \*gl:
        the gather list of packet fragments

.. _`uldrx_handler.description`:

Description
-----------

Deliver an ingress offload packet to a ULD.  All processing is done by
the ULD, we just maintain statistics.

.. _`cxgb4_register_uld`:

cxgb4_register_uld
==================

.. c:function:: int cxgb4_register_uld(enum cxgb4_uld type, const struct cxgb4_uld_info *p)

    register an upper-layer driver

    :param enum cxgb4_uld type:
        the ULD type

    :param const struct cxgb4_uld_info \*p:
        the ULD methods

.. _`cxgb4_register_uld.description`:

Description
-----------

Registers an upper-layer driver with this driver and notifies the ULD
about any presently available devices that support its type.  Returns
\ ``-EBUSY``\  if a ULD of the same type is already registered.

.. _`cxgb4_unregister_uld`:

cxgb4_unregister_uld
====================

.. c:function:: int cxgb4_unregister_uld(enum cxgb4_uld type)

    unregister an upper-layer driver

    :param enum cxgb4_uld type:
        the ULD type

.. _`cxgb4_unregister_uld.description`:

Description
-----------

Unregisters an existing upper-layer driver.

.. This file was automatic generated / don't edit.


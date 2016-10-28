.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_main.c

.. _`link_start`:

link_start
==========

.. c:function:: int link_start(struct net_device *dev)

    enable a port

    :param struct net_device \*dev:
        the port to enable

.. _`link_start.description`:

Description
-----------

Performs the MAC and PHY actions needed to enable a port.

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

.. _`cxgb4_write_rss`:

cxgb4_write_rss
===============

.. c:function:: int cxgb4_write_rss(const struct port_info *pi, const u16 *queues)

    write the RSS table for a given port

    :param const struct port_info \*pi:
        the port

    :param const u16 \*queues:
        array of queue indices for RSS

.. _`cxgb4_write_rss.description`:

Description
-----------

Sets up the portion of the HW RSS table for the port's VI to distribute
packets to the Rx queues in \ ``queues``\ .
Should never be called before setting up sge eth rx queues

.. _`setup_rss`:

setup_rss
=========

.. c:function:: int setup_rss(struct adapter *adap)

    configure RSS

    :param struct adapter \*adap:
        the adapter

.. _`setup_rss.description`:

Description
-----------

Sets up RSS for each port.

.. _`setup_sge_queues`:

setup_sge_queues
================

.. c:function:: int setup_sge_queues(struct adapter *adap)

    configure SGE Tx/Rx/response queues

    :param struct adapter \*adap:
        the adapter

.. _`setup_sge_queues.description`:

Description
-----------

Determines how many sets of SGE queues to use and initializes them.
We support multiple queue sets per port if we have MSI-X, otherwise
just one queue set per port.

.. _`cxgb4_set_rspq_intr_params`:

cxgb4_set_rspq_intr_params
==========================

.. c:function:: int cxgb4_set_rspq_intr_params(struct sge_rspq *q, unsigned int us, unsigned int cnt)

    set a queue's interrupt holdoff parameters

    :param struct sge_rspq \*q:
        the Rx queue

    :param unsigned int us:
        the hold-off time in us, or 0 to disable timer

    :param unsigned int cnt:
        the hold-off packet count, or 0 to disable counter

.. _`cxgb4_set_rspq_intr_params.description`:

Description
-----------

Sets an Rx queue's interrupt hold-off time and packet count.  At least
one of the two needs to be enabled for the queue to generate interrupts.

.. _`cxgb4_create_server`:

cxgb4_create_server
===================

.. c:function:: int cxgb4_create_server(const struct net_device *dev, unsigned int stid, __be32 sip, __be16 sport, __be16 vlan, unsigned int queue)

    create an IP server

    :param const struct net_device \*dev:
        the device

    :param unsigned int stid:
        the server TID

    :param __be32 sip:
        local IP address to bind server to

    :param __be16 sport:
        the server's TCP port

    :param __be16 vlan:
        *undescribed*

    :param unsigned int queue:
        queue to direct messages from this server to

.. _`cxgb4_create_server.description`:

Description
-----------

Create an IP server for the given port and address.
Returns <0 on error and one of the \ ``NET_XMIT``\ \_\* values on success.

.. _`cxgb4_best_mtu`:

cxgb4_best_mtu
==============

.. c:function:: unsigned int cxgb4_best_mtu(const unsigned short *mtus, unsigned short mtu, unsigned int *idx)

    find the entry in the MTU table closest to an MTU

    :param const unsigned short \*mtus:
        the HW MTU table

    :param unsigned short mtu:
        the target MTU

    :param unsigned int \*idx:
        index of selected entry in the MTU table

.. _`cxgb4_best_mtu.description`:

Description
-----------

Returns the index and the value in the HW MTU table that is closest to
but does not exceed \ ``mtu``\ , unless \ ``mtu``\  is smaller than any value in the
table, in which case that smallest available value is selected.

.. _`cxgb4_best_aligned_mtu`:

cxgb4_best_aligned_mtu
======================

.. c:function:: unsigned int cxgb4_best_aligned_mtu(const unsigned short *mtus, unsigned short header_size, unsigned short data_size_max, unsigned short data_size_align, unsigned int *mtu_idxp)

    find best MTU, [hopefully] data size aligned

    :param const unsigned short \*mtus:
        the HW MTU table

    :param unsigned short header_size:
        Header Size

    :param unsigned short data_size_max:
        maximum Data Segment Size

    :param unsigned short data_size_align:
        desired Data Segment Size Alignment (2^N)

    :param unsigned int \*mtu_idxp:
        HW MTU Table Index return value pointer (possibly NULL)

.. _`cxgb4_best_aligned_mtu.description`:

Description
-----------

Similar to \ :c:func:`cxgb4_best_mtu`\  but instead of searching the Hardware
MTU Table based solely on a Maximum MTU parameter, we break that
parameter up into a Header Size and Maximum Data Segment Size, and
provide a desired Data Segment Size Alignment.  If we find an MTU in
the Hardware MTU Table which will result in a Data Segment Size with
the requested alignment \_and\_ that MTU isn't "too far" from the
closest MTU, then we'll return that rather than the closest MTU.

.. _`cxgb4_tp_smt_idx`:

cxgb4_tp_smt_idx
================

.. c:function:: unsigned int cxgb4_tp_smt_idx(enum chip_type chip, unsigned int viid)

    Get the Source Mac Table index for this VI

    :param enum chip_type chip:
        chip type

    :param unsigned int viid:
        VI id of the given port

.. _`cxgb4_tp_smt_idx.description`:

Description
-----------

Return the SMT index for this VI.

.. _`cxgb4_port_chan`:

cxgb4_port_chan
===============

.. c:function:: unsigned int cxgb4_port_chan(const struct net_device *dev)

    get the HW channel of a port

    :param const struct net_device \*dev:
        the net device for the port

.. _`cxgb4_port_chan.description`:

Description
-----------

Return the HW Tx channel of the given port.

.. _`cxgb4_port_viid`:

cxgb4_port_viid
===============

.. c:function:: unsigned int cxgb4_port_viid(const struct net_device *dev)

    get the VI id of a port

    :param const struct net_device \*dev:
        the net device for the port

.. _`cxgb4_port_viid.description`:

Description
-----------

Return the VI id of the given port.

.. _`cxgb4_port_idx`:

cxgb4_port_idx
==============

.. c:function:: unsigned int cxgb4_port_idx(const struct net_device *dev)

    get the index of a port

    :param const struct net_device \*dev:
        the net device for the port

.. _`cxgb4_port_idx.description`:

Description
-----------

Return the index of the given port.

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

.. _`cxgb_up`:

cxgb_up
=======

.. c:function:: int cxgb_up(struct adapter *adap)

    enable the adapter

    :param struct adapter \*adap:
        adapter being enabled

.. _`cxgb_up.description`:

Description
-----------

Called when the first port is enabled, this function performs the
actions necessary to make an adapter operational, such as completing
the initialization of HW modules, and enabling interrupts.

Must be called with the rtnl lock held.

.. This file was automatic generated / don't edit.


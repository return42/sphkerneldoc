.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_main.c

.. _`link_start`:

link_start
==========

.. c:function:: int link_start(struct net_device *dev)

    enable a port

    :param dev:
        the port to enable
    :type dev: struct net_device \*

.. _`link_start.description`:

Description
-----------

Performs the MAC and PHY actions needed to enable a port.

.. _`cxgb4_write_rss`:

cxgb4_write_rss
===============

.. c:function:: int cxgb4_write_rss(const struct port_info *pi, const u16 *queues)

    write the RSS table for a given port

    :param pi:
        the port
    :type pi: const struct port_info \*

    :param queues:
        array of queue indices for RSS
    :type queues: const u16 \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`setup_rss.description`:

Description
-----------

Sets up RSS for each port.

.. _`setup_sge_queues`:

setup_sge_queues
================

.. c:function:: int setup_sge_queues(struct adapter *adap)

    configure SGE Tx/Rx/response queues

    :param adap:
        the adapter
    :type adap: struct adapter \*

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

    :param q:
        the Rx queue
    :type q: struct sge_rspq \*

    :param us:
        the hold-off time in us, or 0 to disable timer
    :type us: unsigned int

    :param cnt:
        the hold-off packet count, or 0 to disable counter
    :type cnt: unsigned int

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

    :param dev:
        the device
    :type dev: const struct net_device \*

    :param stid:
        the server TID
    :type stid: unsigned int

    :param sip:
        local IP address to bind server to
    :type sip: __be32

    :param sport:
        the server's TCP port
    :type sport: __be16

    :param vlan:
        *undescribed*
    :type vlan: __be16

    :param queue:
        queue to direct messages from this server to
    :type queue: unsigned int

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

    :param mtus:
        the HW MTU table
    :type mtus: const unsigned short \*

    :param mtu:
        the target MTU
    :type mtu: unsigned short

    :param idx:
        index of selected entry in the MTU table
    :type idx: unsigned int \*

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

    :param mtus:
        the HW MTU table
    :type mtus: const unsigned short \*

    :param header_size:
        Header Size
    :type header_size: unsigned short

    :param data_size_max:
        maximum Data Segment Size
    :type data_size_max: unsigned short

    :param data_size_align:
        desired Data Segment Size Alignment (2^N)
    :type data_size_align: unsigned short

    :param mtu_idxp:
        HW MTU Table Index return value pointer (possibly NULL)
    :type mtu_idxp: unsigned int \*

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

    :param chip:
        chip type
    :type chip: enum chip_type

    :param viid:
        VI id of the given port
    :type viid: unsigned int

.. _`cxgb4_tp_smt_idx.description`:

Description
-----------

Return the SMT index for this VI.

.. _`cxgb4_port_chan`:

cxgb4_port_chan
===============

.. c:function:: unsigned int cxgb4_port_chan(const struct net_device *dev)

    get the HW channel of a port

    :param dev:
        the net device for the port
    :type dev: const struct net_device \*

.. _`cxgb4_port_chan.description`:

Description
-----------

Return the HW Tx channel of the given port.

.. _`cxgb4_port_viid`:

cxgb4_port_viid
===============

.. c:function:: unsigned int cxgb4_port_viid(const struct net_device *dev)

    get the VI id of a port

    :param dev:
        the net device for the port
    :type dev: const struct net_device \*

.. _`cxgb4_port_viid.description`:

Description
-----------

Return the VI id of the given port.

.. _`cxgb4_port_idx`:

cxgb4_port_idx
==============

.. c:function:: unsigned int cxgb4_port_idx(const struct net_device *dev)

    get the index of a port

    :param dev:
        the net device for the port
    :type dev: const struct net_device \*

.. _`cxgb4_port_idx.description`:

Description
-----------

Return the index of the given port.

.. _`cxgb_up`:

cxgb_up
=======

.. c:function:: int cxgb_up(struct adapter *adap)

    enable the adapter

    :param adap:
        adapter being enabled
    :type adap: struct adapter \*

.. _`cxgb_up.description`:

Description
-----------

Called when the first port is enabled, this function performs the
actions necessary to make an adapter operational, such as completing
the initialization of HW modules, and enabling interrupts.

Must be called with the rtnl lock held.

.. This file was automatic generated / don't edit.


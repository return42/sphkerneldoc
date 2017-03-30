.. -*- coding: utf-8; mode: rst -*-

#########################################
Linux Networking and Network Devices APIs
#########################################

This documentation is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

For more details see the file COPYING in the source distribution of
Linux.


.. _netcore:

****************
Linux Networking
****************


Networking Base Types
=====================


.. kernel-doc:: include/linux/net.h
    :man-sect: 9
    :internal:


Socket Buffer Functions
=======================


.. kernel-doc:: include/linux/skbuff.h
    :man-sect: 9
    :internal:


.. kernel-doc:: include/net/sock.h
    :man-sect: 9
    :internal:


.. kernel-doc:: net/socket.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/core/skbuff.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/core/sock.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/core/datagram.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/core/stream.c
    :man-sect: 9
    :export:


Socket Filter
=============


.. kernel-doc:: net/core/filter.c
    :man-sect: 9
    :export:


Generic Network Statistics
==========================


.. kernel-doc:: include/uapi/linux/gen_stats.h
    :man-sect: 9
    :internal:


.. kernel-doc:: net/core/gen_stats.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/core/gen_estimator.c
    :man-sect: 9
    :export:


SUN RPC subsystem
=================


.. kernel-doc:: net/sunrpc/xdr.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/svc_xprt.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/xprt.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/sched.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/socklib.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/stats.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/rpc_pipe.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/rpcb_clnt.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sunrpc/clnt.c
    :man-sect: 9
    :export:


WiMAX
=====


.. kernel-doc:: net/wimax/op-msg.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/wimax/op-reset.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/wimax/op-rfkill.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/wimax/stack.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/net/wimax.h
    :man-sect: 9
    :internal:


.. kernel-doc:: include/uapi/linux/wimax.h
    :man-sect: 9
    :internal:


.. _netdev:

**********************
Network device support
**********************


Driver Support
==============


.. kernel-doc:: net/core/dev.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/ethernet/eth.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sched/sch_generic.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/etherdevice.h
    :man-sect: 9
    :internal:


.. kernel-doc:: include/linux/netdevice.h
    :man-sect: 9
    :internal:


PHY Support
===========


.. kernel-doc:: drivers/net/phy/phy.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/net/phy/phy.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/net/phy/phy_device.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/net/phy/phy_device.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/net/phy/mdio_bus.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/net/phy/mdio_bus.c
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------


.. only:: html

  Retrieval
  =========

  * :ref:`genindex`

.. todolist::


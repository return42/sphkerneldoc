.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/tb.h

.. _`tb_switch`:

struct tb_switch
================

.. c:type:: struct tb_switch

    a thunderbolt switch

.. _`tb_switch.definition`:

Definition
----------

.. code-block:: c

    struct tb_switch {
        struct tb_regs_switch_header config;
        struct tb_port *ports;
        struct tb *tb;
        u64 uid;
        int cap_plug_events;
        bool is_unplugged;
        u8 *drom;
    }

.. _`tb_switch.members`:

Members
-------

config
    *undescribed*

ports
    *undescribed*

tb
    *undescribed*

uid
    *undescribed*

cap_plug_events
    *undescribed*

is_unplugged
    *undescribed*

drom
    *undescribed*

.. _`tb_port`:

struct tb_port
==============

.. c:type:: struct tb_port

    a thunderbolt port, part of a tb_switch

.. _`tb_port.definition`:

Definition
----------

.. code-block:: c

    struct tb_port {
        struct tb_regs_port_header config;
        struct tb_switch *sw;
        struct tb_port *remote;
        int cap_phy;
        u8 port;
        bool disabled;
        struct tb_port *dual_link_port;
        u8 link_nr:1;
    }

.. _`tb_port.members`:

Members
-------

config
    *undescribed*

sw
    *undescribed*

remote
    *undescribed*

cap_phy
    *undescribed*

port
    *undescribed*

disabled
    *undescribed*

dual_link_port
    *undescribed*

link_nr
    *undescribed*

.. _`tb_path_hop`:

struct tb_path_hop
==================

.. c:type:: struct tb_path_hop

    routing information for a tb_path

.. _`tb_path_hop.definition`:

Definition
----------

.. code-block:: c

    struct tb_path_hop {
        struct tb_port *in_port;
        struct tb_port *out_port;
        int in_hop_index;
        int in_counter_index;
        int next_hop_index;
    }

.. _`tb_path_hop.members`:

Members
-------

in_port
    *undescribed*

out_port
    *undescribed*

in_hop_index
    *undescribed*

in_counter_index
    *undescribed*

next_hop_index
    *undescribed*

.. _`tb_path_hop.description`:

Description
-----------

Hop configuration is always done on the IN port of a switch.
in_port and out_port have to be on the same switch. Packets arriving on
in_port with "hop" = in_hop_index will get routed to through out_port. The
next hop to take (on out_port->remote) is determined by next_hop_index.

in_counter_index is the index of a counter (in TB_CFG_COUNTERS) on the in
port.

.. _`tb_path_port`:

enum tb_path_port
=================

.. c:type:: enum tb_path_port

    path options mask

.. _`tb_path_port.definition`:

Definition
----------

.. code-block:: c

    enum tb_path_port {
        TB_PATH_NONE,
        TB_PATH_SOURCE,
        TB_PATH_INTERNAL,
        TB_PATH_DESTINATION,
        TB_PATH_ALL
    };

.. _`tb_path_port.constants`:

Constants
---------

TB_PATH_NONE
    *undescribed*

TB_PATH_SOURCE
    *undescribed*

TB_PATH_INTERNAL
    *undescribed*

TB_PATH_DESTINATION
    *undescribed*

TB_PATH_ALL
    *undescribed*

.. _`tb_path`:

struct tb_path
==============

.. c:type:: struct tb_path

    a unidirectional path between two ports

.. _`tb_path.definition`:

Definition
----------

.. code-block:: c

    struct tb_path {
        struct tb *tb;
        int nfc_credits;
        enum tb_path_port ingress_shared_buffer;
        enum tb_path_port egress_shared_buffer;
        enum tb_path_port ingress_fc_enable;
        enum tb_path_port egress_fc_enable;
        int priority:3;
        int weight:4;
        bool drop_packages;
        bool activated;
        struct tb_path_hop *hops;
        int path_length;
    }

.. _`tb_path.members`:

Members
-------

tb
    *undescribed*

nfc_credits
    *undescribed*

ingress_shared_buffer
    *undescribed*

egress_shared_buffer
    *undescribed*

ingress_fc_enable
    *undescribed*

egress_fc_enable
    *undescribed*

priority
    *undescribed*

weight
    *undescribed*

drop_packages
    *undescribed*

activated
    *undescribed*

hops
    *undescribed*

path_length
    *undescribed*

.. _`tb_path.description`:

Description
-----------

A path consists of a number of hops (see tb_path_hop). To establish a PCIe
tunnel two paths have to be created between the two PCIe ports.

.. _`tb`:

struct tb
=========

.. c:type:: struct tb

    main thunderbolt bus structure

.. _`tb.definition`:

Definition
----------

.. code-block:: c

    struct tb {
        struct mutex lock;
        struct tb_nhi *nhi;
        struct tb_ctl *ctl;
        struct workqueue_struct *wq;
        struct tb_switch *root_switch;
        struct list_head tunnel_list;
        bool hotplug_active;
    }

.. _`tb.members`:

Members
-------

lock
    *undescribed*

nhi
    *undescribed*

ctl
    *undescribed*

wq
    *undescribed*

root_switch
    *undescribed*

tunnel_list
    *undescribed*

hotplug_active
    *undescribed*

.. _`tb_upstream_port`:

tb_upstream_port
================

.. c:function:: struct tb_port *tb_upstream_port(struct tb_switch *sw)

    return the upstream port of a switch

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_upstream_port.description`:

Description
-----------

Every switch has an upstream port (for the root switch it is the NHI).

During switch alloc/init \ :c:func:`tb_upstream_port`\ ->remote may be NULL, even for
non root switches (on the NHI port remote is always NULL).

.. _`tb_upstream_port.return`:

Return
------

Returns the upstream port of the switch.

.. _`tb_downstream_route`:

tb_downstream_route
===================

.. c:function:: u64 tb_downstream_route(struct tb_port *port)

    get route to downstream switch

    :param struct tb_port \*port:
        *undescribed*

.. _`tb_downstream_route.description`:

Description
-----------

Port must not be the upstream port (otherwise a loop is created).

.. _`tb_downstream_route.return`:

Return
------

Returns a route to the switch behind \ ``port``\ .

.. This file was automatic generated / don't edit.


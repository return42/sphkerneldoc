.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/tb.h

.. _`tb_switch_nvm`:

struct tb_switch_nvm
====================

.. c:type:: struct tb_switch_nvm

    Structure holding switch NVM information

.. _`tb_switch_nvm.definition`:

Definition
----------

.. code-block:: c

    struct tb_switch_nvm {
        u8 major;
        u8 minor;
        int id;
        struct nvmem_device *active;
        struct nvmem_device *non_active;
        void *buf;
        size_t buf_data_size;
        bool authenticating;
    }

.. _`tb_switch_nvm.members`:

Members
-------

major
    Major version number of the active NVM portion

minor
    Minor version number of the active NVM portion

id
    Identifier used with both NVM portions

active
    Active portion NVMem device

non_active
    Non-active portion NVMem device

buf
    Buffer where the NVM image is stored before it is written to
    the actual NVM flash device

buf_data_size
    Number of bytes actually consumed by the new NVM
    image

authenticating
    The switch is authenticating the new NVM

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
        struct device dev;
        struct tb_regs_switch_header config;
        struct tb_port *ports;
        struct tb_dma_port *dma_port;
        struct tb *tb;
        u64 uid;
        uuid_t *uuid;
        u16 vendor;
        u16 device;
        const char *vendor_name;
        const char *device_name;
        unsigned int generation;
        int cap_plug_events;
        bool is_unplugged;
        u8 *drom;
        struct tb_switch_nvm *nvm;
        bool no_nvm_upgrade;
        bool safe_mode;
        bool boot;
        bool rpm;
        unsigned int authorized;
        struct work_struct work;
        enum tb_security_level security_level;
        u8 *key;
        u8 connection_id;
        u8 connection_key;
        u8 link;
        u8 depth;
    }

.. _`tb_switch.members`:

Members
-------

dev
    Device for the switch

config
    Switch configuration

ports
    Ports in this switch

dma_port
    If the switch has port supporting DMA configuration based
    mailbox this will hold the pointer to that (%NULL
    otherwise). If set it also means the switch has
    upgradeable NVM.

tb
    Pointer to the domain the switch belongs to

uid
    Unique ID of the switch

uuid
    UUID of the switch (or \ ``NULL``\  if not supported)

vendor
    Vendor ID of the switch

device
    Device ID of the switch

vendor_name
    Name of the vendor (or \ ``NULL``\  if not known)

device_name
    Name of the device (or \ ``NULL``\  if not known)

generation
    Switch Thunderbolt generation

cap_plug_events
    Offset to the plug events capability (%0 if not found)

is_unplugged
    The switch is going away

drom
    DROM of the switch (%NULL if not found)

nvm
    Pointer to the NVM if the switch has one (%NULL otherwise)

no_nvm_upgrade
    Prevent NVM upgrade of this switch

safe_mode
    The switch is in safe-mode

boot
    Whether the switch was already authorized on boot or not

rpm
    The switch supports runtime PM

authorized
    Whether the switch is authorized by user or policy

work
    Work used to automatically authorize a switch

security_level
    Switch supported security level

key
    Contains the key used to challenge the device or \ ``NULL``\  if not
    supported. Size of the key is \ ``TB_SWITCH_KEY_SIZE``\ .

connection_id
    Connection ID used with ICM messaging

connection_key
    Connection key used with ICM messaging

link
    Root switch link this switch is connected (ICM only)

depth
    Depth in the chain this switch is connected (ICM only)

.. _`tb_switch.description`:

Description
-----------

When the switch is being added or removed to the domain (other
switches) you need to have domain lock held. For switch authorization
internal switch_lock is enough.

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
        struct tb_xdomain *xdomain;
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
    Cached port configuration read from registers

sw
    Switch the port belongs to

remote
    Remote port (%NULL if not connected)

xdomain
    Remote host (%NULL if not connected)

cap_phy
    Offset, zero if not found

port
    Port number on switch

disabled
    Disabled by eeprom

dual_link_port
    If the switch is connected using two ports, points
    to the other port.

link_nr
    Is this primary or secondary port on the dual_link.

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

.. _`tb_cm_ops`:

struct tb_cm_ops
================

.. c:type:: struct tb_cm_ops

    Connection manager specific operations vector

.. _`tb_cm_ops.definition`:

Definition
----------

.. code-block:: c

    struct tb_cm_ops {
        int (*driver_ready)(struct tb *tb);
        int (*start)(struct tb *tb);
        void (*stop)(struct tb *tb);
        int (*suspend_noirq)(struct tb *tb);
        int (*resume_noirq)(struct tb *tb);
        int (*suspend)(struct tb *tb);
        void (*complete)(struct tb *tb);
        int (*runtime_suspend)(struct tb *tb);
        int (*runtime_resume)(struct tb *tb);
        void (*handle_event)(struct tb *tb, enum tb_cfg_pkg_type, const void *buf, size_t size);
        int (*get_boot_acl)(struct tb *tb, uuid_t *uuids, size_t nuuids);
        int (*set_boot_acl)(struct tb *tb, const uuid_t *uuids, size_t nuuids);
        int (*approve_switch)(struct tb *tb, struct tb_switch *sw);
        int (*add_switch_key)(struct tb *tb, struct tb_switch *sw);
        int (*challenge_switch_key)(struct tb *tb, struct tb_switch *sw, const u8 *challenge, u8 *response);
        int (*disconnect_pcie_paths)(struct tb *tb);
        int (*approve_xdomain_paths)(struct tb *tb, struct tb_xdomain *xd);
        int (*disconnect_xdomain_paths)(struct tb *tb, struct tb_xdomain *xd);
    }

.. _`tb_cm_ops.members`:

Members
-------

driver_ready
    Called right after control channel is started. Used by
    ICM to send driver ready message to the firmware.

start
    Starts the domain

stop
    Stops the domain

suspend_noirq
    Connection manager specific suspend_noirq

resume_noirq
    Connection manager specific resume_noirq

suspend
    Connection manager specific suspend

complete
    Connection manager specific complete

runtime_suspend
    Connection manager specific runtime_suspend

runtime_resume
    Connection manager specific runtime_resume

handle_event
    Handle thunderbolt event

get_boot_acl
    Get boot ACL list

set_boot_acl
    Set boot ACL list

approve_switch
    Approve switch

add_switch_key
    Add key to switch

challenge_switch_key
    Challenge switch using key

disconnect_pcie_paths
    Disconnects PCIe paths before NVM update

approve_xdomain_paths
    Approve (establish) XDomain DMA paths

disconnect_xdomain_paths
    Disconnect XDomain DMA paths

.. _`tb_upstream_port`:

tb_upstream_port
================

.. c:function:: struct tb_port *tb_upstream_port(struct tb_switch *sw)

    return the upstream port of a switch

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

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

    :param port:
        *undescribed*
    :type port: struct tb_port \*

.. _`tb_downstream_route.description`:

Description
-----------

Port must not be the upstream port (otherwise a loop is created).

.. _`tb_downstream_route.return`:

Return
------

Returns a route to the switch behind \ ``port``\ .

.. This file was automatic generated / don't edit.


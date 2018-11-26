.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_verbs.h

.. _`rdma_hw_stats`:

struct rdma_hw_stats
====================

.. c:type:: struct rdma_hw_stats

    \ ``lock``\  - Mutex to protect parallel write access to lifespan and values of counters, which are 64bits and not guaranteeed to be written atomicaly on 32bits systems. \ ``timestamp``\  - Used by the core code to track when the last update was \ ``lifespan``\  - Used by the core code to determine how old the counters should be before being updated again.  Stored in jiffies, defaults to 10 milliseconds, drivers can override the default be specifying their own value during their allocation routine. \ ``name``\  - Array of pointers to static names used for the counters in directory. \ ``num_counters``\  - How many hardware counters there are.  If name is shorter than this number, a kernel oops will result.  Driver authors are encouraged to leave BUILD_BUG_ON(ARRAY_SIZE(@name) < num_counters) in their code to prevent this. \ ``value``\  - Array of u64 counters that are accessed by the sysfs code and filled in by the drivers get_stats routine

.. _`rdma_hw_stats.definition`:

Definition
----------

.. code-block:: c

    struct rdma_hw_stats {
        struct mutex lock;
        unsigned long timestamp;
        unsigned long lifespan;
        const char * const *names;
        int num_counters;
        u64 value[];
    }

.. _`rdma_hw_stats.members`:

Members
-------

lock
    *undescribed*

timestamp
    *undescribed*

lifespan
    *undescribed*

names
    *undescribed*

num_counters
    *undescribed*

value
    *undescribed*

.. _`rdma_alloc_hw_stats_struct`:

rdma_alloc_hw_stats_struct
==========================

.. c:function:: struct rdma_hw_stats *rdma_alloc_hw_stats_struct(const char * const *names, int num_counters, unsigned long lifespan)

    Helper function to allocate dynamic struct for drivers. \ ``names``\  - Array of static const char \* \ ``num_counters``\  - How many elements in array \ ``lifespan``\  - How many milliseconds between updates

    :param names:
        *undescribed*
    :type names: const char \* const \*

    :param num_counters:
        *undescribed*
    :type num_counters: int

    :param lifespan:
        *undescribed*
    :type lifespan: unsigned long

.. _`ib_rate_to_mult`:

ib_rate_to_mult
===============

.. c:function:: __attribute_const__ int ib_rate_to_mult(enum ib_rate rate)

    Convert the IB rate enum to a multiple of the base rate of 2.5 Gbit/sec.  For example, IB_RATE_5_GBPS will be converted to 2, since 5 Gbit/sec is 2 \* 2.5 Gbit/sec.

    :param rate:
        rate to convert.
    :type rate: enum ib_rate

.. _`ib_rate_to_mbps`:

ib_rate_to_mbps
===============

.. c:function:: __attribute_const__ int ib_rate_to_mbps(enum ib_rate rate)

    Convert the IB rate enum to Mbps. For example, IB_RATE_2_5_GBPS will be converted to 2500.

    :param rate:
        rate to convert.
    :type rate: enum ib_rate

.. _`ib_mr_type`:

enum ib_mr_type
===============

.. c:type:: enum ib_mr_type

    memory region type

.. _`ib_mr_type.definition`:

Definition
----------

.. code-block:: c

    enum ib_mr_type {
        IB_MR_TYPE_MEM_REG,
        IB_MR_TYPE_SIGNATURE,
        IB_MR_TYPE_SG_GAPS
    };

.. _`ib_mr_type.constants`:

Constants
---------

IB_MR_TYPE_MEM_REG
    memory region that is used for
    normal registration

IB_MR_TYPE_SIGNATURE
    memory region that is used for
    signature operations (data-integrity
    capable regions)

IB_MR_TYPE_SG_GAPS
    memory region that is capable to
    register any arbitrary sg lists (without
    the normal mr constraints - see
    ib_map_mr_sg)

.. _`ib_t10_dif_domain`:

struct ib_t10_dif_domain
========================

.. c:type:: struct ib_t10_dif_domain

    Parameters specific for T10-DIF domain.

.. _`ib_t10_dif_domain.definition`:

Definition
----------

.. code-block:: c

    struct ib_t10_dif_domain {
        enum ib_t10_dif_bg_type bg_type;
        u16 pi_interval;
        u16 bg;
        u16 app_tag;
        u32 ref_tag;
        bool ref_remap;
        bool app_escape;
        bool ref_escape;
        u16 apptag_check_mask;
    }

.. _`ib_t10_dif_domain.members`:

Members
-------

bg_type
    T10-DIF block guard type (CRC\|CSUM)

pi_interval
    protection information interval.

bg
    seed of guard computation.

app_tag
    application tag of guard block

ref_tag
    initial guard block reference tag.

ref_remap
    Indicate wethear the reftag increments each block

app_escape
    Indicate to skip block check if apptag=0xffff

ref_escape
    Indicate to skip block check if reftag=0xffffffff

apptag_check_mask
    check bitmask of application tag.

.. _`ib_sig_domain`:

struct ib_sig_domain
====================

.. c:type:: struct ib_sig_domain

    Parameters for signature domain

.. _`ib_sig_domain.definition`:

Definition
----------

.. code-block:: c

    struct ib_sig_domain {
        enum ib_signature_type sig_type;
        union {
            struct ib_t10_dif_domain dif;
        } sig;
    }

.. _`ib_sig_domain.members`:

Members
-------

sig_type
    specific signauture type

sig
    union of all signature domain attributes that may
    be used to set domain layout.

.. _`ib_sig_attrs`:

struct ib_sig_attrs
===================

.. c:type:: struct ib_sig_attrs

    Parameters for signature handover operation

.. _`ib_sig_attrs.definition`:

Definition
----------

.. code-block:: c

    struct ib_sig_attrs {
        u8 check_mask;
        struct ib_sig_domain mem;
        struct ib_sig_domain wire;
    }

.. _`ib_sig_attrs.members`:

Members
-------

check_mask
    bitmask for signature byte check (8 bytes)

mem
    memory domain layout desciptor.

wire
    wire domain layout desciptor.

.. _`ib_sig_err`:

struct ib_sig_err
=================

.. c:type:: struct ib_sig_err

    signature error descriptor

.. _`ib_sig_err.definition`:

Definition
----------

.. code-block:: c

    struct ib_sig_err {
        enum ib_sig_err_type err_type;
        u32 expected;
        u32 actual;
        u64 sig_err_offset;
        u32 key;
    }

.. _`ib_sig_err.members`:

Members
-------

err_type
    *undescribed*

expected
    *undescribed*

actual
    *undescribed*

sig_err_offset
    *undescribed*

key
    *undescribed*

.. _`ib_mr_status`:

struct ib_mr_status
===================

.. c:type:: struct ib_mr_status

    Memory region status container

.. _`ib_mr_status.definition`:

Definition
----------

.. code-block:: c

    struct ib_mr_status {
        u32 fail_status;
        struct ib_sig_err sig_err;
    }

.. _`ib_mr_status.members`:

Members
-------

fail_status
    Bitmask of MR checks status. For each
    failed check a corresponding status bit is set.

sig_err
    Additional info for IB_MR_CEHCK_SIG_STATUS
    failure.

.. _`mult_to_ib_rate`:

mult_to_ib_rate
===============

.. c:function:: __attribute_const__ enum ib_rate mult_to_ib_rate(int mult)

    Convert a multiple of 2.5 Gbit/sec to an IB rate enum.

    :param mult:
        multiple to convert.
    :type mult: int

.. _`rdma_netdev`:

struct rdma_netdev
==================

.. c:type:: struct rdma_netdev

    rdma netdev For cases where netstack interfacing is required.

.. _`rdma_netdev.definition`:

Definition
----------

.. code-block:: c

    struct rdma_netdev {
        void *clnt_priv;
        struct ib_device *hca;
        u8 port_num;
        void (*free_rdma_netdev)(struct net_device *netdev);
        void (*set_id)(struct net_device *netdev, int id);
        int (*send)(struct net_device *dev, struct sk_buff *skb, struct ib_ah *address, u32 dqpn);
        int (*attach_mcast)(struct net_device *dev, struct ib_device *hca,union ib_gid *gid, u16 mlid, int set_qkey, u32 qkey);
        int (*detach_mcast)(struct net_device *dev, struct ib_device *hca, union ib_gid *gid, u16 mlid);
    }

.. _`rdma_netdev.members`:

Members
-------

clnt_priv
    *undescribed*

hca
    *undescribed*

port_num
    *undescribed*

free_rdma_netdev
    *undescribed*

set_id
    *undescribed*

send
    *undescribed*

attach_mcast
    *undescribed*

detach_mcast
    *undescribed*

.. _`ib_is_destroy_retryable`:

ib_is_destroy_retryable
=======================

.. c:function:: bool ib_is_destroy_retryable(int ret, enum rdma_remove_reason why, struct ib_uobject *uobj)

    Check whether the uobject destruction is retryable.

    :param ret:
        The initial destruction return code
    :type ret: int

    :param why:
        remove reason
    :type why: enum rdma_remove_reason

    :param uobj:
        The uobject that is destroyed
    :type uobj: struct ib_uobject \*

.. _`ib_is_destroy_retryable.description`:

Description
-----------

This function is a helper function that IB layer and low-level drivers
can use to consider whether the destruction of the given uobject is
retry-able.
It checks the original return code, if it wasn't success the destruction
is retryable according to the ucontext state (i.e. cleanup_retryable) and
the remove reason. (i.e. why).
Must be called with the object locked for destroy.

.. _`ib_destroy_usecnt`:

ib_destroy_usecnt
=================

.. c:function:: int ib_destroy_usecnt(atomic_t *usecnt, enum rdma_remove_reason why, struct ib_uobject *uobj)

    Called during destruction to check the usecnt

    :param usecnt:
        The usecnt atomic
    :type usecnt: atomic_t \*

    :param why:
        remove reason
    :type why: enum rdma_remove_reason

    :param uobj:
        The uobject that is destroyed
    :type uobj: struct ib_uobject \*

.. _`ib_destroy_usecnt.description`:

Description
-----------

Non-zero usecnts will block destruction unless destruction was triggered by
a ucontext cleanup.

.. _`ib_modify_qp_is_ok`:

ib_modify_qp_is_ok
==================

.. c:function:: bool ib_modify_qp_is_ok(enum ib_qp_state cur_state, enum ib_qp_state next_state, enum ib_qp_type type, enum ib_qp_attr_mask mask)

    Check that the supplied attribute mask contains all required attributes and no attributes not allowed for the given QP state transition.

    :param cur_state:
        Current QP state
    :type cur_state: enum ib_qp_state

    :param next_state:
        Next QP state
    :type next_state: enum ib_qp_state

    :param type:
        QP type
    :type type: enum ib_qp_type

    :param mask:
        Mask of supplied QP attributes
    :type mask: enum ib_qp_attr_mask

.. _`ib_modify_qp_is_ok.description`:

Description
-----------

This function is a helper function that a low-level driver's
modify_qp method can use to validate the consumer's input.  It
checks that cur_state and next_state are valid QP states, that a
transition from cur_state to next_state is allowed by the IB spec,
and that the attribute mask supplied is allowed for the transition.

.. _`rdma_cap_ib_switch`:

rdma_cap_ib_switch
==================

.. c:function:: bool rdma_cap_ib_switch(const struct ib_device *device)

    Check if the device is IB switch

    :param device:
        Device to check
    :type device: const struct ib_device \*

.. _`rdma_cap_ib_switch.description`:

Description
-----------

Device driver is responsible for setting is_switch bit on
in ib_device structure at init time.

.. _`rdma_cap_ib_switch.return`:

Return
------

true if the device is IB switch.

.. _`rdma_start_port`:

rdma_start_port
===============

.. c:function:: u8 rdma_start_port(const struct ib_device *device)

    Return the first valid port number for the device specified

    :param device:
        Device to be checked
    :type device: const struct ib_device \*

.. _`rdma_start_port.description`:

Description
-----------

Return start port number

.. _`rdma_end_port`:

rdma_end_port
=============

.. c:function:: u8 rdma_end_port(const struct ib_device *device)

    Return the last valid port number for the device specified

    :param device:
        Device to be checked
    :type device: const struct ib_device \*

.. _`rdma_end_port.description`:

Description
-----------

Return last port number

.. _`rdma_cap_ib_mad`:

rdma_cap_ib_mad
===============

.. c:function:: bool rdma_cap_ib_mad(const struct ib_device *device, u8 port_num)

    Check if the port of a device supports Infiniband Management Datagrams.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_ib_mad.description`:

Description
-----------

Management Datagrams (MAD) are a required part of the InfiniBand
specification and are supported on all InfiniBand devices.  A slightly
extended version are also supported on OPA interfaces.

.. _`rdma_cap_ib_mad.return`:

Return
------

true if the port supports sending/receiving of MAD packets.

.. _`rdma_cap_opa_mad`:

rdma_cap_opa_mad
================

.. c:function:: bool rdma_cap_opa_mad(struct ib_device *device, u8 port_num)

    Check if the port of device provides support for OPA Management Datagrams.

    :param device:
        Device to check
    :type device: struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_opa_mad.description`:

Description
-----------

Intel OmniPath devices extend and/or replace the InfiniBand Management
datagrams with their own versions.  These OPA MADs share many but not all of
the characteristics of InfiniBand MADs.

.. _`rdma_cap_opa_mad.opa-mads-differ-in-the-following-ways`:

OPA MADs differ in the following ways
-------------------------------------


1) MADs are variable size up to 2K
IBTA defined MADs remain fixed at 256 bytes
2) OPA SMPs must carry valid PKeys
3) OPA SMP packets are a different format

.. _`rdma_cap_opa_mad.return`:

Return
------

true if the port supports OPA MAD packet formats.

.. _`rdma_cap_ib_smi`:

rdma_cap_ib_smi
===============

.. c:function:: bool rdma_cap_ib_smi(const struct ib_device *device, u8 port_num)

    Check if the port of a device provides an Infiniband Subnet Management Agent (SMA) on the Subnet Management Interface (SMI).

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_ib_smi.description`:

Description
-----------

Each InfiniBand node is required to provide a Subnet Management Agent
that the subnet manager can access.  Prior to the fabric being fully
configured by the subnet manager, the SMA is accessed via a well known
interface called the Subnet Management Interface (SMI).  This interface
uses directed route packets to communicate with the SM to get around the
chicken and egg problem of the SM needing to know what's on the fabric
in order to configure the fabric, and needing to configure the fabric in
order to send packets to the devices on the fabric.  These directed
route packets do not need the fabric fully configured in order to reach
their destination.  The SMI is the only method allowed to send
directed route packets on an InfiniBand fabric.

.. _`rdma_cap_ib_smi.return`:

Return
------

true if the port provides an SMI.

.. _`rdma_cap_ib_cm`:

rdma_cap_ib_cm
==============

.. c:function:: bool rdma_cap_ib_cm(const struct ib_device *device, u8 port_num)

    Check if the port of device has the capability Infiniband Communication Manager.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_ib_cm.description`:

Description
-----------

The InfiniBand Communication Manager is one of many pre-defined General
Service Agents (GSA) that are accessed via the General Service
Interface (GSI).  It's role is to facilitate establishment of connections
between nodes as well as other management related tasks for established
connections.

.. _`rdma_cap_ib_cm.return`:

Return
------

true if the port supports an IB CM (this does not guarantee that
a CM is actually running however).

.. _`rdma_cap_iw_cm`:

rdma_cap_iw_cm
==============

.. c:function:: bool rdma_cap_iw_cm(const struct ib_device *device, u8 port_num)

    Check if the port of device has the capability IWARP Communication Manager.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_iw_cm.description`:

Description
-----------

Similar to above, but specific to iWARP connections which have a different
managment protocol than InfiniBand.

.. _`rdma_cap_iw_cm.return`:

Return
------

true if the port supports an iWARP CM (this does not guarantee that
a CM is actually running however).

.. _`rdma_cap_ib_sa`:

rdma_cap_ib_sa
==============

.. c:function:: bool rdma_cap_ib_sa(const struct ib_device *device, u8 port_num)

    Check if the port of device has the capability Infiniband Subnet Administration.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_ib_sa.description`:

Description
-----------

An InfiniBand Subnet Administration (SA) service is a pre-defined General
Service Agent (GSA) provided by the Subnet Manager (SM).  On InfiniBand
fabrics, devices should resolve routes to other hosts by contacting the
SA to query the proper route.

.. _`rdma_cap_ib_sa.return`:

Return
------

true if the port should act as a client to the fabric Subnet
Administration interface.  This does not imply that the SA service is
running locally.

.. _`rdma_cap_ib_mcast`:

rdma_cap_ib_mcast
=================

.. c:function:: bool rdma_cap_ib_mcast(const struct ib_device *device, u8 port_num)

    Check if the port of device has the capability Infiniband Multicast.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_ib_mcast.description`:

Description
-----------

InfiniBand multicast registration is more complex than normal IPv4 or
IPv6 multicast registration.  Each Host Channel Adapter must register
with the Subnet Manager when it wishes to join a multicast group.  It
should do so only once regardless of how many queue pairs it subscribes
to this group.  And it should leave the group only after all queue pairs
attached to the group have been detached.

.. _`rdma_cap_ib_mcast.return`:

Return
------

true if the port must undertake the additional adminstrative
overhead of registering/unregistering with the SM and tracking of the
total number of queue pairs attached to the multicast group.

.. _`rdma_cap_af_ib`:

rdma_cap_af_ib
==============

.. c:function:: bool rdma_cap_af_ib(const struct ib_device *device, u8 port_num)

    Check if the port of device has the capability Native Infiniband Address.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_af_ib.description`:

Description
-----------

InfiniBand addressing uses a port's GUID + Subnet Prefix to make a default
GID.  RoCE uses a different mechanism, but still generates a GID via
a prescribed mechanism and port specific data.

.. _`rdma_cap_af_ib.return`:

Return
------

true if the port uses a GID address to identify devices on the
network.

.. _`rdma_cap_eth_ah`:

rdma_cap_eth_ah
===============

.. c:function:: bool rdma_cap_eth_ah(const struct ib_device *device, u8 port_num)

    Check if the port of device has the capability Ethernet Address Handle.

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_eth_ah.description`:

Description
-----------

RoCE is InfiniBand over Ethernet, and it uses a well defined technique
to fabricate GIDs over Ethernet/IP specific addresses native to the
port.  Normally, packet headers are generated by the sending host
adapter, but when sending connectionless datagrams, we must manually
inject the proper headers for the fabric we are communicating over.

.. _`rdma_cap_eth_ah.return`:

Return
------

true if we are running as a RoCE port and must force the
addition of a Global Route Header built from our Ethernet Address
Handle into our header list for connectionless packets.

.. _`rdma_cap_opa_ah`:

rdma_cap_opa_ah
===============

.. c:function:: bool rdma_cap_opa_ah(struct ib_device *device, u8 port_num)

    Check if the port of device supports OPA Address handles

    :param device:
        Device to check
    :type device: struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_opa_ah.return`:

Return
------

true if we are running on an OPA device which supports
the extended OPA addressing.

.. _`rdma_max_mad_size`:

rdma_max_mad_size
=================

.. c:function:: size_t rdma_max_mad_size(const struct ib_device *device, u8 port_num)

    Return the max MAD size required by this RDMA Port.

    :param device:
        Device
    :type device: const struct ib_device \*

    :param port_num:
        Port number
    :type port_num: u8

.. _`rdma_max_mad_size.description`:

Description
-----------

This MAD size includes the MAD headers and MAD payload.  No other headers
are included.

Return the max MAD size required by the Port.  Will return 0 if the port
does not support MADs

.. _`rdma_cap_roce_gid_table`:

rdma_cap_roce_gid_table
=======================

.. c:function:: bool rdma_cap_roce_gid_table(const struct ib_device *device, u8 port_num)

    Check if the port of device uses roce_gid_table

    :param device:
        Device to check
    :type device: const struct ib_device \*

    :param port_num:
        Port number to check
    :type port_num: u8

.. _`rdma_cap_roce_gid_table.description`:

Description
-----------

RoCE GID table mechanism manages the various GIDs for a device.

.. _`rdma_cap_roce_gid_table.note`:

NOTE
----

if allocating the port's GID table has failed, this call will still
return true, but any RoCE GID table API will fail.

.. _`rdma_cap_roce_gid_table.return`:

Return
------

true if the port uses RoCE GID table mechanism in order to manage
its GIDs.

.. _`rdma_create_ah`:

rdma_create_ah
==============

.. c:function:: struct ib_ah *rdma_create_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr)

    Creates an address handle for the given address vector.

    :param pd:
        The protection domain associated with the address handle.
    :type pd: struct ib_pd \*

    :param ah_attr:
        The attributes of the address vector.
    :type ah_attr: struct rdma_ah_attr \*

.. _`rdma_create_ah.description`:

Description
-----------

The address handle is used to reference a local or global destination
in all UD QP post sends.

.. _`rdma_create_user_ah`:

rdma_create_user_ah
===================

.. c:function:: struct ib_ah *rdma_create_user_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr, struct ib_udata *udata)

    Creates an address handle for the given address vector. It resolves destination mac address for ah attribute of RoCE type.

    :param pd:
        The protection domain associated with the address handle.
    :type pd: struct ib_pd \*

    :param ah_attr:
        The attributes of the address vector.
    :type ah_attr: struct rdma_ah_attr \*

    :param udata:
        pointer to user's input output buffer information need by
        provider driver.
    :type udata: struct ib_udata \*

.. _`rdma_create_user_ah.description`:

Description
-----------

It returns 0 on success and returns appropriate error code on error.
The address handle is used to reference a local or global destination
in all UD QP post sends.

.. _`ib_get_gids_from_rdma_hdr`:

ib_get_gids_from_rdma_hdr
=========================

.. c:function:: int ib_get_gids_from_rdma_hdr(const union rdma_network_hdr *hdr, enum rdma_network_type net_type, union ib_gid *sgid, union ib_gid *dgid)

    Get sgid and dgid from GRH or IPv4 header work completion.

    :param hdr:
        the L3 header to parse
    :type hdr: const union rdma_network_hdr \*

    :param net_type:
        type of header to parse
    :type net_type: enum rdma_network_type

    :param sgid:
        place to store source gid
    :type sgid: union ib_gid \*

    :param dgid:
        place to store destination gid
    :type dgid: union ib_gid \*

.. _`ib_get_rdma_header_version`:

ib_get_rdma_header_version
==========================

.. c:function:: int ib_get_rdma_header_version(const union rdma_network_hdr *hdr)

    Get the header version

    :param hdr:
        the L3 header to parse
    :type hdr: const union rdma_network_hdr \*

.. _`ib_init_ah_attr_from_wc`:

ib_init_ah_attr_from_wc
=======================

.. c:function:: int ib_init_ah_attr_from_wc(struct ib_device *device, u8 port_num, const struct ib_wc *wc, const struct ib_grh *grh, struct rdma_ah_attr *ah_attr)

    Initializes address handle attributes from a work completion.

    :param device:
        Device on which the received message arrived.
    :type device: struct ib_device \*

    :param port_num:
        Port on which the received message arrived.
    :type port_num: u8

    :param wc:
        Work completion associated with the received message.
    :type wc: const struct ib_wc \*

    :param grh:
        References the received global route header.  This parameter is
        ignored unless the work completion indicates that the GRH is valid.
    :type grh: const struct ib_grh \*

    :param ah_attr:
        Returned attributes that can be used when creating an address
        handle for replying to the message.
        When \ :c:func:`ib_init_ah_attr_from_wc`\  returns success,
        (a) for IB link layer it optionally contains a reference to SGID attribute
        when GRH is present for IB link layer.
        (b) for RoCE link layer it contains a reference to SGID attribute.
        User must invoke \ :c:func:`rdma_cleanup_ah_attr_gid_attr`\  to release reference to SGID
        attributes which are initialized using \ :c:func:`ib_init_ah_attr_from_wc`\ .
    :type ah_attr: struct rdma_ah_attr \*

.. _`ib_create_ah_from_wc`:

ib_create_ah_from_wc
====================

.. c:function:: struct ib_ah *ib_create_ah_from_wc(struct ib_pd *pd, const struct ib_wc *wc, const struct ib_grh *grh, u8 port_num)

    Creates an address handle associated with the sender of the specified work completion.

    :param pd:
        The protection domain associated with the address handle.
    :type pd: struct ib_pd \*

    :param wc:
        Work completion information associated with a received message.
    :type wc: const struct ib_wc \*

    :param grh:
        References the received global route header.  This parameter is
        ignored unless the work completion indicates that the GRH is valid.
    :type grh: const struct ib_grh \*

    :param port_num:
        The outbound port number to associate with the address.
    :type port_num: u8

.. _`ib_create_ah_from_wc.description`:

Description
-----------

The address handle is used to reference a local or global destination
in all UD QP post sends.

.. _`rdma_modify_ah`:

rdma_modify_ah
==============

.. c:function:: int rdma_modify_ah(struct ib_ah *ah, struct rdma_ah_attr *ah_attr)

    Modifies the address vector associated with an address handle.

    :param ah:
        The address handle to modify.
    :type ah: struct ib_ah \*

    :param ah_attr:
        The new address vector attributes to associate with the
        address handle.
    :type ah_attr: struct rdma_ah_attr \*

.. _`rdma_query_ah`:

rdma_query_ah
=============

.. c:function:: int rdma_query_ah(struct ib_ah *ah, struct rdma_ah_attr *ah_attr)

    Queries the address vector associated with an address handle.

    :param ah:
        The address handle to query.
    :type ah: struct ib_ah \*

    :param ah_attr:
        The address vector attributes associated with the address
        handle.
    :type ah_attr: struct rdma_ah_attr \*

.. _`rdma_destroy_ah`:

rdma_destroy_ah
===============

.. c:function:: int rdma_destroy_ah(struct ib_ah *ah)

    Destroys an address handle.

    :param ah:
        The address handle to destroy.
    :type ah: struct ib_ah \*

.. _`ib_create_srq`:

ib_create_srq
=============

.. c:function:: struct ib_srq *ib_create_srq(struct ib_pd *pd, struct ib_srq_init_attr *srq_init_attr)

    Creates a SRQ associated with the specified protection domain.

    :param pd:
        The protection domain associated with the SRQ.
    :type pd: struct ib_pd \*

    :param srq_init_attr:
        A list of initial attributes required to create the
        SRQ.  If SRQ creation succeeds, then the attributes are updated to
        the actual capabilities of the created SRQ.
    :type srq_init_attr: struct ib_srq_init_attr \*

.. _`ib_create_srq.description`:

Description
-----------

srq_attr->max_wr and srq_attr->max_sge are read the determine the
requested size of the SRQ, and set to the actual values allocated
on return.  If \ :c:func:`ib_create_srq`\  succeeds, then max_wr and max_sge
will always be at least as large as the requested values.

.. _`ib_modify_srq`:

ib_modify_srq
=============

.. c:function:: int ib_modify_srq(struct ib_srq *srq, struct ib_srq_attr *srq_attr, enum ib_srq_attr_mask srq_attr_mask)

    Modifies the attributes for the specified SRQ.

    :param srq:
        The SRQ to modify.
    :type srq: struct ib_srq \*

    :param srq_attr:
        On input, specifies the SRQ attributes to modify.  On output,
        the current values of selected SRQ attributes are returned.
    :type srq_attr: struct ib_srq_attr \*

    :param srq_attr_mask:
        A bit-mask used to specify which attributes of the SRQ
        are being modified.
    :type srq_attr_mask: enum ib_srq_attr_mask

.. _`ib_modify_srq.description`:

Description
-----------

The mask may contain IB_SRQ_MAX_WR to resize the SRQ and/or
IB_SRQ_LIMIT to set the SRQ's limit and request notification when
the number of receives queued drops below the limit.

.. _`ib_query_srq`:

ib_query_srq
============

.. c:function:: int ib_query_srq(struct ib_srq *srq, struct ib_srq_attr *srq_attr)

    Returns the attribute list and current values for the specified SRQ.

    :param srq:
        The SRQ to query.
    :type srq: struct ib_srq \*

    :param srq_attr:
        The attributes of the specified SRQ.
    :type srq_attr: struct ib_srq_attr \*

.. _`ib_destroy_srq`:

ib_destroy_srq
==============

.. c:function:: int ib_destroy_srq(struct ib_srq *srq)

    Destroys the specified SRQ.

    :param srq:
        The SRQ to destroy.
    :type srq: struct ib_srq \*

.. _`ib_post_srq_recv`:

ib_post_srq_recv
================

.. c:function:: int ib_post_srq_recv(struct ib_srq *srq, const struct ib_recv_wr *recv_wr, const struct ib_recv_wr **bad_recv_wr)

    Posts a list of work requests to the specified SRQ.

    :param srq:
        The SRQ to post the work request on.
    :type srq: struct ib_srq \*

    :param recv_wr:
        A list of work requests to post on the receive queue.
    :type recv_wr: const struct ib_recv_wr \*

    :param bad_recv_wr:
        On an immediate failure, this parameter will reference
        the work request that failed to be posted on the QP.
    :type bad_recv_wr: const struct ib_recv_wr \*\*

.. _`ib_create_qp`:

ib_create_qp
============

.. c:function:: struct ib_qp *ib_create_qp(struct ib_pd *pd, struct ib_qp_init_attr *qp_init_attr)

    Creates a QP associated with the specified protection domain.

    :param pd:
        The protection domain associated with the QP.
    :type pd: struct ib_pd \*

    :param qp_init_attr:
        A list of initial attributes required to create the
        QP.  If QP creation succeeds, then the attributes are updated to
        the actual capabilities of the created QP.
    :type qp_init_attr: struct ib_qp_init_attr \*

.. _`ib_modify_qp_with_udata`:

ib_modify_qp_with_udata
=======================

.. c:function:: int ib_modify_qp_with_udata(struct ib_qp *qp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    Modifies the attributes for the specified QP.

    :param qp:
        The QP to modify.
    :type qp: struct ib_qp \*

    :param attr:
        On input, specifies the QP attributes to modify.  On output,
        the current values of selected QP attributes are returned.
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        A bit-mask used to specify which attributes of the QP
        are being modified.
    :type attr_mask: int

    :param udata:
        pointer to user's input output buffer information
        are being modified.
        It returns 0 on success and returns appropriate error code on error.
    :type udata: struct ib_udata \*

.. _`ib_modify_qp`:

ib_modify_qp
============

.. c:function:: int ib_modify_qp(struct ib_qp *qp, struct ib_qp_attr *qp_attr, int qp_attr_mask)

    Modifies the attributes for the specified QP and then transitions the QP to the given state.

    :param qp:
        The QP to modify.
    :type qp: struct ib_qp \*

    :param qp_attr:
        On input, specifies the QP attributes to modify.  On output,
        the current values of selected QP attributes are returned.
    :type qp_attr: struct ib_qp_attr \*

    :param qp_attr_mask:
        A bit-mask used to specify which attributes of the QP
        are being modified.
    :type qp_attr_mask: int

.. _`ib_query_qp`:

ib_query_qp
===========

.. c:function:: int ib_query_qp(struct ib_qp *qp, struct ib_qp_attr *qp_attr, int qp_attr_mask, struct ib_qp_init_attr *qp_init_attr)

    Returns the attribute list and current values for the specified QP.

    :param qp:
        The QP to query.
    :type qp: struct ib_qp \*

    :param qp_attr:
        The attributes of the specified QP.
    :type qp_attr: struct ib_qp_attr \*

    :param qp_attr_mask:
        A bit-mask used to select specific attributes to query.
    :type qp_attr_mask: int

    :param qp_init_attr:
        Additional attributes of the selected QP.
    :type qp_init_attr: struct ib_qp_init_attr \*

.. _`ib_query_qp.description`:

Description
-----------

The qp_attr_mask may be used to limit the query to gathering only the
selected attributes.

.. _`ib_destroy_qp`:

ib_destroy_qp
=============

.. c:function:: int ib_destroy_qp(struct ib_qp *qp)

    Destroys the specified QP.

    :param qp:
        The QP to destroy.
    :type qp: struct ib_qp \*

.. _`ib_open_qp`:

ib_open_qp
==========

.. c:function:: struct ib_qp *ib_open_qp(struct ib_xrcd *xrcd, struct ib_qp_open_attr *qp_open_attr)

    Obtain a reference to an existing sharable QP. \ ``xrcd``\  - XRC domain

    :param xrcd:
        *undescribed*
    :type xrcd: struct ib_xrcd \*

    :param qp_open_attr:
        Attributes identifying the QP to open.
    :type qp_open_attr: struct ib_qp_open_attr \*

.. _`ib_open_qp.description`:

Description
-----------

Returns a reference to a sharable QP.

.. _`ib_close_qp`:

ib_close_qp
===========

.. c:function:: int ib_close_qp(struct ib_qp *qp)

    Release an external reference to a QP.

    :param qp:
        The QP handle to release
    :type qp: struct ib_qp \*

.. _`ib_close_qp.description`:

Description
-----------

The opened QP handle is released by the caller.  The underlying
shared QP is not destroyed until all internal references are released.

.. _`ib_post_send`:

ib_post_send
============

.. c:function:: int ib_post_send(struct ib_qp *qp, const struct ib_send_wr *send_wr, const struct ib_send_wr **bad_send_wr)

    Posts a list of work requests to the send queue of the specified QP.

    :param qp:
        The QP to post the work request on.
    :type qp: struct ib_qp \*

    :param send_wr:
        A list of work requests to post on the send queue.
    :type send_wr: const struct ib_send_wr \*

    :param bad_send_wr:
        On an immediate failure, this parameter will reference
        the work request that failed to be posted on the QP.
    :type bad_send_wr: const struct ib_send_wr \*\*

.. _`ib_post_send.description`:

Description
-----------

While IBA Vol. 1 section 11.4.1.1 specifies that if an immediate
error is returned, the QP state shall not be affected,
\ :c:func:`ib_post_send`\  will return an immediate error after queueing any
earlier work requests in the list.

.. _`ib_post_recv`:

ib_post_recv
============

.. c:function:: int ib_post_recv(struct ib_qp *qp, const struct ib_recv_wr *recv_wr, const struct ib_recv_wr **bad_recv_wr)

    Posts a list of work requests to the receive queue of the specified QP.

    :param qp:
        The QP to post the work request on.
    :type qp: struct ib_qp \*

    :param recv_wr:
        A list of work requests to post on the receive queue.
    :type recv_wr: const struct ib_recv_wr \*

    :param bad_recv_wr:
        On an immediate failure, this parameter will reference
        the work request that failed to be posted on the QP.
    :type bad_recv_wr: const struct ib_recv_wr \*\*

.. _`__ib_create_cq`:

\__ib_create_cq
===============

.. c:function:: struct ib_cq *__ib_create_cq(struct ib_device *device, ib_comp_handler comp_handler, void (*event_handler)(struct ib_event *, void *), void *cq_context, const struct ib_cq_init_attr *cq_attr, const char *caller)

    Creates a CQ on the specified device.

    :param device:
        The device on which to create the CQ.
    :type device: struct ib_device \*

    :param comp_handler:
        A user-specified callback that is invoked when a
        completion event occurs on the CQ.
    :type comp_handler: ib_comp_handler

    :param void (\*event_handler)(struct ib_event \*, void \*):
        A user-specified callback that is invoked when an
        asynchronous event not associated with a completion occurs on the CQ.

    :param cq_context:
        Context associated with the CQ returned to the user via
        the associated completion and event handlers.
    :type cq_context: void \*

    :param cq_attr:
        The attributes the CQ should be created upon.
    :type cq_attr: const struct ib_cq_init_attr \*

    :param caller:
        *undescribed*
    :type caller: const char \*

.. _`__ib_create_cq.description`:

Description
-----------

Users can examine the cq structure to determine the actual CQ size.

.. _`ib_resize_cq`:

ib_resize_cq
============

.. c:function:: int ib_resize_cq(struct ib_cq *cq, int cqe)

    Modifies the capacity of the CQ.

    :param cq:
        The CQ to resize.
    :type cq: struct ib_cq \*

    :param cqe:
        The minimum size of the CQ.
    :type cqe: int

.. _`ib_resize_cq.description`:

Description
-----------

Users can examine the cq structure to determine the actual CQ size.

.. _`rdma_set_cq_moderation`:

rdma_set_cq_moderation
======================

.. c:function:: int rdma_set_cq_moderation(struct ib_cq *cq, u16 cq_count, u16 cq_period)

    Modifies moderation params of the CQ

    :param cq:
        The CQ to modify.
    :type cq: struct ib_cq \*

    :param cq_count:
        number of CQEs that will trigger an event
    :type cq_count: u16

    :param cq_period:
        max period of time in usec before triggering an event
    :type cq_period: u16

.. _`ib_destroy_cq`:

ib_destroy_cq
=============

.. c:function:: int ib_destroy_cq(struct ib_cq *cq)

    Destroys the specified CQ.

    :param cq:
        The CQ to destroy.
    :type cq: struct ib_cq \*

.. _`ib_poll_cq`:

ib_poll_cq
==========

.. c:function:: int ib_poll_cq(struct ib_cq *cq, int num_entries, struct ib_wc *wc)

    poll a CQ for completion(s)

    :param cq:
        the CQ being polled
    :type cq: struct ib_cq \*

    :param num_entries:
        maximum number of completions to return
    :type num_entries: int

    :param wc:
        array of at least \ ``num_entries``\  \ :c:type:`struct ib_wc <ib_wc>`\  where completions
        will be returned
    :type wc: struct ib_wc \*

.. _`ib_poll_cq.description`:

Description
-----------

Poll a CQ for (possibly multiple) completions.  If the return value
is < 0, an error occurred.  If the return value is >= 0, it is the
number of completions returned.  If the return value is
non-negative and < num_entries, then the CQ was emptied.

.. _`ib_req_notify_cq`:

ib_req_notify_cq
================

.. c:function:: int ib_req_notify_cq(struct ib_cq *cq, enum ib_cq_notify_flags flags)

    Request completion notification on a CQ.

    :param cq:
        The CQ to generate an event for.
    :type cq: struct ib_cq \*

    :param flags:
        Must contain exactly one of \ ``IB_CQ_SOLICITED``\  or \ ``IB_CQ_NEXT_COMP``\ 
        to request an event on the next solicited event or next work
        completion at any type, respectively. \ ``IB_CQ_REPORT_MISSED_EVENTS``\ 
        may also be \|ed in to request a hint about missed events, as
        described below.
    :type flags: enum ib_cq_notify_flags

.. _`ib_req_notify_cq.return-value`:

Return Value
------------

< 0 means an error occurred while requesting notification
== 0 means notification was requested successfully, and if
IB_CQ_REPORT_MISSED_EVENTS was passed in, then no events
were missed and it is safe to wait for another event.  In
this case is it guaranteed that any work completions added
to the CQ since the last CQ poll will trigger a completion
notification event.
> 0 is only returned if IB_CQ_REPORT_MISSED_EVENTS was passed
in.  It means that the consumer must poll the CQ again to
make sure it is empty to avoid missing an event because of a
race between requesting notification and an entry being
added to the CQ.  This return value means it is possible
(but not guaranteed) that a work completion has been added
to the CQ since the last poll without triggering a
completion notification event.

.. _`ib_req_ncomp_notif`:

ib_req_ncomp_notif
==================

.. c:function:: int ib_req_ncomp_notif(struct ib_cq *cq, int wc_cnt)

    Request completion notification when there are at least the specified number of unreaped completions on the CQ.

    :param cq:
        The CQ to generate an event for.
    :type cq: struct ib_cq \*

    :param wc_cnt:
        The number of unreaped completions that should be on the
        CQ before an event is generated.
    :type wc_cnt: int

.. _`ib_dma_mapping_error`:

ib_dma_mapping_error
====================

.. c:function:: int ib_dma_mapping_error(struct ib_device *dev, u64 dma_addr)

    check a DMA addr for error

    :param dev:
        The device for which the dma_addr was created
    :type dev: struct ib_device \*

    :param dma_addr:
        The DMA address to check
    :type dma_addr: u64

.. _`ib_dma_map_single`:

ib_dma_map_single
=================

.. c:function:: u64 ib_dma_map_single(struct ib_device *dev, void *cpu_addr, size_t size, enum dma_data_direction direction)

    Map a kernel virtual address to DMA address

    :param dev:
        The device for which the dma_addr is to be created
    :type dev: struct ib_device \*

    :param cpu_addr:
        The kernel virtual address
    :type cpu_addr: void \*

    :param size:
        The size of the region in bytes
    :type size: size_t

    :param direction:
        The direction of the DMA
    :type direction: enum dma_data_direction

.. _`ib_dma_unmap_single`:

ib_dma_unmap_single
===================

.. c:function:: void ib_dma_unmap_single(struct ib_device *dev, u64 addr, size_t size, enum dma_data_direction direction)

    Destroy a mapping created by \ :c:func:`ib_dma_map_single`\ 

    :param dev:
        The device for which the DMA address was created
    :type dev: struct ib_device \*

    :param addr:
        The DMA address
    :type addr: u64

    :param size:
        The size of the region in bytes
    :type size: size_t

    :param direction:
        The direction of the DMA
    :type direction: enum dma_data_direction

.. _`ib_dma_map_page`:

ib_dma_map_page
===============

.. c:function:: u64 ib_dma_map_page(struct ib_device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction direction)

    Map a physical page to DMA address

    :param dev:
        The device for which the dma_addr is to be created
    :type dev: struct ib_device \*

    :param page:
        The page to be mapped
    :type page: struct page \*

    :param offset:
        The offset within the page
    :type offset: unsigned long

    :param size:
        The size of the region in bytes
    :type size: size_t

    :param direction:
        The direction of the DMA
    :type direction: enum dma_data_direction

.. _`ib_dma_unmap_page`:

ib_dma_unmap_page
=================

.. c:function:: void ib_dma_unmap_page(struct ib_device *dev, u64 addr, size_t size, enum dma_data_direction direction)

    Destroy a mapping created by \ :c:func:`ib_dma_map_page`\ 

    :param dev:
        The device for which the DMA address was created
    :type dev: struct ib_device \*

    :param addr:
        The DMA address
    :type addr: u64

    :param size:
        The size of the region in bytes
    :type size: size_t

    :param direction:
        The direction of the DMA
    :type direction: enum dma_data_direction

.. _`ib_dma_map_sg`:

ib_dma_map_sg
=============

.. c:function:: int ib_dma_map_sg(struct ib_device *dev, struct scatterlist *sg, int nents, enum dma_data_direction direction)

    Map a scatter/gather list to DMA addresses

    :param dev:
        The device for which the DMA addresses are to be created
    :type dev: struct ib_device \*

    :param sg:
        The array of scatter/gather entries
    :type sg: struct scatterlist \*

    :param nents:
        The number of scatter/gather entries
    :type nents: int

    :param direction:
        The direction of the DMA
    :type direction: enum dma_data_direction

.. _`ib_dma_unmap_sg`:

ib_dma_unmap_sg
===============

.. c:function:: void ib_dma_unmap_sg(struct ib_device *dev, struct scatterlist *sg, int nents, enum dma_data_direction direction)

    Unmap a scatter/gather list of DMA addresses

    :param dev:
        The device for which the DMA addresses were created
    :type dev: struct ib_device \*

    :param sg:
        The array of scatter/gather entries
    :type sg: struct scatterlist \*

    :param nents:
        The number of scatter/gather entries
    :type nents: int

    :param direction:
        The direction of the DMA
    :type direction: enum dma_data_direction

.. _`ib_sg_dma_address`:

ib_sg_dma_address
=================

.. c:function:: u64 ib_sg_dma_address(struct ib_device *dev, struct scatterlist *sg)

    Return the DMA address from a scatter/gather entry

    :param dev:
        The device for which the DMA addresses were created
    :type dev: struct ib_device \*

    :param sg:
        The scatter/gather entry
    :type sg: struct scatterlist \*

.. _`ib_sg_dma_address.note`:

Note
----

this function is obsolete. To do: change all occurrences of
\ :c:func:`ib_sg_dma_address`\  into \ :c:func:`sg_dma_address`\ .

.. _`ib_sg_dma_len`:

ib_sg_dma_len
=============

.. c:function:: unsigned int ib_sg_dma_len(struct ib_device *dev, struct scatterlist *sg)

    Return the DMA length from a scatter/gather entry

    :param dev:
        The device for which the DMA addresses were created
    :type dev: struct ib_device \*

    :param sg:
        The scatter/gather entry
    :type sg: struct scatterlist \*

.. _`ib_sg_dma_len.note`:

Note
----

this function is obsolete. To do: change all occurrences of
\ :c:func:`ib_sg_dma_len`\  into \ :c:func:`sg_dma_len`\ .

.. _`ib_dma_sync_single_for_cpu`:

ib_dma_sync_single_for_cpu
==========================

.. c:function:: void ib_dma_sync_single_for_cpu(struct ib_device *dev, u64 addr, size_t size, enum dma_data_direction dir)

    Prepare DMA region to be accessed by CPU

    :param dev:
        The device for which the DMA address was created
    :type dev: struct ib_device \*

    :param addr:
        The DMA address
    :type addr: u64

    :param size:
        The size of the region in bytes
    :type size: size_t

    :param dir:
        The direction of the DMA
    :type dir: enum dma_data_direction

.. _`ib_dma_sync_single_for_device`:

ib_dma_sync_single_for_device
=============================

.. c:function:: void ib_dma_sync_single_for_device(struct ib_device *dev, u64 addr, size_t size, enum dma_data_direction dir)

    Prepare DMA region to be accessed by device

    :param dev:
        The device for which the DMA address was created
    :type dev: struct ib_device \*

    :param addr:
        The DMA address
    :type addr: u64

    :param size:
        The size of the region in bytes
    :type size: size_t

    :param dir:
        The direction of the DMA
    :type dir: enum dma_data_direction

.. _`ib_dma_alloc_coherent`:

ib_dma_alloc_coherent
=====================

.. c:function:: void *ib_dma_alloc_coherent(struct ib_device *dev, size_t size, dma_addr_t *dma_handle, gfp_t flag)

    Allocate memory and map it for DMA

    :param dev:
        The device for which the DMA address is requested
    :type dev: struct ib_device \*

    :param size:
        The size of the region to allocate in bytes
    :type size: size_t

    :param dma_handle:
        A pointer for returning the DMA address of the region
    :type dma_handle: dma_addr_t \*

    :param flag:
        memory allocator flags
    :type flag: gfp_t

.. _`ib_dma_free_coherent`:

ib_dma_free_coherent
====================

.. c:function:: void ib_dma_free_coherent(struct ib_device *dev, size_t size, void *cpu_addr, dma_addr_t dma_handle)

    Free memory allocated by \ :c:func:`ib_dma_alloc_coherent`\ 

    :param dev:
        The device for which the DMA addresses were allocated
    :type dev: struct ib_device \*

    :param size:
        The size of the region
    :type size: size_t

    :param cpu_addr:
        the address returned by \ :c:func:`ib_dma_alloc_coherent`\ 
    :type cpu_addr: void \*

    :param dma_handle:
        the DMA address returned by \ :c:func:`ib_dma_alloc_coherent`\ 
    :type dma_handle: dma_addr_t

.. _`ib_dereg_mr`:

ib_dereg_mr
===========

.. c:function:: int ib_dereg_mr(struct ib_mr *mr)

    Deregisters a memory region and removes it from the HCA translation table.

    :param mr:
        The memory region to deregister.
    :type mr: struct ib_mr \*

.. _`ib_dereg_mr.description`:

Description
-----------

This function can fail, if the memory region has memory windows bound to it.

.. _`ib_update_fast_reg_key`:

ib_update_fast_reg_key
======================

.. c:function:: void ib_update_fast_reg_key(struct ib_mr *mr, u8 newkey)

    updates the key portion of the fast_reg MR R_Key and L_Key. \ ``mr``\  - struct ib_mr pointer to be updated. \ ``newkey``\  - new key to be used.

    :param mr:
        *undescribed*
    :type mr: struct ib_mr \*

    :param newkey:
        *undescribed*
    :type newkey: u8

.. _`ib_inc_rkey`:

ib_inc_rkey
===========

.. c:function:: u32 ib_inc_rkey(u32 rkey)

    increments the key portion of the given rkey. Can be used for calculating a new rkey for type 2 memory windows. \ ``rkey``\  - the rkey to increment.

    :param rkey:
        *undescribed*
    :type rkey: u32

.. _`ib_alloc_fmr`:

ib_alloc_fmr
============

.. c:function:: struct ib_fmr *ib_alloc_fmr(struct ib_pd *pd, int mr_access_flags, struct ib_fmr_attr *fmr_attr)

    Allocates a unmapped fast memory region.

    :param pd:
        The protection domain associated with the unmapped region.
    :type pd: struct ib_pd \*

    :param mr_access_flags:
        Specifies the memory access rights.
    :type mr_access_flags: int

    :param fmr_attr:
        Attributes of the unmapped region.
    :type fmr_attr: struct ib_fmr_attr \*

.. _`ib_alloc_fmr.description`:

Description
-----------

A fast memory region must be mapped before it can be used as part of
a work request.

.. _`ib_map_phys_fmr`:

ib_map_phys_fmr
===============

.. c:function:: int ib_map_phys_fmr(struct ib_fmr *fmr, u64 *page_list, int list_len, u64 iova)

    Maps a list of physical pages to a fast memory region.

    :param fmr:
        The fast memory region to associate with the pages.
    :type fmr: struct ib_fmr \*

    :param page_list:
        An array of physical pages to map to the fast memory region.
    :type page_list: u64 \*

    :param list_len:
        The number of pages in page_list.
    :type list_len: int

    :param iova:
        The I/O virtual address to use with the mapped region.
    :type iova: u64

.. _`ib_unmap_fmr`:

ib_unmap_fmr
============

.. c:function:: int ib_unmap_fmr(struct list_head *fmr_list)

    Removes the mapping from a list of fast memory regions.

    :param fmr_list:
        A linked list of fast memory regions to unmap.
    :type fmr_list: struct list_head \*

.. _`ib_dealloc_fmr`:

ib_dealloc_fmr
==============

.. c:function:: int ib_dealloc_fmr(struct ib_fmr *fmr)

    Deallocates a fast memory region.

    :param fmr:
        The fast memory region to deallocate.
    :type fmr: struct ib_fmr \*

.. _`ib_attach_mcast`:

ib_attach_mcast
===============

.. c:function:: int ib_attach_mcast(struct ib_qp *qp, union ib_gid *gid, u16 lid)

    Attaches the specified QP to a multicast group.

    :param qp:
        QP to attach to the multicast group.  The QP must be type
        IB_QPT_UD.
    :type qp: struct ib_qp \*

    :param gid:
        Multicast group GID.
    :type gid: union ib_gid \*

    :param lid:
        Multicast group LID in host byte order.
    :type lid: u16

.. _`ib_attach_mcast.description`:

Description
-----------

In order to send and receive multicast packets, subnet
administration must have created the multicast group and configured
the fabric appropriately.  The port associated with the specified
QP must also be a member of the multicast group.

.. _`ib_detach_mcast`:

ib_detach_mcast
===============

.. c:function:: int ib_detach_mcast(struct ib_qp *qp, union ib_gid *gid, u16 lid)

    Detaches the specified QP from a multicast group.

    :param qp:
        QP to detach from the multicast group.
    :type qp: struct ib_qp \*

    :param gid:
        Multicast group GID.
    :type gid: union ib_gid \*

    :param lid:
        Multicast group LID in host byte order.
    :type lid: u16

.. _`__ib_alloc_xrcd`:

\__ib_alloc_xrcd
================

.. c:function:: struct ib_xrcd *__ib_alloc_xrcd(struct ib_device *device, const char *caller)

    Allocates an XRC domain.

    :param device:
        The device on which to allocate the XRC domain.
    :type device: struct ib_device \*

    :param caller:
        Module name for kernel consumers
    :type caller: const char \*

.. _`ib_dealloc_xrcd`:

ib_dealloc_xrcd
===============

.. c:function:: int ib_dealloc_xrcd(struct ib_xrcd *xrcd)

    Deallocates an XRC domain.

    :param xrcd:
        The XRC domain to deallocate.
    :type xrcd: struct ib_xrcd \*

.. _`ib_check_mr_status`:

ib_check_mr_status
==================

.. c:function:: int ib_check_mr_status(struct ib_mr *mr, u32 check_mask, struct ib_mr_status *mr_status)

    lightweight check of MR status. This routine may provide status checks on a selected ib_mr. first use is for signature status check.

    :param mr:
        A memory region.
    :type mr: struct ib_mr \*

    :param check_mask:
        Bitmask of which checks to perform from
        ib_mr_status_check enumeration.
    :type check_mask: u32

    :param mr_status:
        The container of relevant status checks.
        failed checks will be indicated in the status bitmask
        and the relevant info shall be in the error item.
    :type mr_status: struct ib_mr_status \*

.. _`rdma_ah_find_type`:

rdma_ah_find_type
=================

.. c:function:: enum rdma_ah_attr_type rdma_ah_find_type(struct ib_device *dev, u8 port_num)

    Return address handle type.

    :param dev:
        Device to be checked
    :type dev: struct ib_device \*

    :param port_num:
        Port number
    :type port_num: u8

.. _`ib_lid_cpu16`:

ib_lid_cpu16
============

.. c:function:: u16 ib_lid_cpu16(u32 lid)

    Return lid in 16bit CPU encoding. In the current implementation the only way to get get the 32bit lid is from other sources for OPA. For IB, lids will always be 16bits so cast the value accordingly.

    :param lid:
        A 32bit LID
    :type lid: u32

.. _`ib_lid_be16`:

ib_lid_be16
===========

.. c:function:: __be16 ib_lid_be16(u32 lid)

    Return lid in 16bit BE encoding.

    :param lid:
        A 32bit LID
    :type lid: u32

.. _`ib_get_vector_affinity`:

ib_get_vector_affinity
======================

.. c:function:: const struct cpumask *ib_get_vector_affinity(struct ib_device *device, int comp_vector)

    Get the affinity mappings of a given completion vector

    :param device:
        the rdma device
    :type device: struct ib_device \*

    :param comp_vector:
        index of completion vector
    :type comp_vector: int

.. _`ib_get_vector_affinity.description`:

Description
-----------

Returns NULL on failure, otherwise a corresponding cpu map of the
completion vector (returns all-cpus map if the device driver doesn't
implement get_vector_affinity).

.. _`rdma_roce_rescan_device`:

rdma_roce_rescan_device
=======================

.. c:function:: void rdma_roce_rescan_device(struct ib_device *ibdev)

    Rescan all of the network devices in the system and add their gids, as needed, to the relevant RoCE devices.

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

.. _`rdma_set_device_sysfs_group`:

rdma_set_device_sysfs_group
===========================

.. c:function:: void rdma_set_device_sysfs_group(struct ib_device *dev, const struct attribute_group *group)

    Set device attributes group to have driver specific sysfs entries at for infiniband class.

    :param dev:
        *undescribed*
    :type dev: struct ib_device \*

    :param group:
        Pointer to group which should be added when device
        is registered with sysfs.
        \ :c:func:`rdma_set_device_sysfs_group`\  allows existing drivers to expose one
        group per device to have sysfs attributes.
    :type group: const struct attribute_group \*

.. _`rdma_set_device_sysfs_group.note`:

NOTE
----

New drivers should not make use of this API; instead new device
parameter should be exposed via netlink command. This API and mechanism
exist only for existing drivers.

.. This file was automatic generated / don't edit.


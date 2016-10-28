.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/uwb.h

.. _`uwb_dev`:

struct uwb_dev
==============

.. c:type:: struct uwb_dev

    a UWB Device

.. _`uwb_dev.definition`:

Definition
----------

.. code-block:: c

    struct uwb_dev {
        struct mutex mutex;
        struct list_head list_node;
        struct device dev;
        struct uwb_rc *rc;
        struct uwb_beca_e *bce;
        struct uwb_mac_addr mac_addr;
        struct uwb_dev_addr dev_addr;
        int beacon_slot;
        unsigned long streams[BITS_TO_LONGS(UWB_NUM_STREAMS)];
        unsigned long last_availability_bm[BITS_TO_LONGS(UWB_NUM_MAS)];
    }

.. _`uwb_dev.members`:

Members
-------

mutex
    *undescribed*

list_node
    *undescribed*

dev
    *undescribed*

rc
    UWB Radio Controller that discovered the device (kind of its
    parent).

bce
    a beacon cache entry for this device; or NULL if the device
    is a local radio controller.

mac_addr
    the EUI-48 address of this device.

dev_addr
    the current DevAddr used by this device.

beacon_slot
    the slot number the beacon is using.

streams
    bitmap of streams allocated to reservations targeted at
    this device.  For an RC, this is the streams allocated for
    reservations targeted at DevAddrs.

.. _`uwb_dev.description`:

Description
-----------

A UWB device may either by a neighbor or part of a local radio
controller.

.. _`uwb_mas_bm`:

struct uwb_mas_bm
=================

.. c:type:: struct uwb_mas_bm

    a bitmap of all MAS in a superframe

.. _`uwb_mas_bm.definition`:

Definition
----------

.. code-block:: c

    struct uwb_mas_bm {
        unsigned long bm[BITS_TO_LONGS(UWB_NUM_MAS)];
        unsigned long unsafe_bm[BITS_TO_LONGS(UWB_NUM_MAS)];
        int safe;
        int unsafe;
    }

.. _`uwb_mas_bm.members`:

Members
-------

bm
    a bitmap of length #UWB_NUM_MAS

safe
    *undescribed*

unsafe
    *undescribed*

.. _`uwb_rsv_target`:

struct uwb_rsv_target
=====================

.. c:type:: struct uwb_rsv_target

    the target of a reservation.

.. _`uwb_rsv_target.definition`:

Definition
----------

.. code-block:: c

    struct uwb_rsv_target {
        enum uwb_rsv_target_type type;
        union {unnamed_union};
    }

.. _`uwb_rsv_target.members`:

Members
-------

type
    *undescribed*

{unnamed_union}
    anonymous


.. _`uwb_rsv_target.description`:

Description
-----------

Reservations unicast and targeted at a single device
(UWB_RSV_TARGET_DEV); or (e.g., in the case of WUSB) targeted at a
specific (private) DevAddr (UWB_RSV_TARGET_DEVADDR).

.. _`uwb_rsv`:

struct uwb_rsv
==============

.. c:type:: struct uwb_rsv

    a DRP reservation

.. _`uwb_rsv.definition`:

Definition
----------

.. code-block:: c

    struct uwb_rsv {
        struct uwb_rc *rc;
        struct list_head rc_node;
        struct list_head pal_node;
        struct kref kref;
        struct uwb_dev *owner;
        struct uwb_rsv_target target;
        enum uwb_drp_type type;
        int max_mas;
        int min_mas;
        int max_interval;
        bool is_multicast;
        uwb_rsv_cb_f callback;
        void *pal_priv;
        enum uwb_rsv_state state;
        bool needs_release_companion_mas;
        u8 stream;
        u8 tiebreaker;
        struct uwb_mas_bm mas;
        struct uwb_ie_drp *drp_ie;
        struct uwb_rsv_move mv;
        bool ie_valid;
        struct timer_list timer;
        struct work_struct handle_timeout_work;
    }

.. _`uwb_rsv.members`:

Members
-------

rc
    the radio controller this reservation is for
    (as target or owner)

rc_node
    a list node for the RC

pal_node
    a list node for the PAL

kref
    *undescribed*

owner
    the UWB device owning this reservation

target
    the target UWB device

type
    reservation type

max_mas
    maxiumum number of MAS

min_mas
    minimum number of MAS

max_interval
    *undescribed*

is_multicast
    true iff multicast

callback
    callback function when the reservation completes

pal_priv
    private data for the PAL making the reservation

state
    *undescribed*

needs_release_companion_mas
    *undescribed*

stream
    stream index allocated for this reservation

tiebreaker
    conflict tiebreaker for this reservation

mas
    reserved MAS

drp_ie
    the DRP IE

mv
    *undescribed*

ie_valid
    true iff the DRP IE matches the reservation parameters

timer
    *undescribed*

handle_timeout_work
    *undescribed*

.. _`uwb_rsv.description`:

Description
-----------

DRP reservations are uniquely identified by the owner, target and
stream index.  However, when using a DevAddr as a target (e.g., for
a WUSB cluster reservation) the responses may be received from
devices with different DevAddrs.  In this case, reservations are
uniquely identified by just the stream index.  A number of stream
indexes (UWB_NUM_GLOBAL_STREAMS) are reserved for this.

.. _`uwb_drp_avail`:

struct uwb_drp_avail
====================

.. c:type:: struct uwb_drp_avail

    a radio controller's view of MAS usage

.. _`uwb_drp_avail.definition`:

Definition
----------

.. code-block:: c

    struct uwb_drp_avail {
        unsigned long global[BITS_TO_LONGS(UWB_NUM_MAS)];
        unsigned long local[BITS_TO_LONGS(UWB_NUM_MAS)];
        unsigned long pending[BITS_TO_LONGS(UWB_NUM_MAS)];
        struct uwb_ie_drp_avail ie;
        bool ie_valid;
    }

.. _`uwb_drp_avail.members`:

Members
-------

global
    MAS unused by neighbors (excluding reservations targeted
    or owned by the local radio controller) or the beaon period

local
    MAS unused by local established reservations

pending
    MAS unused by local pending reservations

ie
    DRP Availability IE to be included in the beacon

ie_valid
    true iff \ ``ie``\  is valid and does not need to regenerated from
    \ ``global``\  and \ ``local``\ 

.. _`uwb_drp_avail.description`:

Description
-----------

Each radio controller maintains a view of MAS usage or
availability. MAS available for a new reservation are determined
from the intersection of \ ``global``\ , \ ``local``\ , and \ ``pending``\ .

The radio controller must transmit a DRP Availability IE that's the
intersection of \ ``global``\  and \ ``local``\ .

A set bit indicates the MAS is unused and available.

rc->rsvs_mutex should be held before accessing this data structure.

[ECMA-368] section 17.4.3.

.. _`uwb_pal`:

struct uwb_pal
==============

.. c:type:: struct uwb_pal

    a UWB PAL

.. _`uwb_pal.definition`:

Definition
----------

.. code-block:: c

    struct uwb_pal {
        struct list_head node;
        const char *name;
        struct device *device;
        struct uwb_rc *rc;
        void (*channel_changed)(struct uwb_pal *pal, int channel);
        void (*new_rsv)(struct uwb_pal *pal, struct uwb_rsv *rsv);
        int channel;
        struct dentry *debugfs_dir;
    }

.. _`uwb_pal.members`:

Members
-------

node
    *undescribed*

name
    descriptive name for this PAL (wusbhc, wlp, etc.).

device
    a device for the PAL.  Used to link the PAL and the radio
    controller in sysfs.

rc
    the radio controller the PAL uses.

channel_changed
    called when the channel used by the radio changes.
    A channel of -1 means the channel has been stopped.

new_rsv
    called when a peer requests a reservation (may be NULL if
    the PAL cannot accept reservation requests).

channel
    channel being used by the PAL; 0 if the PAL isn't using
    the radio; -1 if the PAL wishes to use the radio but
    cannot.

debugfs_dir
    a debugfs directory which the PAL can use for its own
    debugfs files.

.. _`uwb_pal.description`:

Description
-----------

A Protocol Adaptation Layer (PAL) is a user of the WiMedia UWB
radio platform (e.g., WUSB, WLP or Bluetooth UWB AMP).

The PALs using a radio controller must register themselves to
permit the UWB stack to coordinate usage of the radio between the
various PALs or to allow PALs to response to certain requests from
peers.

A struct uwb_pal should be embedded in a containing structure
belonging to the PAL and initialized with \ :c:func:`uwb_pal_init`\ ).  Fields
should be set appropriately by the PAL before registering the PAL
with \ :c:func:`uwb_pal_register`\ .

.. _`uwb_dev_for_each_f`:

uwb_dev_for_each_f
==================

.. c:function:: int uwb_dev_for_each_f(struct device *dev, void *priv)

    :param struct device \*dev:
        Linux device instance
        'uwb_dev = container_of(dev, struct uwb_dev, dev)'

    :param void \*priv:
        Data passed by the caller to 'uwb_{dev,rc}\ :c:func:`_foreach`\ '.

.. _`uwb_rsv_is_owner`:

uwb_rsv_is_owner
================

.. c:function:: bool uwb_rsv_is_owner(struct uwb_rsv *rsv)

    is the owner of this reservation the RC?

    :param struct uwb_rsv \*rsv:
        the reservation

.. _`uwb_notifs`:

enum uwb_notifs
===============

.. c:type:: enum uwb_notifs

    UWB events that can be passed to any listeners

.. _`uwb_notifs.definition`:

Definition
----------

.. code-block:: c

    enum uwb_notifs {
        UWB_NOTIF_ONAIR,
        UWB_NOTIF_OFFAIR
    };

.. _`uwb_notifs.constants`:

Constants
---------

UWB_NOTIF_ONAIR
    a new neighbour has joined the beacon group.

UWB_NOTIF_OFFAIR
    a neighbour has left the beacon group.

.. _`uwb_notifs.description`:

Description
-----------

Higher layers can register callback functions with the radio
controller using \ :c:func:`uwb_notifs_register`\ . The radio controller
maintains a list of all registered handlers and will notify all
nodes when an event occurs.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/bus.h

.. _`brcmf_bus_ops`:

struct brcmf_bus_ops
====================

.. c:type:: struct brcmf_bus_ops

    bus callback operations.

.. _`brcmf_bus_ops.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_bus_ops {
        int (*preinit)(struct device *dev);
        void (*stop)(struct device *dev);
        int (*txdata)(struct device *dev, struct sk_buff *skb);
        int (*txctl)(struct device *dev, unsigned char *msg, uint len);
        int (*rxctl)(struct device *dev, unsigned char *msg, uint len);
        struct pktq * (*gettxq)(struct device *dev);
        void (*wowl_config)(struct device *dev, bool enabled);
        size_t (*get_ramsize)(struct device *dev);
        int (*get_memdump)(struct device *dev, void *data, size_t len);
    }

.. _`brcmf_bus_ops.members`:

Members
-------

preinit
    execute bus/device specific dongle init commands (optional).

stop
    clear pending frames, disable data flow.

txdata
    send a data frame to the dongle. When the data
    has been transferred, the common driver must be
    notified using \ :c:func:`brcmf_txcomplete`\ . The common
    driver calls this function with interrupts
    disabled.

txctl
    transmit a control request message to dongle.

rxctl
    receive a control response message from dongle.

gettxq
    obtain a reference of bus transmit queue (optional).

wowl_config
    specify if dongle is configured for wowl when going to suspend

get_ramsize
    obtain size of device memory.

get_memdump
    obtain device memory dump in provided buffer.

.. _`brcmf_bus_ops.description`:

Description
-----------

This structure provides an abstract interface towards the
bus specific driver. For control messages to common driver
will assure there is only one active transaction. Unless
indicated otherwise these callbacks are mandatory.

.. _`brcmf_bus_msgbuf`:

struct brcmf_bus_msgbuf
=======================

.. c:type:: struct brcmf_bus_msgbuf

    bus ringbuf if in case of msgbuf.

.. _`brcmf_bus_msgbuf.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_bus_msgbuf {
        struct brcmf_commonring  *commonrings;
        struct brcmf_commonring **flowrings;
        u32 rx_dataoffset;
        u32 max_rxbufpost;
        u16 max_flowrings;
        u16 max_submissionrings;
        u16 max_completionrings;
    }

.. _`brcmf_bus_msgbuf.members`:

Members
-------

commonrings
    commonrings which are always there.

flowrings
    commonrings which are dynamically created and destroyed for data.

rx_dataoffset
    if set then all rx data has this this offset.

max_rxbufpost
    maximum number of buffers to post for rx.

max_flowrings
    maximum number of tx flow rings supported.

max_submissionrings
    maximum number of submission rings(h2d) supported.

max_completionrings
    maximum number of completion rings(d2h) supported.

.. _`brcmf_bus`:

struct brcmf_bus
================

.. c:type:: struct brcmf_bus

    interface structure between common and bus layer

.. _`brcmf_bus.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_bus {
        union bus_priv;
        enum brcmf_bus_protocol_type proto_type;
        struct device *dev;
        struct brcmf_pub *drvr;
        enum brcmf_bus_state state;
        uint maxctl;
        unsigned long tx_realloc;
        u32 chip;
        u32 chiprev;
        bool always_use_fws_queue;
        bool wowl_supported;
        const struct brcmf_bus_ops *ops;
        struct brcmf_bus_msgbuf *msgbuf;
    }

.. _`brcmf_bus.members`:

Members
-------

bus_priv
    pointer to private bus device.

proto_type
    protocol type, bcdc or msgbuf

dev
    device pointer of bus device.

drvr
    public driver information.

state
    operational state of the bus interface.

maxctl
    maximum size for rxctl request message.

tx_realloc
    number of tx packets realloced for headroom.

chip
    device identifier of the dongle chip.

chiprev
    revision of the dongle chip.

always_use_fws_queue
    *undescribed*

wowl_supported
    is wowl supported by bus driver.

ops
    *undescribed*

msgbuf
    *undescribed*

.. This file was automatic generated / don't edit.


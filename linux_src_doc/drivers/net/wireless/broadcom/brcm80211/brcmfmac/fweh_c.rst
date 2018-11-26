.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/fweh.c

.. _`brcmf_fweh_queue_item`:

struct brcmf_fweh_queue_item
============================

.. c:type:: struct brcmf_fweh_queue_item

    event item on event queue.

.. _`brcmf_fweh_queue_item.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fweh_queue_item {
        struct list_head q;
        enum brcmf_fweh_event_code code;
        u8 ifidx;
        u8 ifaddr[ETH_ALEN];
        struct brcmf_event_msg_be emsg;
        u32 datalen;
        u8 data[0];
    }

.. _`brcmf_fweh_queue_item.members`:

Members
-------

q
    list element for queuing.

code
    event code.

ifidx
    interface index related to this event.

ifaddr
    ethernet address for interface.

emsg
    common parameters of the firmware event message.

datalen
    *undescribed*

data
    event specific data part of the firmware event.

.. _`brcmf_fweh_event_name`:

struct brcmf_fweh_event_name
============================

.. c:type:: struct brcmf_fweh_event_name

    code, name mapping entry.

.. _`brcmf_fweh_event_name.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fweh_event_name {
        enum brcmf_fweh_event_code code;
        const char *name;
    }

.. _`brcmf_fweh_event_name.members`:

Members
-------

code
    *undescribed*

name
    *undescribed*

.. _`brcmf_fweh_event_name`:

brcmf_fweh_event_name
=====================

.. c:function:: const char *brcmf_fweh_event_name(enum brcmf_fweh_event_code code)

    returns name for given event code.

    :param code:
        code to lookup.
    :type code: enum brcmf_fweh_event_code

.. _`brcmf_fweh_queue_event`:

brcmf_fweh_queue_event
======================

.. c:function:: void brcmf_fweh_queue_event(struct brcmf_fweh_info *fweh, struct brcmf_fweh_queue_item *event)

    create and queue event.

    :param fweh:
        firmware event handling info.
    :type fweh: struct brcmf_fweh_info \*

    :param event:
        event queue entry.
    :type event: struct brcmf_fweh_queue_item \*

.. _`brcmf_fweh_handle_if_event`:

brcmf_fweh_handle_if_event
==========================

.. c:function:: void brcmf_fweh_handle_if_event(struct brcmf_pub *drvr, struct brcmf_event_msg *emsg, void *data)

    handle IF event.

    :param drvr:
        driver information object.
    :type drvr: struct brcmf_pub \*

    :param emsg:
        *undescribed*
    :type emsg: struct brcmf_event_msg \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`brcmf_fweh_dequeue_event`:

brcmf_fweh_dequeue_event
========================

.. c:function:: struct brcmf_fweh_queue_item *brcmf_fweh_dequeue_event(struct brcmf_fweh_info *fweh)

    get event from the queue.

    :param fweh:
        firmware event handling info.
    :type fweh: struct brcmf_fweh_info \*

.. _`brcmf_fweh_event_worker`:

brcmf_fweh_event_worker
=======================

.. c:function:: void brcmf_fweh_event_worker(struct work_struct *work)

    firmware event worker.

    :param work:
        worker object.
    :type work: struct work_struct \*

.. _`brcmf_fweh_p2pdev_setup`:

brcmf_fweh_p2pdev_setup
=======================

.. c:function:: void brcmf_fweh_p2pdev_setup(struct brcmf_if *ifp, bool ongoing)

    P2P device setup ongoing (or not).

    :param ifp:
        ifp on which setup is taking place or finished.
    :type ifp: struct brcmf_if \*

    :param ongoing:
        p2p device setup in progress (or not).
    :type ongoing: bool

.. _`brcmf_fweh_attach`:

brcmf_fweh_attach
=================

.. c:function:: void brcmf_fweh_attach(struct brcmf_pub *drvr)

    initialize firmware event handling.

    :param drvr:
        driver information object.
    :type drvr: struct brcmf_pub \*

.. _`brcmf_fweh_detach`:

brcmf_fweh_detach
=================

.. c:function:: void brcmf_fweh_detach(struct brcmf_pub *drvr)

    cleanup firmware event handling.

    :param drvr:
        driver information object.
    :type drvr: struct brcmf_pub \*

.. _`brcmf_fweh_register`:

brcmf_fweh_register
===================

.. c:function:: int brcmf_fweh_register(struct brcmf_pub *drvr, enum brcmf_fweh_event_code code, brcmf_fweh_handler_t handler)

    register handler for given event code.

    :param drvr:
        driver information object.
    :type drvr: struct brcmf_pub \*

    :param code:
        event code.
    :type code: enum brcmf_fweh_event_code

    :param handler:
        handler for the given event code.
    :type handler: brcmf_fweh_handler_t

.. _`brcmf_fweh_unregister`:

brcmf_fweh_unregister
=====================

.. c:function:: void brcmf_fweh_unregister(struct brcmf_pub *drvr, enum brcmf_fweh_event_code code)

    remove handler for given code.

    :param drvr:
        driver information object.
    :type drvr: struct brcmf_pub \*

    :param code:
        event code.
    :type code: enum brcmf_fweh_event_code

.. _`brcmf_fweh_activate_events`:

brcmf_fweh_activate_events
==========================

.. c:function:: int brcmf_fweh_activate_events(struct brcmf_if *ifp)

    enables firmware events registered.

    :param ifp:
        primary interface object.
    :type ifp: struct brcmf_if \*

.. _`brcmf_fweh_process_event`:

brcmf_fweh_process_event
========================

.. c:function:: void brcmf_fweh_process_event(struct brcmf_pub *drvr, struct brcmf_event *event_packet, u32 packet_len)

    process skb as firmware event.

    :param drvr:
        driver information object.
    :type drvr: struct brcmf_pub \*

    :param event_packet:
        event packet to process.
    :type event_packet: struct brcmf_event \*

    :param packet_len:
        *undescribed*
    :type packet_len: u32

.. _`brcmf_fweh_process_event.description`:

Description
-----------

If the packet buffer contains a firmware event message it will
dispatch the event to a registered handler (using worker).

.. This file was automatic generated / don't edit.


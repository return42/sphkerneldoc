.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/caif/caif_layer.h

.. _`caif_assert`:

caif_assert
===========

.. c:function::  caif_assert( assert)

    Assert function for CAIF.

    :param  assert:
        expression to evaluate.

.. _`caif_assert.description`:

Description
-----------

This function will print a error message and a do WARN_ON if the
assertion failes. Normally this will do a stack up at the current location.

.. _`caif_ctrlcmd`:

enum caif_ctrlcmd
=================

.. c:type:: enum caif_ctrlcmd

    CAIF Stack Control Signaling sent in layer.ctrlcmd().

.. _`caif_ctrlcmd.definition`:

Definition
----------

.. code-block:: c

    enum caif_ctrlcmd {
        CAIF_CTRLCMD_FLOW_OFF_IND,
        CAIF_CTRLCMD_FLOW_ON_IND,
        CAIF_CTRLCMD_REMOTE_SHUTDOWN_IND,
        CAIF_CTRLCMD_INIT_RSP,
        CAIF_CTRLCMD_DEINIT_RSP,
        CAIF_CTRLCMD_INIT_FAIL_RSP,
        _CAIF_CTRLCMD_PHYIF_FLOW_OFF_IND,
        _CAIF_CTRLCMD_PHYIF_FLOW_ON_IND,
        _CAIF_CTRLCMD_PHYIF_DOWN_IND
    };

.. _`caif_ctrlcmd.constants`:

Constants
---------

CAIF_CTRLCMD_FLOW_OFF_IND
    Flow Control is OFF, transmit function
    should stop sending data

CAIF_CTRLCMD_FLOW_ON_IND
    Flow Control is ON, transmit function
    can start sending data

CAIF_CTRLCMD_REMOTE_SHUTDOWN_IND
    Remote end modem has decided to close
    down channel

CAIF_CTRLCMD_INIT_RSP
    Called initially when the layer below
    has finished initialization

CAIF_CTRLCMD_DEINIT_RSP
    Called when de-initialization is
    complete

CAIF_CTRLCMD_INIT_FAIL_RSP
    Called if initialization fails

_CAIF_CTRLCMD_PHYIF_FLOW_OFF_IND
    CAIF Link layer temporarily cannot
    send more packets.

_CAIF_CTRLCMD_PHYIF_FLOW_ON_IND
    Called if CAIF Link layer is able
    to send packets again.

_CAIF_CTRLCMD_PHYIF_DOWN_IND
    Called if CAIF Link layer is going
    down.

.. _`caif_ctrlcmd.description`:

Description
-----------

These commands are sent upwards in the CAIF stack to the CAIF Client.
They are used for signaling originating from the modem or CAIF Link Layer.
These are either responses (\*\_RSP) or events (\*\_IND).

.. _`caif_modemcmd`:

enum caif_modemcmd
==================

.. c:type:: enum caif_modemcmd

    Modem Control Signaling, sent from CAIF Client to the CAIF Link Layer or modem.

.. _`caif_modemcmd.definition`:

Definition
----------

.. code-block:: c

    enum caif_modemcmd {
        CAIF_MODEMCMD_FLOW_ON_REQ,
        CAIF_MODEMCMD_FLOW_OFF_REQ,
        _CAIF_MODEMCMD_PHYIF_USEFULL,
        _CAIF_MODEMCMD_PHYIF_USELESS
    };

.. _`caif_modemcmd.constants`:

Constants
---------

CAIF_MODEMCMD_FLOW_ON_REQ
    Flow Control is ON, transmit function
    can start sending data.

CAIF_MODEMCMD_FLOW_OFF_REQ
    Flow Control is OFF, transmit function
    should stop sending data.

_CAIF_MODEMCMD_PHYIF_USEFULL
    Notify physical layer that it is in use

_CAIF_MODEMCMD_PHYIF_USELESS
    Notify physical layer that it is
    no longer in use.

.. _`caif_modemcmd.description`:

Description
-----------

These are requests sent 'downwards' in the stack.
Flow ON, OFF can be indicated to the modem.

.. _`caif_direction`:

enum caif_direction
===================

.. c:type:: enum caif_direction

    CAIF Packet Direction. Indicate if a packet is to be sent out or to be received in.

.. _`caif_direction.definition`:

Definition
----------

.. code-block:: c

    enum caif_direction {
        CAIF_DIR_IN,
        CAIF_DIR_OUT
    };

.. _`caif_direction.constants`:

Constants
---------

CAIF_DIR_IN
    Incoming packet received.

CAIF_DIR_OUT
    Outgoing packet to be transmitted.

.. _`cflayer`:

struct cflayer
==============

.. c:type:: struct cflayer

    CAIF Stack layer. Defines the framework for the CAIF Core Stack.

.. _`cflayer.definition`:

Definition
----------

.. code-block:: c

    struct cflayer {
        struct cflayer *up;
        struct cflayer *dn;
        struct list_head node;
        int (*receive)(struct cflayer *layr, struct cfpkt *cfpkt);
        int (*transmit)(struct cflayer *layr, struct cfpkt *cfpkt);
        void (*ctrlcmd)(struct cflayer *layr, enum caif_ctrlcmd ctrl,int phyid);
        int (*modemcmd)(struct cflayer *layr, enum caif_modemcmd ctrl);
        unsigned int id;
        char name;
    }

.. _`cflayer.members`:

Members
-------

up
    Pointer up to the layer above.

dn
    Pointer down to the layer below.

node
    List node used when layer participate in a list.

receive
    Packet receive function.

transmit
    Packet transmit funciton.

ctrlcmd
    Used for control signalling upwards in the stack.

modemcmd
    Used for control signaling downwards in the stack.

id
    The identity of this layer

name
    Name of the layer.

.. _`cflayer.description`:

Description
-----------

This structure defines the layered structure in CAIF.

It defines CAIF layering structure, used by all CAIF Layers and the
layers interfacing CAIF.

In order to integrate with CAIF an adaptation layer on top of the CAIF stack
and PHY layer below the CAIF stack
must be implemented. These layer must follow the design principles below.

.. _`cflayer.principles-for-layering-of-protocol-layers`:

Principles for layering of protocol layers
------------------------------------------

- All layers must use this structure. If embedding it, then place this
structure first in the layer specific structure.

- Each layer should not depend on any others layer's private data.

- In order to send data upwards do
layer->up->receive(layer->up, packet);

- In order to send data downwards do
layer->dn->transmit(layer->dn, info, packet);

.. _`layer_set_up`:

layer_set_up
============

.. c:function::  layer_set_up( layr,  above)

    Set the up pointer for a specified layer.

    :param  layr:
        Layer where up pointer shall be set.

    :param  above:
        Layer above.

.. _`layer_set_dn`:

layer_set_dn
============

.. c:function::  layer_set_dn( layr,  below)

    Set the down pointer for a specified layer.

    :param  layr:
        Layer where down pointer shall be set.

    :param  below:
        Layer below.

.. _`dev_info`:

struct dev_info
===============

.. c:type:: struct dev_info

    Physical Device info information about physical layer.

.. _`dev_info.definition`:

Definition
----------

.. code-block:: c

    struct dev_info {
        void *dev;
        unsigned int id;
    }

.. _`dev_info.members`:

Members
-------

dev
    Pointer to native physical device.

id
    Physical ID of the physical connection used by the
    logical CAIF connection. Used by service layers to
    identify their physical id to Caif MUX (CFMUXL)so
    that the MUX can add the correct physical ID to the
    packet.

.. _`caif_payload_info`:

struct caif_payload_info
========================

.. c:type:: struct caif_payload_info

    Payload information embedded in packet (sk_buff).

.. _`caif_payload_info.definition`:

Definition
----------

.. code-block:: c

    struct caif_payload_info {
        struct dev_info *dev_info;
        unsigned short hdr_len;
        unsigned short channel_id;
    }

.. _`caif_payload_info.members`:

Members
-------

dev_info
    Information about the receiving device.

hdr_len
    Header length, used to align pay load on 32bit boundary.

channel_id
    Channel ID of the logical CAIF connection.
    Used by mux to insert channel id into the caif packet.

.. This file was automatic generated / don't edit.


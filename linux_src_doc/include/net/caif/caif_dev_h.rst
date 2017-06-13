.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/caif/caif_dev.h

.. _`caif_param`:

struct caif_param
=================

.. c:type:: struct caif_param

    CAIF parameters.

.. _`caif_param.definition`:

Definition
----------

.. code-block:: c

    struct caif_param {
        u16 size;
        u8 data;
    }

.. _`caif_param.members`:

Members
-------

size
    Length of data

data
    Binary Data Blob

.. _`caif_connect_request`:

struct caif_connect_request
===========================

.. c:type:: struct caif_connect_request

    Request data for CAIF channel setup.

.. _`caif_connect_request.definition`:

Definition
----------

.. code-block:: c

    struct caif_connect_request {
        enum caif_protocol_type protocol;
        struct sockaddr_caif sockaddr;
        enum caif_channel_priority priority;
        enum caif_link_selector link_selector;
        int ifindex;
        struct caif_param param;
    }

.. _`caif_connect_request.members`:

Members
-------

protocol
    Type of CAIF protocol to use (at, datagram etc)

sockaddr
    Socket address to connect.

priority
    Priority of the connection.

link_selector
    Link selector (high bandwidth or low latency)

ifindex
    kernel index of the interface.

param
    Connect Request parameters (CAIF_SO_REQ_PARAM).

.. _`caif_connect_request.description`:

Description
-----------

This struct is used when connecting a CAIF channel.
It contains all CAIF channel configuration options.

.. _`caif_connect_client`:

caif_connect_client
===================

.. c:function:: int caif_connect_client(struct net *net, struct caif_connect_request *conn_req, struct cflayer *client_layer, int *ifindex, int *headroom, int *tailroom)

    Connect a client to CAIF Core Stack.

    :param struct net \*net:
        *undescribed*

    :param struct caif_connect_request \*conn_req:
        *undescribed*

    :param struct cflayer \*client_layer:
        User implementation of client layer. This layer
        MUST have receive and control callback functions
        implemented.

    :param int \*ifindex:
        Link layer interface index used for this connection.

    :param int \*headroom:
        Head room needed by CAIF protocol.

    :param int \*tailroom:
        Tail room needed by CAIF protocol.

.. _`caif_connect_client.description`:

Description
-----------

This function connects a CAIF channel. The Client must implement
the struct cflayer. This layer represents the Client layer and holds
receive functions and control callback functions. Control callback
function will receive information about connect/disconnect responses,
flow control etc (see enum caif_control).
E.g. CAIF Socket will call this function for each socket it connects
and have one client_layer instance for each socket.

.. _`caif_disconnect_client`:

caif_disconnect_client
======================

.. c:function:: int caif_disconnect_client(struct net *net, struct cflayer *client_layer)

    Disconnects a client from the CAIF stack.

    :param struct net \*net:
        *undescribed*

    :param struct cflayer \*client_layer:
        Client layer to be disconnected.

.. _`caif_client_register_refcnt`:

caif_client_register_refcnt
===========================

.. c:function:: void caif_client_register_refcnt(struct cflayer *adapt_layer, void (*hold)(struct cflayer *lyr), void (*put)(struct cflayer *lyr))

    register ref-count functions provided by client.

    :param struct cflayer \*adapt_layer:
        Client layer using CAIF Stack.

    :param void (\*hold)(struct cflayer \*lyr):
        Function provided by client layer increasing ref-count

    :param void (\*put)(struct cflayer \*lyr):
        Function provided by client layer decreasing ref-count

.. _`caif_client_register_refcnt.description`:

Description
-----------

Client of the CAIF Stack must register functions for reference counting.
These functions are called by the CAIF Stack for every upstream packet,
and must therefore be implemented efficiently.

Client should call caif_free_client when reference count degrease to zero.

.. _`caif_free_client`:

caif_free_client
================

.. c:function:: void caif_free_client(struct cflayer *adap_layer)

    Free memory used to manage the client in the CAIF Stack.

    :param struct cflayer \*adap_layer:
        *undescribed*

.. _`caif_free_client.description`:

Description
-----------

This function must be called from client layer in order to free memory.
Caller must guarantee that no packets are in flight upstream when calling
this function.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_net.h

.. _`dvb_net`:

struct dvb_net
==============

.. c:type:: struct dvb_net

    describes a DVB network interface

.. _`dvb_net.definition`:

Definition
----------

.. code-block:: c

    struct dvb_net {
        struct dvb_device *dvbdev;
        struct net_device *device[DVB_NET_DEVICES_MAX];
        int state[DVB_NET_DEVICES_MAX];
        unsigned int exit:1;
        struct dmx_demux *demux;
        struct mutex ioctl_mutex;
    }

.. _`dvb_net.members`:

Members
-------

dvbdev
    pointer to \ :c:type:`struct dvb_device <dvb_device>`\ .

device
    array of pointers to \ :c:type:`struct net_device <net_device>`\ .

state
    array of integers to each net device. A value
    different than zero means that the interface is
    in usage.

exit
    flag to indicate when the device is being removed.

demux
    pointer to \ :c:type:`struct dmx_demux <dmx_demux>`\ .

ioctl_mutex
    protect access to this struct.

.. _`dvb_net.description`:

Description
-----------

Currently, the core supports up to \ ``DVB_NET_DEVICES_MAX``\  (10) network
devices.

.. _`dvb_net_init`:

dvb_net_init
============

.. c:function:: int dvb_net_init(struct dvb_adapter *adap, struct dvb_net *dvbnet, struct dmx_demux *dmxdemux)

    nitializes a digital TV network device and registers it.

    :param struct dvb_adapter \*adap:
        pointer to \ :c:type:`struct dvb_adapter <dvb_adapter>`\ .

    :param struct dvb_net \*dvbnet:
        pointer to \ :c:type:`struct dvb_net <dvb_net>`\ .

    :param struct dmx_demux \*dmxdemux:
        pointer to \ :c:type:`struct dmx_demux <dmx_demux>`\ .

.. _`dvb_net_release`:

dvb_net_release
===============

.. c:function:: void dvb_net_release(struct dvb_net *dvbnet)

    releases a digital TV network device and unregisters it.

    :param struct dvb_net \*dvbnet:
        pointer to \ :c:type:`struct dvb_net <dvb_net>`\ .

.. This file was automatic generated / don't edit.


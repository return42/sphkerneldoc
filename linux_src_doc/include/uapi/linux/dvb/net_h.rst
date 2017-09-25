.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/dvb/net.h

.. _`dvb_net_if`:

struct dvb_net_if
=================

.. c:type:: struct dvb_net_if

    describes a DVB network interface

.. _`dvb_net_if.definition`:

Definition
----------

.. code-block:: c

    struct dvb_net_if {
        __u16 pid;
        __u16 if_num;
        __u8 feedtype;
    #define DVB_NET_FEEDTYPE_MPE 0 
    #define DVB_NET_FEEDTYPE_ULE 1 
    }

.. _`dvb_net_if.members`:

Members
-------

pid
    Packet ID (PID) of the MPEG-TS that contains data

if_num
    number of the Digital TV interface.

feedtype
    *undescribed*

.. _`dvb_net_if.description`:

Description
-----------

A MPEG-TS stream may contain packet IDs with IP packages on it.
This struct describes it, and the type of encoding.

     - \ ``DVB_NET_FEEDTYPE_MPE``\  for MPE encoding
     - \ ``DVB_NET_FEEDTYPE_ULE``\  for ULE encoding.

.. This file was automatic generated / don't edit.


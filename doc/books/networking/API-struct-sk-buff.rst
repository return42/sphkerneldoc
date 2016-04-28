.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-sk-buff:

==============
struct sk_buff
==============

*man struct sk_buff(9)*

*4.6.0-rc5*

socket buffer


Synopsis
========

.. code-block:: c

    struct sk_buff {
      union {unnamed_union};
      __u16 inner_transport_header;
      __u16 inner_network_header;
      __u16 inner_mac_header;
      __be16 protocol;
      __u16 transport_header;
      __u16 network_header;
      __u16 mac_header;
      sk_buff_data_t tail;
      sk_buff_data_t end;
      unsigned char * head;
      unsigned char * data;
      unsigned int truesize;
      atomic_t users;
    };


Members
=======

{unnamed_union}
    anonymous

inner_transport_header
    Inner transport layer header (encapsulation)

inner_network_header
    Network layer header (encapsulation)

inner_mac_header
    Link layer header (encapsulation)

protocol
    Packet protocol from driver

transport_header
    Transport layer header

network_header
    Network layer header

mac_header
    Link layer header

tail
    Tail pointer

end
    End pointer

head
    Head of buffer

data
    Data head pointer

truesize
    Buffer size

users
    User count - see {datagram,tcp}.c


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

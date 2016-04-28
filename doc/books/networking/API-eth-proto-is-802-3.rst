.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-proto-is-802-3:

==================
eth_proto_is_802_3
==================

*man eth_proto_is_802_3(9)*

*4.6.0-rc5*

Determine if a given Ethertype/length is a protocol


Synopsis
========

.. c:function:: bool eth_proto_is_802_3( __be16 proto )

Arguments
=========

``proto``
    Ethertype/length value to be tested


Description
===========

Check that the value from the Ethertype/length field is a valid
Ethertype.

Return true if the valid is an 802.3 supported Ethertype.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

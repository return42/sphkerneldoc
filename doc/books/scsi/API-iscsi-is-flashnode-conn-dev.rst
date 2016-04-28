.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-is-flashnode-conn-dev:

===========================
iscsi_is_flashnode_conn_dev
===========================

*man iscsi_is_flashnode_conn_dev(9)*

*4.6.0-rc5*

verify passed device is to be flashnode conn


Synopsis
========

.. c:function:: int iscsi_is_flashnode_conn_dev( struct device * dev, void * data )

Arguments
=========

``dev``
    device to verify

``data``
    pointer to data containing value to use for verification


Description
===========

Verifies if the passed device is flashnode conn device


Returns
=======

1 on success 0 on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

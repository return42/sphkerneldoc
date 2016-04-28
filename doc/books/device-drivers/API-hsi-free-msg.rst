.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-free-msg:

============
hsi_free_msg
============

*man hsi_free_msg(9)*

*4.6.0-rc5*

Free an HSI message


Synopsis
========

.. c:function:: void hsi_free_msg( struct hsi_msg * msg )

Arguments
=========

``msg``
    Pointer to the HSI message


Description
===========

Client is responsible to free the buffers pointed by the scatterlists.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

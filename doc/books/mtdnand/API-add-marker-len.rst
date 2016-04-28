.. -*- coding: utf-8; mode: rst -*-

.. _API-add-marker-len:

==============
add_marker_len
==============

*man add_marker_len(9)*

*4.6.0-rc5*

compute the length of the marker in data area


Synopsis
========

.. c:function:: u32 add_marker_len( struct nand_bbt_descr * td )

Arguments
=========

``td``
    BBT descriptor used for computation


Description
===========

The length will be 0 if the marker is located in OOB area.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

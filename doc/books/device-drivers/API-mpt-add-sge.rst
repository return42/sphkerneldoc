.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-add-sge:

===========
mpt_add_sge
===========

*man mpt_add_sge(9)*

*4.6.0-rc5*

Place a simple 32 bit SGE at address pAddr.


Synopsis
========

.. c:function:: void mpt_add_sge( void * pAddr, u32 flagslength, dma_addr_t dma_addr )

Arguments
=========

``pAddr``
    virtual address for SGE

``flagslength``
    SGE flags and data transfer length

``dma_addr``
    Physical address


Description
===========

This routine places a MPT request frame back on the MPT adapter's FreeQ.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

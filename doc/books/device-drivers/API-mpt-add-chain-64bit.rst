.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-add-chain-64bit:

===================
mpt_add_chain_64bit
===================

*man mpt_add_chain_64bit(9)*

*4.6.0-rc5*

Place a 64 bit chain SGE at address pAddr.


Synopsis
========

.. c:function:: void mpt_add_chain_64bit( void * pAddr, u8 next, u16 length, dma_addr_t dma_addr )

Arguments
=========

``pAddr``
    virtual address for SGE

``next``
    nextChainOffset value (u32's)

``length``
    length of next SGL segment

``dma_addr``
    Physical address


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

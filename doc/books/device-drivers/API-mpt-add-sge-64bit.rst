
.. _API-mpt-add-sge-64bit:

=================
mpt_add_sge_64bit
=================

*man mpt_add_sge_64bit(9)*

*4.6.0-rc1*

Place a simple 64 bit SGE at address pAddr.


Synopsis
========

.. c:function:: void mpt_add_sge_64bit( void * pAddr, u32 flagslength, dma_addr_t dma_addr )

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

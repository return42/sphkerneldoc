
.. _API-mpt-add-chain:

=============
mpt_add_chain
=============

*man mpt_add_chain(9)*

*4.6.0-rc1*

Place a 32 bit chain SGE at address pAddr.


Synopsis
========

.. c:function:: void mpt_add_chain( void * pAddr, u8 next, u16 length, dma_addr_t dma_addr )

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

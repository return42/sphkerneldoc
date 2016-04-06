
.. _API-hsi-alloc-msg:

=============
hsi_alloc_msg
=============

*man hsi_alloc_msg(9)*

*4.6.0-rc1*

Allocate an HSI message


Synopsis
========

.. c:function:: struct hsi_msg ⋆ hsi_alloc_msg( unsigned int nents, gfp_t flags )

Arguments
=========

``nents``
    Number of memory entries

``flags``
    Kernel allocation flags


Description
===========

nents can be 0. This mainly makes sense for read transfer. In that case, HSI drivers will call the complete callback when there is data to be read without consuming it.

Return NULL on failure or a pointer to an hsi_msg on success.

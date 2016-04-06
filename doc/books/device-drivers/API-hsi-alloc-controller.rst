
.. _API-hsi-alloc-controller:

====================
hsi_alloc_controller
====================

*man hsi_alloc_controller(9)*

*4.6.0-rc1*

Allocate an HSI controller and its ports


Synopsis
========

.. c:function:: struct hsi_controller ⋆ hsi_alloc_controller( unsigned int n_ports, gfp_t flags )

Arguments
=========

``n_ports``
    Number of ports on the HSI controller

``flags``
    Kernel allocation flags


Description
===========

Return NULL on failure or a pointer to an hsi_controller on success.

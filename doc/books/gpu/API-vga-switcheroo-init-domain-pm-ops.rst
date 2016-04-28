.. -*- coding: utf-8; mode: rst -*-

.. _API-vga-switcheroo-init-domain-pm-ops:

=================================
vga_switcheroo_init_domain_pm_ops
=================================

*man vga_switcheroo_init_domain_pm_ops(9)*

*4.6.0-rc5*

helper for driver power control


Synopsis
========

.. c:function:: int vga_switcheroo_init_domain_pm_ops( struct device * dev, struct dev_pm_domain * domain )

Arguments
=========

``dev``
    vga client device

``domain``
    power domain


Description
===========

Helper for GPUs whose power state is controlled by the driver's runtime
pm. After the GPU has been suspended, the handler needs to be called to
cut power to the GPU. Likewise it needs to reinstate power before the
GPU can resume. To this end, this helper augments the suspend/resume
functions by the requisite calls to the handler. It needs only be called
on platforms where the power switch is separate to the device being
powered down.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

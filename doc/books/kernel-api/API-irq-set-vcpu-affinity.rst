.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-vcpu-affinity:

=====================
irq_set_vcpu_affinity
=====================

*man irq_set_vcpu_affinity(9)*

*4.6.0-rc5*

Set vcpu affinity for the interrupt


Synopsis
========

.. c:function:: int irq_set_vcpu_affinity( unsigned int irq, void * vcpu_info )

Arguments
=========

``irq``
    interrupt number to set affinity

``vcpu_info``
    vCPU specific data


Description
===========

This function uses the vCPU specific data to set the vCPU affinity for
an irq. The vCPU specific data is passed from outside, such as KVM. One
example code path is as below: KVM -> IOMMU ->
``irq_set_vcpu_affinity``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

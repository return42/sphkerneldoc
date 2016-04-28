.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-lrc-irq-handler:

=====================
intel_lrc_irq_handler
=====================

*man intel_lrc_irq_handler(9)*

*4.6.0-rc5*

handle Context Switch interrupts


Synopsis
========

.. c:function:: void intel_lrc_irq_handler( struct intel_engine_cs * ring )

Arguments
=========

``ring``
    Engine Command Streamer to handle.


Description
===========

Check the unread Context Status Buffers and manage the submission of new
contexts to the ELSP accordingly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

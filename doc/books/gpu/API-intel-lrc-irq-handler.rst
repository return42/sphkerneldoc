
.. _API-intel-lrc-irq-handler:

=====================
intel_lrc_irq_handler
=====================

*man intel_lrc_irq_handler(9)*

*4.6.0-rc1*

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

Check the unread Context Status Buffers and manage the submission of new contexts to the ELSP accordingly.

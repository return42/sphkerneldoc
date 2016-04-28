.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-component-async-complete:

================================
snd_soc_component_async_complete
================================

*man snd_soc_component_async_complete(9)*

*4.6.0-rc5*

Ensure asynchronous I/O has completed


Synopsis
========

.. c:function:: void snd_soc_component_async_complete( struct snd_soc_component * component )

Arguments
=========

``component``
    Component for which to wait


Description
===========

This function blocks until all asynchronous I/O which has previously
been scheduled using ``snd_soc_component_update_bits_async`` has
completed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

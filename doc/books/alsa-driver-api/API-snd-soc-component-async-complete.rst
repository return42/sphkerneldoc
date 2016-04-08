
.. _API-snd-soc-component-async-complete:

================================
snd_soc_component_async_complete
================================

*man snd_soc_component_async_complete(9)*

*4.6.0-rc1*

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

This function blocks until all asynchronous I/O which has previously been scheduled using ``snd_soc_component_update_bits_async`` has completed.

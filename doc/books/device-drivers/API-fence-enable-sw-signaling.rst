
.. _API-fence-enable-sw-signaling:

=========================
fence_enable_sw_signaling
=========================

*man fence_enable_sw_signaling(9)*

*4.6.0-rc1*

enable signaling on fence


Synopsis
========

.. c:function:: void fence_enable_sw_signaling( struct fence * fence )

Arguments
=========

``fence``
    [in] the fence to enable


Description
===========

this will request for sw signaling to be enabled, to make the fence complete as soon as possible

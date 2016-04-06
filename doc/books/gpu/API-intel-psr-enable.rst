
.. _API-intel-psr-enable:

================
intel_psr_enable
================

*man intel_psr_enable(9)*

*4.6.0-rc1*

Enable PSR


Synopsis
========

.. c:function:: void intel_psr_enable( struct intel_dp * intel_dp )

Arguments
=========

``intel_dp``
    Intel DP


Description
===========

This function can only be called after the pipe is fully trained and enabled.

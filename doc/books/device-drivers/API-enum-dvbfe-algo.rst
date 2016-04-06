
.. _API-enum-dvbfe-algo:

===============
enum dvbfe_algo
===============

*man enum dvbfe_algo(9)*

*4.6.0-rc1*

defines the algorithm used to tune into a channel


Synopsis
========

.. code-block:: c

    enum dvbfe_algo {
      DVBFE_ALGO_HW,
      DVBFE_ALGO_SW,
      DVBFE_ALGO_CUSTOM,
      DVBFE_ALGO_RECOVERY
    };


Constants
=========

DVBFE_ALGO_HW
    Hardware Algorithm - Devices that support this algorithm do everything in hardware and no software support is needed to handle them. Requesting these devices to LOCK is the
    only thing required, device is supposed to do everything in the hardware.

DVBFE_ALGO_SW
    Software Algorithm - These are dumb devices, that require software to do everything

DVBFE_ALGO_CUSTOM
    Customizable Agorithm - Devices having this algorithm can be customized to have specific algorithms in the frontend driver, rather than simply doing a software zig-zag. In this
    case the zigzag maybe hardware assisted or it maybe completely done in hardware. In all cases, usage of this algorithm, in conjunction with the search and track callbacks,
    utilizes the driver specific algorithm.

DVBFE_ALGO_RECOVERY
    Recovery Algorithm - These devices have AUTO recovery capabilities from LOCK failure

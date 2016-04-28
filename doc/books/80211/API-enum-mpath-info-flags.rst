.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-mpath-info-flags:

=====================
enum mpath_info_flags
=====================

*man enum mpath_info_flags(9)*

*4.6.0-rc5*

mesh path information flags


Synopsis
========

.. code-block:: c

    enum mpath_info_flags {
      MPATH_INFO_FRAME_QLEN,
      MPATH_INFO_SN,
      MPATH_INFO_METRIC,
      MPATH_INFO_EXPTIME,
      MPATH_INFO_DISCOVERY_TIMEOUT,
      MPATH_INFO_DISCOVERY_RETRIES,
      MPATH_INFO_FLAGS
    };


Constants
=========

MPATH_INFO_FRAME_QLEN
    ``frame_qlen`` filled

MPATH_INFO_SN
    ``sn`` filled

MPATH_INFO_METRIC
    ``metric`` filled

MPATH_INFO_EXPTIME
    ``exptime`` filled

MPATH_INFO_DISCOVERY_TIMEOUT
    ``discovery_timeout`` filled

MPATH_INFO_DISCOVERY_RETRIES
    ``discovery_retries`` filled

MPATH_INFO_FLAGS
    ``flags`` filled


Description
===========

Used by the driver to indicate which info in ``struct mpath_info`` it
has filled in during ``get_station`` or ``dump_station``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

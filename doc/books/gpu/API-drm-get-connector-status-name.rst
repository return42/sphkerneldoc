.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-get-connector-status-name:

=============================
drm_get_connector_status_name
=============================

*man drm_get_connector_status_name(9)*

*4.6.0-rc5*

return a string for connector status


Synopsis
========

.. c:function:: const char * drm_get_connector_status_name( enum drm_connector_status status )

Arguments
=========

``status``
    connector status to compute name of


Description
===========

In contrast to the other drm_get_*_name functions this one here
returns a const pointer and hence is threadsafe.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

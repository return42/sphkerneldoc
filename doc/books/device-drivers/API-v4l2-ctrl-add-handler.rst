.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-add-handler:

=====================
v4l2_ctrl_add_handler
=====================

*man v4l2_ctrl_add_handler(9)*

*4.6.0-rc5*

Add all controls from handler ``add`` to handler ``hdl``.


Synopsis
========

.. c:function:: int v4l2_ctrl_add_handler( struct v4l2_ctrl_handler * hdl, struct v4l2_ctrl_handler * add, bool (*filter) const struct v4l2_ctrl *ctrl )

Arguments
=========

``hdl``
    The control handler.

``add``
    The control handler whose controls you want to add to the ``hdl``
    control handler.

``filter``
    This function will filter which controls should be added.


Description
===========

Does nothing if either of the two handlers is a NULL pointer. If
``filter`` is NULL, then all controls are added. Otherwise only those
controls for which ``filter`` returns true will be added. In case of an
error ``hdl``->error will be set to the error code (if it wasn't set
already).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

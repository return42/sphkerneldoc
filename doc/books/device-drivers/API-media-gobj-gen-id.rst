.. -*- coding: utf-8; mode: rst -*-

.. _API-media-gobj-gen-id:

=================
media_gobj_gen_id
=================

*man media_gobj_gen_id(9)*

*4.6.0-rc5*

encapsulates type and ID on at the object ID


Synopsis
========

.. c:function:: u32 media_gobj_gen_id( enum media_gobj_type type, u64 local_id )

Arguments
=========

``type``
    object type as define at enum ``media_gobj_type``.

``local_id``
    next ID, from struct ``media_device``.\ ``id``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

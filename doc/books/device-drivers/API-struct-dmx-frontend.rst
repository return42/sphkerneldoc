.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dmx-frontend:

===================
struct dmx_frontend
===================

*man struct dmx_frontend(9)*

*4.6.0-rc5*

Structure that lists the frontends associated with a demux


Synopsis
========

.. code-block:: c

    struct dmx_frontend {
      struct list_head connectivity_list;
      enum dmx_frontend_source source;
    };


Members
=======

connectivity_list
    List of front-ends that can be connected to a particular demux;

source
    Type of the frontend.


FIXME
=====

this structure should likely be replaced soon by some media-controller
based logic.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

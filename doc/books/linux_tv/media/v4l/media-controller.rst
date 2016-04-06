
.. _media_common:

++++++++++++++++++++
Media Controller API
++++++++++++++++++++

.. _media_controller:

================
Media Controller
================


.. _media-controller-intro:

Introduction
============

Media devices increasingly handle multiple related functions. Many USB cameras include microphones, video capture hardware can also output video, or SoC camera interfaces also
perform memory-to-memory operations similar to video codecs.

Independent functions, even when implemented in the same hardware, can be modelled as separate devices. A USB camera with a microphone will be presented to userspace applications
as V4L2 and ALSA capture devices. The devices' relationships (when using a webcam, end-users shouldn't have to manually select the associated USB microphone), while not made
available directly to applications by the drivers, can usually be retrieved from sysfs.

With more and more advanced SoC devices being introduced, the current approach will not scale. Device topologies are getting increasingly complex and can't always be represented by
a tree structure. Hardware blocks are shared between different functions, creating dependencies between seemingly unrelated devices.

Kernel abstraction APIs such as V4L2 and ALSA provide means for applications to access hardware parameters. As newer hardware expose an increasingly high number of those
parameters, drivers need to guess what applications really require based on limited information, thereby implementing policies that belong to userspace.

The media controller API aims at solving those problems.


.. _media-controller-model:

Media device model
==================

Discovering a device internal topology, and configuring it at runtime, is one of the goals of the media controller API. To achieve this, hardware devices and Linux Kernel
interfaces are modelled as graph objects on an oriented graph. The object types that constitute the graph are:

-  An **entity** is a basic media hardware or software building block. It can correspond to a large variety of logical blocks such as physical hardware devices (CMOS sensor for
   instance), logical hardware devices (a building block in a System-on-Chip image processing pipeline), DMA channels or physical connectors.

-  An **interface** is a graph representation of a Linux Kernel userspace API interface, like a device node or a sysfs file that controls one or more entities in the graph.

-  A **pad** is a data connection endpoint through which an entity can interact with other entities. Data (not restricted to video) produced by an entity flows from the entity's
   output to one or more entity inputs. Pads should not be confused with physical pins at chip boundaries.

-  A **data link** is a point-to-point oriented connection between two pads, either on the same entity or on different entities. Data flows from a source pad to a sink pad.

-  An **interface link** is a point-to-point bidirectional control connection between a Linux Kernel interface and an entity.m


.. toctree::
    :maxdepth: 1

    media-types

.. _media-user-func:

==================
Function Reference
==================


.. toctree::
    :maxdepth: 1

    media-func-open
    media-func-close
    media-func-ioctl
    media-ioc-device-info
    media-ioc-g-topology
    media-ioc-enum-entities
    media-ioc-enum-links
    media-ioc-setup-link

======================
Revision and Copyright
======================


:author:    Pinchart Laurent
:address:   laurent.pinchart@ideasonboard.com
:contrib:   Initial version.

**Copyright** 2010 : Laurent Pinchart

:revision: 1.0.0 / 2010-11-10 (*lp*)

Initial revision

.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/media-entity.h

.. _`media_gobj_type`:

enum media_gobj_type
====================

.. c:type:: enum media_gobj_type

    type of a graph object

.. _`media_gobj_type.definition`:

Definition
----------

.. code-block:: c

    enum media_gobj_type {
        MEDIA_GRAPH_ENTITY,
        MEDIA_GRAPH_PAD,
        MEDIA_GRAPH_LINK,
        MEDIA_GRAPH_INTF_DEVNODE
    };

.. _`media_gobj_type.constants`:

Constants
---------

MEDIA_GRAPH_ENTITY
    Identify a media entity

MEDIA_GRAPH_PAD
    Identify a media pad

MEDIA_GRAPH_LINK
    Identify a media link

MEDIA_GRAPH_INTF_DEVNODE
    Identify a media Kernel API interface via
    a device node

.. _`media_gobj`:

struct media_gobj
=================

.. c:type:: struct media_gobj

    Define a graph object.

.. _`media_gobj.definition`:

Definition
----------

.. code-block:: c

    struct media_gobj {
        struct media_device *mdev;
        u32 id;
        struct list_head list;
    }

.. _`media_gobj.members`:

Members
-------

mdev
    Pointer to the struct \ :c:type:`struct media_device <media_device>`\  that owns the object

id
    Non-zero object ID identifier. The ID should be unique
    inside a media_device, as it is composed by
    \ ``MEDIA_BITS_PER_TYPE``\  to store the type plus
    \ ``MEDIA_BITS_PER_ID``\  to store the ID

list
    List entry stored in one of the per-type mdev object lists

.. _`media_gobj.description`:

Description
-----------

All objects on the media graph should have this struct embedded

.. _`media_entity_enum`:

struct media_entity_enum
========================

.. c:type:: struct media_entity_enum

    An enumeration of media entities.

.. _`media_entity_enum.definition`:

Definition
----------

.. code-block:: c

    struct media_entity_enum {
        unsigned long *bmap;
        int idx_max;
    }

.. _`media_entity_enum.members`:

Members
-------

bmap
    Bit map in which each bit represents one entity at struct
    media_entity->internal_idx.

idx_max
    Number of bits in bmap

.. _`media_graph`:

struct media_graph
==================

.. c:type:: struct media_graph

    Media graph traversal state

.. _`media_graph.definition`:

Definition
----------

.. code-block:: c

    struct media_graph {
        struct {
            struct media_entity *entity;
            struct list_head *link;
        } stack[MEDIA_ENTITY_ENUM_MAX_DEPTH];
        struct media_entity_enum ent_enum;
        int top;
    }

.. _`media_graph.members`:

Members
-------

stack
    Graph traversal stack; the stack contains information
    on the path the media entities to be walked and the
    links through which they were reached.

stack.entity
    pointer to \ :c:type:`struct media_entity <media_entity>`\  at the graph.

stack.link
    pointer to \ :c:type:`struct list_head <list_head>`\ .

ent_enum
    Visited entities

top
    The top of the stack

.. _`media_pipeline`:

struct media_pipeline
=====================

.. c:type:: struct media_pipeline

    Media pipeline related information

.. _`media_pipeline.definition`:

Definition
----------

.. code-block:: c

    struct media_pipeline {
        int streaming_count;
        struct media_graph graph;
    }

.. _`media_pipeline.members`:

Members
-------

streaming_count
    Streaming start count - streaming stop count

graph
    Media graph walk during pipeline start / stop

.. _`media_link`:

struct media_link
=================

.. c:type:: struct media_link

    A link object part of a media graph.

.. _`media_link.definition`:

Definition
----------

.. code-block:: c

    struct media_link {
        struct media_gobj graph_obj;
        struct list_head list;
        union {
            struct media_gobj *gobj0;
            struct media_pad *source;
            struct media_interface *intf;
        } ;
        union {
            struct media_gobj *gobj1;
            struct media_pad *sink;
            struct media_entity *entity;
        } ;
        struct media_link *reverse;
        unsigned long flags;
        bool is_backlink;
    }

.. _`media_link.members`:

Members
-------

graph_obj
    Embedded structure containing the media object common data

list
    Linked list associated with an entity or an interface that
    owns the link.

{unnamed_union}
    anonymous

gobj0
    Part of a union. Used to get the pointer for the first
    graph_object of the link.

source
    Part of a union. Used only if the first object (gobj0) is
    a pad. In that case, it represents the source pad.

intf
    Part of a union. Used only if the first object (gobj0) is
    an interface.

{unnamed_union}
    anonymous

gobj1
    Part of a union. Used to get the pointer for the second
    graph_object of the link.

sink
    Part of a union. Used only if the second object (gobj1) is
    a pad. In that case, it represents the sink pad.

entity
    Part of a union. Used only if the second object (gobj1) is
    an entity.

reverse
    Pointer to the link for the reverse direction of a pad to pad
    link.

flags
    Link flags, as defined in uapi/media.h (MEDIA_LNK_FL_*)

is_backlink
    Indicate if the link is a backlink.

.. _`media_pad_signal_type`:

enum media_pad_signal_type
==========================

.. c:type:: enum media_pad_signal_type

    type of the signal inside a media pad

.. _`media_pad_signal_type.definition`:

Definition
----------

.. code-block:: c

    enum media_pad_signal_type {
        PAD_SIGNAL_DEFAULT,
        PAD_SIGNAL_ANALOG,
        PAD_SIGNAL_DV,
        PAD_SIGNAL_AUDIO
    };

.. _`media_pad_signal_type.constants`:

Constants
---------

PAD_SIGNAL_DEFAULT
    Default signal. Use this when all inputs or all outputs are
    uniquely identified by the pad number.

PAD_SIGNAL_ANALOG
    The pad contains an analog signal. It can be Radio Frequency,
    Intermediate Frequency, a baseband signal or sub-cariers.
    Tuner inputs, IF-PLL demodulators, composite and s-video signals
    should use it.

PAD_SIGNAL_DV
    Contains a digital video signal, with can be a bitstream of samples
    taken from an analog TV video source. On such case, it usually
    contains the VBI data on it.

PAD_SIGNAL_AUDIO
    Contains an Intermediate Frequency analog signal from an audio
    sub-carrier or an audio bitstream. IF signals are provided by tuners
    and consumed by audio AM/FM decoders. Bitstream audio is provided by
    an audio decoder.

.. _`media_pad`:

struct media_pad
================

.. c:type:: struct media_pad

    A media pad graph object.

.. _`media_pad.definition`:

Definition
----------

.. code-block:: c

    struct media_pad {
        struct media_gobj graph_obj;
        struct media_entity *entity;
        u16 index;
        enum media_pad_signal_type sig_type;
        unsigned long flags;
    }

.. _`media_pad.members`:

Members
-------

graph_obj
    Embedded structure containing the media object common data

entity
    Entity this pad belongs to

index
    Pad index in the entity pads array, numbered from 0 to n

sig_type
    Type of the signal inside a media pad

flags
    Pad flags, as defined in
    :ref:`include/uapi/linux/media.h <media_header>`
    (seek for ``MEDIA_PAD_FL_*``)

.. _`media_entity_operations`:

struct media_entity_operations
==============================

.. c:type:: struct media_entity_operations

    Media entity operations

.. _`media_entity_operations.definition`:

Definition
----------

.. code-block:: c

    struct media_entity_operations {
        int (*get_fwnode_pad)(struct fwnode_endpoint *endpoint);
        int (*link_setup)(struct media_entity *entity,const struct media_pad *local, const struct media_pad *remote, u32 flags);
        int (*link_validate)(struct media_link *link);
    }

.. _`media_entity_operations.members`:

Members
-------

get_fwnode_pad
    Return the pad number based on a fwnode endpoint or
    a negative value on error. This operation can be used
    to map a fwnode to a media pad number. Optional.

link_setup
    Notify the entity of link changes. The operation can
    return an error, in which case link setup will be
    cancelled. Optional.

link_validate
    Return whether a link is valid from the entity point of
    view. The \ :c:func:`media_pipeline_start`\  function
    validates all links by calling this operation. Optional.

.. _`media_entity_operations.description`:

Description
-----------

.. note::

   Those these callbacks are called with struct &media_device.graph_mutex
   mutex held.

.. _`media_entity_type`:

enum media_entity_type
======================

.. c:type:: enum media_entity_type

    Media entity type

.. _`media_entity_type.definition`:

Definition
----------

.. code-block:: c

    enum media_entity_type {
        MEDIA_ENTITY_TYPE_BASE,
        MEDIA_ENTITY_TYPE_VIDEO_DEVICE,
        MEDIA_ENTITY_TYPE_V4L2_SUBDEV
    };

.. _`media_entity_type.constants`:

Constants
---------

MEDIA_ENTITY_TYPE_BASE
    The entity isn't embedded in another subsystem structure.

MEDIA_ENTITY_TYPE_VIDEO_DEVICE
    The entity is embedded in a struct video_device instance.

MEDIA_ENTITY_TYPE_V4L2_SUBDEV
    The entity is embedded in a struct v4l2_subdev instance.

.. _`media_entity_type.description`:

Description
-----------

Media entity objects are often not instantiated directly, but the media
entity structure is inherited by (through embedding) other subsystem-specific
structures. The media entity type identifies the type of the subclass
structure that implements a media entity instance.

This allows runtime type identification of media entities and safe casting to
the correct object type. For instance, a media entity structure instance
embedded in a v4l2_subdev structure instance will have the type
\ ``MEDIA_ENTITY_TYPE_V4L2_SUBDEV``\  and can safely be cast to a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
structure using the \ :c:func:`container_of`\  macro.

.. _`media_entity`:

struct media_entity
===================

.. c:type:: struct media_entity

    A media entity graph object.

.. _`media_entity.definition`:

Definition
----------

.. code-block:: c

    struct media_entity {
        struct media_gobj graph_obj;
        const char *name;
        enum media_entity_type obj_type;
        u32 function;
        unsigned long flags;
        u16 num_pads;
        u16 num_links;
        u16 num_backlinks;
        int internal_idx;
        struct media_pad *pads;
        struct list_head links;
        const struct media_entity_operations *ops;
        int stream_count;
        int use_count;
        struct media_pipeline *pipe;
        union {
            struct {
                u32 major;
                u32 minor;
            } dev;
        } info;
    }

.. _`media_entity.members`:

Members
-------

graph_obj
    Embedded structure containing the media object common data.

name
    Entity name.

obj_type
    Type of the object that implements the media_entity.

function
    Entity main function, as defined in
    :ref:`include/uapi/linux/media.h <media_header>`
    (seek for ``MEDIA_ENT_F_*``)

flags
    Entity flags, as defined in
    :ref:`include/uapi/linux/media.h <media_header>`
    (seek for ``MEDIA_ENT_FL_*``)

num_pads
    Number of sink and source pads.

num_links
    Total number of links, forward and back, enabled and disabled.

num_backlinks
    Number of backlinks

internal_idx
    An unique internal entity specific number. The numbers are
    re-used if entities are unregistered or registered again.

pads
    Pads array with the size defined by \ ``num_pads``\ .

links
    List of data links.

ops
    Entity operations.

stream_count
    Stream count for the entity.

use_count
    Use count for the entity.

pipe
    Pipeline this entity belongs to.

info
    Union with devnode information.  Kept just for backward
    compatibility.

info.dev
    Contains device major and minor info.

info.dev.major
    device node major, if the device is a devnode.

info.dev.minor
    device node minor, if the device is a devnode.

.. _`media_entity.description`:

Description
-----------

.. note::

   @stream_count and @use_count reference counts must never be
   negative, but are signed integers on purpose: a simple ``WARN_ON(<0)``
   check can be used to detect reference count bugs that would make them
   negative.

.. _`media_interface`:

struct media_interface
======================

.. c:type:: struct media_interface

    A media interface graph object.

.. _`media_interface.definition`:

Definition
----------

.. code-block:: c

    struct media_interface {
        struct media_gobj graph_obj;
        struct list_head links;
        u32 type;
        u32 flags;
    }

.. _`media_interface.members`:

Members
-------

graph_obj
    embedded graph object

links
    List of links pointing to graph entities

type
    Type of the interface as defined in
    :ref:`include/uapi/linux/media.h <media_header>`
    (seek for ``MEDIA_INTF_T_*``)

flags
    Interface flags as defined in
    :ref:`include/uapi/linux/media.h <media_header>`
    (seek for ``MEDIA_INTF_FL_*``)

.. _`media_interface.description`:

Description
-----------

.. note::

   Currently, no flags for &media_interface is defined.

.. _`media_intf_devnode`:

struct media_intf_devnode
=========================

.. c:type:: struct media_intf_devnode

    A media interface via a device node.

.. _`media_intf_devnode.definition`:

Definition
----------

.. code-block:: c

    struct media_intf_devnode {
        struct media_interface intf;
        u32 major;
        u32 minor;
    }

.. _`media_intf_devnode.members`:

Members
-------

intf
    embedded interface object

major
    Major number of a device node

minor
    Minor number of a device node

.. _`media_entity_id`:

media_entity_id
===============

.. c:function:: u32 media_entity_id(struct media_entity *entity)

    return the media entity graph object id

    :param entity:
        pointer to \ :c:type:`struct media_entity <media_entity>`\ 
    :type entity: struct media_entity \*

.. _`media_type`:

media_type
==========

.. c:function:: enum media_gobj_type media_type(struct media_gobj *gobj)

    return the media object type

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: struct media_gobj \*

.. _`media_id`:

media_id
========

.. c:function:: u32 media_id(struct media_gobj *gobj)

    return the media object ID

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: struct media_gobj \*

.. _`media_gobj_gen_id`:

media_gobj_gen_id
=================

.. c:function:: u32 media_gobj_gen_id(enum media_gobj_type type, u64 local_id)

    encapsulates type and ID on at the object ID

    :param type:
        object type as define at enum \ :c:type:`struct media_gobj_type <media_gobj_type>`\ .
    :type type: enum media_gobj_type

    :param local_id:
        next ID, from struct \ :c:type:`media_device.id <media_device>`\ .
    :type local_id: u64

.. _`is_media_entity_v4l2_video_device`:

is_media_entity_v4l2_video_device
=================================

.. c:function:: bool is_media_entity_v4l2_video_device(struct media_entity *entity)

    Check if the entity is a video_device

    :param entity:
        pointer to entity
    :type entity: struct media_entity \*

.. _`is_media_entity_v4l2_video_device.return`:

Return
------

\ ``true``\  if the entity is an instance of a video_device object and can
safely be cast to a struct video_device using the \ :c:func:`container_of`\  macro, or
\ ``false``\  otherwise.

.. _`is_media_entity_v4l2_subdev`:

is_media_entity_v4l2_subdev
===========================

.. c:function:: bool is_media_entity_v4l2_subdev(struct media_entity *entity)

    Check if the entity is a v4l2_subdev

    :param entity:
        pointer to entity
    :type entity: struct media_entity \*

.. _`is_media_entity_v4l2_subdev.return`:

Return
------

\ ``true``\  if the entity is an instance of a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  object and can
safely be cast to a struct \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  using the \ :c:func:`container_of`\  macro, or
\ ``false``\  otherwise.

.. _`__media_entity_enum_init`:

__media_entity_enum_init
========================

.. c:function:: int __media_entity_enum_init(struct media_entity_enum *ent_enum, int idx_max)

    Initialise an entity enumeration

    :param ent_enum:
        Entity enumeration to be initialised
    :type ent_enum: struct media_entity_enum \*

    :param idx_max:
        Maximum number of entities in the enumeration
    :type idx_max: int

.. _`__media_entity_enum_init.return`:

Return
------

Returns zero on success or a negative error code.

.. _`media_entity_enum_cleanup`:

media_entity_enum_cleanup
=========================

.. c:function:: void media_entity_enum_cleanup(struct media_entity_enum *ent_enum)

    Release resources of an entity enumeration

    :param ent_enum:
        Entity enumeration to be released
    :type ent_enum: struct media_entity_enum \*

.. _`media_entity_enum_zero`:

media_entity_enum_zero
======================

.. c:function:: void media_entity_enum_zero(struct media_entity_enum *ent_enum)

    Clear the entire enum

    :param ent_enum:
        Entity enumeration to be cleared
    :type ent_enum: struct media_entity_enum \*

.. _`media_entity_enum_set`:

media_entity_enum_set
=====================

.. c:function:: void media_entity_enum_set(struct media_entity_enum *ent_enum, struct media_entity *entity)

    Mark a single entity in the enum

    :param ent_enum:
        Entity enumeration
    :type ent_enum: struct media_entity_enum \*

    :param entity:
        Entity to be marked
    :type entity: struct media_entity \*

.. _`media_entity_enum_clear`:

media_entity_enum_clear
=======================

.. c:function:: void media_entity_enum_clear(struct media_entity_enum *ent_enum, struct media_entity *entity)

    Unmark a single entity in the enum

    :param ent_enum:
        Entity enumeration
    :type ent_enum: struct media_entity_enum \*

    :param entity:
        Entity to be unmarked
    :type entity: struct media_entity \*

.. _`media_entity_enum_test`:

media_entity_enum_test
======================

.. c:function:: bool media_entity_enum_test(struct media_entity_enum *ent_enum, struct media_entity *entity)

    Test whether the entity is marked

    :param ent_enum:
        Entity enumeration
    :type ent_enum: struct media_entity_enum \*

    :param entity:
        Entity to be tested
    :type entity: struct media_entity \*

.. _`media_entity_enum_test.description`:

Description
-----------

Returns \ ``true``\  if the entity was marked.

.. _`media_entity_enum_test_and_set`:

media_entity_enum_test_and_set
==============================

.. c:function:: bool media_entity_enum_test_and_set(struct media_entity_enum *ent_enum, struct media_entity *entity)

    Test whether the entity is marked, and mark it

    :param ent_enum:
        Entity enumeration
    :type ent_enum: struct media_entity_enum \*

    :param entity:
        Entity to be tested
    :type entity: struct media_entity \*

.. _`media_entity_enum_test_and_set.description`:

Description
-----------

Returns \ ``true``\  if the entity was marked, and mark it before doing so.

.. _`media_entity_enum_empty`:

media_entity_enum_empty
=======================

.. c:function:: bool media_entity_enum_empty(struct media_entity_enum *ent_enum)

    Test whether the entire enum is empty

    :param ent_enum:
        Entity enumeration
    :type ent_enum: struct media_entity_enum \*

.. _`media_entity_enum_empty.return`:

Return
------

\ ``true``\  if the entity was empty.

.. _`media_entity_enum_intersects`:

media_entity_enum_intersects
============================

.. c:function:: bool media_entity_enum_intersects(struct media_entity_enum *ent_enum1, struct media_entity_enum *ent_enum2)

    Test whether two enums intersect

    :param ent_enum1:
        First entity enumeration
    :type ent_enum1: struct media_entity_enum \*

    :param ent_enum2:
        Second entity enumeration
    :type ent_enum2: struct media_entity_enum \*

.. _`media_entity_enum_intersects.return`:

Return
------

\ ``true``\  if entity enumerations \ ``ent_enum1``\  and \ ``ent_enum2``\  intersect,
otherwise \ ``false``\ .

.. _`gobj_to_entity`:

gobj_to_entity
==============

.. c:function::  gobj_to_entity( gobj)

    returns the struct \ :c:type:`struct media_entity <media_entity>`\  pointer from the \ ``gobj``\  contained on it.

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: 

.. _`gobj_to_pad`:

gobj_to_pad
===========

.. c:function::  gobj_to_pad( gobj)

    returns the struct \ :c:type:`struct media_pad <media_pad>`\  pointer from the \ ``gobj``\  contained on it.

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: 

.. _`gobj_to_link`:

gobj_to_link
============

.. c:function::  gobj_to_link( gobj)

    returns the struct \ :c:type:`struct media_link <media_link>`\  pointer from the \ ``gobj``\  contained on it.

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: 

.. _`gobj_to_intf`:

gobj_to_intf
============

.. c:function::  gobj_to_intf( gobj)

    returns the struct \ :c:type:`struct media_interface <media_interface>`\  pointer from the \ ``gobj``\  contained on it.

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: 

.. _`intf_to_devnode`:

intf_to_devnode
===============

.. c:function::  intf_to_devnode( intf)

    returns the struct media_intf_devnode pointer from the \ ``intf``\  contained on it.

    :param intf:
        Pointer to struct \ :c:type:`struct media_intf_devnode <media_intf_devnode>`\ 
    :type intf: 

.. _`media_gobj_create`:

media_gobj_create
=================

.. c:function:: void media_gobj_create(struct media_device *mdev, enum media_gobj_type type, struct media_gobj *gobj)

    Initialize a graph object

    :param mdev:
        Pointer to the \ :c:type:`struct media_device <media_device>`\  that contains the object
    :type mdev: struct media_device \*

    :param type:
        Type of the object
    :type type: enum media_gobj_type

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: struct media_gobj \*

.. _`media_gobj_create.description`:

Description
-----------

This routine initializes the embedded struct \ :c:type:`struct media_gobj <media_gobj>`\  inside a
media graph object. It is called automatically if ``media_*_create``
function calls are used. However, if the object (entity, link, pad,
interface) is embedded on some other object, this function should be
called before registering the object at the media controller.

.. _`media_gobj_destroy`:

media_gobj_destroy
==================

.. c:function:: void media_gobj_destroy(struct media_gobj *gobj)

    Stop using a graph object on a media device

    :param gobj:
        Pointer to the struct \ :c:type:`struct media_gobj <media_gobj>`\  graph object
    :type gobj: struct media_gobj \*

.. _`media_gobj_destroy.description`:

Description
-----------

This should be called by all routines like \ :c:func:`media_device_unregister`\ 
that remove/destroy media graph objects.

.. _`media_entity_pads_init`:

media_entity_pads_init
======================

.. c:function:: int media_entity_pads_init(struct media_entity *entity, u16 num_pads, struct media_pad *pads)

    Initialize the entity pads

    :param entity:
        entity where the pads belong
    :type entity: struct media_entity \*

    :param num_pads:
        total number of sink and source pads
    :type num_pads: u16

    :param pads:
        Array of \ ``num_pads``\  pads.
    :type pads: struct media_pad \*

.. _`media_entity_pads_init.description`:

Description
-----------

The pads array is managed by the entity driver and passed to
\ :c:func:`media_entity_pads_init`\  where its pointer will be stored in the
\ :c:type:`struct media_entity <media_entity>`\  structure.

If no pads are needed, drivers could either directly fill
\ :c:type:`media_entity->num_pads <media_entity>`\  with 0 and \ :c:type:`media_entity->pads <media_entity>`\  with \ ``NULL``\  or call
this function that will do the same.

As the number of pads is known in advance, the pads array is not allocated
dynamically but is managed by the entity driver. Most drivers will embed the
pads array in a driver-specific structure, avoiding dynamic allocation.

Drivers must set the direction of every pad in the pads array before calling
\ :c:func:`media_entity_pads_init`\ . The function will initialize the other pads fields.

.. _`media_entity_cleanup`:

media_entity_cleanup
====================

.. c:function:: void media_entity_cleanup(struct media_entity *entity)

    free resources associated with an entity

    :param entity:
        entity where the pads belong
    :type entity: struct media_entity \*

.. _`media_entity_cleanup.description`:

Description
-----------

This function must be called during the cleanup phase after unregistering
the entity (currently, it does nothing).

.. _`media_get_pad_index`:

media_get_pad_index
===================

.. c:function:: int media_get_pad_index(struct media_entity *entity, bool is_sink, enum media_pad_signal_type sig_type)

    retrieves a pad index from an entity

    :param entity:
        entity where the pads belong
    :type entity: struct media_entity \*

    :param is_sink:
        true if the pad is a sink, false if it is a source
    :type is_sink: bool

    :param sig_type:
        type of signal of the pad to be search
    :type sig_type: enum media_pad_signal_type

.. _`media_get_pad_index.description`:

Description
-----------

This helper function finds the first pad index inside an entity that
satisfies both \ ``is_sink``\  and \ ``sig_type``\  conditions.

.. _`media_get_pad_index.return`:

Return
------


On success, return the pad number. If the pad was not found or the media
entity is a NULL pointer, return -EINVAL.

.. _`media_create_pad_link`:

media_create_pad_link
=====================

.. c:function:: int media_create_pad_link(struct media_entity *source, u16 source_pad, struct media_entity *sink, u16 sink_pad, u32 flags)

    creates a link between two entities.

    :param source:
        pointer to \ :c:type:`struct media_entity <media_entity>`\  of the source pad.
    :type source: struct media_entity \*

    :param source_pad:
        number of the source pad in the pads array
    :type source_pad: u16

    :param sink:
        pointer to \ :c:type:`struct media_entity <media_entity>`\  of the sink pad.
    :type sink: struct media_entity \*

    :param sink_pad:
        number of the sink pad in the pads array.
    :type sink_pad: u16

    :param flags:
        Link flags, as defined in
        :ref:`include/uapi/linux/media.h <media_header>`
        ( seek for ``MEDIA_LNK_FL_*``)
    :type flags: u32

.. _`media_create_pad_link.valid-values-for-flags`:

Valid values for flags
----------------------


\ ``MEDIA_LNK_FL_ENABLED``\ 
  Indicates that the link is enabled and can be used to transfer media data.
  When two or more links target a sink pad, only one of them can be
  enabled at a time.

\ ``MEDIA_LNK_FL_IMMUTABLE``\ 
  Indicates that the link enabled state can't be modified at runtime. If
  \ ``MEDIA_LNK_FL_IMMUTABLE``\  is set, then \ ``MEDIA_LNK_FL_ENABLED``\  must also be
  set, since an immutable link is always enabled.

.. note::

   Before calling this function, media_entity_pads_init() and
   media_device_register_entity() should be called previously for both ends.

.. _`media_create_pad_links`:

media_create_pad_links
======================

.. c:function:: int media_create_pad_links(const struct media_device *mdev, const u32 source_function, struct media_entity *source, const u16 source_pad, const u32 sink_function, struct media_entity *sink, const u16 sink_pad, u32 flags, const bool allow_both_undefined)

    creates a link between two entities.

    :param mdev:
        Pointer to the media_device that contains the object
    :type mdev: const struct media_device \*

    :param source_function:
        Function of the source entities. Used only if \ ``source``\  is
        NULL.
    :type source_function: const u32

    :param source:
        pointer to \ :c:type:`struct media_entity <media_entity>`\  of the source pad. If NULL, it will use
        all entities that matches the \ ``sink_function``\ .
    :type source: struct media_entity \*

    :param source_pad:
        number of the source pad in the pads array
    :type source_pad: const u16

    :param sink_function:
        Function of the sink entities. Used only if \ ``sink``\  is NULL.
    :type sink_function: const u32

    :param sink:
        pointer to \ :c:type:`struct media_entity <media_entity>`\  of the sink pad. If NULL, it will use
        all entities that matches the \ ``sink_function``\ .
    :type sink: struct media_entity \*

    :param sink_pad:
        number of the sink pad in the pads array.
    :type sink_pad: const u16

    :param flags:
        Link flags, as defined in include/uapi/linux/media.h.
    :type flags: u32

    :param allow_both_undefined:
        if \ ``true``\ , then both \ ``source``\  and \ ``sink``\  can be NULL.
        In such case, it will create a crossbar between all entities that
        matches \ ``source_function``\  to all entities that matches \ ``sink_function``\ .
        If \ ``false``\ , it will return 0 and won't create any link if both \ ``source``\ 
        and \ ``sink``\  are NULL.
    :type allow_both_undefined: const bool

.. _`media_create_pad_links.valid-values-for-flags`:

Valid values for flags
----------------------


A \ ``MEDIA_LNK_FL_ENABLED``\  flag indicates that the link is enabled and can be
     used to transfer media data. If multiple links are created and this
     flag is passed as an argument, only the first created link will have
     this flag.

A \ ``MEDIA_LNK_FL_IMMUTABLE``\  flag indicates that the link enabled state can't
     be modified at runtime. If \ ``MEDIA_LNK_FL_IMMUTABLE``\  is set, then
     \ ``MEDIA_LNK_FL_ENABLED``\  must also be set since an immutable link is
     always enabled.

It is common for some devices to have multiple source and/or sink entities
of the same type that should be linked. While \ :c:func:`media_create_pad_link`\ 
creates link by link, this function is meant to allow 1:n, n:1 and even
cross-bar (n:n) links.

.. note::

   Before calling this function, media_entity_pads_init() and
   media_device_register_entity() should be called previously for the
   entities to be linked.

.. _`media_entity_remove_links`:

media_entity_remove_links
=========================

.. c:function:: void media_entity_remove_links(struct media_entity *entity)

    remove all links associated with an entity

    :param entity:
        pointer to \ :c:type:`struct media_entity <media_entity>`\ 
    :type entity: struct media_entity \*

.. _`media_entity_remove_links.description`:

Description
-----------

.. note::

   This is called automatically when an entity is unregistered via
   media_device_register_entity().

.. _`__media_entity_setup_link`:

__media_entity_setup_link
=========================

.. c:function:: int __media_entity_setup_link(struct media_link *link, u32 flags)

    Configure a media link without locking

    :param link:
        The link being configured
    :type link: struct media_link \*

    :param flags:
        Link configuration flags
    :type flags: u32

.. _`__media_entity_setup_link.description`:

Description
-----------

The bulk of link setup is handled by the two entities connected through the
link. This function notifies both entities of the link configuration change.

If the link is immutable or if the current and new configuration are
identical, return immediately.

The user is expected to hold link->source->parent->mutex. If not,
\ :c:func:`media_entity_setup_link`\  should be used instead.

.. _`media_entity_setup_link`:

media_entity_setup_link
=======================

.. c:function:: int media_entity_setup_link(struct media_link *link, u32 flags)

    changes the link flags properties in runtime

    :param link:
        pointer to \ :c:type:`struct media_link <media_link>`\ 
    :type link: struct media_link \*

    :param flags:
        the requested new link flags
    :type flags: u32

.. _`media_entity_setup_link.description`:

Description
-----------

The only configurable property is the \ ``MEDIA_LNK_FL_ENABLED``\  link flag
flag to enable/disable a link. Links marked with the
\ ``MEDIA_LNK_FL_IMMUTABLE``\  link flag can not be enabled or disabled.

When a link is enabled or disabled, the media framework calls the
link_setup operation for the two entities at the source and sink of the
link, in that order. If the second link_setup call fails, another
link_setup call is made on the first entity to restore the original link
flags.

Media device drivers can be notified of link setup operations by setting the
\ :c:type:`media_device.link_notify <media_device>`\  pointer to a callback function. If provided, the
notification callback will be called before enabling and after disabling
links.

Entity drivers must implement the link_setup operation if any of their links
is non-immutable. The operation must either configure the hardware or store
the configuration information to be applied later.

Link configuration must not have any side effect on other links. If an
enabled link at a sink pad prevents another link at the same pad from
being enabled, the link_setup operation must return \ ``-EBUSY``\  and can't
implicitly disable the first enabled link.

.. note::

   The valid values of the flags for the link is the same as described
   on media_create_pad_link(), for pad to pad links or the same as described
   on media_create_intf_link(), for interface to entity links.

.. _`media_entity_find_link`:

media_entity_find_link
======================

.. c:function:: struct media_link *media_entity_find_link(struct media_pad *source, struct media_pad *sink)

    Find a link between two pads

    :param source:
        Source pad
    :type source: struct media_pad \*

    :param sink:
        Sink pad
    :type sink: struct media_pad \*

.. _`media_entity_find_link.return`:

Return
------

returns a pointer to the link between the two entities. If no
such link exists, return \ ``NULL``\ .

.. _`media_entity_remote_pad`:

media_entity_remote_pad
=======================

.. c:function:: struct media_pad *media_entity_remote_pad(const struct media_pad *pad)

    Find the pad at the remote end of a link

    :param pad:
        Pad at the local end of the link
    :type pad: const struct media_pad \*

.. _`media_entity_remote_pad.description`:

Description
-----------

Search for a remote pad connected to the given pad by iterating over all
links originating or terminating at that pad until an enabled link is found.

.. _`media_entity_remote_pad.return`:

Return
------

returns a pointer to the pad at the remote end of the first found
enabled link, or \ ``NULL``\  if no enabled link has been found.

.. _`media_entity_get`:

media_entity_get
================

.. c:function:: struct media_entity *media_entity_get(struct media_entity *entity)

    Get a reference to the parent module

    :param entity:
        The entity
    :type entity: struct media_entity \*

.. _`media_entity_get.description`:

Description
-----------

Get a reference to the parent media device module.

The function will return immediately if \ ``entity``\  is \ ``NULL``\ .

.. _`media_entity_get.return`:

Return
------

returns a pointer to the entity on success or \ ``NULL``\  on failure.

.. _`media_entity_get_fwnode_pad`:

media_entity_get_fwnode_pad
===========================

.. c:function:: int media_entity_get_fwnode_pad(struct media_entity *entity, struct fwnode_handle *fwnode, unsigned long direction_flags)

    Get pad number from fwnode

    :param entity:
        The entity
    :type entity: struct media_entity \*

    :param fwnode:
        Pointer to the fwnode_handle which should be used to find the pad
    :type fwnode: struct fwnode_handle \*

    :param direction_flags:
        Expected direction of the pad, as defined in
        :ref:`include/uapi/linux/media.h <media_header>`
        (seek for ``MEDIA_PAD_FL_*``)
    :type direction_flags: unsigned long

.. _`media_entity_get_fwnode_pad.description`:

Description
-----------

This function can be used to resolve the media pad number from
a fwnode. This is useful for devices which use more complex
mappings of media pads.

If the entity does not implement the \ :c:func:`get_fwnode_pad`\  operation
then this function searches the entity for the first pad that
matches the \ ``direction_flags``\ .

.. _`media_entity_get_fwnode_pad.return`:

Return
------

returns the pad number on success or a negative error code.

.. _`media_graph_walk_init`:

media_graph_walk_init
=====================

.. c:function:: int media_graph_walk_init(struct media_graph *graph, struct media_device *mdev)

    Allocate resources used by graph walk.

    :param graph:
        Media graph structure that will be used to walk the graph
    :type graph: struct media_graph \*

    :param mdev:
        Pointer to the \ :c:type:`struct media_device <media_device>`\  that contains the object
    :type mdev: struct media_device \*

.. _`media_graph_walk_cleanup`:

media_graph_walk_cleanup
========================

.. c:function:: void media_graph_walk_cleanup(struct media_graph *graph)

    Release resources used by graph walk.

    :param graph:
        Media graph structure that will be used to walk the graph
    :type graph: struct media_graph \*

.. _`media_entity_put`:

media_entity_put
================

.. c:function:: void media_entity_put(struct media_entity *entity)

    Release the reference to the parent module

    :param entity:
        The entity
    :type entity: struct media_entity \*

.. _`media_entity_put.description`:

Description
-----------

Release the reference count acquired by \ :c:func:`media_entity_get`\ .

The function will return immediately if \ ``entity``\  is \ ``NULL``\ .

.. _`media_graph_walk_start`:

media_graph_walk_start
======================

.. c:function:: void media_graph_walk_start(struct media_graph *graph, struct media_entity *entity)

    Start walking the media graph at a given entity

    :param graph:
        Media graph structure that will be used to walk the graph
    :type graph: struct media_graph \*

    :param entity:
        Starting entity
    :type entity: struct media_entity \*

.. _`media_graph_walk_start.description`:

Description
-----------

Before using this function, \ :c:func:`media_graph_walk_init`\  must be
used to allocate resources used for walking the graph. This
function initializes the graph traversal structure to walk the
entities graph starting at the given entity. The traversal
structure must not be modified by the caller during graph
traversal. After the graph walk, the resources must be released
using \ :c:func:`media_graph_walk_cleanup`\ .

.. _`media_graph_walk_next`:

media_graph_walk_next
=====================

.. c:function:: struct media_entity *media_graph_walk_next(struct media_graph *graph)

    Get the next entity in the graph

    :param graph:
        Media graph structure
    :type graph: struct media_graph \*

.. _`media_graph_walk_next.description`:

Description
-----------

Perform a depth-first traversal of the given media entities graph.

The graph structure must have been previously initialized with a call to
\ :c:func:`media_graph_walk_start`\ .

.. _`media_graph_walk_next.return`:

Return
------

returns the next entity in the graph or \ ``NULL``\  if the whole graph
have been traversed.

.. _`media_pipeline_start`:

media_pipeline_start
====================

.. c:function:: int media_pipeline_start(struct media_entity *entity, struct media_pipeline *pipe)

    Mark a pipeline as streaming

    :param entity:
        Starting entity
    :type entity: struct media_entity \*

    :param pipe:
        Media pipeline to be assigned to all entities in the pipeline.
    :type pipe: struct media_pipeline \*

.. _`media_pipeline_start.description`:

Description
-----------

Mark all entities connected to a given entity through enabled links, either
directly or indirectly, as streaming. The given pipeline object is assigned
to every entity in the pipeline and stored in the media_entity pipe field.

Calls to this function can be nested, in which case the same number of
\ :c:func:`media_pipeline_stop`\  calls will be required to stop streaming. The
pipeline pointer must be identical for all nested calls to
\ :c:func:`media_pipeline_start`\ .

.. _`__media_pipeline_start`:

__media_pipeline_start
======================

.. c:function:: int __media_pipeline_start(struct media_entity *entity, struct media_pipeline *pipe)

    Mark a pipeline as streaming

    :param entity:
        Starting entity
    :type entity: struct media_entity \*

    :param pipe:
        Media pipeline to be assigned to all entities in the pipeline.
    :type pipe: struct media_pipeline \*

.. _`__media_pipeline_start.description`:

Description
-----------

..note:: This is the non-locking version of \ :c:func:`media_pipeline_start`\ 

.. _`media_pipeline_stop`:

media_pipeline_stop
===================

.. c:function:: void media_pipeline_stop(struct media_entity *entity)

    Mark a pipeline as not streaming

    :param entity:
        Starting entity
    :type entity: struct media_entity \*

.. _`media_pipeline_stop.description`:

Description
-----------

Mark all entities connected to a given entity through enabled links, either
directly or indirectly, as not streaming. The media_entity pipe field is
reset to \ ``NULL``\ .

If multiple calls to \ :c:func:`media_pipeline_start`\  have been made, the same
number of calls to this function are required to mark the pipeline as not
streaming.

.. _`__media_pipeline_stop`:

__media_pipeline_stop
=====================

.. c:function:: void __media_pipeline_stop(struct media_entity *entity)

    Mark a pipeline as not streaming

    :param entity:
        Starting entity
    :type entity: struct media_entity \*

.. _`__media_pipeline_stop.description`:

Description
-----------

.. note:: This is the non-locking version of \ :c:func:`media_pipeline_stop`\ 

.. _`media_devnode_create`:

media_devnode_create
====================

.. c:function:: struct media_intf_devnode *media_devnode_create(struct media_device *mdev, u32 type, u32 flags, u32 major, u32 minor)

    creates and initializes a device node interface

    :param mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 
    :type mdev: struct media_device \*

    :param type:
        type of the interface, as given by
        :ref:`include/uapi/linux/media.h <media_header>`
        ( seek for ``MEDIA_INTF_T_*``) macros.
    :type type: u32

    :param flags:
        Interface flags, as defined in
        :ref:`include/uapi/linux/media.h <media_header>`
        ( seek for ``MEDIA_INTF_FL_*``)
    :type flags: u32

    :param major:
        Device node major number.
    :type major: u32

    :param minor:
        Device node minor number.
    :type minor: u32

.. _`media_devnode_create.return`:

Return
------

if succeeded, returns a pointer to the newly allocated
     \ :c:type:`struct media_intf_devnode <media_intf_devnode>`\  pointer.

.. note::

   Currently, no flags for &media_interface is defined.

.. _`media_devnode_remove`:

media_devnode_remove
====================

.. c:function:: void media_devnode_remove(struct media_intf_devnode *devnode)

    removes a device node interface

    :param devnode:
        pointer to \ :c:type:`struct media_intf_devnode <media_intf_devnode>`\  to be freed.
    :type devnode: struct media_intf_devnode \*

.. _`media_devnode_remove.description`:

Description
-----------

When a device node interface is removed, all links to it are automatically
removed.

.. _`media_create_intf_link`:

media_create_intf_link
======================

.. c:function::  media_create_intf_link(struct media_entity *entity, struct media_interface *intf, u32 flags)

    creates a link between an entity and an interface

    :param entity:
        pointer to \ ``media_entity``\ 
    :type entity: struct media_entity \*

    :param intf:
        pointer to \ ``media_interface``\ 
    :type intf: struct media_interface \*

    :param flags:
        Link flags, as defined in
        :ref:`include/uapi/linux/media.h <media_header>`
        ( seek for ``MEDIA_LNK_FL_*``)
    :type flags: u32

.. _`media_create_intf_link.valid-values-for-flags`:

Valid values for flags
----------------------



\ ``MEDIA_LNK_FL_ENABLED``\ 
  Indicates that the interface is connected to the entity hardware.
  That's the default value for interfaces. An interface may be disabled if
  the hardware is busy due to the usage of some other interface that it is
  currently controlling the hardware.

  A typical example is an hybrid TV device that handle only one type of
  stream on a given time. So, when the digital TV is streaming,
  the V4L2 interfaces won't be enabled, as such device is not able to
  also stream analog TV or radio.

.. note::

   Before calling this function, media_devnode_create() should be called for
   the interface and media_device_register_entity() should be called for the
   interface that will be part of the link.

.. _`__media_remove_intf_link`:

__media_remove_intf_link
========================

.. c:function:: void __media_remove_intf_link(struct media_link *link)

    remove a single interface link

    :param link:
        pointer to \ :c:type:`struct media_link <media_link>`\ .
    :type link: struct media_link \*

.. _`__media_remove_intf_link.description`:

Description
-----------

.. note:: This is an unlocked version of \ :c:func:`media_remove_intf_link`\ 

.. _`media_remove_intf_link`:

media_remove_intf_link
======================

.. c:function:: void media_remove_intf_link(struct media_link *link)

    remove a single interface link

    :param link:
        pointer to \ :c:type:`struct media_link <media_link>`\ .
    :type link: struct media_link \*

.. _`media_remove_intf_link.description`:

Description
-----------

.. note:: Prefer to use this one, instead of \ :c:func:`__media_remove_intf_link`\ 

.. _`__media_remove_intf_links`:

__media_remove_intf_links
=========================

.. c:function:: void __media_remove_intf_links(struct media_interface *intf)

    remove all links associated with an interface

    :param intf:
        pointer to \ :c:type:`struct media_interface <media_interface>`\ 
    :type intf: struct media_interface \*

.. _`__media_remove_intf_links.description`:

Description
-----------

.. note:: This is an unlocked version of \ :c:func:`media_remove_intf_links`\ .

.. _`media_remove_intf_links`:

media_remove_intf_links
=======================

.. c:function:: void media_remove_intf_links(struct media_interface *intf)

    remove all links associated with an interface

    :param intf:
        pointer to \ :c:type:`struct media_interface <media_interface>`\ 
    :type intf: struct media_interface \*

.. _`media_remove_intf_links.description`:

Description
-----------

.. note::

  #) This is called automatically when an entity is unregistered via
     media_device_register_entity() and by media_devnode_remove().

  #) Prefer to use this one, instead of __media_remove_intf_links().

.. _`media_entity_call`:

media_entity_call
=================

.. c:function::  media_entity_call( entity,  operation,  args...)

    Calls a struct media_entity_operations operation on an entity

    :param entity:
        entity where the \ ``operation``\  will be called
    :type entity: 

    :param operation:
        type of the operation. Should be the name of a member of
        struct \ :c:type:`struct media_entity_operations <media_entity_operations>`\ .
    :type operation: 

.. _`media_entity_call.description`:

Description
-----------

This helper function will check if \ ``operation``\  is not \ ``NULL``\ . On such case,
it will issue a call to \ ``operation``\ (@entity, \ ``args``\ \).

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_entity.c

.. _`vsp1_entity_get_pad_config`:

vsp1_entity_get_pad_config
==========================

.. c:function:: struct v4l2_subdev_pad_config *vsp1_entity_get_pad_config(struct vsp1_entity *entity, struct v4l2_subdev_pad_config *cfg, enum v4l2_subdev_format_whence which)

    Get the pad configuration for an entity

    :param struct vsp1_entity \*entity:
        the entity

    :param struct v4l2_subdev_pad_config \*cfg:
        the TRY pad configuration

    :param enum v4l2_subdev_format_whence which:
        configuration selector (ACTIVE or TRY)

.. _`vsp1_entity_get_pad_config.description`:

Description
-----------

When called with which set to V4L2_SUBDEV_FORMAT_ACTIVE the caller must hold
the entity lock to access the returned configuration.

Return the pad configuration requested by the which argument. The TRY
configuration is passed explicitly to the function through the cfg argument
and simply returned when requested. The ACTIVE configuration comes from the
entity structure.

.. _`vsp1_entity_get_pad_format`:

vsp1_entity_get_pad_format
==========================

.. c:function:: struct v4l2_mbus_framefmt *vsp1_entity_get_pad_format(struct vsp1_entity *entity, struct v4l2_subdev_pad_config *cfg, unsigned int pad)

    Get a pad format from storage for an entity

    :param struct vsp1_entity \*entity:
        the entity

    :param struct v4l2_subdev_pad_config \*cfg:
        the configuration storage

    :param unsigned int pad:
        the pad number

.. _`vsp1_entity_get_pad_format.description`:

Description
-----------

Return the format stored in the given configuration for an entity's pad. The
configuration can be an ACTIVE or TRY configuration.

.. _`vsp1_entity_get_pad_selection`:

vsp1_entity_get_pad_selection
=============================

.. c:function:: struct v4l2_rect *vsp1_entity_get_pad_selection(struct vsp1_entity *entity, struct v4l2_subdev_pad_config *cfg, unsigned int pad, unsigned int target)

    Get a pad selection from storage for entity

    :param struct vsp1_entity \*entity:
        the entity

    :param struct v4l2_subdev_pad_config \*cfg:
        the configuration storage

    :param unsigned int pad:
        the pad number

    :param unsigned int target:
        the selection target

.. _`vsp1_entity_get_pad_selection.description`:

Description
-----------

Return the selection rectangle stored in the given configuration for an
entity's pad. The configuration can be an ACTIVE or TRY configuration. The
selection target can be COMPOSE or CROP.

.. _`vsp1_entity_remote_pad`:

vsp1_entity_remote_pad
======================

.. c:function:: struct media_pad *vsp1_entity_remote_pad(struct media_pad *pad)

    Find the pad at the remote end of a link

    :param struct media_pad \*pad:
        Pad at the local end of the link

.. _`vsp1_entity_remote_pad.description`:

Description
-----------

Search for a remote pad connected to the given pad by iterating over all
links originating or terminating at that pad until an enabled link is found.

Our link setup implementation guarantees that the output fan-out will not be
higher than one for the data pipelines, except for the links to the HGO and
HGT that can be enabled in addition to a regular data link. When traversing
outgoing links this function ignores HGO and HGT entities and should thus be
used in place of the generic \ :c:func:`media_entity_remote_pad`\  function to traverse
data pipelines.

Return a pointer to the pad at the remote end of the first found enabled
link, or NULL if no enabled link has been found.

.. This file was automatic generated / don't edit.


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

.. This file was automatic generated / don't edit.



.. _media-ioc-enum-links:

==========================
ioctl MEDIA_IOC_ENUM_LINKS
==========================

*man MEDIA_IOC_ENUM_LINKS(2)*

Enumerate all pads and links for a given entity


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct media_links_enum *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <media-func-open>`.

``request``
    MEDIA_IOC_ENUM_LINKS

``argp``


Description
===========

To enumerate pads and/or links for a given entity, applications set the entity field of a struct :ref:`media_links_enum <media-links-enum>` structure and initialize the struct
:ref:`media_pad_desc <media-pad-desc>` and struct :ref:`media_link_desc <media-link-desc>` structure arrays pointed by the ``pads`` and ``links`` fields. They then call the
MEDIA_IOC_ENUM_LINKS ioctl with a pointer to this structure.

If the ``pads`` field is not NULL, the driver fills the ``pads`` array with information about the entity's pads. The array must have enough room to store all the entity's pads. The
number of pads can be retrieved with the :ref:`MEDIA_IOC_ENUM_ENTITIES <media-ioc-enum-entities>` ioctl.

If the ``links`` field is not NULL, the driver fills the ``links`` array with information about the entity's outbound links. The array must have enough room to store all the
entity's outbound links. The number of outbound links can be retrieved with the :ref:`MEDIA_IOC_ENUM_ENTITIES <media-ioc-enum-entities>` ioctl.

Only forward links that originate at one of the entity's source pads are returned during the enumeration process.


.. _media-links-enum:

.. table:: struct media_links_enum

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``entity``                                    | Entity id, set by the application.                                                         |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ⋆\ ``pads``                                   | Pointer to a pads array allocated by the application. Ignored if NULL.                     |
    | :ref:`media_pad_desc    <media-pad-desc>`     |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ⋆\ ``links``                                  | Pointer to a links array allocated by the application. Ignored if NULL.                    |
    | :ref:`media_link_desc    <media-link-desc>`   |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _media-pad-desc:

.. table:: struct media_pad_desc

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``entity``                                    | ID of the entity this pad belongs to.                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u16                                         | ``index``                                     | 0-based pad index.                                                                         |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``flags``                                     | Pad flags, see :ref:`media-pad-flag`   for more details.                                   |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _media-link-desc:

.. table:: struct media_link_desc

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ``source``                                    | Pad at the origin of this link.                                                            |
    | :ref:`media_pad_desc    <media-pad-desc>`     |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ``sink``                                      | Pad at the target of this link.                                                            |
    | :ref:`media_pad_desc    <media-pad-desc>`     |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``flags``                                     | Link flags, see :ref:`media-link-flag`   for more details.                                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    The struct :ref:`media_links_enum <media-links-enum>` ``id`` references a non-existing entity.

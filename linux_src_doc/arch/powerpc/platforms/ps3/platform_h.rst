.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/platform.h

.. _`ps3_spu_resource_type`:

enum ps3_spu_resource_type
==========================

.. c:type:: enum ps3_spu_resource_type

    Type of spu resource.

.. _`ps3_spu_resource_type.definition`:

Definition
----------

.. code-block:: c

    enum ps3_spu_resource_type {
        PS3_SPU_RESOURCE_TYPE_SHARED,
        PS3_SPU_RESOURCE_TYPE_EXCLUSIVE
    };

.. _`ps3_spu_resource_type.constants`:

Constants
---------

PS3_SPU_RESOURCE_TYPE_SHARED
    *undescribed*

PS3_SPU_RESOURCE_TYPE_EXCLUSIVE
    *undescribed*

.. _`ps3_spu_resource_type.description`:

Description
-----------

Returned by \ :c:func:`ps3_repository_read_spu_resource_id`\ .

.. This file was automatic generated / don't edit.


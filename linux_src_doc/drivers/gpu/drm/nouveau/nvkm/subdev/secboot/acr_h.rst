.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/acr.h

.. _`nvkm_acr_func`:

struct nvkm_acr_func
====================

.. c:type:: struct nvkm_acr_func

    properties and functions specific to an ACR

.. _`nvkm_acr_func.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_acr_func {
        void (*dtor)(struct nvkm_acr *);
        int (*oneinit)(struct nvkm_acr *, struct nvkm_secboot *);
        int (*fini)(struct nvkm_acr *, struct nvkm_secboot *, bool);
        int (*load)(struct nvkm_acr *, struct nvkm_falcon *, struct nvkm_gpuobj *, u64);
        int (*reset)(struct nvkm_acr *, struct nvkm_secboot *, unsigned long);
    }

.. _`nvkm_acr_func.members`:

Members
-------

dtor
    *undescribed*

oneinit
    *undescribed*

fini
    *undescribed*

load
    make the ACR ready to run on the given secboot device

reset
    reset the specified falcon

.. _`nvkm_acr`:

struct nvkm_acr
===============

.. c:type:: struct nvkm_acr

    instance of an ACR

.. _`nvkm_acr.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_acr {
        const struct nvkm_acr_func *func;
        const struct nvkm_subdev *subdev;
        enum nvkm_secboot_falcon boot_falcon;
        unsigned long managed_falcons;
        unsigned long optional_falcons;
    }

.. _`nvkm_acr.members`:

Members
-------

func
    *undescribed*

subdev
    *undescribed*

boot_falcon
    ID of the falcon that will perform secure boot

managed_falcons
    bitfield of falcons managed by this ACR

optional_falcons
    bitfield of falcons we can live without

.. This file was automatic generated / don't edit.


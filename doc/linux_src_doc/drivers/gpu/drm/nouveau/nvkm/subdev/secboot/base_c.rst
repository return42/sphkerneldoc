.. -*- coding: utf-8; mode: rst -*-

======
base.c
======


.. _`nvkm_secboot_falcon_run`:

nvkm_secboot_falcon_run
=======================

.. c:function:: int nvkm_secboot_falcon_run (struct nvkm_secboot *sb)

    run the falcon that will perform secure boot

    :param struct nvkm_secboot \*sb:

        *undescribed*



.. _`nvkm_secboot_falcon_run.description`:

Description
-----------


This function is to be called after all chip-specific preparations have
been completed. It will start the falcon to perform secure boot, wait for
it to halt, and report if an error occurred.



.. _`nvkm_secboot_reset`:

nvkm_secboot_reset
==================

.. c:function:: int nvkm_secboot_reset (struct nvkm_secboot *sb, u32 falcon)

    reset specified falcon

    :param struct nvkm_secboot \*sb:

        *undescribed*

    :param u32 falcon:

        *undescribed*



.. _`nvkm_secboot_start`:

nvkm_secboot_start
==================

.. c:function:: int nvkm_secboot_start (struct nvkm_secboot *sb, u32 falcon)

    start specified falcon

    :param struct nvkm_secboot \*sb:

        *undescribed*

    :param u32 falcon:

        *undescribed*



.. _`nvkm_secboot_is_managed`:

nvkm_secboot_is_managed
=======================

.. c:function:: bool nvkm_secboot_is_managed (struct nvkm_secboot *secboot, enum nvkm_secboot_falcon fid)

    check whether a given falcon is securely-managed

    :param struct nvkm_secboot \*secboot:

        *undescribed*

    :param enum nvkm_secboot_falcon fid:

        *undescribed*


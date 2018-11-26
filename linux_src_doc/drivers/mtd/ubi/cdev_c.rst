.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/cdev.c

.. _`get_exclusive`:

get_exclusive
=============

.. c:function:: int get_exclusive(struct ubi_volume_desc *desc)

    get exclusive access to an UBI volume.

    :param desc:
        volume descriptor
    :type desc: struct ubi_volume_desc \*

.. _`get_exclusive.description`:

Description
-----------

This function changes UBI volume open mode to "exclusive". Returns previous
mode value (positive integer) in case of success and a negative error code
in case of failure.

.. _`revoke_exclusive`:

revoke_exclusive
================

.. c:function:: void revoke_exclusive(struct ubi_volume_desc *desc, int mode)

    revoke exclusive mode.

    :param desc:
        volume descriptor
    :type desc: struct ubi_volume_desc \*

    :param mode:
        new mode to switch to
    :type mode: int

.. _`verify_mkvol_req`:

verify_mkvol_req
================

.. c:function:: int verify_mkvol_req(const struct ubi_device *ubi, const struct ubi_mkvol_req *req)

    verify volume creation request.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param req:
        the request to check
    :type req: const struct ubi_mkvol_req \*

.. _`verify_mkvol_req.description`:

Description
-----------

This function zero if the request is correct, and \ ``-EINVAL``\  if not.

.. _`verify_rsvol_req`:

verify_rsvol_req
================

.. c:function:: int verify_rsvol_req(const struct ubi_device *ubi, const struct ubi_rsvol_req *req)

    verify volume re-size request.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param req:
        the request to check
    :type req: const struct ubi_rsvol_req \*

.. _`verify_rsvol_req.description`:

Description
-----------

This function returns zero if the request is correct, and \ ``-EINVAL``\  if not.

.. _`rename_volumes`:

rename_volumes
==============

.. c:function:: int rename_volumes(struct ubi_device *ubi, struct ubi_rnvol_req *req)

    rename UBI volumes.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param req:
        volumes re-name request
    :type req: struct ubi_rnvol_req \*

.. _`rename_volumes.description`:

Description
-----------

This is a helper function for the volume re-name IOCTL which validates the
the request, opens the volume and calls corresponding volumes management
function. Returns zero in case of success and a negative error code in case
of failure.

.. This file was automatic generated / don't edit.


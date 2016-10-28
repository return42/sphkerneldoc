.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpmng.c

.. _`mc_get_version`:

mc_get_version
==============

.. c:function:: int mc_get_version(struct fsl_mc_io *mc_io, u32 cmd_flags, struct mc_version *mc_ver_info)

    Retrieves the Management Complex firmware version information

    :param struct fsl_mc_io \*mc_io:
        Pointer to opaque I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param struct mc_version \*mc_ver_info:
        Returned version information structure

.. _`mc_get_version.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmng_get_container_id`:

dpmng_get_container_id
======================

.. c:function:: int dpmng_get_container_id(struct fsl_mc_io *mc_io, u32 cmd_flags, int *container_id)

    Get container ID associated with a given portal.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int \*container_id:
        Requested container ID

.. _`dpmng_get_container_id.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/skylake/skl-sst-utils.c

.. _`skl_get_pvt_id`:

skl_get_pvt_id
==============

.. c:function:: int skl_get_pvt_id(struct skl_sst *ctx, uuid_le *uuid_mod, int instance_id)

    generate a private id for use as module id

    :param struct skl_sst \*ctx:
        driver context

    :param uuid_le \*uuid_mod:
        module's uuid

    :param int instance_id:
        module's instance id

.. _`skl_get_pvt_id.description`:

Description
-----------

This generates a 128 bit private unique id for a module TYPE so that
module instance is unique

.. _`skl_put_pvt_id`:

skl_put_pvt_id
==============

.. c:function:: int skl_put_pvt_id(struct skl_sst *ctx, uuid_le *uuid_mod, int *pvt_id)

    free up the private id allocated

    :param struct skl_sst \*ctx:
        driver context

    :param uuid_le \*uuid_mod:
        module's uuid

    :param int \*pvt_id:
        module pvt id

.. _`skl_put_pvt_id.description`:

Description
-----------

This frees a 128 bit private unique id previously generated

.. This file was automatic generated / don't edit.


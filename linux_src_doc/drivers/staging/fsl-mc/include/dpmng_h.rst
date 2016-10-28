.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dpmng.h

.. _`mc_ver_major`:

MC_VER_MAJOR
============

.. c:function::  MC_VER_MAJOR()

.. _`mc_version`:

struct mc_version
=================

.. c:type:: struct mc_version


.. _`mc_version.definition`:

Definition
----------

.. code-block:: c

    struct mc_version {
        u32 major;
        u32 minor;
        u32 revision;
    }

.. _`mc_version.members`:

Members
-------

major
    Major version number: incremented on API compatibility changes

minor
    Minor version number: incremented on API additions (that are
    backward compatible); reset when major version is incremented

revision
    Internal revision number: incremented on implementation changes
    and/or bug fixes that have no impact on API

.. This file was automatic generated / don't edit.

